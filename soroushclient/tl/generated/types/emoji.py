from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class EmojiKeyword(TLObject):
    CONSTRUCTOR_ID = 0xD5B3B9F9
    FIELDS = [
        TLField("keyword", "string"),
        TLField("emoticons", "string", is_vector=True),
    ]
    keyword: Optional[str]
    emoticons: Optional[List[str]]

class EmojiKeywordDeleted(TLObject):
    CONSTRUCTOR_ID = 0x236DF622
    FIELDS = [
        TLField("keyword", "string"),
        TLField("emoticons", "string", is_vector=True),
    ]
    keyword: Optional[str]
    emoticons: Optional[List[str]]

class EmojiKeywordsDifference(TLObject):
    CONSTRUCTOR_ID = 0x5CC761BD
    FIELDS = [
        TLField("lang_code", "string"),
        TLField("from_version", "int"),
        TLField("version", "int"),
        TLField("keywords", "EmojiKeyword", is_vector=True),
    ]
    lang_code: Optional[str]
    from_version: Optional[int]
    version: Optional[int]
    keywords: Optional[List[TLObject]]

class EmojiURL(TLObject):
    CONSTRUCTOR_ID = 0xA575739D
    FIELDS = [TLField("url", "string")]
    url: Optional[str]

class EmojiLanguage(TLObject):
    CONSTRUCTOR_ID = 0xB3FB5361
    FIELDS = [TLField("lang_code", "string")]
    lang_code: Optional[str]

class EmojiStatusEmpty(TLObject):
    CONSTRUCTOR_ID = 0x2DE11AAE
    FIELDS = []

class EmojiStatus(TLObject):
    CONSTRUCTOR_ID = 0x929B619D
    FIELDS = [TLField("document_id", "long")]
    document_id: Optional[int]

class EmojiStatusUntil(TLObject):
    CONSTRUCTOR_ID = 0xFA30A8C7
    FIELDS = [
        TLField("document_id", "long"),
        TLField("until", "int"),
    ]
    document_id: Optional[int]
    until: Optional[int]

class EmojiListNotModified(TLObject):
    CONSTRUCTOR_ID = 0x481EADFA
    FIELDS = []

class EmojiList(TLObject):
    CONSTRUCTOR_ID = 0x7A1E11D1
    FIELDS = [
        TLField("hash", "long"),
        TLField("document_id", "long", is_vector=True),
    ]
    hash: Optional[int]
    document_id: Optional[List[int]]

class EmojiGroup(TLObject):
    CONSTRUCTOR_ID = 0x7A9ABDA9
    FIELDS = [
        TLField("title", "string"),
        TLField("icon_emoji_id", "long"),
        TLField("emoticons", "string", is_vector=True),
    ]
    title: Optional[str]
    icon_emoji_id: Optional[int]
    emoticons: Optional[List[str]]