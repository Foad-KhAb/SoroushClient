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
class InputPrivacyKeySavedMusic(TLObject):
    CONSTRUCTOR_ID = 0x4DBE9226
    FIELDS = []
class PrivacyKeySavedMusic(TLObject):
    CONSTRUCTOR_ID = 0xFF7A571B
    FIELDS = []