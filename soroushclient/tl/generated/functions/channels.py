from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField, TLRequest


class GetFullChannelRequest(TLRequest):
    CONSTRUCTOR_ID = 0x08736A09
    FIELDS = [TLField("channel", "InputChannel")]
    channel: Optional[TLObject]

class JoinChannelRequest(TLRequest):
    CONSTRUCTOR_ID = 0x24B524C5
    FIELDS = [TLField("channel", "InputChannel")]
    channel: Optional[TLObject]

class LeaveChannelRequest(TLRequest):
    CONSTRUCTOR_ID = 0xF836AA95
    FIELDS = [TLField("channel", "InputChannel")]
    channel: Optional[TLObject]

class GetParticipants(TLRequest):
    CONSTRUCTOR_ID = 0x77CED9D0
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("filter", "ChannelParticipantsFilter"),
        TLField("offset", "int"),
        TLField("limit", "int"),
        TLField("hash", "long"),
    ]
    channel: Optional[TLObject]
    filter: Optional[TLObject]
    offset: Optional[int]
    limit: Optional[int]
    hash: Optional[int]

class EditAdmin(TLRequest):
    CONSTRUCTOR_ID = 0xD33C8902
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("user_id", "InputUser"),
        TLField("admin_rights", "ChatAdminRights"),
        TLField("rank", "string"),
    ]
    channel: Optional[TLObject]
    user_id: Optional[TLObject]
    admin_rights: Optional[TLObject]
    rank: Optional[str]

class EditBanned(TLRequest):
    CONSTRUCTOR_ID = 0x96E6CD81
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("participant", "InputPeer"),
        TLField("banned_rights", "ChatBannedRights"),
    ]
    channel: Optional[TLObject]
    participant: Optional[TLObject]
    banned_rights: Optional[TLObject]
class GetMessages(TLRequest):
    CONSTRUCTOR_ID = 0xAD8C9A23
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("id", "InputMessage", is_vector=True),
    ]
    channel: Optional[TLObject]
    id: Optional[List[TLObject]]

class ReadHistory(TLRequest):
    CONSTRUCTOR_ID = 0xCC104937
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("max_id", "int"),
    ]
    channel: Optional[TLObject]
    max_id: Optional[int]

class DeleteMessages(TLRequest):
    CONSTRUCTOR_ID = 0x84C1FD4E
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("id", "int", is_vector=True),
    ]
    channel: Optional[TLObject]
    id: Optional[List[int]]

class GetChannels(TLRequest):
    CONSTRUCTOR_ID = 0x0A7F6BBB
    FIELDS = [TLField("id", "InputChannel", is_vector=True)]
    id: Optional[List[TLObject]]

class CreateChannel(TLRequest):
    CONSTRUCTOR_ID = 0x91006707
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("broadcast", "true", flag_group=0, flag_bit=0),
        TLField("megagroup", "true", flag_group=0, flag_bit=1),
        TLField("for_import", "true", flag_group=0, flag_bit=3),
        TLField("forum", "true", flag_group=0, flag_bit=5),
        TLField("title", "string"),
        TLField("about", "string"),
        TLField("geo_point", "InputGeoPoint", flag_group=0, flag_bit=2),
        TLField("address", "string", flag_group=0, flag_bit=2),
        TLField("ttl_period", "int", flag_group=0, flag_bit=4),
    ]
    broadcast: Optional[bool]
    megagroup: Optional[bool]
    for_import: Optional[bool]
    forum: Optional[bool]
    title: Optional[str]
    about: Optional[str]
    geo_point: Optional[TLObject]
    address: Optional[str]
    ttl_period: Optional[int]

class EditTitle(TLRequest):
    CONSTRUCTOR_ID = 0x566DECD0
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("title", "string"),
    ]
    channel: Optional[TLObject]
    title: Optional[str]

