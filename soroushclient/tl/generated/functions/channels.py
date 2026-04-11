from soroushclient.tl.base import TLField, TLRequest


class GetFullChannelRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8736a09
    FIELDS = [
        TLField("channel", "InputChannel"),
    ]
class JoinChannelRequest(TLRequest):
    CONSTRUCTOR_ID = 0x24b524c5
    FIELDS = [
        TLField("channel", "InputChannel"),
    ]
class LeaveChannelRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf836aa95
    FIELDS = [
        TLField("channel", "InputChannel"),
    ]