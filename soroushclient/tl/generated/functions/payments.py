from typing import Optional

from soroushclient.tl.base import TLField, TLObject, TLRequest


class GetPaymentForm(TLRequest):
    CONSTRUCTOR_ID = 0x37148DBB
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("invoice", "InputInvoice"),
        TLField("theme_params", "DataJSON", flag_group=0, flag_bit=0),
    ]
    invoice: Optional[TLObject]
    theme_params: Optional[TLObject]

class GetPaymentReceipt(TLRequest):
    CONSTRUCTOR_ID = 0x2478D1CC
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]

class ValidateRequestedInfo(TLRequest):
    CONSTRUCTOR_ID = 0xB6C8F12B
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("save", "true", flag_group=0, flag_bit=0),
        TLField("invoice", "InputInvoice"),
        TLField("info", "PaymentRequestedInfo"),
    ]
    save: Optional[bool]
    invoice: Optional[TLObject]
    info: Optional[TLObject]

class SendPaymentForm(TLRequest):
    CONSTRUCTOR_ID = 0x2D03522F
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("form_id", "long"),
        TLField("invoice", "InputInvoice"),
        TLField("requested_info_id", "string", flag_group=0, flag_bit=0),
        TLField("shipping_option_id", "string", flag_group=0, flag_bit=1),
        TLField("credentials", "InputPaymentCredentials"),
        TLField("tip_amount", "long", flag_group=0, flag_bit=2),
    ]
    form_id: Optional[int]
    invoice: Optional[TLObject]
    requested_info_id: Optional[str]
    shipping_option_id: Optional[str]
    credentials: Optional[TLObject]
    tip_amount: Optional[int]

class GetSavedInfo(TLRequest):
    CONSTRUCTOR_ID = 0x227D824B
    FIELDS = []

class CheckGiftCode(TLRequest):
    CONSTRUCTOR_ID = 0x8E51B4C1
    FIELDS = [TLField("slug", "string")]
    slug: Optional[str]

class ApplyGiftCode(TLRequest):
    CONSTRUCTOR_ID = 0xF6E26854
    FIELDS = [TLField("slug", "string")]
    slug: Optional[str]

class GetGiveawayInfo(TLRequest):
    CONSTRUCTOR_ID = 0xF4239425
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]