class EditPhoto(TLRequest):
    CONSTRUCTOR_ID = 0xF12E57C9
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("photo", "InputChatPhoto"),
    ]
    channel: Optional[TLObject]
    photo: Optional[TLObject]

class CheckUsername(TLRequest):
    CONSTRUCTOR_ID = 0x10E6BD2C
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("username", "string"),
    ]
    channel: Optional[TLObject]
    username: Optional[str]

class UpdateUsername(TLRequest):
    CONSTRUCTOR_ID = 0x3514B3DE
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("username", "string"),
    ]
    channel: Optional[TLObject]
    username: Optional[str]

class InviteToChannel(TLRequest):
    CONSTRUCTOR_ID = 0x199F3A6C
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("users", "InputUser", is_vector=True),
    ]
    channel: Optional[TLObject]
    users: Optional[List[TLObject]]

class DeleteChannel(TLRequest):
    CONSTRUCTOR_ID = 0xC0111FE3
    FIELDS = [TLField("channel", "InputChannel")]
    channel: Optional[TLObject]

class ToggleSignatures(TLRequest):
    CONSTRUCTOR_ID = 0x1F69B606
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("enabled", "Bool"),
    ]
    channel: Optional[TLObject]
    enabled: Optional[bool]

class GetAdminedPublicChannels(TLRequest):
    CONSTRUCTOR_ID = 0xF8B036AF
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("by_location", "true", flag_group=0, flag_bit=0),
        TLField("check_limit", "true", flag_group=0, flag_bit=1),
        TLField("for_personal", "true", flag_group=0, flag_bit=2),
    ]
    by_location: Optional[bool]
    check_limit: Optional[bool]
    for_personal: Optional[bool]

class ReadMessageContents(TLRequest):
    CONSTRUCTOR_ID = 0xEAB5DC38
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("id", "int", is_vector=True),
    ]
    channel: Optional[TLObject]
    id: Optional[List[int]]

class TogglePreHistoryHidden(TLRequest):
    CONSTRUCTOR_ID = 0xEABBB94C
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("enabled", "Bool"),
    ]
    channel: Optional[TLObject]
    enabled: Optional[bool]

class GetGroupsForDiscussion(TLRequest):
    CONSTRUCTOR_ID = 0xF5DAD378
    FIELDS = []

class SetDiscussionGroup(TLRequest):
    CONSTRUCTOR_ID = 0x40582BB2
    FIELDS = [
        TLField("broadcast", "InputChannel"),
        TLField("group", "InputChannel"),
    ]
    broadcast: Optional[TLObject]
    group: Optional[TLObject]

class GetSendAs(TLRequest):
    CONSTRUCTOR_ID = 0x0DC770EE
    FIELDS = [TLField("peer", "InputPeer")]
    peer: Optional[TLObject]

class ToggleJoinToSend(TLRequest):
    CONSTRUCTOR_ID = 0xE4CB9580
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("enabled", "Bool"),
    ]
    channel: Optional[TLObject]
    enabled: Optional[bool]

class ToggleJoinRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4C2985B6
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("enabled", "Bool"),
    ]
    channel: Optional[TLObject]
    enabled: Optional[bool]

class ReorderUsernames(TLRequest):
    CONSTRUCTOR_ID = 0xB45CED1D
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("order", "string", is_vector=True),
    ]
    channel: Optional[TLObject]
    order: Optional[List[str]]

class ToggleUsername(TLRequest):
    CONSTRUCTOR_ID = 0x50F24105
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("username", "string"),
        TLField("active", "Bool"),
    ]
    channel: Optional[TLObject]
    username: Optional[str]
    active: Optional[bool]

class DeactivateAllUsernames(TLRequest):
    CONSTRUCTOR_ID = 0x0A245DD3
    FIELDS = [TLField("channel", "InputChannel")]
    channel: Optional[TLObject]

class ToggleForum(TLRequest):
    CONSTRUCTOR_ID = 0xA4298B29
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("enabled", "Bool"),
    ]
    channel: Optional[TLObject]
    enabled: Optional[bool]

