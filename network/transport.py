import asyncio
import logging
import os
import ssl as ssl_mod
import struct

import websockets
from soroushclient.crypto.aes import aes_ctr

logger = logging.getLogger(__name__)

WS_URI = "wss://im-server.splus.ir/apiws"
WS_ORIGIN = "https://web.splus.ir"
WS_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
OBFUSCATE_TAG = bytes.fromhex("efefefef")


class ObfuscatedTransport:
    def __init__(self):
        self._ws = None
        self._encrypt = None
        self._decrypt = None
        self._lock = None

    def _init_header(self) -> bytes:
        FORBIDDEN = [
            bytes.fromhex("50567247"),
            bytes.fromhex("474554"),
            bytes.fromhex("504f5354"),
            bytes.fromhex("eeeeeeee"),
        ]
        while True:
            n = bytearray(os.urandom(64))
            if n[0] == 0xEF:
                continue
            if n[4:8] == b"\x00\x00\x00\x00":
                continue
            if any(n[: len(p)] == bytearray(p) for p in FORBIDDEN):
                continue
            break

        enc_key = bytes(n[8:40])
        enc_iv = bytes(n[40:56])
        rev = bytes(n[8:56])[::-1]
        dec_key = rev[0:32]
        dec_iv = rev[32:48]

        enc = aes_ctr(enc_key, enc_iv)
        dec = aes_ctr(dec_key, dec_iv)

        n[56:60] = OBFUSCATE_TAG
        encrypted = bytearray(enc.update(bytes(n)))
        n[56:64] = encrypted[56:64]

        self._encrypt = aes_ctr(enc_key, enc_iv)
        self._encrypt.update(bytes(64))
        self._decrypt = dec

        return bytes(n)

    async def connect(self):
        self._lock = asyncio.Lock()
        ssl_ctx = ssl_mod.create_default_context()
        self._ws = await websockets.connect(
            WS_URI,
            ssl=ssl_ctx,
            subprotocols=["binary"],
            additional_headers={
                "Origin": WS_ORIGIN,
                "User-Agent": WS_UA,
                "Accept-Language": "fa-IR,fa;q=0.9,en;q=0.8",
                "Cache-Control": "no-cache",
            },
            ping_interval=20,
            ping_timeout=10,
            max_size=64 * 1024 * 1024,
        )
        header = self._init_header()
        logger.info(f"[transport] obfuscation header: {header.hex()}")
        await self._ws.send(header)

    async def disconnect(self):
        if self._ws:
            await self._ws.close()
            self._ws = None

    async def send(self, payload: bytes):
        assert len(payload) % 4 == 0, f"payload not multiple of 4: {len(payload)}"
        n = len(payload) // 4
        if n < 0x7F:
            frame = bytes([n]) + payload
        else:
            frame = bytes([0x7F, n & 0xFF, (n >> 8) & 0xFF, (n >> 16) & 0xFF]) + payload
        encrypted = self._encrypt.update(frame)
        async with self._lock:
            await self._ws.send(encrypted)

    async def recv(self) -> bytes:
        raw = await self._ws.recv()
        if isinstance(raw, str):
            raw = raw.encode()
        decrypted = self._decrypt.update(raw)
        first = decrypted[0]
        if first == 0x7F:
            payload = decrypted[4:]
        else:
            payload = decrypted[1:]
        if len(payload) == 4:
            code = struct.unpack_from("<i", payload)[0]
            raise ConnectionError(f"Transport error: {code}")
        return payload
