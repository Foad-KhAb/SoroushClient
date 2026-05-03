from typing import Optional, List

from soroushclient.tl.base import TLField, TLObject


class LabeledPrice(TLObject):
    CONSTRUCTOR_ID = 0xCB296BF8
    FIELDS = [
        TLField("label", "string"),
        TLField("amount", "long"),
    ]
    label: Optional[str]
    amount: Optional[int]

class Invoice(TLObject):
    CONSTRUCTOR_ID = 0x5DB95A15
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("test", "true", flag_group=0, flag_bit=0),
        TLField("name_requested", "true", flag_group=0, flag_bit=1),
        TLField("phone_requested", "true", flag_group=0, flag_bit=2),
        TLField("email_requested", "true", flag_group=0, flag_bit=3),
        TLField("shipping_address_requested", "true", flag_group=0, flag_bit=4),
        TLField("flexible", "true", flag_group=0, flag_bit=5),
        TLField("phone_to_provider", "true", flag_group=0, flag_bit=6),
        TLField("email_to_provider", "true", flag_group=0, flag_bit=7),
        TLField("recurring", "true", flag_group=0, flag_bit=9),
        TLField("currency", "string"),
        TLField("prices", "LabeledPrice", is_vector=True),
        TLField("max_tip_amount", "long", flag_group=0, flag_bit=8),
        TLField("suggested_tip_amounts", "long", flag_group=0, flag_bit=8, is_vector=True),
        TLField("terms_url", "string", flag_group=0, flag_bit=10),
    ]
    test: Optional[bool]
    name_requested: Optional[bool]
    phone_requested: Optional[bool]
    email_requested: Optional[bool]
    shipping_address_requested: Optional[bool]
    flexible: Optional[bool]
    phone_to_provider: Optional[bool]
    email_to_provider: Optional[bool]
    recurring: Optional[bool]
    currency: Optional[str]
    prices: Optional[List[TLObject]]
    max_tip_amount: Optional[int]
    suggested_tip_amounts: Optional[List[int]]
    terms_url: Optional[str]

class PaymentCharge(TLObject):
    CONSTRUCTOR_ID = 0xEA02C27E
    FIELDS = [
        TLField("id", "string"),
        TLField("provider_charge_id", "string"),
    ]
    id: Optional[str]
    provider_charge_id: Optional[str]

class PostAddress(TLObject):
    CONSTRUCTOR_ID = 0x1E8CAAEB
    FIELDS = [
        TLField("street_line1", "string"),
        TLField("street_line2", "string"),
        TLField("city", "string"),
        TLField("state", "string"),
        TLField("country_iso2", "string"),
        TLField("post_code", "string"),
    ]
    street_line1: Optional[str]
    street_line2: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country_iso2: Optional[str]
    post_code: Optional[str]

class PaymentRequestedInfo(TLObject):
    CONSTRUCTOR_ID = 0x909C3F94
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("name", "string", flag_group=0, flag_bit=0),
        TLField("phone", "string", flag_group=0, flag_bit=1),
        TLField("email", "string", flag_group=0, flag_bit=2),
        TLField("shipping_address", "PostAddress", flag_group=0, flag_bit=3),
    ]
    name: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    shipping_address: Optional[TLObject]

class PaymentSavedCredentialsCard(TLObject):
    CONSTRUCTOR_ID = 0xCDC27A1F
    FIELDS = [
        TLField("id", "string"),
        TLField("title", "string"),
    ]
    id: Optional[str]
    title: Optional[str]

class ShippingOption(TLObject):
    CONSTRUCTOR_ID = 0xB6213CDF
    FIELDS = [
        TLField("id", "string"),
        TLField("title", "string"),
        TLField("prices", "LabeledPrice", is_vector=True),
    ]
    id: Optional[str]
    title: Optional[str]
    prices: Optional[List[TLObject]]

class InputPaymentCredentialsSaved(TLObject):
    CONSTRUCTOR_ID = 0xC10EB2CF
    FIELDS = [
        TLField("id", "string"),
        TLField("tmp_password", "bytes"),
    ]
    id: Optional[str]
    tmp_password: Optional[bytes]

class InputPaymentCredentials(TLObject):
    CONSTRUCTOR_ID = 0x3417D728
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("save", "true", flag_group=0, flag_bit=0),
        TLField("data", "DataJSON"),
    ]
    save: Optional[bool]
    data: Optional[TLObject]

class InputPaymentCredentialsApplePay(TLObject):
    CONSTRUCTOR_ID = 0x0AA1C39F
    FIELDS = [TLField("payment_data", "DataJSON")]
    payment_data: Optional[TLObject]

class InputPaymentCredentialsGooglePay(TLObject):
    CONSTRUCTOR_ID = 0x8AC32801
    FIELDS = [TLField("payment_token", "DataJSON")]
    payment_token: Optional[TLObject]

class PaymentFormMethod(TLObject):
    CONSTRUCTOR_ID = 0x88F8F21B
    FIELDS = [
        TLField("url", "string"),
        TLField("title", "string"),
    ]
    url: Optional[str]
    title: Optional[str]

