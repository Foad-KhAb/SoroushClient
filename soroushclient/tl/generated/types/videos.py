from soroushclient.tl.base import TLObject, TLField


class VideoSize(TLObject):
    CONSTRUCTOR_ID = 0xde33b094
    FIELDS = [
        TLField("flags",           "int",    flag_group=0, flag_indicator=True),
        TLField("type",            "string"),
        TLField("w",               "int"),
        TLField("h",               "int"),
        TLField("size",            "int"),
        TLField("video_start_ts",  "double", flag_group=0, flag_bit=0),
    ]

