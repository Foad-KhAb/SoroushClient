from soroushclient.tl.base import TLObject, TLField


class PhotoSizeEmpty(TLObject):
    CONSTRUCTOR_ID = 0x0e17e23c
    FIELDS = [TLField("type", "string")]

class PhotoSize(TLObject):
    CONSTRUCTOR_ID = 0x75c78e60
    FIELDS = [TLField("type","string"), TLField("w","int"), TLField("h","int"), TLField("size","int")]

class PhotoCachedSize(TLObject):
    CONSTRUCTOR_ID = 0x021e1ad6
    FIELDS = [TLField("type","string"), TLField("w","int"), TLField("h","int"), TLField("bytes","bytes")]

class PhotoStrippedSize(TLObject):
    CONSTRUCTOR_ID = 0xe0b0bc2e
    FIELDS = [TLField("type","string"), TLField("bytes","bytes")]

class PhotoSizeProgressive(TLObject):
    CONSTRUCTOR_ID = 0xfa3efb95
    FIELDS = [TLField("type","string"), TLField("w","int"), TLField("h","int"), TLField("sizes","int",is_vector=True)]

class PhotoPathSize(TLObject):
    CONSTRUCTOR_ID = 0xd8214d41
    FIELDS = [TLField("type","string"), TLField("bytes","bytes")]

class PhotoEmpty(TLObject):
    CONSTRUCTOR_ID = 0x2331b22d
    FIELDS = [TLField("id", "long")]

class Photo(TLObject):
    CONSTRUCTOR_ID = 0xfb197a65
    FIELDS = [
        TLField("flags",          "int",   flag_group=0, flag_indicator=True),
        TLField("has_stickers",   "true",  flag_group=0, flag_bit=0),
        TLField("id",             "long"),
        TLField("access_hash",    "long"),
        TLField("file_reference", "bytes"),
        TLField("date",           "int"),
        TLField("sizes",          "PhotoSize", is_vector=True),
        TLField("video_sizes",    "VideoSize", flag_group=0, flag_bit=1, is_vector=True),
        TLField("dc_id",          "int"),
    ]

