from typing import Optional

from soroushclient.tl.base import TLField, TLObject


class InputFileLocation(TLObject):
    CONSTRUCTOR_ID = 0xDFDAABE1
    FIELDS = [
        TLField("volume_id", "long"),
        TLField("local_id", "int"),
        TLField("secret", "long"),
        TLField("file_reference", "bytes"),
    ]
    volume_id: Optional[int]
    local_id: Optional[int]
    secret: Optional[int]
    file_reference: Optional[bytes]

class InputEncryptedFileLocation(TLObject):
    CONSTRUCTOR_ID = 0xF5235D55
    FIELDS = [
        TLField("id", "long"),
        TLField("access_hash", "long"),
    ]
    id: Optional[int]
    access_hash: Optional[int]

class InputDocumentFileLocation(TLObject):
    CONSTRUCTOR_ID = 0xBAD07584
    FIELDS = [
        TLField("id", "long"),
        TLField("access_hash", "long"),
        TLField("file_reference", "bytes"),
        TLField("thumb_size", "string"),
    ]
    id: Optional[int]
    access_hash: Optional[int]
    file_reference: Optional[bytes]
    thumb_size: Optional[str]

class InputSecureFileLocation(TLObject):
    CONSTRUCTOR_ID = 0xCBC7EE28
    FIELDS = [
        TLField("id", "long"),
        TLField("access_hash", "long"),
    ]
    id: Optional[int]
    access_hash: Optional[int]

class InputTakeoutFileLocation(TLObject):
    CONSTRUCTOR_ID = 0x29BE5899
    FIELDS = []

class InputPhotoFileLocation(TLObject):
    CONSTRUCTOR_ID = 0x40181FFE
    FIELDS = [
        TLField("id", "long"),
        TLField("access_hash", "long"),
        TLField("file_reference", "bytes"),
        TLField("thumb_size", "string"),
    ]
    id: Optional[int]
    access_hash: Optional[int]
    file_reference: Optional[bytes]
    thumb_size: Optional[str]

class InputPhotoLegacyFileLocation(TLObject):
    CONSTRUCTOR_ID = 0xD83466F3
    FIELDS = [
        TLField("id", "long"),
        TLField("access_hash", "long"),
        TLField("file_reference", "bytes"),
        TLField("volume_id", "long"),
        TLField("local_id", "int"),
        TLField("secret", "long"),
    ]
    id: Optional[int]
    access_hash: Optional[int]
    file_reference: Optional[bytes]
    volume_id: Optional[int]
    local_id: Optional[int]
    secret: Optional[int]

class InputPeerPhotoFileLocation(TLObject):
    CONSTRUCTOR_ID = 0x37257E99
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("big", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputPeer"),
        TLField("photo_id", "long"),
    ]
    big: Optional[bool]
    peer: Optional[TLObject]
    photo_id: Optional[int]

class InputStickerSetThumb(TLObject):
    CONSTRUCTOR_ID = 0x9D84F3DB
    FIELDS = [
        TLField("stickerset", "InputStickerSet"),
        TLField("thumb_version", "int"),
    ]
    stickerset: Optional[TLObject]
    thumb_version: Optional[int]

class InputWebFileLocation(TLObject):
    CONSTRUCTOR_ID = 0xC239D686
    FIELDS = [
        TLField("url", "string"),
        TLField("access_hash", "long"),
    ]
    url: Optional[str]
    access_hash: Optional[int]

class InputWebFileGeoPointLocation(TLObject):
    CONSTRUCTOR_ID = 0x9F2221C9
    FIELDS = [
        TLField("geo_point", "InputGeoPoint"),
        TLField("access_hash", "long"),
        TLField("w", "int"),
        TLField("h", "int"),
        TLField("zoom", "int"),
        TLField("scale", "int"),
    ]
    geo_point: Optional[TLObject]
    access_hash: Optional[int]
    w: Optional[int]
    h: Optional[int]
    zoom: Optional[int]
    scale: Optional[int]

class InputWebFileAudioAlbumThumbLocation(TLObject):
    CONSTRUCTOR_ID = 0xF46FE924
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("small", "true", flag_group=0, flag_bit=2),
        TLField("document", "InputDocument", flag_group=0, flag_bit=0),
        TLField("title", "string", flag_group=0, flag_bit=1),
        TLField("performer", "string", flag_group=0, flag_bit=1),
    ]
    small: Optional[bool]
    document: Optional[TLObject]
    title: Optional[str]
    performer: Optional[str]