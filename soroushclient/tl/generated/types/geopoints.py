from soroushclient.tl.base import TLField, TLObject


class GeoPointEmpty(TLObject):
    CONSTRUCTOR_ID = 0x1117dd5f
    FIELDS = []

class GeoPoint(TLObject):
    CONSTRUCTOR_ID = 0xb2a2f663
    FIELDS = [
        TLField("flags",             "int",    flag_group=0, flag_indicator=True),
        TLField("long",              "double"),
        TLField("lat",               "double"),
        TLField("access_hash",       "long"),
        TLField("accuracy_radius",   "int",    flag_group=0, flag_bit=0),
    ]

