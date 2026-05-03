from typing import Optional, List

from soroushclient.tl.base import TLField, TLObject


class UploadFile(TLObject):
    CONSTRUCTOR_ID = 0x096A18D5
    FIELDS = [
        TLField("type", "storage.FileType"),
        TLField("mtime", "int"),
        TLField("bytes", "bytes"),
    ]
    type: Optional[TLObject]
    mtime: Optional[int]
    bytes: Optional[bytes]

class UploadFileCdnRedirect(TLObject):
    CONSTRUCTOR_ID = 0xF18CDA44
    FIELDS = [
        TLField("dc_id", "int"),
        TLField("file_token", "bytes"),
        TLField("encryption_key", "bytes"),
        TLField("encryption_iv", "bytes"),
        TLField("file_hashes", "FileHash", is_vector=True),
    ]
    dc_id: Optional[int]
    file_token: Optional[bytes]
    encryption_key: Optional[bytes]
    encryption_iv: Optional[bytes]
    file_hashes: Optional[List[TLObject]]

class UploadWebFile(TLObject):
    CONSTRUCTOR_ID = 0x21E753BC
    FIELDS = [
        TLField("size", "int"),
        TLField("mime_type", "string"),
        TLField("file_type", "storage.FileType"),
        TLField("mtime", "int"),
        TLField("bytes", "bytes"),
    ]
    size: Optional[int]
    mime_type: Optional[str]
    file_type: Optional[TLObject]
    mtime: Optional[int]
    bytes: Optional[bytes]

class UploadCdnFileReuploadNeeded(TLObject):
    CONSTRUCTOR_ID = 0xEEA8E46E
    FIELDS = [TLField("request_token", "bytes")]
    request_token: Optional[bytes]

class UploadCdnFile(TLObject):
    CONSTRUCTOR_ID = 0xA99FCA4F
    FIELDS = [TLField("bytes", "bytes")]
    bytes: Optional[bytes]

class CdnPublicKey(TLObject):
    CONSTRUCTOR_ID = 0xC982EABA
    FIELDS = [
        TLField("dc_id", "int"),
        TLField("public_key", "string"),
    ]
    dc_id: Optional[int]
    public_key: Optional[str]

class CdnConfig(TLObject):
    CONSTRUCTOR_ID = 0x5725E40A
    FIELDS = [TLField("public_keys", "CdnPublicKey", is_vector=True)]
    public_keys: Optional[List[TLObject]]