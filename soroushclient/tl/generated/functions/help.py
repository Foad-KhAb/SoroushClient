from typing import Optional

from soroushclient.tl.base import TLObject, TLField, TLRequest


class GetConfig(TLRequest):
    CONSTRUCTOR_ID = 0xC4F9186B
    FIELDS = []

class GetNearestDc(TLRequest):
    CONSTRUCTOR_ID = 0x1FB33026
    FIELDS = []

class GetSupport(TLRequest):
    CONSTRUCTOR_ID = 0x9CDF08CD
    FIELDS = []

class AcceptTermsOfService(TLRequest):
    CONSTRUCTOR_ID = 0xEE72F79A
    FIELDS = [TLField("id", "DataJSON")]
    id: Optional[TLObject]

class GetAppConfig(TLRequest):
    CONSTRUCTOR_ID = 0x61E3F854
    FIELDS = [TLField("hash", "int")]
    hash: Optional[int]

class GetCountriesList(TLRequest):
    CONSTRUCTOR_ID = 0x735787A8
    FIELDS = [
        TLField("lang_code", "string"),
        TLField("hash", "int"),
    ]
    lang_code: Optional[str]
    hash: Optional[int]

class GetPremiumPromo(TLRequest):
    CONSTRUCTOR_ID = 0xB81B93D4
    FIELDS = []

class GetPeerColors(TLRequest):
    CONSTRUCTOR_ID = 0xDA80F42F
    FIELDS = [TLField("hash", "int")]
    hash: Optional[int]

class GetTimezonesList(TLRequest):
    CONSTRUCTOR_ID = 0x49B30240
    FIELDS = [TLField("hash", "int")]
    hash: Optional[int]