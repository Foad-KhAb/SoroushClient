from soroushclient.tl.base import TLObject, TLField


class Updates(TLObject):
    CONSTRUCTOR_ID = 0x74ae4240
    FIELDS = [
        TLField("updates", "Update",  is_vector=True),
        TLField("users",   "User",    is_vector=True),
        TLField("chats",   "Chat",    is_vector=True),
        TLField("date",    "int"),
        TLField("seq",     "int"),
    ]
class UpdatesTooLong(TLObject):
    CONSTRUCTOR_ID = 0xe317af7e
    FIELDS = []

class UpdateShort(TLObject):
    CONSTRUCTOR_ID = 0x78d4dec1
    FIELDS = [TLField("update","Update"), TLField("date","int")]

class UpdatesCombined(TLObject):
    CONSTRUCTOR_ID = 0x725b04c3
    FIELDS = [
        TLField("updates",   "Update", is_vector=True),
        TLField("users",     "User",   is_vector=True),
        TLField("chats",     "Chat",   is_vector=True),
        TLField("date",      "int"),
        TLField("seq_start", "int"),
        TLField("seq",       "int"),
    ]

class UpdateShortSentMessage(TLObject):
    CONSTRUCTOR_ID = 0x9015e101
    FIELDS = [
        TLField("flags",      "int",  flag_group=0, flag_indicator=True),
        TLField("out",        "true", flag_group=0, flag_bit=1),
        TLField("id",         "int"),
        TLField("pts",        "int"),
        TLField("pts_count",  "int"),
        TLField("date",       "int"),
        TLField("media",      "MessageMedia",  flag_group=0, flag_bit=9),
        TLField("entities",   "MessageEntity", flag_group=0, flag_bit=7, is_vector=True),
        TLField("ttl_period", "int",  flag_group=0, flag_bit=25),
    ]

class UpdateNewMessage(TLObject):
    CONSTRUCTOR_ID = 0x1f2b0afd
    FIELDS = [TLField("message","Message"), TLField("pts","int"), TLField("pts_count","int")]

class UpdateNewChannelMessage(TLObject):
    CONSTRUCTOR_ID = 0x62ba04d9
    FIELDS = [TLField("message","Message"), TLField("pts","int"), TLField("pts_count","int")]

class UpdateEditMessage(TLObject):
    CONSTRUCTOR_ID = 0xe40370a3
    FIELDS = [TLField("message","Message"), TLField("pts","int"), TLField("pts_count","int")]

class UpdateEditChannelMessage(TLObject):
    CONSTRUCTOR_ID = 0x1b3f4df7
    FIELDS = [TLField("message","Message"), TLField("pts","int"), TLField("pts_count","int")]

class UpdateDeleteMessages(TLObject):
    CONSTRUCTOR_ID = 0xa20db0e5
    FIELDS = [TLField("messages","int",is_vector=True), TLField("pts","int"), TLField("pts_count","int")]

class UpdateReadHistoryInbox(TLObject):
    CONSTRUCTOR_ID = 0x9c974fdf
    FIELDS = [
        TLField("flags",              "int",  flag_group=0, flag_indicator=True),
        TLField("folder_id",          "int",  flag_group=0, flag_bit=0),
        TLField("peer",               "Peer"),
        TLField("max_id",             "int"),
        TLField("still_unread_count", "int"),
        TLField("pts",                "int"),
        TLField("pts_count",          "int"),
    ]

class UpdateReadHistoryOutbox(TLObject):
    CONSTRUCTOR_ID = 0x2f2f21bf
    FIELDS = [TLField("peer","Peer"), TLField("max_id","int"), TLField("pts","int"), TLField("pts_count","int")]

class UpdateUserStatus(TLObject):
    CONSTRUCTOR_ID = 0xe5bdf8de
    FIELDS = [TLField("user_id","long"), TLField("status","UserStatus")]

class UpdateChannel(TLObject):
    CONSTRUCTOR_ID = 0x635b4c09
    FIELDS = [TLField("channel_id","long")]

class UpdateUser(TLObject):
    CONSTRUCTOR_ID = 0x20529438
    FIELDS = [TLField("user_id","long")]

class UpdateMessageID(TLObject):
    CONSTRUCTOR_ID = 0x4e90bfd6
    FIELDS = [TLField("id","int"), TLField("random_id","long")]

class UpdateReadChannelInbox(TLObject):
    CONSTRUCTOR_ID = 0x922e6e10
    FIELDS = [
        TLField("flags",              "int",  flag_group=0, flag_indicator=True),
        TLField("folder_id",          "int",  flag_group=0, flag_bit=0),
        TLField("channel_id",         "long"),
        TLField("max_id",             "int"),
        TLField("still_unread_count", "int"),
        TLField("pts",                "int"),
    ]

class UpdateDraftMessage(TLObject):
    CONSTRUCTOR_ID = 0x1b49ec6d
    FIELDS = [
        TLField("flags",       "int",  flag_group=0, flag_indicator=True),
        TLField("peer",        "Peer"),
        TLField("top_msg_id",  "int",  flag_group=0, flag_bit=0),
        TLField("draft",       "DraftMessage"),
    ]

class UpdateDialogPinned(TLObject):
    CONSTRUCTOR_ID = 0x6e6fe51c
    FIELDS = [
        TLField("flags",     "int",  flag_group=0, flag_indicator=True),
        TLField("pinned",    "true", flag_group=0, flag_bit=0),
        TLField("folder_id", "int",  flag_group=0, flag_bit=1),
        TLField("peer",      "DialogPeer"),
    ]

class UpdateNotifySettings(TLObject):
    CONSTRUCTOR_ID = 0xbec268ef
    FIELDS = [TLField("peer","NotifyPeer"), TLField("notify_settings","PeerNotifySettings")]

class UpdatePeerBlocked(TLObject):
    CONSTRUCTOR_ID = 0xebe07752
    FIELDS = [
        TLField("flags",                    "int",  flag_group=0, flag_indicator=True),
        TLField("blocked",                  "true", flag_group=0, flag_bit=0),
        TLField("blocked_my_stories_from",  "true", flag_group=0, flag_bit=1),
        TLField("peer_id",                  "Peer"),
    ]
