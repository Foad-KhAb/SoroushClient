from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from soroushclient.tl.base import TLField, TLObject

if TYPE_CHECKING:
    from soroushclient.tl.generated import DraftMessage, Peer, PeerNotifySettings


class Dialog(TLObject):
    CONSTRUCTOR_ID = 0xD58A08C6
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("pinned", "true", flag_group=0, flag_bit=2),
        TLField("unread_mark", "true", flag_group=0, flag_bit=3),
        TLField("view_forum_as_messages", "true", flag_group=0, flag_bit=6),
        TLField("peer", "Peer"),
        TLField("top_message", "int"),
        TLField("read_inbox_max_id", "int"),
        TLField("read_outbox_max_id", "int"),
        TLField("unread_count", "int"),
        TLField("unread_mentions_count", "int"),
        TLField("unread_reactions_count", "int"),
        TLField("notify_settings", "PeerNotifySettings"),
        TLField("pts", "int", flag_group=0, flag_bit=0),
        TLField("draft", "DraftMessage", flag_group=0, flag_bit=1),
        TLField("folder_id", "int", flag_group=0, flag_bit=4),
        TLField("ttl_period", "int", flag_group=0, flag_bit=5),
    ]
    pinned: Optional[bool]
    unread_mark: Optional[bool]
    view_forum_as_messages: Optional[bool]
    peer: Optional[Peer]
    top_message: Optional[int]
    read_inbox_max_id: Optional[int]
    read_outbox_max_id: Optional[int]
    unread_count: Optional[int]
    unread_mentions_count: Optional[int]
    unread_reactions_count: Optional[int]
    notify_settings: Optional[PeerNotifySettings]
    pts: Optional[int]
    draft: Optional[DraftMessage]
    folder_id: Optional[int]
    ttl_period: Optional[int]


class MessagesDialogs(TLObject):
    CONSTRUCTOR_ID = 0x15BA6C40
    FIELDS = [
        TLField("dialogs", "Dialog", is_vector=True),
        TLField("messages", "Message", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]

    dialogs: Optional[List[TLObject]]
    messages: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]


class MessagesDialogsSlice(TLObject):
    CONSTRUCTOR_ID = 0x71E094F3
    FIELDS = [
        TLField("count", "int", skip_cid=True),
        TLField("dialogs", "Dialog", is_vector=True),
        TLField("messages", "Message", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]

    count: Optional[int]
    dialogs: Optional[List[TLObject]]
    messages: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]


class MessagesDialogsNotModified(TLObject):
    CONSTRUCTOR_ID = 0xF0E3E596
    FIELDS = [TLField("count", "int")]
    count: Optional[int]


class MessagesAffectedMessages(TLObject):
    CONSTRUCTOR_ID = 0x84D19185
    FIELDS = [TLField("pts", "int"), TLField("pts_count", "int")]
    pts: Optional[int]
    pts_count: Optional[int]
