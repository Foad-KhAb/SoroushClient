from typing import Optional

from soroushclient.tl.base import TLObject, TLField


class DcOption(TLObject):
    CONSTRUCTOR_ID = 0x18B7A10D
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("ipv6", "true", flag_group=0, flag_bit=0),
        TLField("media_only", "true", flag_group=0, flag_bit=1),
        TLField("tcpo_only", "true", flag_group=0, flag_bit=2),
        TLField("cdn", "true", flag_group=0, flag_bit=3),
        TLField("static", "true", flag_group=0, flag_bit=4),
        TLField("this_port_only", "true", flag_group=0, flag_bit=5),
        TLField("id", "int"),
        TLField("ip_address", "string"),
        TLField("port", "int"),
        TLField("secret", "bytes", flag_group=0, flag_bit=10),
    ]
    ipv6: Optional[bool]
    media_only: Optional[bool]
    tcpo_only: Optional[bool]
    cdn: Optional[bool]
    static: Optional[bool]
    this_port_only: Optional[bool]
    id: Optional[int]
    ip_address: Optional[str]
    port: Optional[int]
    secret: Optional[bytes]

class NearestDc(TLObject):
    CONSTRUCTOR_ID = 0x8E1A1775
    FIELDS = [
        TLField("country", "string"),
        TLField("this_dc", "int"),
        TLField("nearest_dc", "int"),
    ]
    country: Optional[str]
    this_dc: Optional[int]
    nearest_dc: Optional[int]

class InputClientProxy(TLObject):
    CONSTRUCTOR_ID = 0x75588B3F
    FIELDS = [
        TLField("address", "string"),
        TLField("port", "int"),
    ]
    address: Optional[str]
    port: Optional[int]