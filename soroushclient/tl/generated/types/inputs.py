from typing import Optional

from soroushclient.tl.base import TLField, TLObject
from soroushclient.tl.generated.types.base_types import InputPeer


class InputPeerEmpty(InputPeer):
    CONSTRUCTOR_ID = 0x7F3B18EA
    FIELDS = []


class InputPeerSelf(InputPeer):
    CONSTRUCTOR_ID = 0x7DA07EC9
    FIELDS = []


class InputPeerChat(InputPeer):
    CONSTRUCTOR_ID = 0x35A95CB9
    FIELDS = [
        TLField("chat_id", "long", skip_cid=True),
    ]

    chat_id: Optional[int]


class InputPeerUser(InputPeer):
    CONSTRUCTOR_ID = 0xDDE8A54C
    FIELDS = [
        TLField("user_id", "long", skip_cid=True),
        TLField("access_hash", "long", skip_cid=True),
    ]

    user_id: Optional[int]
    access_hash: Optional[int]


class InputPeerChannel(InputPeer):
    CONSTRUCTOR_ID = 0x27BCBBFC
    FIELDS = [
        TLField("channel_id", "long", skip_cid=True),
        TLField("access_hash", "long", skip_cid=True),
    ]

    channel_id: Optional[int]
    access_hash: Optional[int]


class InputPeerUserFromMessage(InputPeer):
    CONSTRUCTOR_ID = 0xA87B0A1C
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int", skip_cid=True),
        TLField("user_id", "long", skip_cid=True),
    ]

    peer: Optional[TLObject]
    msg_id: Optional[int]
    user_id: Optional[int]


class InputPeerChannelFromMessage(InputPeer):
    CONSTRUCTOR_ID = 0xBD2A0840
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int", skip_cid=True),
        TLField("channel_id", "long", skip_cid=True),
    ]

    peer: Optional[TLObject]
    msg_id: Optional[int]
    channel_id: Optional[int]


class InputUserEmpty(TLObject):
    CONSTRUCTOR_ID = 0xB98886CF
    FIELDS = []


class InputUserSelf(TLObject):
    CONSTRUCTOR_ID = 0xF7C1B13F
    FIELDS = []


class InputUser(TLObject):
    CONSTRUCTOR_ID = 0xF21158C6
    FIELDS = [
        TLField("user_id", "long", skip_cid=True),
        TLField("access_hash", "long", skip_cid=True),
    ]

    user_id: Optional[int]
    access_hash: Optional[int]


class InputUserFromMessage(TLObject):
    CONSTRUCTOR_ID = 0x1DA448E2
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int", skip_cid=True),
        TLField("user_id", "long", skip_cid=True),
    ]

    peer: Optional[TLObject]
    msg_id: Optional[int]
    user_id: Optional[int]


class InputStickerSetEmpty(TLObject):
    CONSTRUCTOR_ID = 0xFFB62B95
    FIELDS = []


class InputStickerSetID(TLObject):
    CONSTRUCTOR_ID = 0x9DE7A269
    FIELDS = [
        TLField("id", "long", skip_cid=True),
        TLField("access_hash", "long", skip_cid=True),
    ]

    id: Optional[int]
    access_hash: Optional[int]


class InputStickerSetShortName(TLObject):
    CONSTRUCTOR_ID = 0x861CC8A0
    FIELDS = [
        TLField("short_name", "string"),
    ]

    short_name: Optional[str]


class InputGroupCallStream(TLObject):
    CONSTRUCTOR_ID = 0x598A92A
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("call", "InputGroupCall"),
        TLField("time_ms", "long", skip_cid=True),
        TLField("scale", "int", skip_cid=True),
        TLField("video_channel", "int", flag_group=0, flag_bit=0, skip_cid=True),
        TLField("video_quality", "int", flag_group=0, flag_bit=0, skip_cid=True),
    ]

    call: Optional[TLObject]
    time_ms: Optional[int]
    scale: Optional[int]
    video_channel: Optional[int]
    video_quality: Optional[int]


class InputChannel(TLObject):
    CONSTRUCTOR_ID = 0xF35AEC28
    FIELDS = [
        TLField("channel_id", "long", skip_cid=True),
        TLField("access_hash", "long", skip_cid=True),
    ]

    channel_id: Optional[int]
    access_hash: Optional[int]


class InputChannelEmpty(TLObject):
    CONSTRUCTOR_ID = 0xEE8C1E86
    FIELDS = []
