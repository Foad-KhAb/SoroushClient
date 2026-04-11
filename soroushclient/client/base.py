import asyncio
import json
import os

import websockets

from soroushclient.network.constants import ID_RPC_RESULT, ID_MSG_CONTAINER, ID_BAD_SERVER_SALT, ID_NEW_SESSION, \
    ID_MSGS_ACK
from soroushclient.network.session import MTProtoSession
from soroushclient.network.transport import ObfuscatedTransport
from soroushclient.tl.base import TLObject
from soroushclient.tl.generated import InputPeerEmpty, GetFullChannelRequest, SignInRequest, CodeSettings, \
    SendCodeRequest, SentCode, InputChannel, JoinChannelRequest, LeaveChannelRequest
from soroushclient.tl.generated.functions.chats import GetFullChatRequest
from soroushclient.tl.generated.functions.dialogs import GetDialogsRequest
from soroushclient.tl.reader import TLReader
from soroushclient.tl.writer import TLWriter

import logging
logger = logging.getLogger(__name__)

class SoroushClient:
    def __init__(self, api_id: int, api_hash: str, session_file="soroush.json"):
        self.api_id           = api_id
        self.api_hash         = api_hash
        self.session_file     = session_file
        self._transport       = ObfuscatedTransport()
        self._session         = MTProtoSession(self._transport)
        self._phone           = None
        self._phone_code_hash = None
        self._pending         : dict = {}
        self._recv_task       = None

    # ── lifecycle ─────────────────────────────────────────

    async def connect(self):
        await self._transport.connect()
        is_new = not self._load_session()
        if is_new:
            await self._session.create_auth_key()
            self._save_session()
        logger.info(f"[client] auth_key_id={self._session.auth_key_id}")

        self._recv_task = asyncio.ensure_future(self._recv_loop())
        logger.info(f"[client] Connected.")
        if not is_new:
            await self._ping()

    async def disconnect(self):
        if self._recv_task:
            self._recv_task.cancel()
        await self._transport.disconnect()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *_):
        await self.disconnect()

    # ── session ───────────────────────────────────────────

    def _save_session(self):
        with open(self.session_file, "w") as f:
            json.dump({
                "auth_key":    self._session.auth_key.hex(),
                "auth_key_id": self._session.auth_key_id,
                "server_salt": self._session.server_salt,
                "session_id":  self._session.session_id,
            }, f)

    def _load_session(self) -> bool:
        if not os.path.exists(self.session_file):
            return False
        with open(self.session_file) as f:
            d = json.load(f)
        self._session.auth_key    = bytes.fromhex(d["auth_key"])
        self._session.auth_key_id = d["auth_key_id"]
        self._session.server_salt = d["server_salt"]
        self._session.session_id  = d["session_id"]
        logger.info("[client] Session loaded from disk.")
        return True

    # ── recv loop ─────────────────────────────────────────

    async def _recv_loop(self):
        while True:
            try:
                cid, r = await self._session.recv()
                self._dispatch(cid, r)
            except asyncio.CancelledError:
                break
            except websockets.exceptions.ConnectionClosed as e:
                logger.info(f"[recv_loop] WebSocket closed: {e}")
                break
            except Exception as e:
                logger.info(f"[recv_loop] error: {e}")

    def _dispatch(self, cid: int, r: TLReader):
        if cid == ID_RPC_RESULT:
            req_msg_id = r.read_long()
            inner_cid  = r.read_int(signed=False)
            fut = self._pending.pop(req_msg_id, None)
            if fut and not fut.done():
                fut.set_result((inner_cid, r))
        elif cid == ID_MSG_CONTAINER:
            count = r.read_int()
            for _ in range(count):
                r.read_long()
                r.read_int()
                r.read_int()
                inner_cid = r.read_int(signed=False)
                self._dispatch(inner_cid, r)
        elif cid == ID_BAD_SERVER_SALT:
            r.read_long()
            r.read_int()
            r.read_int()
            new_salt = r.read_long()
            self._session.server_salt = new_salt
            self._save_session()
            logger.info(f"[mtproto] Salt updated: {new_salt}")
        elif cid == ID_NEW_SESSION:
            r.read_long()
            r.read_long()
            new_salt = r.read_long()
            self._session.server_salt = new_salt
            self._save_session()
            logger.info(f"[mtproto] New session, salt={new_salt}")
        elif cid == ID_MSGS_ACK:
            pass
        else:
            logger.warning(f"[dispatch] unhandled cid={cid:#010x}")

    # ── internal ──────────────────────────────────────────

    async def _ping(self):
        import random
        w = TLWriter()
        w.write_int(0x7abe77ec, signed=False)
        w.write_long(random.randint(0, 2**63))
        try:
            await self._session.send(w.getvalue())
            await asyncio.sleep(0.5)
            logger.info("[client] Ping sent.")
        except Exception as e:
            logger.info(f"[client] Ping error: {e}")

    async def _call(self, body: bytes, timeout=10.0):
        loop   = asyncio.get_event_loop()
        fut    = loop.create_future()
        msg_id = await self._session.send(body)
        self._pending[msg_id] = fut
        return await asyncio.wait_for(fut, timeout=timeout)

    def _wrap_init(self, query: bytes) -> bytes:
        init = TLWriter()
        init.write_int(0xc1cd5ea9, signed=False)
        init.write_int(0, signed=False)
        init.write_int(self.api_id)
        init.write_string("SoroushClient")
        init.write_string("1.0.0")
        init.write_string("1.0.0")
        init.write_string("fa")
        init.write_string("")
        init.write_string("fa")
        init.write_raw(query)

        w = TLWriter()
        w.write_int(0xda9b0d0d, signed=False)
        w.write_int(181)
        w.write_raw(init.getvalue())
        return w.getvalue()

    # ── auth ──────────────────────────────────────────────

    async def send_code(self, phone: str) -> SentCode:
        req = SendCodeRequest(
            phone_number=phone,
            api_id=self.api_id,
            api_hash=self.api_hash,
            settings=CodeSettings(),
        )
        cid, r = await self._call(self._wrap_init(req.to_bytes()))
        result = req.parse_response(cid, r)
        self._phone = phone
        self._phone_code_hash = result.phone_code_hash
        return result

    async def sign_in(self, code: str) -> TLObject:
        req = SignInRequest(
            phone_number=self._phone,
            phone_code_hash=self._phone_code_hash,
            phone_code=code,
        )
        cid, r = await self._call(req.to_bytes())
        return req.parse_response(cid, r)

    async def get_dialogs(self, limit=20) -> TLObject:
        req = GetDialogsRequest(
            offset_date=0,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=limit,
            hash=0,
        )
        cid, r = await self._call(self._wrap_init(req.to_bytes()))
        return req.parse_response(cid, r)
    async def get_full_channel(self, channel) -> TLObject:
        req = GetFullChannelRequest(channel=channel)
        cid, r = await self._call(self._wrap_init(req.to_bytes()))
        return req.parse_response(cid, r)
    async def get_full_chat(self, chat_id) -> TLObject:
        req = GetFullChatRequest(chat_id=chat_id)
        cid, r = await self._call(self._wrap_init(req.to_bytes()))
        return req.parse_response(cid, r)
    async def join_channel(self, channel:InputChannel) -> TLObject:
        req = JoinChannelRequest(channel=channel)
        cid, r = await self._call(self._wrap_init(req.to_bytes()))
        return req.parse_response(cid, r)
    async def leave_channel(self, channel:InputChannel) -> TLObject:
        req = LeaveChannelRequest(channel=channel)
        cid, r = await self._call(self._wrap_init(req.to_bytes()))
        return req.parse_response(cid, r)