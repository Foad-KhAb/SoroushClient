import hashlib
import os
import struct
import time

from soroushclient.crypto.aes import aes_ige_encrypt, aes_ige_decrypt
from soroushclient.crypto.auth_key import generate_key_iv
from soroushclient.crypto.factorize import _factorize
from soroushclient.crypto.rsa import SOROUSH_RSA_KEYS, rsa_encrypt
from soroushclient.crypto.utils import _bytes_to_int, _int_to_bytes, sha1
from soroushclient.network.constants import ID_REQ_PQ_MULTI, ID_RES_PQ, ID_REQ_DH_PARAMS, ID_SERVER_DH_OK, \
    ID_CLIENT_DH_INNER, ID_SET_CLIENT_DH, ID_DH_GEN_OK
from soroushclient.network.transport import ObfuscatedTransport
from soroushclient.tl.reader import TLReader
from soroushclient.tl.writer import TLWriter

import logging
logger = logging.getLogger(__name__)

class MTProtoSession:
    def __init__(self, transport: ObfuscatedTransport):
        self.transport    = transport
        self.auth_key     : bytes = None
        self.auth_key_id  : int   = None
        self.server_salt  : int   = 0
        self.session_id   : int   = struct.unpack("<q", os.urandom(8))[0]
        self._seq_no      : int   = 0

    def _new_msg_id(self) -> int:
        t   = time.time()
        sec = int(t)
        ns  = int((t - sec) * 1e9)
        return (sec << 32) | (ns & ~3)

    def _next_seq(self, content_related: bool) -> int:
        n = self._seq_no * 2 + (1 if content_related else 0)
        if content_related:
            self._seq_no += 1
        return n

    async def _send_plain(self, body: bytes):
        msg_id = self._new_msg_id()
        data   = (
            b'\x00' * 8
            + struct.pack("<q", msg_id)
            + struct.pack("<I", len(body))
            + body
        )
        await self.transport.send(data)
        return msg_id

    async def _recv_plain(self) -> bytes:
        raw      = await self.transport.recv()
        body_len = struct.unpack_from("<I", raw, 16)[0]
        return raw[20:20 + body_len]

    async def send(self, body: bytes, content_related=True) -> int:
        msg_id  = self._new_msg_id()
        seq     = self._next_seq(content_related)
        inner   = (
            struct.pack("<q", self.server_salt)
            + struct.pack("<q", self.session_id)
            + struct.pack("<q", msg_id)
            + struct.pack("<i", seq)
            + struct.pack("<I", len(body))
            + body
        )
        pad_len = ((-len(inner) - 12) % 16) + 12
        if (8 + 16 + len(inner) + pad_len) % 4 != 0:
            pad_len += 4 - ((8 + 16 + len(inner) + pad_len) % 4)
        inner  += os.urandom(pad_len)
        msg_key = hashlib.sha256(self.auth_key[88:120] + inner).digest()[8:24]
        key, iv = generate_key_iv(self.auth_key, msg_key, client=True)
        enc     = aes_ige_encrypt(inner, key, iv)
        packet  = struct.pack("<q", self.auth_key_id) + msg_key + enc
        await self.transport.send(packet)
        return msg_id

    async def recv(self) -> tuple:
        data = await self.transport.recv()
        if len(data) < 8:
            raise ConnectionError(f"Frame too short: {data.hex()}")
        auth_key_id = struct.unpack_from("<q", data, 0)[0]
        if auth_key_id == 0:
            body_len = struct.unpack_from("<I", data, 16)[0]
            body     = data[20:20 + body_len]
            r        = TLReader(body)
            cid      = r.read_int(signed=False)
            return cid, r
        msg_key  = data[8:24]
        enc      = data[24:]
        key, iv  = generate_key_iv(self.auth_key, msg_key, client=False)
        inner    = aes_ige_decrypt(enc, key, iv)
        body_len = struct.unpack_from("<I", inner, 28)[0]
        body     = inner[32:32 + body_len]
        r        = TLReader(body)
        cid      = r.read_int(signed=False)
        return cid, r

    async def create_auth_key(self):
        nonce = int.from_bytes(os.urandom(16), "little")

        w = TLWriter()
        w.write_int(ID_REQ_PQ_MULTI, signed=False)
        w.write_raw(nonce.to_bytes(16, "little"))
        await self._send_plain(w.getvalue())

        raw = await self._recv_plain()
        r   = TLReader(raw)
        cid = r.read_int(signed=False)
        assert cid == ID_RES_PQ, f"Expected resPQ, got {cid:#010x}"
        _nonce16    = r.read_raw(16)
        srv_nonce16 = r.read_raw(16)
        pq_bytes    = r.read_bytes()
        pq          = _bytes_to_int(pq_bytes)
        r.read_int(signed=False)
        count        = r.read_int()
        fingerprints = [r.read_long(signed=False) for _ in range(count)]
        logger.info(f"[dh] resPQ ok, pq={pq}, fingerprints={fingerprints}")

        p, q      = _factorize(pq)
        new_nonce = int.from_bytes(os.urandom(32), "little")

        p_bytes      = _int_to_bytes(p,  (p.bit_length()  + 7) // 8)
        q_bytes      = _int_to_bytes(q,  (q.bit_length()  + 7) // 8)
        pq_bytes_ser = _int_to_bytes(pq, (pq.bit_length() + 7) // 8)

        inner = TLWriter()
        inner.write_int(0xa9f55f95, signed=False)
        inner.write_bytes(pq_bytes_ser)
        inner.write_bytes(p_bytes)
        inner.write_bytes(q_bytes)
        inner.write_raw(nonce.to_bytes(16, "little"))
        inner.write_raw(srv_nonce16)
        inner.write_raw(new_nonce.to_bytes(32, "little"))
        inner.write_int(2)
        inner_data = inner.getvalue()
        logger.info(f"[dh] inner_data len={len(inner_data)}")

        fp = next((f for f in fingerprints if f in SOROUSH_RSA_KEYS), None)
        if fp is None:
            raise RuntimeError(f"No matching RSA key for fingerprints: {fingerprints}")
        fp, encrypted = rsa_encrypt(inner_data, fp)
        logger.info(f"[dh] rsa encrypted len={len(encrypted)}")

        w = TLWriter()
        w.write_int(ID_REQ_DH_PARAMS, signed=False)
        w.write_raw(nonce.to_bytes(16, "little"))
        w.write_raw(srv_nonce16)
        w.write_bytes(p_bytes)
        w.write_bytes(q_bytes)
        w.write_long(fp, signed=False)
        w.write_bytes(encrypted)
        await self._send_plain(w.getvalue())

        raw = await self._recv_plain()
        r   = TLReader(raw)
        cid = r.read_int(signed=False)
        assert cid == ID_SERVER_DH_OK, f"Expected server_DH_params_ok, got {cid:#010x}"
        r.read_raw(16)
        r.read_raw(16)
        enc_answer = r.read_bytes()
        logger.info(f"[dh] server_DH_params_ok, enc_answer len={len(enc_answer)}")

        nn        = new_nonce.to_bytes(32, "little")
        sn        = srv_nonce16
        sha_nn_sn = sha1(nn + sn)
        sha_sn_nn = sha1(sn + nn)
        sha_nn_nn = sha1(nn + nn)
        tmp_key   = sha_nn_sn + sha_sn_nn[:12]
        tmp_iv    = sha_sn_nn[12:] + sha_nn_nn + nn[:4]

        answer_full = aes_ige_decrypt(enc_answer, tmp_key, tmp_iv)
        answer      = answer_full[20:]

        ra  = TLReader(answer)
        got = ra.read_int(signed=False)
        assert got == 0xb5890dba, f"Expected server_DH_inner_data, got {got:#010x}"
        ra.read_raw(16)
        ra.read_raw(16)
        g        = ra.read_int()
        dh_prime = _bytes_to_int(ra.read_bytes())
        g_a      = _bytes_to_int(ra.read_bytes())
        logger.info(f"[dh] server_DH_inner_data ok, g={g}")

        b              = _bytes_to_int(os.urandom(256))
        g_b            = pow(g, b, dh_prime)
        auth_key_int   = pow(g_a, b, dh_prime)
        auth_key_bytes = _int_to_bytes(auth_key_int, 256)

        self.server_salt = struct.unpack("<q",
            bytes(a ^ b for a, b in zip(nn[:8], sn[:8]))
        )[0]

        ci           = TLWriter()
        ci.write_int(ID_CLIENT_DH_INNER, signed=False)
        ci.write_raw(nonce.to_bytes(16, "little"))
        ci.write_raw(srv_nonce16)
        ci.write_long(0)
        ci.write_bytes(_int_to_bytes(g_b, (g_b.bit_length() + 7) // 8))
        ci_data      = ci.getvalue()
        ci_enc       = sha1(ci_data) + ci_data
        ci_enc      += bytes((-len(ci_enc)) % 16)
        ci_encrypted = aes_ige_encrypt(ci_enc, tmp_key, tmp_iv)

        w = TLWriter()
        w.write_int(ID_SET_CLIENT_DH, signed=False)
        w.write_raw(nonce.to_bytes(16, "little"))
        w.write_raw(srv_nonce16)
        w.write_bytes(ci_encrypted)
        await self._send_plain(w.getvalue())

        raw = await self._recv_plain()
        r   = TLReader(raw)
        cid = r.read_int(signed=False)
        assert cid == ID_DH_GEN_OK, f"DH failed: {cid:#010x}"

        self.auth_key    = auth_key_bytes
        self.auth_key_id = struct.unpack("<q", sha1(auth_key_bytes)[-8:])[0]
        logger.info("[dh] Auth key generated successfully!")
