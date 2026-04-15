from soroushclient.tl.base import TLObject


class BoolTrue(TLObject):
    CONSTRUCTOR_ID = 0x997275B5
    FIELDS = []

    def __bool__(self):
        return True

    def __repr__(self):
        return "BoolTrue"


class BoolFalse(TLObject):
    CONSTRUCTOR_ID = 0xBC799737
    FIELDS = []

    def __bool__(self):
        return False

    def __repr__(self):
        return "BoolFalse"
