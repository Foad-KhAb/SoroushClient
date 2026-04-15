import asyncio
import json
import logging
import os
from typing import Callable, List

import websockets

from soroushclient.client.auth_cli import PhoneLoginCLI
from soroushclient.network.constants import (
    ID_BAD_SERVER_SALT,
    ID_MSG_CONTAINER,
    ID_MSGS_ACK,
    ID_NEW_SESSION,
    ID_RPC_RESULT,
)
from soroushclient.network.session import MTProtoSession
from soroushclient.network.transport import ObfuscatedTransport
from soroushclient.tl.base import TLObject
from soroushclient.tl.generated import (
    CodeSettings,
    GetFullChannelRequest,
    InputChannel,
    InputPeer,
    InputPeerEmpty,
    JoinChannelRequest,
    LeaveChannelRequest,
    ResolvedPeer,
    ResolveUsername,
    SendCodeRequest,
    SentCode,
    SignInRequest,
)
from soroushclient.tl.generated.functions.chats import GetFullChatRequest
from soroushclient.tl.generated.functions.dialogs import GetDialogsRequest
from soroushclient.tl.generated.functions.messages import (
    GetHistoryRequest,
    ImportChatInvite,
)
from soroushclient.tl.reader import TLReader
from soroushclient.tl.writer import TLWriter

logger = logging.getLogger(__name__)


