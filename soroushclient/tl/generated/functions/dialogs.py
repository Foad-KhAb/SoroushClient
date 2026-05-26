from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField, TLRequest


class GetDialogsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xA0F4CB4F
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("exclude_pinned", "true", flag_group=0, flag_bit=0),
        TLField("folder_id", "int", flag_group=0, flag_bit=1),
        TLField("offset_date", "int"),
        TLField("offset_id", "int"),
        TLField("offset_peer", "InputPeer"),
        TLField("limit", "int"),
        TLField("hash", "long"),
    ]
    exclude_pinned: Optional[bool]
    folder_id: Optional[int]
    offset_date: Optional[int]
    offset_id: Optional[int]
    offset_peer: Optional[TLObject]
    limit: Optional[int]
    hash: Optional[int]

class GetPinnedDialogs(TLRequest):
    CONSTRUCTOR_ID = 0xD6B94DF2
    FIELDS = [TLField("folder_id", "int")]
    folder_id: Optional[int]

class ToggleDialogPin(TLRequest):
    CONSTRUCTOR_ID = 0xA731E257
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("pinned", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputDialogPeer"),
    ]
    pinned: Optional[bool]
    peer: Optional[TLObject]

class GetPeerDialogs(TLRequest):
    CONSTRUCTOR_ID = 0xE470BCFD
    FIELDS = [TLField("peers", "InputDialogPeer", is_vector=True)]
    peers: Optional[List[TLObject]]

class MarkDialogUnread(TLRequest):
    CONSTRUCTOR_ID = 0xC286D98F
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("unread", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputDialogPeer"),
    ]
    unread: Optional[bool]
    peer: Optional[TLObject]

class GetDialogFilters(TLRequest):
    CONSTRUCTOR_ID = 0xEFD48C89
    FIELDS = []

class GetSuggestedDialogFilters(TLRequest):
    CONSTRUCTOR_ID = 0xA29CD42C
    FIELDS = []

class UpdateDialogFilter(TLRequest):
    CONSTRUCTOR_ID = 0x1AD4A04A
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("id", "int"),
        TLField("filter", "DialogFilter", flag_group=0, flag_bit=0),
    ]
    id: Optional[int]
    filter: Optional[TLObject]

class UpdateDialogFiltersOrder(TLRequest):
    CONSTRUCTOR_ID = 0xC563C1E4
    FIELDS = [TLField("order", "int", is_vector=True)]
    order: Optional[List[int]]

class ToggleDialogFilterTags(TLRequest):
    CONSTRUCTOR_ID = 0xFD2DDA49
    FIELDS = [TLField("enabled", "Bool")]
    enabled: Optional[bool]