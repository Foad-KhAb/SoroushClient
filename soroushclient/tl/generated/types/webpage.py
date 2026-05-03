from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class WebPageEmpty(TLObject):
    CONSTRUCTOR_ID = 555358088
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("id", "long"),
        TLField("url", "string", flag_group=0, flag_bit=0),
    ]
    id: Optional[int]
    url: Optional[str]


class WebPagePending(TLObject):
    CONSTRUCTOR_ID = 2966502983
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("id", "long"),
        TLField("url", "string", flag_group=0, flag_bit=0),
        TLField("date", "int"),
    ]
    id: Optional[int]
    url: Optional[str]
    date: Optional[int]


class WebPage(TLObject):
    CONSTRUCTOR_ID = 3902555570
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
        TLField("cached_page", "Page", flag_group=0, flag_bit=10),
        TLField("attributes", "WebPageAttribute", flag_group=0, flag_bit=12, is_vector=True),
    ]
    has_large_media: Optional[bool]
    id: Optional[int]
    url: Optional[str]
    display_url: Optional[str]
    hash: Optional[int]
    type: Optional[str]
    site_name: Optional[str]
    title: Optional[str]
    description: Optional[str]
    photo: Optional[TLObject]
    embed_url: Optional[str]
    embed_type: Optional[str]
    embed_width: Optional[int]
    embed_height: Optional[int]
    duration: Optional[int]
    author: Optional[str]
    document: Optional[TLObject]
    cached_page: Optional[TLObject]
    attributes: Optional[List[TLObject]]


class WebPageNotModified(TLObject):
    CONSTRUCTOR_ID = 1930545681
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("cached_page_views", "int", flag_group=0, flag_bit=0),
    ]
    cached_page_views: Optional[int]