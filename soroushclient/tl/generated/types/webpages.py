from soroushclient.tl.base import TLField, TLObject


class WebPageEmpty(TLObject):
    CONSTRUCTOR_ID = 0x211A1788
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("id", "long"),
        TLField("url", "string", flag_group=0, flag_bit=0),
    ]


class WebPagePending(TLObject):
    CONSTRUCTOR_ID = 0xB0D13E47
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("id", "long"),
        TLField("url", "string", flag_group=0, flag_bit=0),
        TLField("date", "int"),
    ]


class WebPage(TLObject):
    CONSTRUCTOR_ID = 0xE89C45B2
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("has_large_media", "true", flag_group=0, flag_bit=13),
        TLField("id", "long"),
        TLField("url", "string"),
        TLField("display_url", "string"),
        TLField("hash", "int"),
        TLField("type", "string", flag_group=0, flag_bit=0),
        TLField("site_name", "string", flag_group=0, flag_bit=1),
        TLField("title", "string", flag_group=0, flag_bit=2),
        TLField("description", "string", flag_group=0, flag_bit=3),
        TLField("photo", "Photo", flag_group=0, flag_bit=4),
        TLField("embed_url", "string", flag_group=0, flag_bit=5),
        TLField("embed_type", "string", flag_group=0, flag_bit=5),
        TLField("embed_width", "int", flag_group=0, flag_bit=6),
        TLField("embed_height", "int", flag_group=0, flag_bit=6),
        TLField("duration", "int", flag_group=0, flag_bit=7),
        TLField("author", "string", flag_group=0, flag_bit=8),
        TLField("document", "Document", flag_group=0, flag_bit=9),
        TLField(
            "attributes", "WebPageAttribute", flag_group=0, flag_bit=12, is_vector=True
        ),
    ]
