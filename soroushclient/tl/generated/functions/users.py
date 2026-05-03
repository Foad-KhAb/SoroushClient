from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField, TLRequest


class GetUsers(TLRequest):
    CONSTRUCTOR_ID = 0x0D91A548
    FIELDS = [TLField("id", "InputUser", is_vector=True)]
    id: Optional[List[TLObject]]

class GetFullUser(TLRequest):
    CONSTRUCTOR_ID = 0xB60F5918
    FIELDS = [TLField("id", "InputUser")]
    id: Optional[TLObject]

class GetSavedMusic(TLRequest):
    CONSTRUCTOR_ID = 0x788D7FE3
    FIELDS = [
        TLField("id", "InputUser"),
        TLField("offset", "int"),
        TLField("limit", "int"),
        TLField("hash", "long"),
    ]
    id: Optional[TLObject]
    offset: Optional[int]
    limit: Optional[int]
    hash: Optional[int]

class GetSavedMusicByID(TLRequest):
    CONSTRUCTOR_ID = 0x7573A4E9
    FIELDS = [
        TLField("id", "InputUser"),
        TLField("documents", "InputDocument", is_vector=True),
    ]
    id: Optional[TLObject]
    documents: Optional[List[TLObject]]