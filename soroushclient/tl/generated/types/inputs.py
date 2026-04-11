from soroushclient.tl.base import TLObject, TLField


class InputPeerEmpty(TLObject):
    CONSTRUCTOR_ID = 0x7f3b18ea
    FIELDS = []

class InputPeerSelf(TLObject):
    CONSTRUCTOR_ID = 0x7da07ec9
    FIELDS = []

class InputPeerChat(TLObject):
    CONSTRUCTOR_ID = 0x35a95cb9
    FIELDS = [TLField("chat_id", "long")]

class InputPeerUser(TLObject):
    CONSTRUCTOR_ID = 0xdde8a54c
    FIELDS = [TLField("user_id", "long"), TLField("access_hash", "long")]

class InputPeerChannel(TLObject):
    CONSTRUCTOR_ID = 0x27bcbbfc
    FIELDS = [TLField("channel_id", "long"), TLField("access_hash", "long")]

class InputPeerUserFromMessage(TLObject):
    CONSTRUCTOR_ID = 0xa87b0a1c
    FIELDS = [TLField("peer", "InputPeer"), TLField("msg_id", "int"), TLField("user_id", "long")]

class InputPeerChannelFromMessage(TLObject):
    CONSTRUCTOR_ID = 0xbd2a0840
    FIELDS = [TLField("peer", "InputPeer"), TLField("msg_id", "int"), TLField("channel_id", "long")]

class InputUserEmpty(TLObject):
    CONSTRUCTOR_ID = 0xb98886cf
    FIELDS = []

class InputUserSelf(TLObject):
    CONSTRUCTOR_ID = 0xf7c1b13f
    FIELDS = []

class InputUser(TLObject):
    CONSTRUCTOR_ID = 0xf21158c6
    FIELDS = [TLField("user_id", "long"), TLField("access_hash", "long")]

class InputUserFromMessage(TLObject):
    CONSTRUCTOR_ID = 0x1da448e2
    FIELDS = [TLField("peer", "InputPeer"), TLField("msg_id", "int"), TLField("user_id", "long")]


class InputStickerSetEmpty(TLObject):
    CONSTRUCTOR_ID = 0xffb62b95
    FIELDS = []

class InputStickerSetID(TLObject):
    CONSTRUCTOR_ID = 0x9de7a269
    FIELDS = [TLField("id","long"), TLField("access_hash","long")]

class InputStickerSetShortName(TLObject):
    CONSTRUCTOR_ID = 0x861cc8a0
    FIELDS = [TLField("short_name","string")]

class InputGroupCallStream(TLObject):
    CONSTRUCTOR_ID = 0x598a92a
    FIELDS = [
        TLField("flags",          "int",            flag_group=0, flag_indicator=True),
        TLField("call",           "InputGroupCall"),
        TLField("time_ms",        "long"),
        TLField("scale",          "int"),
        TLField("video_channel",  "int",            flag_group=0, flag_bit=0),
        TLField("video_quality",  "int",            flag_group=0, flag_bit=0),
    ]

class InputChannel(TLObject):
    CONSTRUCTOR_ID = 0xf35aec28
    FIELDS = [
        TLField("channel_id",   "long"),
        TLField("access_hash",  "long"),
    ]
class InputChannelEmpty(TLObject):
    CONSTRUCTOR_ID = 0xee8c1e86
    FIELDS = []
