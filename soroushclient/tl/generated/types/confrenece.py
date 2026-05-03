from typing import Optional, List

from soroushclient.tl.base import TLField, TLObject


class ConferenceCreated(TLObject):
    CONSTRUCTOR_ID = 0x4C403063
    FIELDS = [TLField("slug", "string")]
    slug: Optional[str]

class ConferenceCall(TLObject):
    CONSTRUCTOR_ID = 0xF36441D5
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("id", "long"),
        TLField("access_hash", "long"),
        TLField("seq", "int"),
        TLField("start_time", "int"),
        TLField("version", "string"),
        TLField("name", "string", flag_group=0, flag_bit=0),
        TLField("slug", "string"),
        TLField("owner", "Peer"),
    ]
    id: Optional[int]
    access_hash: Optional[int]
    seq: Optional[int]
    start_time: Optional[int]
    version: Optional[str]
    name: Optional[str]
    slug: Optional[str]
    owner: Optional[TLObject]

class ConferenceConferenceCall(TLObject):
    CONSTRUCTOR_ID = 0x278E3AE9
    FIELDS = [
        TLField("conference", "ConferenceCall"),
        TLField("participants", "ConferenceParticipant", is_vector=True),
        TLField("participants_next_offset", "string"),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    conference: Optional[TLObject]
    participants: Optional[List[TLObject]]
    participants_next_offset: Optional[str]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class BannedConferenceParticipants(TLObject):
    CONSTRUCTOR_ID = 0xB8B6C743
    FIELDS = [
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class ActiveConferenceCalls(TLObject):
    CONSTRUCTOR_ID = 0x98EC9D82
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("conferences", "ConferenceCall", is_vector=True),
        TLField("next_offset", "string", flag_group=0, flag_bit=0),
    ]
    conferences: Optional[List[TLObject]]
    next_offset: Optional[str]

class ConferenceParticipant(TLObject):
    CONSTRUCTOR_ID = 0x814BA431
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("id", "string"),
    ]
    peer: Optional[TLObject]
    id: Optional[str]

class InputConferenceCall(TLObject):
    CONSTRUCTOR_ID = 0xB2264016
    FIELDS = [
        TLField("id", "long"),
        TLField("access_hash", "long"),
    ]
    id: Optional[int]
    access_hash: Optional[int]

class InputConferenceParticipant(TLObject):
    CONSTRUCTOR_ID = 0xD5CE9E2C
    FIELDS = [TLField("id", "string")]
    id: Optional[str]

class InputConferenceMediaTrack(TLObject):
    CONSTRUCTOR_ID = 0x98587857
    FIELDS = [TLField("id", "string")]
    id: Optional[str]