from soroushclient.tl.base import TLField, TLObject


class Updates(TLObject):
    CONSTRUCTOR_ID = 0x74AE4240
    FIELDS = [
        TLField("updates", "Update", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("date", "int"),
        TLField("seq", "int"),
    ]


class UpdatesTooLong(TLObject):
    CONSTRUCTOR_ID = 0xE317AF7E
    FIELDS = []


class UpdateShort(TLObject):
    CONSTRUCTOR_ID = 0x78D4DEC1
    FIELDS = [TLField("update", "Update"), TLField("date", "int")]


class UpdatesCombined(TLObject):
    CONSTRUCTOR_ID = 0x725B04C3
    FIELDS = [
        TLField("updates", "Update", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("date", "int"),
        TLField("seq_start", "int"),
        TLField("seq", "int"),
    ]


class UpdateShortSentMessage(TLObject):
    CONSTRUCTOR_ID = 0x9015E101
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("out", "true", flag_group=0, flag_bit=1),
        TLField("id", "int"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
        TLField("date", "int"),
        TLField("media", "MessageMedia", flag_group=0, flag_bit=9),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=7, is_vector=True),
        TLField("ttl_period", "int", flag_group=0, flag_bit=25),
    ]


class UpdateNewMessage(TLObject):
    CONSTRUCTOR_ID = 0x1F2B0AFD
    FIELDS = [
        TLField("message", "Message"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]


class UpdateNewChannelMessage(TLObject):
    CONSTRUCTOR_ID = 0x62BA04D9
    FIELDS = [
        TLField("message", "Message"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]


class UpdateEditMessage(TLObject):
    CONSTRUCTOR_ID = 0xE40370A3
    FIELDS = [
        TLField("message", "Message"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]


class UpdateEditChannelMessage(TLObject):
    CONSTRUCTOR_ID = 0x1B3F4DF7
    FIELDS = [
        TLField("message", "Message"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]


class UpdateDeleteMessages(TLObject):
    CONSTRUCTOR_ID = 0xA20DB0E5
    FIELDS = [
        TLField("messages", "int", is_vector=True),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]


class UpdateReadHistoryInbox(TLObject):
    CONSTRUCTOR_ID = 0x9C974FDF
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("folder_id", "int", flag_group=0, flag_bit=0),
        TLField("peer", "Peer"),
        TLField("max_id", "int"),
        TLField("still_unread_count", "int"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]


class UpdateReadHistoryOutbox(TLObject):
    CONSTRUCTOR_ID = 0x2F2F21BF
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("max_id", "int"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]


class UpdateUserStatus(TLObject):
    CONSTRUCTOR_ID = 0xE5BDF8DE
    FIELDS = [TLField("user_id", "long"), TLField("status", "UserStatus")]


class UpdateChannel(TLObject):
    CONSTRUCTOR_ID = 0x635B4C09
    FIELDS = [TLField("channel_id", "long")]


class UpdateUser(TLObject):
    CONSTRUCTOR_ID = 0x20529438
    FIELDS = [TLField("user_id", "long")]


class UpdateMessageID(TLObject):
    CONSTRUCTOR_ID = 0x4E90BFD6
    FIELDS = [TLField("id", "int"), TLField("random_id", "long")]


class UpdateReadChannelInbox(TLObject):
    CONSTRUCTOR_ID = 0x922E6E10
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("folder_id", "int", flag_group=0, flag_bit=0),
        TLField("channel_id", "long"),
        TLField("max_id", "int"),
        TLField("still_unread_count", "int"),
        TLField("pts", "int"),
    ]


class UpdateDraftMessage(TLObject):
    CONSTRUCTOR_ID = 0x1B49EC6D
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "Peer"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=0),
        TLField("draft", "DraftMessage"),
    ]


class UpdateDialogPinned(TLObject):
    CONSTRUCTOR_ID = 0x6E6FE51C
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("pinned", "true", flag_group=0, flag_bit=0),
        TLField("folder_id", "int", flag_group=0, flag_bit=1),
        TLField("peer", "DialogPeer"),
    ]


class UpdateNotifySettings(TLObject):
    CONSTRUCTOR_ID = 0xBEC268EF
    FIELDS = [
        TLField("peer", "NotifyPeer"),
        TLField("notify_settings", "PeerNotifySettings"),
    ]


class UpdatePeerBlocked(TLObject):
    CONSTRUCTOR_ID = 0xEBE07752
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("blocked", "true", flag_group=0, flag_bit=0),
        TLField("blocked_my_stories_from", "true", flag_group=0, flag_bit=1),
        TLField("peer_id", "Peer"),
    ]
