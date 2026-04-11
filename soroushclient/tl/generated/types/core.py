from soroushclient.tl.base import TLObject


class BoolTrue(TLObject):
    CONSTRUCTOR_ID = 0x997275b5
    FIELDS = []
    def __bool__(self): return True
    def __repr__(self): return "BoolTrue"

class BoolFalse(TLObject):
    CONSTRUCTOR_ID = 0xbc799737
    FIELDS = []
    def __bool__(self): return False
    def __repr__(self): return "BoolFalse"
