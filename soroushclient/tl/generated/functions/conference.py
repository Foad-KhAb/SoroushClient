from typing import Optional

from soroushclient.tl.base import TLObject, TLField, TLRequest


class CreateConferenceCall(TLRequest):
    CONSTRUCTOR_ID = 0x350BA3BD
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("version", "string"),
        TLField("random_id", "long"),
        TLField("name", "string", flag_group=0, flag_bit=0),
    ]
    version: Optional[str]
    random_id: Optional[int]
    name: Optional[str]

class ResolveConferenceCall(TLRequest):
    CONSTRUCTOR_ID = 0x3AF930B4
    FIELDS = [TLField("slug", "string")]
    slug: Optional[str]

class GetConferenceCall(TLRequest):
    CONSTRUCTOR_ID = 0x78BA8198
    FIELDS = [TLField("conference", "InputConferenceCall")]
    conference: Optional[TLObject]

class JoinConferenceCall(TLRequest):
    CONSTRUCTOR_ID = 0x2B04C211
    FIELDS = [
        TLField("version", "string"),
        TLField("conference", "InputConferenceCall"),
    ]
    version: Optional[str]
    conference: Optional[TLObject]

class LeaveConferenceCall(TLRequest):
    CONSTRUCTOR_ID = 0xE5F83A5E
    FIELDS = [TLField("conference", "InputConferenceCall")]
    conference: Optional[TLObject]

class DiscardConferenceCall(TLRequest):
    CONSTRUCTOR_ID = 0x51620842
    FIELDS = [TLField("conference", "InputConferenceCall")]
    conference: Optional[TLObject]

class RemoveConferenceParticipant(TLRequest):
    CONSTRUCTOR_ID = 0x2D3E2518
    FIELDS = [
        TLField("conference", "InputConferenceCall"),
        TLField("participant", "InputConferenceParticipant"),
    ]
    conference: Optional[TLObject]
    participant: Optional[TLObject]

class BanConferenceParticipant(TLRequest):
    CONSTRUCTOR_ID = 0x799A53FC
    FIELDS = [
        TLField("conference", "InputConferenceCall"),
        TLField("peer", "InputPeer"),
    ]
    conference: Optional[TLObject]
    peer: Optional[TLObject]

class UnbanConferenceParticipant(TLRequest):
    CONSTRUCTOR_ID = 0xADD30F09
    FIELDS = [
        TLField("conference", "InputConferenceCall"),
        TLField("peer", "InputPeer"),
    ]
    conference: Optional[TLObject]
    peer: Optional[TLObject]

class GetBannedConferenceParticipants(TLRequest):
    CONSTRUCTOR_ID = 0x7D69C24C
    FIELDS = [TLField("conference", "InputConferenceCall")]
    conference: Optional[TLObject]

class GetActiveConferenceCalls(TLRequest):
    CONSTRUCTOR_ID = 0xC3F93E37
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("limit", "int"),
        TLField("offset", "string", flag_group=0, flag_bit=0),
    ]
    limit: Optional[int]
    offset: Optional[str]

class MuteConferenceParticipant(TLRequest):
    CONSTRUCTOR_ID = 0xD9A6240F
    FIELDS = [
        TLField("conference", "InputConferenceCall"),
        TLField("participant", "InputConferenceParticipant"),
        TLField("track", "InputConferenceMediaTrack"),
    ]
    conference: Optional[TLObject]
    participant: Optional[TLObject]
    track: Optional[TLObject]