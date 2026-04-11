from soroushclient.tl.base import TLField, TLObject


class PhotoSizeEmpty(TLObject):
    CONSTRUCTOR_ID = 0x0E17E23C
    FIELDS = [TLField("type", "string")]


class PhotoSize(TLObject):
    CONSTRUCTOR_ID = 0x75C78E60
    FIELDS = [
        TLField("type", "string"),
        TLField("w", "int"),
        TLField("h", "int"),
        TLField("size", "int"),
    ]


class PhotoCachedSize(TLObject):
    CONSTRUCTOR_ID = 0x021E1AD6
    FIELDS = [
        TLField("type", "string"),
        TLField("w", "int"),
        TLField("h", "int"),
        TLField("bytes", "bytes"),
    ]


class PhotoStrippedSize(TLObject):
    CONSTRUCTOR_ID = 0xE0B0BC2E
    FIELDS = [TLField("type", "string"), TLField("bytes", "bytes")]


class PhotoSizeProgressive(TLObject):
    CONSTRUCTOR_ID = 0xFA3EFB95
    FIELDS = [
        TLField("type", "string"),
        TLField("w", "int"),
        TLField("h", "int"),
        TLField("sizes", "int", is_vector=True),
    ]


class PhotoPathSize(TLObject):
    CONSTRUCTOR_ID = 0xD8214D41
    FIELDS = [TLField("type", "string"), TLField("bytes", "bytes")]


class PhotoEmpty(TLObject):
    CONSTRUCTOR_ID = 0x2331B22D
    FIELDS = [TLField("id", "long")]


class Photo(TLObject):
    CONSTRUCTOR_ID = 0xFB197A65
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("has_stickers", "true", flag_group=0, flag_bit=0),
        TLField("id", "long"),
        TLField("access_hash", "long"),
        TLField("file_reference", "bytes"),
        TLField("date", "int"),
        TLField("sizes", "PhotoSize", is_vector=True),
        TLField("video_sizes", "VideoSize", flag_group=0, flag_bit=1, is_vector=True),
        TLField("dc_id", "int"),
    ]
