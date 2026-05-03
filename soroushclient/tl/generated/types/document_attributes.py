from typing import Optional

from soroushclient.tl.base import TLField, TLObject


class DocumentAttributeImageSize(TLObject):
    CONSTRUCTOR_ID = 0x6C37C15C
    FIELDS = [
        TLField("w", "int"),
        TLField("h", "int"),
    ]
    w: Optional[int]
    h: Optional[int]

class DocumentAttributeAnimated(TLObject):
    CONSTRUCTOR_ID = 0x11B58939
    FIELDS = []

class DocumentAttributeSticker(TLObject):
    CONSTRUCTOR_ID = 0x6319D612
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("mask", "true", flag_group=0, flag_bit=1),
        TLField("alt", "string"),
        TLField("stickerset", "InputStickerSet"),
        TLField("mask_coords", "MaskCoords", flag_group=0, flag_bit=0),
    ]
    mask: Optional[bool]
    alt: Optional[str]
    stickerset: Optional[TLObject]
    mask_coords: Optional[TLObject]

class DocumentAttributeVideo(TLObject):
    CONSTRUCTOR_ID = 0xD38FF1C2
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("round_message", "true", flag_group=0, flag_bit=0),
        TLField("supports_streaming", "true", flag_group=0, flag_bit=1),
        TLField("nosound", "true", flag_group=0, flag_bit=3),
        TLField("duration", "double"),
        TLField("w", "int"),
        TLField("h", "int"),
        TLField("preload_prefix_size", "int", flag_group=0, flag_bit=2),
    ]
    round_message: Optional[bool]
    supports_streaming: Optional[bool]
    nosound: Optional[bool]
    duration: Optional[float]
    w: Optional[int]
    h: Optional[int]
    preload_prefix_size: Optional[int]

class DocumentAttributeAudio(TLObject):
    CONSTRUCTOR_ID = 0x9852F9C6
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("voice", "true", flag_group=0, flag_bit=10),
        TLField("duration", "int"),
        TLField("title", "string", flag_group=0, flag_bit=0),
        TLField("performer", "string", flag_group=0, flag_bit=1),
        TLField("waveform", "bytes", flag_group=0, flag_bit=2),
    ]
    voice: Optional[bool]
    duration: Optional[int]
    title: Optional[str]
    performer: Optional[str]
    waveform: Optional[bytes]

class DocumentAttributeFilename(TLObject):
    CONSTRUCTOR_ID = 0x15590068
    FIELDS = [TLField("file_name", "string")]
    file_name: Optional[str]

class DocumentAttributeHasStickers(TLObject):
    CONSTRUCTOR_ID = 0x9801D2F7
    FIELDS = []

class DocumentAttributeCustomEmoji(TLObject):
    CONSTRUCTOR_ID = 0xFD149899
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("free", "true", flag_group=0, flag_bit=0),
        TLField("text_color", "true", flag_group=0, flag_bit=1),
        TLField("alt", "string"),
        TLField("stickerset", "InputStickerSet"),
    ]
    free: Optional[bool]
    text_color: Optional[bool]
    alt: Optional[str]
    stickerset: Optional[TLObject]