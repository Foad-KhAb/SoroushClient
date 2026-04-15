from soroushclient.tl.base import TLField, TLRequest


class GetFullChannelRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8736A09
    FIELDS = [
        TLField("channel", "InputChannel"),
    ]


class JoinChannelRequest(TLRequest):
    CONSTRUCTOR_ID = 0x24B524C5
    FIELDS = [
        TLField("channel", "InputChannel"),
    ]


class LeaveChannelRequest(TLRequest):
    CONSTRUCTOR_ID = 0xF836AA95
    FIELDS = [
        TLField("channel", "InputChannel"),
    ]
