from typing import List, Optional

from soroushclient.tl.base import TLField, TLRequest
from soroushclient.tl.generated import BaseMessage, InputPeer, MessageViews, Updates


class GetHistoryRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4423E6C5
    RESPONSE_TYPE = BaseMessage
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("offset_id", "int", skip_cid=True),
        TLField("offset_date", "int", skip_cid=True),
        TLField("add_offset", "int", skip_cid=True),
        TLField("limit", "int", skip_cid=True),
        TLField("max_id", "long", skip_cid=True),
        TLField("min_id", "long", skip_cid=True),
        TLField("hash", "long", skip_cid=True),
    ]
    peer: Optional[InputPeer]
    offset_id: Optional[int]
    offset_date: Optional[int]
    add_offset: Optional[int]
    limit: Optional[int]
    max_id: Optional[int]
    min_id: Optional[int]
    hash: Optional[int]


class ImportChatInvite(TLRequest):
    CONSTRUCTOR_ID = 0x6C50051C
    RESPONSE_TYPE = Updates
    FIELDS = [
        TLField("hash", "string", skip_cid=True),
    ]
    hash: str


class GetMessagesViews(TLRequest):
    CONSTRUCTOR_ID = 0x5784D3E1
    RESPONSE_TYPE = MessageViews
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int", skip_cid=True, is_vector=True),
        TLField("increment", "Bool"),
    ]

    peer: Optional[InputPeer]
    id: Optional[List[int]]
    increment: Optional[bool]
