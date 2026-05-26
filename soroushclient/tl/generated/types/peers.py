from typing import Optional

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
    chat_id: Optional[int]

class InputPeerUser(TLObject):
    CONSTRUCTOR_ID = 0xDDE8A54C
    FIELDS = [
        TLField("user_id", "long"),
        TLField("access_hash", "long"),
    ]
    user_id: Optional[int]
    access_hash: Optional[int]

class InputPeerChannel(TLObject):
    CONSTRUCTOR_ID = 0x27BCBBFC
    FIELDS = [
        TLField("channel_id", "long"),
        TLField("access_hash", "long"),
    ]
    channel_id: Optional[int]
    access_hash: Optional[int]

class InputPeerUserFromMessage(TLObject):
    CONSTRUCTOR_ID = 0xA87B0A1C
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
        TLField("user_id", "long"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    user_id: Optional[int]

class InputPeerChannelFromMessage(TLObject):
    CONSTRUCTOR_ID = 0xBD2A0840
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
        TLField("channel_id", "long"),
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
        TLField("user_id", "long"),
        TLField("access_hash", "long"),
    ]
    user_id: Optional[int]
    access_hash: Optional[int]

class InputUserFromMessage(TLObject):
    CONSTRUCTOR_ID = 0x1DA448E2
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
        TLField("user_id", "long"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    user_id: Optional[int]

class PeerUser(TLObject):
    CONSTRUCTOR_ID = 0x59511722
    FIELDS = [TLField("user_id", "long")]
    user_id: Optional[int]

class PeerChat(TLObject):
    CONSTRUCTOR_ID = 0x36C6019A
    FIELDS = [TLField("chat_id", "long")]
    chat_id: Optional[int]

class PeerChannel(TLObject):
    CONSTRUCTOR_ID = 0xA2A5371E
    FIELDS = [TLField("channel_id", "long")]
    channel_id: Optional[int]

class InputChannelEmpty(TLObject):
    CONSTRUCTOR_ID = 0xEE8C1E86
    FIELDS = []

class InputChannel(TLObject):
    CONSTRUCTOR_ID = 0xF35AEC28
    FIELDS = [
        TLField("channel_id", "long"),
        TLField("access_hash", "long"),
    ]
    channel_id: Optional[int]
    access_hash: Optional[int]

class InputChannelFromMessage(TLObject):
    CONSTRUCTOR_ID = 0x5B934F9D
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
        TLField("channel_id", "long"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    channel_id: Optional[int]