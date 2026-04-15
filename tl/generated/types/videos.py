from soroushclient.tl.base import TLField, TLObject


class VideoSize(TLObject):
    CONSTRUCTOR_ID = 0xDE33B094
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("type", "string"),
        TLField("w", "int"),
        TLField("h", "int"),
        TLField("size", "int"),
        TLField("video_start_ts", "double", flag_group=0, flag_bit=0),
    ]
