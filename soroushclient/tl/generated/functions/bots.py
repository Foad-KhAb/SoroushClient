from typing import Optional

from soroushclient.tl.base import TLField, TLObject, TLRequest


class CanSendMessage(TLRequest):
    CONSTRUCTOR_ID = 0x1359F4E6
    FIELDS = [TLField("bot", "InputUser")]
    bot: Optional[TLObject]

class AllowSendMessage(TLRequest):
    CONSTRUCTOR_ID = 0xF132E3EF
    FIELDS = [TLField("bot", "InputUser")]
    bot: Optional[TLObject]

class InvokeWebViewCustomMethod(TLRequest):
    CONSTRUCTOR_ID = 0x087FC5E7
    FIELDS = [
        TLField("bot", "InputUser"),
        TLField("custom_method", "string"),
        TLField("params", "DataJSON"),
    ]
    bot: Optional[TLObject]
    custom_method: Optional[str]
    params: Optional[TLObject]