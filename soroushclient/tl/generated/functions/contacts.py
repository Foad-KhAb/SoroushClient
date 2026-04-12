from soroushclient.tl.base import TLField, TLRequest
from soroushclient.tl.generated.types.contacts import Found, ResolvedPeer


class SearchRequest(TLRequest):
    CONSTRUCTOR_ID = 0x11F812D8
    RESPONSE_TYPE = Found
    FIELDS = [
        TLField("q", "string", skip_cid=True),
        TLField("limit", "int", skip_cid=True),
    ]


class ResolveUsername(TLRequest):
    CONSTRUCTOR_ID = 0xF93CCBA3
    RESPONSE_TYPE = ResolvedPeer
    FIELDS = [
        TLField("username", "string", skip_cid=True),
    ]
