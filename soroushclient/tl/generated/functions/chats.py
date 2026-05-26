from typing import List, Optional

from soroushclient.tl.base import TLField, TLRequest, TLObject


class GetFullChatRequest(TLRequest):
    CONSTRUCTOR_ID = 0xAEB00B34
    FIELDS = [TLField("chat_id", "long")]
    chat_id: Optional[int]

class CreateChat(TLRequest):
    CONSTRUCTOR_ID = 0x0034A818
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("users", "InputUser", is_vector=True),
        TLField("title", "string"),
        TLField("ttl_period", "int", flag_group=0, flag_bit=0),
    ]
    users: Optional[List[TLObject]]
    title: Optional[str]
    ttl_period: Optional[int]

class EditChatTitle(TLRequest):
    CONSTRUCTOR_ID = 0x73783FFD
    FIELDS = [
        TLField("chat_id", "long"),
        TLField("title", "string"),
    ]
    chat_id: Optional[int]
    title: Optional[str]

class EditChatPhoto(TLRequest):
    CONSTRUCTOR_ID = 0x35DDD674
    FIELDS = [
        TLField("chat_id", "long"),
        TLField("photo", "InputChatPhoto"),
    ]
    chat_id: Optional[int]
    photo: Optional[TLObject]

class AddChatUser(TLRequest):
    CONSTRUCTOR_ID = 0xF24753E3
    FIELDS = [
        TLField("chat_id", "long"),
        TLField("user_id", "InputUser"),
        TLField("fwd_limit", "int"),
    ]
    chat_id: Optional[int]
    user_id: Optional[TLObject]
    fwd_limit: Optional[int]

class DeleteChatUser(TLRequest):
    CONSTRUCTOR_ID = 0xA2185CAB
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("revoke_history", "true", flag_group=0, flag_bit=0),
        TLField("chat_id", "long"),
        TLField("user_id", "InputUser"),
    ]
    revoke_history: Optional[bool]
    chat_id: Optional[int]
    user_id: Optional[TLObject]

class DeleteChat(TLRequest):
    CONSTRUCTOR_ID = 0x5BD0EE50
    FIELDS = [TLField("chat_id", "long")]
    chat_id: Optional[int]

class MigrateChat(TLRequest):
    CONSTRUCTOR_ID = 0xA2875319
    FIELDS = [TLField("chat_id", "long")]
    chat_id: Optional[int]

class EditChatAbout(TLRequest):
    CONSTRUCTOR_ID = 0xDEF60797
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("about", "string"),
    ]
    peer: Optional[TLObject]
    about: Optional[str]

class EditChatDefaultBannedRights(TLRequest):
    CONSTRUCTOR_ID = 0xA5866B41
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("banned_rights", "ChatBannedRights"),
    ]
    peer: Optional[TLObject]
    banned_rights: Optional[TLObject]

class GetChats(TLRequest):
    CONSTRUCTOR_ID = 0x49E9528F
    FIELDS = [TLField("id", "long", is_vector=True)]
    id: Optional[List[int]]