class CreateForumTopic(TLRequest):
    CONSTRUCTOR_ID = 0xF40C0224
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("channel", "InputChannel"),
        TLField("title", "string"),
        TLField("icon_color", "int", flag_group=0, flag_bit=0),
        TLField("icon_emoji_id", "long", flag_group=0, flag_bit=3),
        TLField("random_id", "long"),
        TLField("send_as", "InputPeer", flag_group=0, flag_bit=2),
    ]
    channel: Optional[TLObject]
    title: Optional[str]
    icon_color: Optional[int]
    icon_emoji_id: Optional[int]
    random_id: Optional[int]
    send_as: Optional[TLObject]

class GetForumTopics(TLRequest):
    CONSTRUCTOR_ID = 0x0DE560D1
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("channel", "InputChannel"),
        TLField("q", "string", flag_group=0, flag_bit=0),
        TLField("offset_date", "int"),
        TLField("offset_id", "int"),
        TLField("offset_topic", "int"),
        TLField("limit", "int"),
    ]
    channel: Optional[TLObject]
    q: Optional[str]
    offset_date: Optional[int]
    offset_id: Optional[int]
    offset_topic: Optional[int]
    limit: Optional[int]

class GetForumTopicsByID(TLRequest):
    CONSTRUCTOR_ID = 0xB0831EB9
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("topics", "int", is_vector=True),
    ]
    channel: Optional[TLObject]
    topics: Optional[List[int]]

class EditForumTopic(TLRequest):
    CONSTRUCTOR_ID = 0xF4DFA185
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("channel", "InputChannel"),
        TLField("topic_id", "int"),
        TLField("title", "string", flag_group=0, flag_bit=0),
        TLField("icon_emoji_id", "long", flag_group=0, flag_bit=1),
        TLField("closed", "Bool", flag_group=0, flag_bit=2),
        TLField("hidden", "Bool", flag_group=0, flag_bit=3),
    ]
    channel: Optional[TLObject]
    topic_id: Optional[int]
    title: Optional[str]
    icon_emoji_id: Optional[int]
    closed: Optional[bool]
    hidden: Optional[bool]

class UpdatePinnedForumTopic(TLRequest):
    CONSTRUCTOR_ID = 0x6C2D9026
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("topic_id", "int"),
        TLField("pinned", "Bool"),
    ]
    channel: Optional[TLObject]
    topic_id: Optional[int]
    pinned: Optional[bool]

class DeleteTopicHistory(TLRequest):
    CONSTRUCTOR_ID = 0x34435F2D
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("top_msg_id", "int"),
    ]
    channel: Optional[TLObject]
    top_msg_id: Optional[int]

class ToggleParticipantsHidden(TLRequest):
    CONSTRUCTOR_ID = 0x6A6E7854
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("enabled", "Bool"),
    ]
    channel: Optional[TLObject]
    enabled: Optional[bool]

class ToggleViewForumAsMessages(TLRequest):
    CONSTRUCTOR_ID = 0x9738BB15
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("enabled", "Bool"),
    ]
    channel: Optional[TLObject]
    enabled: Optional[bool]

class GetSponsoredMessages(TLRequest):
    CONSTRUCTOR_ID = 0xEC210FBF
    FIELDS = [TLField("channel", "InputChannel")]
    channel: Optional[TLObject]

class ViewSponsoredMessage(TLRequest):
    CONSTRUCTOR_ID = 0xBEAEDB94
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("random_id", "bytes"),
    ]
    channel: Optional[TLObject]
    random_id: Optional[bytes]

class ClickSponsoredMessage(TLRequest):
    CONSTRUCTOR_ID = 0x18AFBC93
    FIELDS = [
        TLField("channel", "InputChannel"),
        TLField("random_id", "bytes"),
    ]
    channel: Optional[TLObject]
    random_id: Optional[bytes]