from typing import Optional, List

from soroushclient.tl.base import TLField, TLObject


class ThirdPartyMessage(TLObject):
    CONSTRUCTOR_ID = 0xD630E7F7
    FIELDS = [
        TLField("third_party_id", "string"),
        TLField("message_type", "string"),
        TLField("content", "bytes"),
    ]
    third_party_id: Optional[str]
    message_type: Optional[str]
    content: Optional[bytes]

class ThirdPartyReply(TLObject):
    CONSTRUCTOR_ID = 0x214899AC
    FIELDS = [
        TLField("message", "ThirdPartyMessage"),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    message: Optional[TLObject]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]