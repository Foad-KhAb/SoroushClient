from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField, TLRequest


class GetBoostsList(TLRequest):
    CONSTRUCTOR_ID = 0x60F67660
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("gifts", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputPeer"),
        TLField("offset", "string"),
        TLField("limit", "int"),
    ]
    gifts: Optional[bool]
    peer: Optional[TLObject]
    offset: Optional[str]
    limit: Optional[int]

class GetMyBoosts(TLRequest):
    CONSTRUCTOR_ID = 0x0BE77B4A
    FIELDS = []

class ApplyBoost(TLRequest):
    CONSTRUCTOR_ID = 0x6B7DA746
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("slots", "int", flag_group=0, flag_bit=0, is_vector=True),
        TLField("peer", "InputPeer"),
    ]
    slots: Optional[List[int]]
    peer: Optional[TLObject]

class GetBoostsStatus(TLRequest):
    CONSTRUCTOR_ID = 0x042F1F61
    FIELDS = [TLField("peer", "InputPeer")]
    peer: Optional[TLObject]