from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField, TLRequest


class RequestCall(TLRequest):
    CONSTRUCTOR_ID = 0x42FF96ED
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("video", "true", flag_group=0, flag_bit=0),
        TLField("user_id", "InputUser"),
        TLField("random_id", "int"),
        TLField("g_a_hash", "bytes"),
        TLField("protocol", "PhoneCallProtocol"),
    ]
    video: Optional[bool]
    user_id: Optional[TLObject]
    random_id: Optional[int]
    g_a_hash: Optional[bytes]
    protocol: Optional[TLObject]

class AcceptCall(TLRequest):
    CONSTRUCTOR_ID = 0x3BD2B4A0
    FIELDS = [
        TLField("peer", "InputPhoneCall"),
        TLField("g_b", "bytes"),
        TLField("protocol", "PhoneCallProtocol"),
    ]
    peer: Optional[TLObject]
    g_b: Optional[bytes]
    protocol: Optional[TLObject]

class ConfirmCall(TLRequest):
    CONSTRUCTOR_ID = 0x2EFE1722
    FIELDS = [
        TLField("peer", "InputPhoneCall"),
        TLField("g_a", "bytes"),
        TLField("key_fingerprint", "long"),
        TLField("protocol", "PhoneCallProtocol"),
    ]
    peer: Optional[TLObject]
    g_a: Optional[bytes]
    key_fingerprint: Optional[int]
    protocol: Optional[TLObject]

class ReceivedCall(TLRequest):
    CONSTRUCTOR_ID = 0x17D54F61
    FIELDS = [TLField("peer", "InputPhoneCall")]
    peer: Optional[TLObject]

class DiscardCall(TLRequest):
    CONSTRUCTOR_ID = 0xB2CBC1C0
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("video", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputPhoneCall"),
        TLField("duration", "int"),
        TLField("reason", "PhoneCallDiscardReason"),
        TLField("connection_id", "long"),
    ]
    video: Optional[bool]
    peer: Optional[TLObject]
    duration: Optional[int]
    reason: Optional[TLObject]
    connection_id: Optional[int]

class SetCallRating(TLRequest):
    CONSTRUCTOR_ID = 0x59EAD627
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("user_initiative", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputPhoneCall"),
        TLField("rating", "int"),
        TLField("comment", "string"),
    ]
    user_initiative: Optional[bool]
    peer: Optional[TLObject]
    rating: Optional[int]
    comment: Optional[str]

class SaveCallDebug(TLRequest):
    CONSTRUCTOR_ID = 0x277ADD7E
    FIELDS = [
        TLField("peer", "InputPhoneCall"),
        TLField("debug", "DataJSON"),
    ]
    peer: Optional[TLObject]
    debug: Optional[TLObject]

class SendSignalingData(TLRequest):
    CONSTRUCTOR_ID = 0xFF7A9383
    FIELDS = [
        TLField("peer", "InputPhoneCall"),
        TLField("data", "bytes"),
    ]
    peer: Optional[TLObject]
    data: Optional[bytes]

class CreateGroupCall(TLRequest):
    CONSTRUCTOR_ID = 0x48CDC6D8
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("rtmp_stream", "true", flag_group=0, flag_bit=2),
        TLField("peer", "InputPeer"),
        TLField("random_id", "int"),
        TLField("title", "string", flag_group=0, flag_bit=0),
        TLField("schedule_date", "int", flag_group=0, flag_bit=1),
    ]
    rtmp_stream: Optional[bool]
    peer: Optional[TLObject]
    random_id: Optional[int]
    title: Optional[str]
    schedule_date: Optional[int]

class JoinGroupCall(TLRequest):
    CONSTRUCTOR_ID = 0xB132FF7B
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("muted", "true", flag_group=0, flag_bit=0),
        TLField("video_stopped", "true", flag_group=0, flag_bit=2),
        TLField("call", "InputGroupCall"),
        TLField("join_as", "InputPeer"),
        TLField("invite_hash", "string", flag_group=0, flag_bit=1),
        TLField("params", "DataJSON"),
    ]
    muted: Optional[bool]
    video_stopped: Optional[bool]
    call: Optional[TLObject]
    join_as: Optional[TLObject]
    invite_hash: Optional[str]
    params: Optional[TLObject]

class LeaveGroupCall(TLRequest):
    CONSTRUCTOR_ID = 0x500377F9
    FIELDS = [
        TLField("call", "InputGroupCall"),
        TLField("source", "int"),
    ]
    call: Optional[TLObject]
    source: Optional[int]

class DiscardGroupCall(TLRequest):
    CONSTRUCTOR_ID = 0x7A777135
    FIELDS = [TLField("call", "InputGroupCall")]
    call: Optional[TLObject]

class GetGroupCall(TLRequest):
    CONSTRUCTOR_ID = 0x041845DB
    FIELDS = [
        TLField("call", "InputGroupCall"),
        TLField("limit", "int"),
    ]
    call: Optional[TLObject]
    limit: Optional[int]

class GetGroupParticipants(TLRequest):
    CONSTRUCTOR_ID = 0xC558D8AB
    FIELDS = [
        TLField("call", "InputGroupCall"),
        TLField("ids", "InputPeer", is_vector=True),
        TLField("sources", "int", is_vector=True),
        TLField("offset", "string"),
        TLField("limit", "int"),
    ]
    call: Optional[TLObject]
    ids: Optional[List[TLObject]]
    sources: Optional[List[int]]
    offset: Optional[str]
    limit: Optional[int]

class EditGroupCallParticipant(TLRequest):
    CONSTRUCTOR_ID = 0xA5273ABF
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("call", "InputGroupCall"),
        TLField("participant", "InputPeer"),
        TLField("muted", "Bool", flag_group=0, flag_bit=0),
        TLField("volume", "int", flag_group=0, flag_bit=1),
        TLField("raise_hand", "Bool", flag_group=0, flag_bit=2),
        TLField("video_stopped", "Bool", flag_group=0, flag_bit=3),
        TLField("video_paused", "Bool", flag_group=0, flag_bit=4),
        TLField("presentation_paused", "Bool", flag_group=0, flag_bit=5),
    ]
    call: Optional[TLObject]
    participant: Optional[TLObject]
    muted: Optional[bool]
    volume: Optional[int]
    raise_hand: Optional[bool]
    video_stopped: Optional[bool]
    video_paused: Optional[bool]
    presentation_paused: Optional[bool]

class ExportGroupCallInvite(TLRequest):
    CONSTRUCTOR_ID = 0xE6AA647F
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("can_self_unmute", "true", flag_group=0, flag_bit=0),
        TLField("call", "InputGroupCall"),
    ]
    can_self_unmute: Optional[bool]
    call: Optional[TLObject]