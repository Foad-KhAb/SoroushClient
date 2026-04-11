from soroushclient.tl.base import TLField, TLObject


class InputPeerEmpty(TLObject):
    CONSTRUCTOR_ID = 0x7F3B18EA
    FIELDS = []


class InputPeerSelf(TLObject):
    CONSTRUCTOR_ID = 0x7DA07EC9
    FIELDS = []


class InputPeerChat(TLObject):
    CONSTRUCTOR_ID = 0x35A95CB9
    FIELDS = [TLField("chat_id", "long")]


class InputPeerUser(TLObject):
    CONSTRUCTOR_ID = 0xDDE8A54C
    FIELDS = [TLField("user_id", "long"), TLField("access_hash", "long")]


class InputPeerChannel(TLObject):
    CONSTRUCTOR_ID = 0x27BCBBFC
    FIELDS = [TLField("channel_id", "long"), TLField("access_hash", "long")]


class InputPeerUserFromMessage(TLObject):
    CONSTRUCTOR_ID = 0xA87B0A1C
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
        TLField("user_id", "long"),
    ]


class InputPeerChannelFromMessage(TLObject):
    CONSTRUCTOR_ID = 0xBD2A0840
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
        TLField("channel_id", "long"),
    ]


class InputUserEmpty(TLObject):
    CONSTRUCTOR_ID = 0xB98886CF
    FIELDS = []


class InputUserSelf(TLObject):
    CONSTRUCTOR_ID = 0xF7C1B13F
    FIELDS = []


class InputUser(TLObject):
    CONSTRUCTOR_ID = 0xF21158C6
    FIELDS = [TLField("user_id", "long"), TLField("access_hash", "long")]


class InputUserFromMessage(TLObject):
    CONSTRUCTOR_ID = 0x1DA448E2
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
        TLField("user_id", "long"),
    ]


class InputStickerSetEmpty(TLObject):
    CONSTRUCTOR_ID = 0xFFB62B95
    FIELDS = []


class InputStickerSetID(TLObject):
    CONSTRUCTOR_ID = 0x9DE7A269
    FIELDS = [TLField("id", "long"), TLField("access_hash", "long")]


class InputStickerSetShortName(TLObject):
    CONSTRUCTOR_ID = 0x861CC8A0
    FIELDS = [TLField("short_name", "string")]


class InputGroupCallStream(TLObject):
    CONSTRUCTOR_ID = 0x598A92A
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("call", "InputGroupCall"),
        TLField("time_ms", "long"),
        TLField("scale", "int"),
        TLField("video_channel", "int", flag_group=0, flag_bit=0),
        TLField("video_quality", "int", flag_group=0, flag_bit=0),
    ]


class InputChannel(TLObject):
    CONSTRUCTOR_ID = 0xF35AEC28
    FIELDS = [
        TLField("channel_id", "long"),
        TLField("access_hash", "long"),
    ]


class InputChannelEmpty(TLObject):
    CONSTRUCTOR_ID = 0xEE8C1E86
    FIELDS = []
