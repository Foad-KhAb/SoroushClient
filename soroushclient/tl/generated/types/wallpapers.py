from typing import Optional

from soroushclient.tl.base import TLField, TLObject


class WallPaper(TLObject):
    CONSTRUCTOR_ID = 0xA437C3ED
    FIELDS = [
        TLField("id", "long"),
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("creator", "true", flag_group=0, flag_bit=0),
        TLField("default", "true", flag_group=0, flag_bit=1),
        TLField("pattern", "true", flag_group=0, flag_bit=3),
        TLField("dark", "true", flag_group=0, flag_bit=4),
        TLField("access_hash", "long"),
        TLField("slug", "string"),
        TLField("document", "Document"),
        TLField("settings", "WallPaperSettings", flag_group=0, flag_bit=2),
    ]
    id: Optional[int]
    creator: Optional[bool]
    default: Optional[bool]
    pattern: Optional[bool]
    dark: Optional[bool]
    access_hash: Optional[int]
    slug: Optional[str]
    document: Optional[TLObject]
    settings: Optional[TLObject]

class WallPaperNoFile(TLObject):
    CONSTRUCTOR_ID = 0xE0804116
    FIELDS = [
        TLField("id", "long"),
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("default", "true", flag_group=0, flag_bit=1),
        TLField("dark", "true", flag_group=0, flag_bit=4),
        TLField("settings", "WallPaperSettings", flag_group=0, flag_bit=2),
    ]
    id: Optional[int]
    default: Optional[bool]
    dark: Optional[bool]
    settings: Optional[TLObject]

class InputWallPaper(TLObject):
    CONSTRUCTOR_ID = 0xE630B979
    FIELDS = [
        TLField("id", "long"),
        TLField("access_hash", "long"),
    ]
    id: Optional[int]
    access_hash: Optional[int]

class InputWallPaperSlug(TLObject):
    CONSTRUCTOR_ID = 0x72091C80
    FIELDS = [TLField("slug", "string")]
    slug: Optional[str]

class InputWallPaperNoFile(TLObject):
    CONSTRUCTOR_ID = 0x967A462E
    FIELDS = [TLField("id", "long")]
    id: Optional[int]