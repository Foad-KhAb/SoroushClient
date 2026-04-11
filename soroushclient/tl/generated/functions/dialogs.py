from soroushclient.tl.base import TLField, TLRequest


class GetDialogsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa0f4cb4f
    FIELDS = [
        TLField("flags",          "int",  flag_group=0, flag_indicator=True),
        TLField("exclude_pinned", "true", flag_group=0, flag_bit=0),
        TLField("folder_id",      "int",  flag_group=0, flag_bit=1),
        TLField("offset_date",    "int"),
        TLField("offset_id",      "int"),
        TLField("offset_peer",    "InputPeer"),
        TLField("limit",          "int"),
        TLField("hash",           "long"),
    ]
