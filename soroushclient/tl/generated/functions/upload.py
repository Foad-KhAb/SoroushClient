from typing import Optional

from soroushclient.tl.base import TLObject, TLField, TLRequest


class GetFile(TLRequest):
    CONSTRUCTOR_ID = 0xBE5335BE
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("precise", "true", flag_group=0, flag_bit=0),
        TLField("cdn_supported", "true", flag_group=0, flag_bit=1),
        TLField("location", "InputFileLocation"),
        TLField("offset", "long"),
        TLField("limit", "int"),
    ]
    precise: Optional[bool]
    cdn_supported: Optional[bool]
    location: Optional[TLObject]
    offset: Optional[int]
    limit: Optional[int]

class SaveFilePart(TLRequest):
    CONSTRUCTOR_ID = 0xB304A621
    FIELDS = [
        TLField("file_id", "long"),
        TLField("file_part", "int"),
        TLField("bytes", "bytes"),
    ]
    file_id: Optional[int]
    file_part: Optional[int]
    bytes: Optional[bytes]

class SaveBigFilePart(TLRequest):
    CONSTRUCTOR_ID = 0xDE7B673D
    FIELDS = [
        TLField("file_id", "long"),
        TLField("file_part", "int"),
        TLField("file_total_parts", "int"),
        TLField("bytes", "bytes"),
    ]
    file_id: Optional[int]
    file_part: Optional[int]
    file_total_parts: Optional[int]
    bytes: Optional[bytes]

class GetWebFile(TLRequest):
    CONSTRUCTOR_ID = 0x24E6818D
    FIELDS = [
        TLField("location", "InputWebFileLocation"),
        TLField("offset", "int"),
        TLField("limit", "int"),
    ]
    location: Optional[TLObject]
    offset: Optional[int]
    limit: Optional[int]