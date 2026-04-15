from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from soroushclient.tl.base import TLField, TLObject

if TYPE_CHECKING:
    from soroushclient.tl.generated import Chat, Peer
    from soroushclient.tl.generated.types.users import User


class Found(TLObject):
    CONSTRUCTOR_ID = 0xB3134D9D
    FIELDS = [
        TLField("my_results", "Peer", is_vector=True),
        TLField("results", "Peer", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    my_result: Optional[Peer]
    results: Optional[Peer]
    chats: Optional[Chat]
    users: Optional[User]


class ResolvedPeer(TLObject):
    CONSTRUCTOR_ID = 0x7F077AD9
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    peer: Optional[Peer]
    chats: Optional[List[Chat]]
    users: Optional[List[User]]
