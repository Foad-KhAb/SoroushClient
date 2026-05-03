from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField, TLRequest


class ExportChatlistInvite(TLRequest):
    CONSTRUCTOR_ID = 0x8472478E
    FIELDS = [
        TLField("chatlist", "InputChatlist"),
        TLField("title", "string"),
        TLField("peers", "InputPeer", is_vector=True),
    ]
    chatlist: Optional[TLObject]
    title: Optional[str]
    peers: Optional[List[TLObject]]

class DeleteExportedInvite(TLRequest):
    CONSTRUCTOR_ID = 0x719C5C5E
    FIELDS = [
        TLField("chatlist", "InputChatlist"),
        TLField("slug", "string"),
    ]
    chatlist: Optional[TLObject]
    slug: Optional[str]

class EditExportedInvite(TLRequest):
    CONSTRUCTOR_ID = 0x653DB63D
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("chatlist", "InputChatlist"),
        TLField("slug", "string"),
        TLField("title", "string", flag_group=0, flag_bit=1),
        TLField("peers", "InputPeer", flag_group=0, flag_bit=2, is_vector=True),
    ]
    chatlist: Optional[TLObject]
    slug: Optional[str]
    title: Optional[str]
    peers: Optional[List[TLObject]]

class GetExportedInvites(TLRequest):
    CONSTRUCTOR_ID = 0xCE03DA83
    FIELDS = [TLField("chatlist", "InputChatlist")]
    chatlist: Optional[TLObject]

class CheckChatlistInvite(TLRequest):
    CONSTRUCTOR_ID = 0x41C10FFF
    FIELDS = [TLField("slug", "string")]
    slug: Optional[str]

class JoinChatlistInvite(TLRequest):
    CONSTRUCTOR_ID = 0xA6B1E39A
    FIELDS = [
        TLField("slug", "string"),
        TLField("peers", "InputPeer", is_vector=True),
    ]
    slug: Optional[str]
    peers: Optional[List[TLObject]]

class GetLeaveChatlistSuggestions(TLRequest):
    CONSTRUCTOR_ID = 0xFDBCD714
    FIELDS = [TLField("chatlist", "InputChatlist")]
    chatlist: Optional[TLObject]

class LeaveChatlist(TLRequest):
    CONSTRUCTOR_ID = 0x74FAE13A
    FIELDS = [
        TLField("chatlist", "InputChatlist"),
        TLField("peers", "InputPeer", is_vector=True),
    ]
    chatlist: Optional[TLObject]
    peers: Optional[List[TLObject]]