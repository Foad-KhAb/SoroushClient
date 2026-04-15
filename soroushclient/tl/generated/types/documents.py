from typing import List, Optional

from soroushclient.tl.base import TLField, TLObject


class DocumentEmpty(TLObject):
    CONSTRUCTOR_ID = 0x36F8C871
    FIELDS = [
        TLField("id", "long", skip_cid=True),
    ]

    id: Optional[int]


class Document(TLObject):
    CONSTRUCTOR_ID = 0x8FD4C4D8
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("id", "long", skip_cid=True),
        TLField("access_hash", "long", skip_cid=True),
        TLField("file_reference", "bytes"),
        TLField("date", "int", skip_cid=True),
        TLField("mime_type", "string"),
        TLField("size", "long", skip_cid=True),
        TLField("thumbs", "PhotoSize", flag_group=0, flag_bit=0, is_vector=True),
        TLField("video_thumbs", "VideoSize", flag_group=0, flag_bit=1, is_vector=True),
        TLField("dc_id", "int", skip_cid=True),
        TLField("attributes", "DocumentAttribute", is_vector=True),
    ]

    id: Optional[int]
    access_hash: Optional[int]
    file_reference: Optional[bytes]
    date: Optional[int]
    mime_type: Optional[str]
    size: Optional[int]
    thumbs: Optional[List[TLObject]]
    video_thumbs: Optional[List[TLObject]]
    dc_id: Optional[int]
    attributes: Optional[List[TLObject]]


class DocumentAttributeImageSize(TLObject):
    CONSTRUCTOR_ID = 0x6C37C15C
    FIELDS = [
        TLField("w", "int", skip_cid=True),
        TLField("h", "int", skip_cid=True),
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
        TLField("w", "int", skip_cid=True),
        TLField("h", "int", skip_cid=True),
        TLField("preload_prefix_size", "int", flag_group=0, flag_bit=2, skip_cid=True),
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
        TLField("duration", "int", skip_cid=True),
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
    FIELDS = [
        TLField("file_name", "string"),
    ]

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