class SoroushClient:
    def __init__(self, api_id: int, api_hash: str, session_file="soroush.json"):
        self.api_id = api_id
        self.api_hash = api_hash
        self.session_file = session_file
        self._transport = ObfuscatedTransport()
        self._session = MTProtoSession(self._transport)
        self._phone = None
        self._phone_code_hash = None
        self._pending: dict = {}
        self._recv_task = None
        self._initialized = False
        self._update_handlers: List[Callable] = []

    async def connect(self):
        await self._transport.connect()
        is_new = not self._load_session()
        if is_new:
            await self._session.create_auth_key()
            self._save_session()
        logger.info(f"[client] auth_key_id={self._session.auth_key_id}")

        self._recv_task = asyncio.ensure_future(self._recv_loop())
        logger.info("[client] Connected.")
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

    def _save_session(self):
        with open(self.session_file, "w") as f:
            json.dump(
                {
                    "auth_key": self._session.auth_key.hex(),
                    "auth_key_id": self._session.auth_key_id,
                    "server_salt": self._session.server_salt,
                    "session_id": self._session.session_id,
                },
                f,
            )

    def _load_session(self) -> bool:
        if not os.path.exists(self.session_file):
            return False
        with open(self.session_file) as f:
            d = json.load(f)
        self._session.auth_key = bytes.fromhex(d["auth_key"])
        self._session.auth_key_id = d["auth_key_id"]
        self._session.server_salt = d["server_salt"]
        self._session.session_id = d["session_id"]
        logger.info("[client] Session loaded from disk.")
        return True

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

    def on_update(self, func: Callable = None):
        """
        Decorator to register a handler for all incoming updates.

        Usage:
            @client.on_update
            async def handler(update):
                print(update)
        """
        if func is not None:
            self._update_handlers.append(func)
            return func

        def decorator(f):
            self._update_handlers.append(f)
            return f

        return decorator

    def add_update_handler(self, func: Callable):
        """Register an update handler function."""
        self._update_handlers.append(func)

    def remove_update_handler(self, func: Callable):
        """Remove a previously registered update handler."""
        self._update_handlers.remove(func)

    async def _fire_update(self, update: TLObject):
        """Dispatch an update to all registered handlers."""
        for handler in self._update_handlers:
            try:
                if asyncio.iscoroutinefunction(handler):
                    await handler(update)
                else:
                    handler(update)
            except Exception as e:
                logger.error(f"[update] handler error: {e}")

    def _dispatch(self, cid: int, r: TLReader):
        if cid == ID_RPC_RESULT:
            req_msg_id = r.read_long()
            inner_cid = r.read_int(signed=False)
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

        elif cid == 0x347773C5:  # Pong
            r.read_long()
            r.read_long()
            logger.debug("pong received")

        elif cid == 0x74AE4240:  # Updates
            obj = TLObject.read_object_with_cid(cid, r)
            if obj and self._update_handlers:
                asyncio.ensure_future(self._fire_update(obj))

        else:
            cls = TLObject._registry.get(cid)
            if cls:
                try:
                    obj = cls.from_reader(r)
                    if self._update_handlers:
                        asyncio.ensure_future(self._fire_update(obj))
                except Exception as e:
                    logger.warning(f"[dispatch] failed to parse cid={cid:#010x}: {e}")
            else:
                logger.warning(f"[dispatch] unhandled cid={cid:#010x}")

    async def _ping(self):
        import random

        w = TLWriter()
        w.write_int(0x7ABE77EC, signed=False)
        w.write_long(random.randint(0, 2**63))
        try:
            await self._session.send(w.getvalue())
            await asyncio.sleep(0.5)
            logger.info("[client] Ping sent.")
        except Exception as e:
            logger.info(f"[client] Ping error: {e}")

    async def _call(self, body: bytes, timeout=10.0):
        loop = asyncio.get_event_loop()
        fut = loop.create_future()
        msg_id = await self._session.send(body)
        self._pending[msg_id] = fut
        return await asyncio.wait_for(fut, timeout=timeout)

    def _wrap_init(self, query: bytes) -> bytes:
        init = TLWriter()
        init.write_int(0xC1CD5EA9, signed=False)  # initConnection CID
        init.write_int(0, signed=False)  # flags
        init.write_int(self.api_id)  # api_id
        init.write_string("Web")  # device_model
        init.write_string("1.0")  # system_version
        init.write_string("1.0")  # app_version
        init.write_string("fa")  # lang_code       ← first
        init.write_string("")  # lang_pack       ← second
        init.write_string("fa")  # system_lang_code ← third
        init.write_raw(query)

        w = TLWriter()
        w.write_int(0xDA9B0D0D, signed=False)
        w.write_int(181)
        w.write_raw(init.getvalue())
        return w.getvalue()

    def _maybe_wrap(self, query: bytes) -> bytes:
        if not self._initialized:
            self._initialized = True
            return self._wrap_init(query)
        return query

    async def start_phone_auth(self):
        await PhoneLoginCLI(
            client=self,
        ).start()

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

    async def get_dialogs(
        self, offset_date=0, offset_id=0, offset_peer=InputPeerEmpty(), limit=20, hash=0
    ) -> TLObject:
        req = GetDialogsRequest(
            offset_date=offset_date,
            offset_id=offset_id,
            offset_peer=offset_peer,
            limit=limit,
            hash=hash,
        )
        cid, r = await self._call(self._maybe_wrap(req.to_bytes()))
        return req.parse_response(cid, r)

    async def get_full_channel(self, channel: InputChannel) -> TLObject:
        req = GetFullChannelRequest(channel=channel)
        cid, r = await self._call(self._wrap_init(req.to_bytes()))
        return req.parse_response(cid, r)

    async def get_full_chat(self, chat_id: str) -> TLObject:
        req = GetFullChatRequest(chat_id=chat_id)
        cid, r = await self._call(self._wrap_init(req.to_bytes()))
        return req.parse_response(cid, r)

    async def join_channel(self, channel: InputChannel) -> TLObject:
        req = JoinChannelRequest(channel=channel)
        cid, r = await self._call(self._wrap_init(req.to_bytes()))
        return req.parse_response(cid, r)

    async def leave_channel(self, channel: InputChannel) -> TLObject:
        req = LeaveChannelRequest(channel=channel)
        cid, r = await self._call(self._wrap_init(req.to_bytes()))
        return req.parse_response(cid, r)

    async def search(self, query: str, limit: int = 20) -> TLObject:
        """
        Search for users and channels globally by name or username.

        This is the global contact/peer search — equivalent to typing
        a name or username into the Soroush search bar.

        Parameters
        ----------
        query : str
            The search term to look up.
            Can be a username, full name, or partial name.
            Examples: "soroush", "john doe", "@channel"

        limit : int, optional
            Maximum number of results to return. Default is 20.

        Returns
        -------
        TLObject
            A Found object containing:
            - my_results : list of Peer objects from your own contacts/chats
                           that match the query (shown first in UI)
            - results    : list of Peer objects from global search results
            - chats      : list of Chat/Channel objects referenced in
                           my_results and results — look up by peer.channel_id
            - users      : list of User objects referenced in
                           my_results and results — look up by peer.user_id

        Examples
        --------
        found = await client.search("soroush", limit=10)

        # get full object for each result
        users_by_id   = {u.id: u for u in found.users}
        chats_by_id   = {c.id: c for c in found.chats}

        for peer in found.results:
            if isinstance(peer, PeerUser):
                print(users_by_id[peer.user_id])
            elif isinstance(peer, PeerChannel):
                print(chats_by_id[peer.channel_id])
        """
        from soroushclient.tl.generated.functions.contacts import SearchRequest

        req = SearchRequest(q=query, limit=limit)
        cid, r = await self._call(self._wrap_init(req.to_bytes()))
        return req.parse_response(cid, r)

    async def resolve_username(self, username: str) -> ResolvedPeer:
        """
        Resolve a username to its full peer information.

        This is the method called when a user taps on a @username link —
        it returns the full user or channel object behind the username.

        Parameters
        ----------
        username : str
            The username to resolve, with or without the @ prefix.
            Examples: "soroush", "@soroush"

        Returns
        -------
        TLObject
            A ResolvedPeer object containing:
            - peer:   Peer object identifying the type and ID (PeerUser or PeerChannel)
            - chats:  list of Chat/Channel objects if the username belongs to a channel
            - users:  list of User objects if the username belongs to a user

        Examples
        --------
        result = await client.resolve_username("soroush")
        peer = result.peer

        if isinstance(peer, PeerChannel):
            channel = next(c for c in result.chats if c.id == peer.channel_id)

        if isinstance(peer, PeerUser):
            user = next(u for u in result.users if u.id == peer.user_id)
        """
        req = ResolveUsername(username=username)
        cid, r = await self._call(self._wrap_init(req.to_bytes()))
        return req.parse_response(cid, r)

    async def get_history(
        self,
        peer: InputPeer,
        offset_id: int = 0,
        offset_date: int = 0,
        add_offset: int = 0,
        limit: int = 20,
        max_id: int = 0,
        min_id: int = 0,
        hash: int = 0,
    ) -> TLObject:
        """
        Fetch the message history of a chat, channel, or user.

        Parameters
        ----------
        peer : InputPeer
            The target conversation to fetch messages from.
            Use InputPeerChannel, InputPeerUser, or InputPeerChat.

        offset_id : int, optional
            Start fetching from this message ID (exclusive).
            Messages older than this ID are returned.
            Use 0 to start from the most recent message.

        offset_date : int, optional
            Start fetching from this Unix timestamp.
            Only used when offset_id is 0.
            Use 0 to ignore date filtering.

        add_offset : int, optional
            Shift the result window relative to offset_id.
            Positive values skip forward, negative values skip backward.
            Useful for centering results around a specific message.
            Use 0 for normal sequential reading.

        limit : int, optional
            Maximum number of messages to return. Default is 20, max is 100.

        max_id : int, optional
            Only return messages with ID less than or equal to this value.
            Use 0 for no upper bound.

        min_id : int, optional
            Only return messages with ID greater than or equal to this value.
            Use 0 for no lower bound.

        hash : int, optional
            Client-side cache hash for detecting unchanged results.
            Server returns MessagesNotModified if history hasn't changed.
            Use 0 to always fetch fresh results.

        Returns
        -------
        TLObject
            A Messages or MessagesSlice object containing:
            - messages: list of Message objects
            - chats:    list of Chat/Channel objects referenced in messages
            - users:    list of User objects referenced in messages
        """
        req = GetHistoryRequest(
            peer=peer,
            offset_id=offset_id,
            offset_date=offset_date,
            add_offset=add_offset,
            limit=limit,
            max_id=max_id,
            min_id=min_id,
            hash=hash,
        )

        cid, r = await self._call(self._maybe_wrap(req.to_bytes()))
        return req.parse_response(cid, r)

    async def join_by_link(self, link: str) -> TLObject:
        """
        Join a chat or channel via an invitation link.

        Automatically extracts the hash from various Soroush invite link formats.

        Parameters
        ----------
        link : str
            The invite link or raw hash. Accepts all of these formats:
            - "https://splus.ir/joingroup/ABC123"
            - "splus.ir/joingroup/ABC123"
            - "ABC123"  (raw hash)

        Returns
        -------
        Updates object containing the joined chat/channel info.

        Raises
        ------
        RpcError
            - INVITE_HASH_EXPIRED  : link has expired
            - INVITE_HASH_INVALID  : link is malformed
            - USER_ALREADY_PARTICIPANT : already a member
        """
        hash_ = link.strip()
        if "/" in hash_:
            hash_ = hash_.rstrip("/").split("/")[-1]

        req = ImportChatInvite(hash=hash_)
        cid, r = await self._call(self._maybe_wrap(req.to_bytes()))
        return req.parse_response(cid, r)

    async def get_messages_views(
        self,
        peer: InputPeer,
        ids: List[int],
        increment: bool = False,
    ) -> TLObject:
        """
        Fetch view counts for one or more messages in a channel.

        Parameters
        ----------
        peer : InputPeer
            The channel containing the messages.
            Use InputPeerChannel(channel_id=..., access_hash=...).

        ids : List[int]
            List of message IDs to fetch views for.
            Can pass up to 100 IDs per call.

        increment : bool, optional
            If True, counts this fetch as a real view (increments the counter).
            If False, just reads the current count without incrementing.
            Default is False — use True only when the user actually opens the message.

        Returns
        -------
        MessageViews object containing:
            - views : list of MessageViews objects, one per message ID
            - chats : list of Chat objects referenced in the response
            - users : list of User objects referenced in the response
        """
        from soroushclient.tl.generated.functions.messages import GetMessagesViews

        req = GetMessagesViews(peer=peer, id=ids, increment=increment)
        cid, r = await self._call(self._maybe_wrap(req.to_bytes()))
        return req.parse_response(cid, r)