class InputInvoiceMessage(TLObject):
    CONSTRUCTOR_ID = 0xC5B56859
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]

class InputInvoiceSlug(TLObject):
    CONSTRUCTOR_ID = 0xC326CAEF
    FIELDS = [TLField("slug", "string")]
    slug: Optional[str]

class InputInvoicePremiumGiftCode(TLObject):
    CONSTRUCTOR_ID = 0x98986C0D
    FIELDS = [
        TLField("purpose", "InputStorePaymentPurpose"),
        TLField("option", "PremiumGiftCodeOption"),
    ]
    purpose: Optional[TLObject]
    option: Optional[TLObject]

class InputStorePaymentPremiumSubscription(TLObject):
    CONSTRUCTOR_ID = 0xA6751E66
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("restore", "true", flag_group=0, flag_bit=0),
        TLField("upgrade", "true", flag_group=0, flag_bit=1),
    ]
    restore: Optional[bool]
    upgrade: Optional[bool]

class InputStorePaymentGiftPremium(TLObject):
    CONSTRUCTOR_ID = 0x616F7FE8
    FIELDS = [
        TLField("user_id", "InputUser"),
        TLField("currency", "string"),
        TLField("amount", "long"),
    ]
    user_id: Optional[TLObject]
    currency: Optional[str]
    amount: Optional[int]

class InputStorePaymentPremiumGiftCode(TLObject):
    CONSTRUCTOR_ID = 0xA3805F3F
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("users", "InputUser", is_vector=True),
        TLField("boost_peer", "InputPeer", flag_group=0, flag_bit=0),
        TLField("currency", "string"),
        TLField("amount", "long"),
    ]
    users: Optional[List[TLObject]]
    boost_peer: Optional[TLObject]
    currency: Optional[str]
    amount: Optional[int]

class InputStorePaymentPremiumGiveaway(TLObject):
    CONSTRUCTOR_ID = 0x7C9375E6
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("only_new_subscribers", "true", flag_group=0, flag_bit=0),
        TLField("boost_peer", "InputPeer"),
        TLField("additional_peers", "InputPeer", flag_group=0, flag_bit=1, is_vector=True),
        TLField("countries_iso2", "string", flag_group=0, flag_bit=2, is_vector=True),
        TLField("random_id", "long"),
        TLField("until_date", "int"),
        TLField("currency", "string"),
        TLField("amount", "long"),
    ]
    only_new_subscribers: Optional[bool]
    boost_peer: Optional[TLObject]
    additional_peers: Optional[List[TLObject]]
    countries_iso2: Optional[List[str]]
    random_id: Optional[int]
    until_date: Optional[int]
    currency: Optional[str]
    amount: Optional[int]

class PremiumGiftOption(TLObject):
    CONSTRUCTOR_ID = 0x74C34319
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("months", "int"),
        TLField("currency", "string"),
        TLField("amount", "long"),
        TLField("bot_url", "string"),
        TLField("store_product", "string", flag_group=0, flag_bit=0),
    ]
    months: Optional[int]
    currency: Optional[str]
    amount: Optional[int]
    bot_url: Optional[str]
    store_product: Optional[str]

class PremiumGiftCodeOption(TLObject):
    CONSTRUCTOR_ID = 0x257E962B
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("users", "int"),
        TLField("months", "int"),
        TLField("store_product", "string", flag_group=0, flag_bit=0),
        TLField("store_quantity", "int", flag_group=0, flag_bit=1),
        TLField("currency", "string"),
        TLField("amount", "long"),
    ]
    users: Optional[int]
    months: Optional[int]
    store_product: Optional[str]
    store_quantity: Optional[int]
    currency: Optional[str]
    amount: Optional[int]

class PremiumSubscriptionOption(TLObject):
    CONSTRUCTOR_ID = 0x5F2D1DF2
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("current", "true", flag_group=0, flag_bit=1),
        TLField("can_purchase_upgrade", "true", flag_group=0, flag_bit=2),
        TLField("transaction", "string", flag_group=0, flag_bit=3),
        TLField("months", "int"),
        TLField("currency", "string"),
        TLField("amount", "long"),
        TLField("bot_url", "string"),
        TLField("store_product", "string", flag_group=0, flag_bit=0),
    ]
    current: Optional[bool]
    can_purchase_upgrade: Optional[bool]
    transaction: Optional[str]
    months: Optional[int]
    currency: Optional[str]
    amount: Optional[int]
    bot_url: Optional[str]
    store_product: Optional[str]

class BankCardOpenUrl(TLObject):
    CONSTRUCTOR_ID = 0xF568028A
    FIELDS = [
        TLField("url", "string"),
        TLField("name", "string"),
    ]
    url: Optional[str]
    name: Optional[str]

class PrepaidGiveaway(TLObject):
    CONSTRUCTOR_ID = 0xB2539D54
    FIELDS = [
        TLField("id", "long"),
        TLField("months", "int"),
        TLField("quantity", "int"),
        TLField("date", "int"),
    ]
    id: Optional[int]
    months: Optional[int]
    quantity: Optional[int]
    date: Optional[int]