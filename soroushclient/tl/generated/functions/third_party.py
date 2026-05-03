from typing import Optional

from soroushclient.tl.base import TLRequest, TLField, TLObject


class ThirdPartyRequest(TLRequest):
    CONSTRUCTOR_ID = 0xC8520739
    FIELDS = [TLField("message", "ThirdPartyMessage")]
    message: Optional[TLObject]

class ThirdPartyTell(TLRequest):
    CONSTRUCTOR_ID = 0xA7EBDF75
    FIELDS = [TLField("message", "ThirdPartyMessage")]
    message: Optional[TLObject]