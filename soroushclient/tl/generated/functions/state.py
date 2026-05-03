from typing import Optional

from soroushclient.tl.base import TLField, TLObject, TLRequest


class GetBroadcastStats(TLRequest):
    CONSTRUCTOR_ID = 0xAB42441A
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("dark", "true", flag_group=0, flag_bit=0),
        TLField("channel", "InputChannel"),
    ]
    dark: Optional[bool]
    channel: Optional[TLObject]

class LoadAsyncGraph(TLRequest):
    CONSTRUCTOR_ID = 0x621D5FA0
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("token", "string"),
        TLField("x", "long", flag_group=0, flag_bit=0),
    ]
    token: Optional[str]
    x: Optional[int]

class GetMegagroupStats(TLRequest):
    CONSTRUCTOR_ID = 0xDCDF8607
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("dark", "true", flag_group=0, flag_bit=0),
        TLField("channel", "InputChannel"),
    ]
    dark: Optional[bool]
    channel: Optional[TLObject]

class GetMessagePublicForwards(TLRequest):
    CONSTRUCTOR_ID = 0x5630281B
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("msg_id", "int"),
        TLField("offset_rate", "int"),
        TLField("offset_peer", "InputPeer"),
        TLField("offset_id", "int"),
        TLField("limit", "int"),
    ]
    channel: Optional[TLObject]
    msg_id: Optional[int]
    offset_rate: Optional[int]
    offset_peer: Optional[TLObject]
    offset_id: Optional[int]
    limit: Optional[int]

class GetMessageStats(TLRequest):
    CONSTRUCTOR_ID = 0xB6E0A3F5
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("dark", "true", flag_group=0, flag_bit=0),
        TLField("channel", "InputChannel"),
        TLField("msg_id", "int"),
    ]
    dark: Optional[bool]
    channel: Optional[TLObject]
    msg_id: Optional[int]

class GetStoryStats(TLRequest):
    CONSTRUCTOR_ID = 0x374FEF40
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("dark", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputPeer"),
        TLField("id", "int"),
    ]
    dark: Optional[bool]
    peer: Optional[TLObject]
    id: Optional[int]

class GetStoryPublicForwards(TLRequest):
    CONSTRUCTOR_ID = 0xA6437EF6
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int"),
        TLField("offset", "string"),
        TLField("limit", "int"),
    ]
    peer: Optional[TLObject]
    id: Optional[int]
    offset: Optional[str]
    limit: Optional[int]