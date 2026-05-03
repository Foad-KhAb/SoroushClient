from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class BaseThemeClassic(TLObject):
    CONSTRUCTOR_ID = 0xC3A12462
    FIELDS = []

class BaseThemeDay(TLObject):
    CONSTRUCTOR_ID = 0xFBD81688
    FIELDS = []

class BaseThemeNight(TLObject):
    CONSTRUCTOR_ID = 0xB7B31EA8
    FIELDS = []

class BaseThemeTinted(TLObject):
    CONSTRUCTOR_ID = 0x6D5F77EE
    FIELDS = []

class BaseThemeArctic(TLObject):
    CONSTRUCTOR_ID = 0x5B11125A
    FIELDS = []

class InputTheme(TLObject):
    CONSTRUCTOR_ID = 0x3C5693E9
    FIELDS = [
        TLField("id", "long"),
        TLField("access_hash", "long"),
    ]
    id: Optional[int]
    access_hash: Optional[int]

class InputThemeSlug(TLObject):
    CONSTRUCTOR_ID = 0xF5890DF1
    FIELDS = [TLField("slug", "string")]
    slug: Optional[str]

class Theme(TLObject):
    CONSTRUCTOR_ID = 0xA00E67D6
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("creator", "true", flag_group=0, flag_bit=0),
        TLField("default", "true", flag_group=0, flag_bit=1),
        TLField("for_chat", "true", flag_group=0, flag_bit=5),
        TLField("id", "long"),
        TLField("access_hash", "long"),
        TLField("slug", "string"),
        TLField("title", "string"),
        TLField("document", "Document", flag_group=0, flag_bit=2),
        TLField("settings", "ThemeSettings", flag_group=0, flag_bit=3, is_vector=True),
        TLField("emoticon", "string", flag_group=0, flag_bit=6),
        TLField("installs_count", "int", flag_group=0, flag_bit=4),
    ]
    creator: Optional[bool]
    default: Optional[bool]
    for_chat: Optional[bool]
    id: Optional[int]
    access_hash: Optional[int]
    slug: Optional[str]
    title: Optional[str]
    document: Optional[TLObject]
    settings: Optional[List[TLObject]]
    emoticon: Optional[str]
    installs_count: Optional[int]