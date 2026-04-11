from soroushclient.tl.base import TLField, TLObject


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


class MessagesDialogs(TLObject):
    """messages.dialogs#15ba6c40"""

    CONSTRUCTOR_ID = 0x15BA6C40
    FIELDS = [
        TLField("dialogs", "Dialog", is_vector=True),
        TLField("messages", "Message", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]


class MessagesDialogsSlice(TLObject):
    """messages.dialogsSlice#71e094f3"""

    CONSTRUCTOR_ID = 0x71E094F3
    FIELDS = [
        TLField("count", "int"),
        TLField("dialogs", "Dialog", is_vector=True),
        TLField("messages", "Message", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]


class MessagesDialogsNotModified(TLObject):
    CONSTRUCTOR_ID = 0xF0E3E596
    FIELDS = [TLField("count", "int")]


class MessagesAffectedMessages(TLObject):
    CONSTRUCTOR_ID = 0x84D19185
    FIELDS = [TLField("pts", "int"), TLField("pts_count", "int")]
