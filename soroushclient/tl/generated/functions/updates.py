from typing import Optional

from soroushclient.tl.base import TLField, TLObject, TLRequest


class GetState(TLRequest):
    CONSTRUCTOR_ID = 0xEDD4882A
    FIELDS = []

class GetDifference(TLRequest):
    CONSTRUCTOR_ID = 0x19C2F763
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("pts", "int"),
        TLField("pts_limit", "int", flag_group=0, flag_bit=1),
        TLField("pts_total_limit", "int", flag_group=0, flag_bit=0),
        TLField("date", "int"),
        TLField("qts", "int"),
        TLField("qts_limit", "int", flag_group=0, flag_bit=2),
    ]
    pts: Optional[int]
    pts_limit: Optional[int]
    pts_total_limit: Optional[int]
    date: Optional[int]
    qts: Optional[int]
    qts_limit: Optional[int]

class GetChannelDifference(TLRequest):
    CONSTRUCTOR_ID = 0x03173D78
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("force", "true", flag_group=0, flag_bit=0),
        TLField("channel", "InputChannel"),
        TLField("filter", "ChannelMessagesFilter"),
        TLField("pts", "int"),
        TLField("limit", "int"),
    ]
    force: Optional[bool]
    channel: Optional[TLObject]
    filter: Optional[TLObject]
    pts: Optional[int]
    limit: Optional[int]

class ToggleMembershipMessageVisibility(TLObject):
    CONSTRUCTOR_ID = 0x075646C0
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("enabled", "Bool", skip_cid=False),
    ]