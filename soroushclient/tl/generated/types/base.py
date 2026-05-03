# Bool, True, Null, Error
from typing import Optional

from soroushclient.tl.base import TLObject, TLField


class BoolFalse(TLObject):
    CONSTRUCTOR_ID = 0xBC799737
    FIELDS = []

class BoolTrue(TLObject):
    CONSTRUCTOR_ID = 0x997275B5
    FIELDS = []

class TrueType(TLObject):
    CONSTRUCTOR_ID = 0x3FEDD339
    FIELDS = []

class Error(TLObject):
    CONSTRUCTOR_ID = 0xC4B9F9BB
    FIELDS = [
        TLField("code", "int"),
        TLField("text", "string"),
    ]
    code: Optional[int]
    text: Optional[str]

class Null(TLObject):
    CONSTRUCTOR_ID = 0x56730BCC
    FIELDS = []