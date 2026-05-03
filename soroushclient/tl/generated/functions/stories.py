from typing import Optional, List

from soroushclient.tl.base import TLRequest, TLField, TLObject


class EditStory(TLRequest):
    CONSTRUCTOR_ID = 0xB583BA46
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "InputPeer"),
        TLField("id", "int"),
        TLField("media", "InputMedia", flag_group=0, flag_bit=0),
        TLField("media_areas", "MediaArea", flag_group=0, flag_bit=3, is_vector=True),
        TLField("caption", "string", flag_group=0, flag_bit=1),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=1, is_vector=True),
        TLField("privacy_rules", "InputPrivacyRule", flag_group=0, flag_bit=2, is_vector=True),
    ]
    peer: Optional[TLObject]
    id: Optional[int]
    media: Optional[TLObject]
    media_areas: Optional[List[TLObject]]
    caption: Optional[str]
    entities: Optional[List[TLObject]]
    privacy_rules: Optional[List[TLObject]]

class DeleteStories(TLRequest):
    CONSTRUCTOR_ID = 0xAE59DB5F
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int", is_vector=True),
    ]
    peer: Optional[TLObject]
    id: Optional[List[int]]

class TogglePinned(TLRequest):
    CONSTRUCTOR_ID = 0x9A75A1EF
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int", is_vector=True),
        TLField("pinned", "Bool"),
    ]
    peer: Optional[TLObject]
    id: Optional[List[int]]
    pinned: Optional[bool]

class GetAllStories(TLRequest):
    CONSTRUCTOR_ID = 0xEEB0D625
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("next", "true", flag_group=0, flag_bit=1),
        TLField("hidden", "true", flag_group=0, flag_bit=2),
        TLField("state", "string", flag_group=0, flag_bit=0),
    ]
    next: Optional[bool]
    hidden: Optional[bool]
    state: Optional[str]

class GetPinnedStories(TLRequest):
    CONSTRUCTOR_ID = 0x5821A5DC
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("offset_id", "int"),
        TLField("limit", "int"),
    ]
    peer: Optional[TLObject]
    offset_id: Optional[int]
    limit: Optional[int]

class GetStoriesArchive(TLRequest):
    CONSTRUCTOR_ID = 0xB4352016
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("offset_id", "int"),
        TLField("limit", "int"),
    ]
    peer: Optional[TLObject]
    offset_id: Optional[int]
    limit: Optional[int]

class GetStoriesByID(TLRequest):
    CONSTRUCTOR_ID = 0x5774CA74
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int", is_vector=True),
    ]
    peer: Optional[TLObject]
    id: Optional[List[int]]

class ReadStories(TLRequest):
    CONSTRUCTOR_ID = 0xA556DAC8
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("max_id", "int"),
    ]
    peer: Optional[TLObject]
    max_id: Optional[int]

class IncrementStoryViews(TLRequest):
    CONSTRUCTOR_ID = 0xB2028AFB
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int", is_vector=True),
    ]
    peer: Optional[TLObject]
    id: Optional[List[int]]

class GetStoryViewsList(TLRequest):
    CONSTRUCTOR_ID = 0x7ED23C57
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("just_contacts", "true", flag_group=0, flag_bit=0),
        TLField("reactions_first", "true", flag_group=0, flag_bit=2),
        TLField("peer", "InputPeer"),
        TLField("q", "string", flag_group=0, flag_bit=1),
        TLField("id", "int"),
        TLField("offset", "string"),
        TLField("limit", "int"),
    ]
    just_contacts: Optional[bool]
    reactions_first: Optional[bool]
    peer: Optional[TLObject]
    q: Optional[str]
    id: Optional[int]
    offset: Optional[str]
    limit: Optional[int]

class ExportStoryLink(TLRequest):
    CONSTRUCTOR_ID = 0x7B8DEF20
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int"),
    ]
    peer: Optional[TLObject]
    id: Optional[int]

class ReportStory(TLRequest):
    CONSTRUCTOR_ID = 0x1923FA8C
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int", is_vector=True),
        TLField("reason", "ReportReason"),
        TLField("message", "string"),
    ]
    peer: Optional[TLObject]
    id: Optional[List[int]]
    reason: Optional[TLObject]
    message: Optional[str]

class ActivateStealthMode(TLRequest):
    CONSTRUCTOR_ID = 0x57BBD166
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("past", "true", flag_group=0, flag_bit=0),
        TLField("future", "true", flag_group=0, flag_bit=1),
    ]
    past: Optional[bool]
    future: Optional[bool]

class SendReaction(TLRequest):
    CONSTRUCTOR_ID = 0x7FD736B2
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("add_to_recent", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputPeer"),
        TLField("story_id", "int"),
        TLField("reaction", "Reaction"),
    ]
    add_to_recent: Optional[bool]
    peer: Optional[TLObject]
    story_id: Optional[int]
    reaction: Optional[TLObject]

class GetPeerStories(TLRequest):
    CONSTRUCTOR_ID = 0x2C4ADA50
    FIELDS = [TLField("peer", "InputPeer")]
    peer: Optional[TLObject]

class GetPeerMaxIDs(TLRequest):
    CONSTRUCTOR_ID = 0x535983C3
    FIELDS = [TLField("id", "InputPeer", is_vector=True)]
    id: Optional[List[TLObject]]

class TogglePeerStoriesHidden(TLRequest):
    CONSTRUCTOR_ID = 0xBD0415C4
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("hidden", "Bool"),
    ]
    peer: Optional[TLObject]
    hidden: Optional[bool]