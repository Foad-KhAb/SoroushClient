from soroushclient.tl.base import TLField, TLRequest
from soroushclient.tl.generated import Messages


class GetHistory(TLRequest):
    CONSTRUCTOR_ID = 0x44290685
    RESPONSE_TYPE = Messages
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
