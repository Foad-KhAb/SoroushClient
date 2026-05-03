from typing import Optional, List

from soroushclient.tl.base import TLField, TLObject


class InputStickerSetEmpty(TLObject):
    CONSTRUCTOR_ID = 0xFFB62B95
    FIELDS = []

class InputStickerSetID(TLObject):
    CONSTRUCTOR_ID = 0x9DE7A269
    FIELDS = [
        TLField("id", "long"),
        TLField("access_hash", "long"),
    ]
    id: Optional[int]
    access_hash: Optional[int]

class InputStickerSetShortName(TLObject):
    CONSTRUCTOR_ID = 0x861CC8A0
    FIELDS = [TLField("short_name", "string")]
    short_name: Optional[str]

class InputStickerSetAnimatedEmoji(TLObject):
    CONSTRUCTOR_ID = 0x028703C8
    FIELDS = []

class InputStickerSetDice(TLObject):
    CONSTRUCTOR_ID = 0xE67F520E
    FIELDS = [TLField("emoticon", "string")]
    emoticon: Optional[str]

class InputStickerSetAnimatedEmojiAnimations(TLObject):
    CONSTRUCTOR_ID = 0x0CDE3739
    FIELDS = []

class InputStickerSetPremiumGifts(TLObject):
    CONSTRUCTOR_ID = 0xC88B3B02
    FIELDS = []

class InputStickerSetEmojiGenericAnimations(TLObject):
    CONSTRUCTOR_ID = 0x04C4D4CE
    FIELDS = []

class InputStickerSetEmojiDefaultStatuses(TLObject):
    CONSTRUCTOR_ID = 0x29D0F5EE
    FIELDS = []

class InputStickerSetEmojiDefaultTopicIcons(TLObject):
    CONSTRUCTOR_ID = 0x44C1F8E9
    FIELDS = []

class StickerSet(TLObject):
    CONSTRUCTOR_ID = 0x2DD14EDC
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("archived", "true", flag_group=0, flag_bit=1),
        TLField("official", "true", flag_group=0, flag_bit=2),
        TLField("masks", "true", flag_group=0, flag_bit=3),
        TLField("animated", "true", flag_group=0, flag_bit=5),
        TLField("videos", "true", flag_group=0, flag_bit=6),
        TLField("emojis", "true", flag_group=0, flag_bit=7),
        TLField("text_color", "true", flag_group=0, flag_bit=9),
        TLField("installed_date", "int", flag_group=0, flag_bit=0),
        TLField("id", "long"),
        TLField("access_hash", "long"),
        TLField("title", "string"),
        TLField("short_name", "string"),
        TLField("thumbs", "PhotoSize", flag_group=0, flag_bit=4, is_vector=True),
        TLField("thumb_dc_id", "int", flag_group=0, flag_bit=4),
        TLField("thumb_version", "int", flag_group=0, flag_bit=4),
        TLField("thumb_document_id", "long", flag_group=0, flag_bit=8),
        TLField("count", "int"),
        TLField("hash", "int"),
    ]
    archived: Optional[bool]
    official: Optional[bool]
    masks: Optional[bool]
    animated: Optional[bool]
    videos: Optional[bool]
    emojis: Optional[bool]
    text_color: Optional[bool]
    installed_date: Optional[int]
    id: Optional[int]
    access_hash: Optional[int]
    title: Optional[str]
    short_name: Optional[str]
    thumbs: Optional[List[TLObject]]
    thumb_dc_id: Optional[int]
    thumb_version: Optional[int]
    thumb_document_id: Optional[int]
    count: Optional[int]
    hash: Optional[int]

class StickerPack(TLObject):
    CONSTRUCTOR_ID = 0x12B299D4
    FIELDS = [
        TLField("emoticon", "string"),
        TLField("documents", "long", is_vector=True),
    ]
    emoticon: Optional[str]
    documents: Optional[List[int]]

class StickerKeyword(TLObject):
    CONSTRUCTOR_ID = 0xFCFEB29C
    FIELDS = [
        TLField("document_id", "long"),
        TLField("keyword", "string", is_vector=True),
    ]
    document_id: Optional[int]
    keyword: Optional[List[str]]

class MaskCoords(TLObject):
    CONSTRUCTOR_ID = 0xAED6DBB2
    FIELDS = [
        TLField("n", "int"),
        TLField("x", "double"),
        TLField("y", "double"),
        TLField("zoom", "double"),
    ]
    n: Optional[int]
    x: Optional[float]
    y: Optional[float]
    zoom: Optional[float]

class InputStickerSetItem(TLObject):
    CONSTRUCTOR_ID = 0x32DA9E9C
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("document", "InputDocument"),
        TLField("emoji", "string"),
        TLField("mask_coords", "MaskCoords", flag_group=0, flag_bit=0),
        TLField("keywords", "string", flag_group=0, flag_bit=1),
    ]
    document: Optional[TLObject]
    emoji: Optional[str]
    mask_coords: Optional[TLObject]
    keywords: Optional[str]

class StickerSetCovered(TLObject):
    CONSTRUCTOR_ID = 0x6410A5D2
    FIELDS = [
        TLField("set", "StickerSet"),
        TLField("cover", "Document"),
    ]
    set: Optional[TLObject]
    cover: Optional[TLObject]

class StickerSetMultiCovered(TLObject):
    CONSTRUCTOR_ID = 0x3407E51B
    FIELDS = [
        TLField("set", "StickerSet"),
        TLField("covers", "Document", is_vector=True),
    ]
    set: Optional[TLObject]
    covers: Optional[List[TLObject]]

class StickerSetFullCovered(TLObject):
    CONSTRUCTOR_ID = 0x40D13C0E
    FIELDS = [
        TLField("set", "StickerSet"),
        TLField("packs", "StickerPack", is_vector=True),
        TLField("keywords", "StickerKeyword", is_vector=True),
        TLField("documents", "Document", is_vector=True),
    ]
    set: Optional[TLObject]
    packs: Optional[List[TLObject]]
    keywords: Optional[List[TLObject]]
    documents: Optional[List[TLObject]]

class StickerSetNoCovered(TLObject):
    CONSTRUCTOR_ID = 0x77B15D1C
    FIELDS = [TLField("set", "StickerSet")]
    set: Optional[TLObject]