from soroushclient.tl.base import TLObject


class StorageFileUnknown(TLObject):
    CONSTRUCTOR_ID = 0xAA963B05
    FIELDS = []

class StorageFilePartial(TLObject):
    CONSTRUCTOR_ID = 0x40BC6F52
    FIELDS = []

class StorageFileJpeg(TLObject):
    CONSTRUCTOR_ID = 0x007EFE0E
    FIELDS = []

class StorageFileGif(TLObject):
    CONSTRUCTOR_ID = 0xCAE1AADF
    FIELDS = []

class StorageFilePng(TLObject):
    CONSTRUCTOR_ID = 0x0A4F63C0
    FIELDS = []

class StorageFilePdf(TLObject):
    CONSTRUCTOR_ID = 0xAE1E508D
    FIELDS = []

class StorageFileMp3(TLObject):
    CONSTRUCTOR_ID = 0x528A0677
    FIELDS = []

class StorageFileMov(TLObject):
    CONSTRUCTOR_ID = 0x4B09EBBC
    FIELDS = []

class StorageFileMp4(TLObject):
    CONSTRUCTOR_ID = 0xB3CEA0E4
    FIELDS = []

class StorageFileWebp(TLObject):
    CONSTRUCTOR_ID = 0x1081464C
    FIELDS = []