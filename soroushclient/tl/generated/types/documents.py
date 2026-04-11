from soroushclient.tl.base import TLField, TLObject


class DocumentEmpty(TLObject):
    CONSTRUCTOR_ID = 0x36f8c871
    FIELDS = [TLField("id", "long")]

class Document(TLObject):
    CONSTRUCTOR_ID = 0x8fd4c4d8
    FIELDS = [
        TLField("flags",          "int",   flag_group=0, flag_indicator=True),
        TLField("id",             "long"),
        TLField("access_hash",    "long"),
        TLField("file_reference", "bytes"),
        TLField("date",           "int"),
        TLField("mime_type",      "string"),
        TLField("size",           "long"),
        TLField("thumbs",         "PhotoSize", flag_group=0, flag_bit=0, is_vector=True),
        TLField("video_thumbs",   "VideoSize", flag_group=0, flag_bit=1, is_vector=True),
        TLField("dc_id",          "int"),
        TLField("attributes",     "DocumentAttribute", is_vector=True),
    ]

class DocumentAttributeImageSize(TLObject):
    CONSTRUCTOR_ID = 0x6c37c15c
    FIELDS = [TLField("w","int"), TLField("h","int")]

class DocumentAttributeAnimated(TLObject):
    CONSTRUCTOR_ID = 0x11b58939
    FIELDS = []

class DocumentAttributeSticker(TLObject):
    CONSTRUCTOR_ID = 0x6319d612
    FIELDS = [
        TLField("flags",       "int",   flag_group=0, flag_indicator=True),
        TLField("mask",        "true",  flag_group=0, flag_bit=1),
        TLField("alt",         "string"),
        TLField("stickerset",  "InputStickerSet"),
        TLField("mask_coords", "MaskCoords", flag_group=0, flag_bit=0),
    ]

class DocumentAttributeVideo(TLObject):
    CONSTRUCTOR_ID = 0xd38ff1c2
    FIELDS = [
        TLField("flags",               "int",   flag_group=0, flag_indicator=True),
        TLField("round_message",       "true",  flag_group=0, flag_bit=0),
        TLField("supports_streaming",  "true",  flag_group=0, flag_bit=1),
        TLField("nosound",             "true",  flag_group=0, flag_bit=3),
        TLField("duration",            "double"),   # ← 8 bytes, NOT int/flags-conditional
        TLField("w",                   "int"),      # always present
        TLField("h",                   "int"),      # always present
        TLField("preload_prefix_size", "int",   flag_group=0, flag_bit=2),
    ]


class DocumentAttributeAudio(TLObject):
    CONSTRUCTOR_ID = 0x9852f9c6
    FIELDS = [
        TLField("flags",     "int",   flag_group=0, flag_indicator=True),
        TLField("voice",     "true",  flag_group=0, flag_bit=10),
        TLField("duration",  "int"),
        TLField("title",     "string", flag_group=0, flag_bit=0),
        TLField("performer", "string", flag_group=0, flag_bit=1),
        TLField("waveform",  "bytes",  flag_group=0, flag_bit=2),
    ]


class DocumentAttributeFilename(TLObject):
    CONSTRUCTOR_ID = 0x15590068
    FIELDS = [
        TLField("file_name", "string"),
    ]


class DocumentAttributeHasStickers(TLObject):
    CONSTRUCTOR_ID = 0x9801d2f7
    FIELDS = []


class DocumentAttributeCustomEmoji(TLObject):
    CONSTRUCTOR_ID = 0xfd149899
    FIELDS = [
        TLField("flags",      "int",             flag_group=0, flag_indicator=True),
        TLField("free",       "true",            flag_group=0, flag_bit=0),
        TLField("text_color", "true",            flag_group=0, flag_bit=1),
        TLField("alt",        "string"),
        TLField("stickerset", "InputStickerSet"),
    ]
