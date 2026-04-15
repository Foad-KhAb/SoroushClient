from typing import Optional

from soroushclient.tl.base import TLField, TLObject


class GeoPointEmpty(TLObject):
    CONSTRUCTOR_ID = 0x1117DD5F
    FIELDS = []


class GeoPoint(TLObject):
    CONSTRUCTOR_ID = 0xB2A2F663
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("long", "double"),
        TLField("lat", "double"),
        TLField("access_hash", "long", skip_cid=True),
        TLField("accuracy_radius", "int", flag_group=0, flag_bit=0, skip_cid=True),
    ]

    long: Optional[float]
    lat: Optional[float]
    access_hash: Optional[int]
    accuracy_radius: Optional[int]
