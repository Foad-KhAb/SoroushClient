from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class StarGift(TLObject):
    CONSTRUCTOR_ID = 0x80AC53C3
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("limited", "true", flag_group=0, flag_bit=0),
        TLField("sold_out", "true", flag_group=0, flag_bit=1),
        TLField("birthday", "true", flag_group=0, flag_bit=2),
        TLField("require_premium", "true", flag_group=0, flag_bit=7),
        TLField("limited_per_user", "true", flag_group=0, flag_bit=8),
        TLField("id", "long"),
        TLField("sticker", "Document"),
        TLField("stars", "long"),
        TLField("availability_remains", "int", flag_group=0, flag_bit=0),
        TLField("availability_total", "int", flag_group=0, flag_bit=0),
        TLField("availability_resale", "long", flag_group=0, flag_bit=4),
        TLField("convert_stars", "long"),
        TLField("first_sale_date", "int", flag_group=0, flag_bit=1),
        TLField("last_sale_date", "int", flag_group=0, flag_bit=1),
        TLField("upgrade_stars", "long", flag_group=0, flag_bit=3),
        TLField("resell_min_stars", "long", flag_group=0, flag_bit=4),
        TLField("title", "string", flag_group=0, flag_bit=5),
        TLField("released_by", "Peer", flag_group=0, flag_bit=6),
        TLField("per_user_total", "int", flag_group=0, flag_bit=8),
        TLField("per_user_remains", "int", flag_group=0, flag_bit=8),
        TLField("locked_until_date", "int", flag_group=0, flag_bit=9),
    ]
    limited: Optional[bool]
    sold_out: Optional[bool]
    birthday: Optional[bool]
    require_premium: Optional[bool]
    limited_per_user: Optional[bool]
    id: Optional[int]
    sticker: Optional[TLObject]
    stars: Optional[int]
    availability_remains: Optional[int]
    availability_total: Optional[int]
    availability_resale: Optional[int]
    convert_stars: Optional[int]
    first_sale_date: Optional[int]
    last_sale_date: Optional[int]
    upgrade_stars: Optional[int]
    resell_min_stars: Optional[int]
    title: Optional[str]
    released_by: Optional[TLObject]
    per_user_total: Optional[int]
    per_user_remains: Optional[int]
    locked_until_date: Optional[int]

class StarGiftUnique(TLObject):
    CONSTRUCTOR_ID = 0x1BEFE865
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("require_premium", "true", flag_group=0, flag_bit=6),
        TLField("resale_ton_only", "true", flag_group=0, flag_bit=7),
        TLField("theme_available", "true", flag_group=0, flag_bit=9),
        TLField("id", "long"),
        TLField("gift_id", "long"),
        TLField("title", "string"),
        TLField("slug", "string"),
        TLField("num", "int"),
        TLField("owner_id", "Peer", flag_group=0, flag_bit=0),
        TLField("owner_name", "string", flag_group=0, flag_bit=1),
        TLField("owner_address", "string", flag_group=0, flag_bit=2),
        TLField("attributes", "StarGiftAttribute", is_vector=True),
        TLField("availability_issued", "int"),
        TLField("availability_total", "int"),
        TLField("gift_address", "string", flag_group=0, flag_bit=3),
        TLField("resell_amount", "StarsAmount", flag_group=0, flag_bit=4, is_vector=True),
        TLField("released_by", "Peer", flag_group=0, flag_bit=5),
        TLField("value_amount", "long", flag_group=0, flag_bit=8),
        TLField("value_currency", "string", flag_group=0, flag_bit=8),
        TLField("theme_peer", "Peer", flag_group=0, flag_bit=10),
    ]
    require_premium: Optional[bool]
    resale_ton_only: Optional[bool]
    theme_available: Optional[bool]
    id: Optional[int]
    gift_id: Optional[int]
    title: Optional[str]
    slug: Optional[str]
    num: Optional[int]
    owner_id: Optional[TLObject]
    owner_name: Optional[str]
    owner_address: Optional[str]
    attributes: Optional[List[TLObject]]
    availability_issued: Optional[int]
    availability_total: Optional[int]
    gift_address: Optional[str]
    resell_amount: Optional[List[TLObject]]
    released_by: Optional[TLObject]
    value_amount: Optional[int]
    value_currency: Optional[str]
    theme_peer: Optional[TLObject]

class StarGiftAttributeModel(TLObject):
    CONSTRUCTOR_ID = 0x39D99013
    FIELDS = [
        TLField("name", "string"),
        TLField("document", "Document"),
        TLField("rarity_permille", "int"),
    ]
    name: Optional[str]
    document: Optional[TLObject]
    rarity_permille: Optional[int]

class StarGiftAttributePattern(TLObject):
    CONSTRUCTOR_ID = 0x13ACFF19
    FIELDS = [
        TLField("name", "string"),
        TLField("document", "Document"),
        TLField("rarity_permille", "int"),
    ]
    name: Optional[str]
    document: Optional[TLObject]
    rarity_permille: Optional[int]

class StarGiftAttributeBackdrop(TLObject):
    CONSTRUCTOR_ID = 0xD93D859C
    FIELDS = [
        TLField("name", "string"),
        TLField("backdrop_id", "int"),
        TLField("center_color", "int"),
        TLField("edge_color", "int"),
        TLField("pattern_color", "int"),
        TLField("text_color", "int"),
        TLField("rarity_permille", "int"),
    ]
    name: Optional[str]
    backdrop_id: Optional[int]
    center_color: Optional[int]
    edge_color: Optional[int]
    pattern_color: Optional[int]
    text_color: Optional[int]
    rarity_permille: Optional[int]

class StarGiftAttributeOriginalDetails(TLObject):
    CONSTRUCTOR_ID = 0xE0BFF26C
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("sender_id", "Peer", flag_group=0, flag_bit=0),
        TLField("recipient_id", "Peer"),
        TLField("date", "int"),
        TLField("message", "TextWithEntities", flag_group=0, flag_bit=1),
    ]
    sender_id: Optional[TLObject]
    recipient_id: Optional[TLObject]
    date: Optional[int]
    message: Optional[TLObject]