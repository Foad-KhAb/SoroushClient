from typing import Optional, List

from soroushclient.tl.base import TLField, TLObject, TLRequest


class GetMessages(TLRequest):
    CONSTRUCTOR_ID = 0x63C66506
    FIELDS = [TLField("id", "InputMessage", is_vector=True)]
    id: Optional[List[TLObject]]

class GetHistoryRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4423E6C5
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("offset_id", "int"),
        TLField("offset_date", "int"),
        TLField("add_offset", "int"),
        TLField("limit", "int"),
        TLField("max_id", "int"),
        TLField("min_id", "int"),
        TLField("hash", "long"),
    ]
    peer: Optional[TLObject]
    offset_id: Optional[int]
    offset_date: Optional[int]
    add_offset: Optional[int]
    limit: Optional[int]
    max_id: Optional[int]
    min_id: Optional[int]
    hash: Optional[int]

class Search(TLRequest):
    CONSTRUCTOR_ID = 0xA0FDA762
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "InputPeer"),
        TLField("q", "string"),
        TLField("from_id", "InputPeer", flag_group=0, flag_bit=0),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=1),
        TLField("filter", "MessagesFilter"),
        TLField("min_date", "int"),
        TLField("max_date", "int"),
        TLField("offset_id", "int"),
        TLField("add_offset", "int"),
        TLField("limit", "int"),
        TLField("max_id", "int"),
        TLField("min_id", "int"),
        TLField("hash", "long"),
    ]
    peer: Optional[TLObject]
    q: Optional[str]
    from_id: Optional[TLObject]
    top_msg_id: Optional[int]
    filter: Optional[TLObject]
    min_date: Optional[int]
    max_date: Optional[int]
    offset_id: Optional[int]
    add_offset: Optional[int]
    limit: Optional[int]
    max_id: Optional[int]
    min_id: Optional[int]
    hash: Optional[int]

class ReadHistory(TLRequest):
    CONSTRUCTOR_ID = 0x0E306D3A
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("max_id", "int"),
    ]
    peer: Optional[TLObject]
    max_id: Optional[int]

class DeleteHistory(TLRequest):
    CONSTRUCTOR_ID = 0xB08F922A
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("just_clear", "true", flag_group=0, flag_bit=0),
        TLField("revoke", "true", flag_group=0, flag_bit=1),
        TLField("peer", "InputPeer"),
        TLField("max_id", "int"),
        TLField("min_date", "int", flag_group=0, flag_bit=2),
        TLField("max_date", "int", flag_group=0, flag_bit=3),
    ]
    just_clear: Optional[bool]
    revoke: Optional[bool]
    peer: Optional[TLObject]
    max_id: Optional[int]
    min_date: Optional[int]
    max_date: Optional[int]

class DeleteMessages(TLRequest):
    CONSTRUCTOR_ID = 0xE547869B
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("revoke", "true", flag_group=0, flag_bit=0),
        TLField("id", "int", is_vector=True),
        TLField("peer", "InputPeer", flag_group=0, flag_bit=30),
    ]
    revoke: Optional[bool]
    id: Optional[List[int]]
    peer: Optional[TLObject]

class ReceivedMessages(TLRequest):
    CONSTRUCTOR_ID = 0x05A954C0
    FIELDS = [TLField("max_id", "int")]
    max_id: Optional[int]

class SetTyping(TLRequest):
    CONSTRUCTOR_ID = 0x58943EE2
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "InputPeer"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=0),
        TLField("action", "SendMessageAction"),
    ]
    peer: Optional[TLObject]
    top_msg_id: Optional[int]
    action: Optional[TLObject]

class SendMedia(TLRequest):
    CONSTRUCTOR_ID = 0x72CCC23D
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("silent", "true", flag_group=0, flag_bit=5),
        TLField("background", "true", flag_group=0, flag_bit=6),
        TLField("clear_draft", "true", flag_group=0, flag_bit=7),
        TLField("noforwards", "true", flag_group=0, flag_bit=14),
        TLField("update_stickersets_order", "true", flag_group=0, flag_bit=15),
        TLField("invert_media", "true", flag_group=0, flag_bit=16),
        TLField("peer", "InputPeer"),
        TLField("reply_to", "InputReplyTo", flag_group=0, flag_bit=0),
        TLField("media", "InputMedia"),
        TLField("message", "string"),
        TLField("random_id", "long"),
        TLField("reply_markup", "ReplyMarkup", flag_group=0, flag_bit=2),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=3, is_vector=True),
        TLField("schedule_date", "int", flag_group=0, flag_bit=10),
        TLField("send_as", "InputPeer", flag_group=0, flag_bit=13),
    ]
    silent: Optional[bool]
    background: Optional[bool]
    clear_draft: Optional[bool]
    noforwards: Optional[bool]
    update_stickersets_order: Optional[bool]
    invert_media: Optional[bool]
    peer: Optional[TLObject]
    reply_to: Optional[TLObject]
    media: Optional[TLObject]
    message: Optional[str]
    random_id: Optional[int]
    reply_markup: Optional[TLObject]
    entities: Optional[List[TLObject]]
    schedule_date: Optional[int]
    send_as: Optional[TLObject]

class ForwardMessages(TLRequest):
    CONSTRUCTOR_ID = 0xC661BBC4
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("silent", "true", flag_group=0, flag_bit=5),
        TLField("background", "true", flag_group=0, flag_bit=6),
        TLField("with_my_score", "true", flag_group=0, flag_bit=8),
        TLField("drop_author", "true", flag_group=0, flag_bit=11),
        TLField("drop_media_captions", "true", flag_group=0, flag_bit=12),
        TLField("noforwards", "true", flag_group=0, flag_bit=14),
        TLField("from_peer", "InputPeer"),
        TLField("id", "int", is_vector=True),
        TLField("random_id", "long", is_vector=True),
        TLField("to_peer", "InputPeer"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=9),
        TLField("schedule_date", "int", flag_group=0, flag_bit=10),
        TLField("send_as", "InputPeer", flag_group=0, flag_bit=13),
    ]
    silent: Optional[bool]
    background: Optional[bool]
    with_my_score: Optional[bool]
    drop_author: Optional[bool]
    drop_media_captions: Optional[bool]
    noforwards: Optional[bool]
    from_peer: Optional[TLObject]
    id: Optional[List[int]]
    random_id: Optional[List[int]]
    to_peer: Optional[TLObject]
    top_msg_id: Optional[int]
    schedule_date: Optional[int]
    send_as: Optional[TLObject]

class EditMessage(TLRequest):
    CONSTRUCTOR_ID = 0x48F71778
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("no_webpage", "true", flag_group=0, flag_bit=1),
        TLField("invert_media", "true", flag_group=0, flag_bit=16),
        TLField("peer", "InputPeer"),
        TLField("id", "int"),
        TLField("message", "string", flag_group=0, flag_bit=11),
        TLField("media", "InputMedia", flag_group=0, flag_bit=14),
        TLField("reply_markup", "ReplyMarkup", flag_group=0, flag_bit=2),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=3, is_vector=True),
        TLField("schedule_date", "int", flag_group=0, flag_bit=15),
    ]
    no_webpage: Optional[bool]
    invert_media: Optional[bool]
    peer: Optional[TLObject]
    id: Optional[int]
    message: Optional[str]
    media: Optional[TLObject]
    reply_markup: Optional[TLObject]
    entities: Optional[List[TLObject]]
    schedule_date: Optional[int]

class GetPeerSettings(TLRequest):
    CONSTRUCTOR_ID = 0xEFD9A6A2
    FIELDS = [TLField("peer", "InputPeer")]
    peer: Optional[TLObject]

class Report(TLRequest):
    CONSTRUCTOR_ID = 0x8953AB4E
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

class ReportSpam(TLRequest):
    CONSTRUCTOR_ID = 0xCF1592DB
    FIELDS = [TLField("peer", "InputPeer")]
    peer: Optional[TLObject]

class ReadMessageContents(TLRequest):
    CONSTRUCTOR_ID = 0x36A73F77
    FIELDS = [TLField("id", "int", is_vector=True)]
    id: Optional[List[int]]

class GetDhConfig(TLRequest):
    CONSTRUCTOR_ID = 0x26CF8950
    FIELDS = [
        TLField("version", "int"),
        TLField("random_length", "int"),
    ]
    version: Optional[int]
    random_length: Optional[int]

class GetWebPagePreview(TLRequest):
    CONSTRUCTOR_ID = 0x8B68B0CC
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("message", "string"),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=3, is_vector=True),
    ]
    message: Optional[str]
    entities: Optional[List[TLObject]]

class ExportChatInvite(TLRequest):
    CONSTRUCTOR_ID = 0xA02CE5D5
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("legacy_revoke_permanent", "true", flag_group=0, flag_bit=2),
        TLField("request_needed", "true", flag_group=0, flag_bit=3),
        TLField("peer", "InputPeer"),
        TLField("expire_date", "int", flag_group=0, flag_bit=0),
        TLField("usage_limit", "int", flag_group=0, flag_bit=1),
        TLField("title", "string", flag_group=0, flag_bit=4),
    ]
    legacy_revoke_permanent: Optional[bool]
    request_needed: Optional[bool]
    peer: Optional[TLObject]
    expire_date: Optional[int]
    usage_limit: Optional[int]
    title: Optional[str]

class CheckChatInvite(TLRequest):
    CONSTRUCTOR_ID = 0x3EADB1BB
    FIELDS = [TLField("hash", "string")]
    hash: Optional[str]

class GetStickerSet(TLRequest):
    CONSTRUCTOR_ID = 0xC8A0EC74
    FIELDS = [
        TLField("stickerset", "InputStickerSet"),
        TLField("hash", "int"),
    ]
    stickerset: Optional[TLObject]
    hash: Optional[int]

class StartBot(TLRequest):
    CONSTRUCTOR_ID = 0xE6DF7378
    FIELDS = [
        TLField("bot", "InputUser"),
        TLField("peer", "InputPeer"),
        TLField("random_id", "long"),
        TLField("start_param", "string"),
    ]
    bot: Optional[TLObject]
    peer: Optional[TLObject]
    random_id: Optional[int]
    start_param: Optional[str]

class SearchGlobal(TLRequest):
    CONSTRUCTOR_ID = 0x4BC6589A
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("folder_id", "int", flag_group=0, flag_bit=0),
        TLField("q", "string"),
        TLField("filter", "MessagesFilter"),
        TLField("min_date", "int"),
        TLField("max_date", "int"),
        TLField("offset_rate", "int"),
        TLField("offset_peer", "InputPeer"),
        TLField("offset_id", "int"),
        TLField("limit", "int"),
    ]
    folder_id: Optional[int]
    q: Optional[str]
    filter: Optional[TLObject]
    min_date: Optional[int]
    max_date: Optional[int]
    offset_rate: Optional[int]
    offset_peer: Optional[TLObject]
    offset_id: Optional[int]
    limit: Optional[int]

class UpdatePinnedMessage(TLRequest):
    CONSTRUCTOR_ID = 0xD2AAF7EC
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("silent", "true", flag_group=0, flag_bit=0),
        TLField("unpin", "true", flag_group=0, flag_bit=1),
        TLField("pm_oneside", "true", flag_group=0, flag_bit=2),
        TLField("peer", "InputPeer"),
        TLField("id", "int"),
    ]
    silent: Optional[bool]
    unpin: Optional[bool]
    pm_oneside: Optional[bool]
    peer: Optional[TLObject]
    id: Optional[int]

class UnpinAllMessages(TLRequest):
    CONSTRUCTOR_ID = 0xEE22B9A8
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "InputPeer"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=0),
    ]
    peer: Optional[TLObject]
    top_msg_id: Optional[int]

class GetUnreadMentions(TLRequest):
    CONSTRUCTOR_ID = 0xF107E790
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "InputPeer"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=0),
        TLField("offset_id", "int"),
        TLField("add_offset", "int"),
        TLField("limit", "int"),
        TLField("max_id", "int"),
        TLField("min_id", "int"),
    ]
    peer: Optional[TLObject]
    top_msg_id: Optional[int]
    offset_id: Optional[int]
    add_offset: Optional[int]
    limit: Optional[int]
    max_id: Optional[int]
    min_id: Optional[int]

class ReadMentions(TLRequest):
    CONSTRUCTOR_ID = 0x36E5BF4D
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "InputPeer"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=0),
    ]
    peer: Optional[TLObject]
    top_msg_id: Optional[int]

class SendMultiMedia(TLRequest):
    CONSTRUCTOR_ID = 0x456E8987
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("silent", "true", flag_group=0, flag_bit=5),
        TLField("background", "true", flag_group=0, flag_bit=6),
        TLField("clear_draft", "true", flag_group=0, flag_bit=7),
        TLField("noforwards", "true", flag_group=0, flag_bit=14),
        TLField("update_stickersets_order", "true", flag_group=0, flag_bit=15),
        TLField("invert_media", "true", flag_group=0, flag_bit=16),
        TLField("peer", "InputPeer"),
        TLField("reply_to", "InputReplyTo", flag_group=0, flag_bit=0),
        TLField("multi_media", "InputSingleMedia", is_vector=True),
        TLField("schedule_date", "int", flag_group=0, flag_bit=10),
        TLField("send_as", "InputPeer", flag_group=0, flag_bit=13),
    ]
    silent: Optional[bool]
    background: Optional[bool]
    clear_draft: Optional[bool]
    noforwards: Optional[bool]
    update_stickersets_order: Optional[bool]
    invert_media: Optional[bool]
    peer: Optional[TLObject]
    reply_to: Optional[TLObject]
    multi_media: Optional[List[TLObject]]
    schedule_date: Optional[int]
    send_as: Optional[TLObject]

class UploadMedia(TLRequest):
    CONSTRUCTOR_ID = 0x519BC2B1
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("media", "InputMedia"),
    ]
    peer: Optional[TLObject]
    media: Optional[TLObject]

class SaveDraft(TLRequest):
    CONSTRUCTOR_ID = 0x7FF3B806
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("no_webpage", "true", flag_group=0, flag_bit=1),
        TLField("invert_media", "true", flag_group=0, flag_bit=6),
        TLField("reply_to", "InputReplyTo", flag_group=0, flag_bit=4),
        TLField("peer", "InputPeer"),
        TLField("message", "string"),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=3, is_vector=True),
        TLField("media", "InputMedia", flag_group=0, flag_bit=5),
    ]
    no_webpage: Optional[bool]
    invert_media: Optional[bool]
    reply_to: Optional[TLObject]
    peer: Optional[TLObject]
    message: Optional[str]
    entities: Optional[List[TLObject]]
    media: Optional[TLObject]

class SendVote(TLRequest):
    CONSTRUCTOR_ID = 0x10EA6184
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
        TLField("options", "bytes", is_vector=True),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    options: Optional[List[bytes]]

class GetPollResults(TLRequest):
    CONSTRUCTOR_ID = 0x73BB643B
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]

class GetOnlines(TLRequest):
    CONSTRUCTOR_ID = 0x6E2BE050
    FIELDS = [TLField("peer", "InputPeer")]
    peer: Optional[TLObject]

class GetReplies(TLRequest):
    CONSTRUCTOR_ID = 0x22DDD30C
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
        TLField("offset_id", "int"),
        TLField("offset_date", "int"),
        TLField("add_offset", "int"),
        TLField("limit", "int"),
        TLField("max_id", "int"),
        TLField("min_id", "int"),
        TLField("hash", "long"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    offset_id: Optional[int]
    offset_date: Optional[int]
    add_offset: Optional[int]
    limit: Optional[int]
    max_id: Optional[int]
    min_id: Optional[int]
    hash: Optional[int]

class GetDiscussionMessage(TLRequest):
    CONSTRUCTOR_ID = 0x446972FD
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]

class ReadDiscussion(TLRequest):
    CONSTRUCTOR_ID = 0xF731A9F4
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
        TLField("read_max_id", "int"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    read_max_id: Optional[int]

class GetScheduledHistory(TLRequest):
    CONSTRUCTOR_ID = 0xF516760B
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("hash", "long"),
    ]
    peer: Optional[TLObject]
    hash: Optional[int]

class SendScheduledMessages(TLRequest):
    CONSTRUCTOR_ID = 0xBD38850A
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int", is_vector=True),
    ]
    peer: Optional[TLObject]
    id: Optional[List[int]]

class DeleteScheduledMessages(TLRequest):
    CONSTRUCTOR_ID = 0x59AE2B16
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int", is_vector=True),
    ]
    peer: Optional[TLObject]
    id: Optional[List[int]]

class GetExportedChatInvites(TLRequest):
    CONSTRUCTOR_ID = 0xA2B5A3F6
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("revoked", "true", flag_group=0, flag_bit=3),
        TLField("peer", "InputPeer"),
        TLField("admin_id", "InputUser"),
        TLField("offset_date", "int", flag_group=0, flag_bit=2),
        TLField("offset_link", "string", flag_group=0, flag_bit=2),
        TLField("limit", "int"),
    ]
    revoked: Optional[bool]
    peer: Optional[TLObject]
    admin_id: Optional[TLObject]
    offset_date: Optional[int]
    offset_link: Optional[str]
    limit: Optional[int]

class EditExportedChatInvite(TLRequest):
    CONSTRUCTOR_ID = 0xBDCA2F75
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("revoked", "true", flag_group=0, flag_bit=2),
        TLField("peer", "InputPeer"),
        TLField("link", "string"),
        TLField("expire_date", "int", flag_group=0, flag_bit=0),
        TLField("usage_limit", "int", flag_group=0, flag_bit=1),
        TLField("request_needed", "Bool", flag_group=0, flag_bit=3),
        TLField("title", "string", flag_group=0, flag_bit=4),
    ]
    revoked: Optional[bool]
    peer: Optional[TLObject]
    link: Optional[str]
    expire_date: Optional[int]
    usage_limit: Optional[int]
    request_needed: Optional[bool]
    title: Optional[str]

class DeleteRevokedExportedChatInvites(TLRequest):
    CONSTRUCTOR_ID = 0x56987BD5
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("admin_id", "InputUser"),
    ]
    peer: Optional[TLObject]
    admin_id: Optional[TLObject]

class DeleteExportedChatInvite(TLRequest):
    CONSTRUCTOR_ID = 0xD464A42B
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("link", "string"),
    ]
    peer: Optional[TLObject]
    link: Optional[str]

class GetChatInviteImporters(TLRequest):
    CONSTRUCTOR_ID = 0xDF04DD4E
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("requested", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputPeer"),
        TLField("link", "string", flag_group=0, flag_bit=1),
        TLField("q", "string", flag_group=0, flag_bit=2),
        TLField("offset_date", "int"),
        TLField("offset_user", "InputUser"),
        TLField("limit", "int"),
    ]
    requested: Optional[bool]
    peer: Optional[TLObject]
    link: Optional[str]
    q: Optional[str]
    offset_date: Optional[int]
    offset_user: Optional[TLObject]
    limit: Optional[int]

class GetMessageReadParticipants(TLRequest):
    CONSTRUCTOR_ID = 0x31C1C44F
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]

class HideChatJoinRequest(TLRequest):
    CONSTRUCTOR_ID = 0x7FE7E815
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("approved", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputPeer"),
        TLField("user_id", "InputUser"),
    ]
    approved: Optional[bool]
    peer: Optional[TLObject]
    user_id: Optional[TLObject]

class HideAllChatJoinRequests(TLRequest):
    CONSTRUCTOR_ID = 0xE085F4EA
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("approved", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputPeer"),
        TLField("link", "string", flag_group=0, flag_bit=1),
    ]
    approved: Optional[bool]
    peer: Optional[TLObject]
    link: Optional[str]

class ToggleNoForwards(TLRequest):
    CONSTRUCTOR_ID = 0xB11EAFA2
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("enabled", "Bool"),
    ]
    peer: Optional[TLObject]
    enabled: Optional[bool]

class SaveDefaultSendAs(TLRequest):
    CONSTRUCTOR_ID = 0xCCFDDF96
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("send_as", "InputPeer"),
    ]
    peer: Optional[TLObject]
    send_as: Optional[TLObject]

class SendReaction(TLRequest):
    CONSTRUCTOR_ID = 0xD30D78D4
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("big", "true", flag_group=0, flag_bit=1),
        TLField("add_to_recent", "true", flag_group=0, flag_bit=2),
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
        TLField("reaction", "Reaction", flag_group=0, flag_bit=0, is_vector=True),
    ]
    big: Optional[bool]
    add_to_recent: Optional[bool]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    reaction: Optional[List[TLObject]]

class GetMessagesReactions(TLRequest):
    CONSTRUCTOR_ID = 0x8BBA90E6
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int", is_vector=True),
    ]
    peer: Optional[TLObject]
    id: Optional[List[int]]

class GetMessageReactionsList(TLRequest):
    CONSTRUCTOR_ID = 0x461B3F48
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "InputPeer"),
        TLField("id", "int"),
        TLField("reaction", "Reaction", flag_group=0, flag_bit=0),
        TLField("offset", "string", flag_group=0, flag_bit=1),
        TLField("limit", "int"),
    ]
    peer: Optional[TLObject]
    id: Optional[int]
    reaction: Optional[TLObject]
    offset: Optional[str]
    limit: Optional[int]

class SetChatAvailableReactions(TLRequest):
    CONSTRUCTOR_ID = 0xFEB16771
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("available_reactions", "ChatReactions"),
    ]
    peer: Optional[TLObject]
    available_reactions: Optional[TLObject]

class GetAvailableReactions(TLRequest):
    CONSTRUCTOR_ID = 0x18DEA0AC
    FIELDS = [TLField("hash", "int")]
    hash: Optional[int]

class SetDefaultReaction(TLRequest):
    CONSTRUCTOR_ID = 0x4F47A016
    FIELDS = [TLField("reaction", "Reaction")]
    reaction: Optional[TLObject]

class TranslateText(TLRequest):
    CONSTRUCTOR_ID = 0x63183030
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "InputPeer", flag_group=0, flag_bit=0),
        TLField("id", "int", flag_group=0, flag_bit=0, is_vector=True),
        TLField("text", "TextWithEntities", flag_group=0, flag_bit=1, is_vector=True),
        TLField("to_lang", "string"),
    ]
    peer: Optional[TLObject]
    id: Optional[List[int]]
    text: Optional[List[TLObject]]
    to_lang: Optional[str]

class GetUnreadReactions(TLRequest):
    CONSTRUCTOR_ID = 0x3223495B
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "InputPeer"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=0),
        TLField("offset_id", "int"),
        TLField("add_offset", "int"),
        TLField("limit", "int"),
        TLField("max_id", "int"),
        TLField("min_id", "int"),
    ]
    peer: Optional[TLObject]
    top_msg_id: Optional[int]
    offset_id: Optional[int]
    add_offset: Optional[int]
    limit: Optional[int]
    max_id: Optional[int]
    min_id: Optional[int]

class ReadReactions(TLRequest):
    CONSTRUCTOR_ID = 0x54AA7F8E
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "InputPeer"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=0),
    ]
    peer: Optional[TLObject]
    top_msg_id: Optional[int]

class TogglePeerTranslations(TLRequest):
    CONSTRUCTOR_ID = 0xE47CB579
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("disabled", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputPeer"),
    ]
    disabled: Optional[bool]
    peer: Optional[TLObject]

class GetWebPage(TLRequest):
    CONSTRUCTOR_ID = 0x8D9692A3
    FIELDS = [
        TLField("url", "string"),
        TLField("hash", "int"),
    ]
    url: Optional[str]
    hash: Optional[int]

class GetDocumentByHash(TLRequest):
    CONSTRUCTOR_ID = 0xB1F2061F
    FIELDS = [
        TLField("sha256", "bytes"),
        TLField("size", "long"),
        TLField("mime_type", "string"),
    ]
    sha256: Optional[bytes]
    size: Optional[int]
    mime_type: Optional[str]

class GetBotCallbackAnswer(TLRequest):
    CONSTRUCTOR_ID = 0x9342CA07
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("game", "true", flag_group=0, flag_bit=1),
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
        TLField("data", "bytes", flag_group=0, flag_bit=0),
        TLField("password", "InputCheckPasswordSRP", flag_group=0, flag_bit=2),
    ]
    game: Optional[bool]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    data: Optional[bytes]
    password: Optional[TLObject]

class GetInlineBotResults(TLRequest):
    CONSTRUCTOR_ID = 0x514E999D
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("bot", "InputUser"),
        TLField("peer", "InputPeer"),
        TLField("geo_point", "InputGeoPoint", flag_group=0, flag_bit=0),
        TLField("query", "string"),
        TLField("offset", "string"),
    ]
    bot: Optional[TLObject]
    peer: Optional[TLObject]
    geo_point: Optional[TLObject]
    query: Optional[str]
    offset: Optional[str]

class SendInlineBotResult(TLRequest):
    CONSTRUCTOR_ID = 0xF7BC68BA
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("silent", "true", flag_group=0, flag_bit=5),
        TLField("background", "true", flag_group=0, flag_bit=6),
        TLField("clear_draft", "true", flag_group=0, flag_bit=7),
        TLField("hide_via", "true", flag_group=0, flag_bit=11),
        TLField("peer", "InputPeer"),
        TLField("reply_to", "InputReplyTo", flag_group=0, flag_bit=0),
        TLField("random_id", "long"),
        TLField("query_id", "long"),
        TLField("id", "string"),
        TLField("schedule_date", "int", flag_group=0, flag_bit=10),
        TLField("send_as", "InputPeer", flag_group=0, flag_bit=13),
    ]
    silent: Optional[bool]
    background: Optional[bool]
    clear_draft: Optional[bool]
    hide_via: Optional[bool]
    peer: Optional[TLObject]
    reply_to: Optional[TLObject]
    random_id: Optional[int]
    query_id: Optional[int]
    id: Optional[str]
    schedule_date: Optional[int]
    send_as: Optional[TLObject]

class RequestUrlAuth(TLRequest):
    CONSTRUCTOR_ID = 0x198FB446
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "InputPeer", flag_group=0, flag_bit=1),
        TLField("msg_id", "int", flag_group=0, flag_bit=1),
        TLField("button_id", "int", flag_group=0, flag_bit=1),
        TLField("url", "string", flag_group=0, flag_bit=2),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    button_id: Optional[int]
    url: Optional[str]

class AcceptUrlAuth(TLRequest):
    CONSTRUCTOR_ID = 0xB12C7125
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("write_allowed", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputPeer", flag_group=0, flag_bit=1),
        TLField("msg_id", "int", flag_group=0, flag_bit=1),
        TLField("button_id", "int", flag_group=0, flag_bit=1),
        TLField("url", "string", flag_group=0, flag_bit=2),
    ]
    write_allowed: Optional[bool]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    button_id: Optional[int]
    url: Optional[str]

class HidePeerSettingsBar(TLRequest):
    CONSTRUCTOR_ID = 0x4FACB138
    FIELDS = [TLField("peer", "InputPeer")]
    peer: Optional[TLObject]

class GetPollVotes(TLRequest):
    CONSTRUCTOR_ID = 0xB86E380E
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "InputPeer"),
        TLField("id", "int"),
        TLField("option", "bytes", flag_group=0, flag_bit=0),
        TLField("offset", "string", flag_group=0, flag_bit=1),
        TLField("limit", "int"),
    ]
    peer: Optional[TLObject]
    id: Optional[int]
    option: Optional[bytes]
    offset: Optional[str]
    limit: Optional[int]

class GetCustomEmojiDocuments(TLRequest):
    CONSTRUCTOR_ID = 0xD9AB0F54
    FIELDS = [TLField("document_id", "long", is_vector=True)]
    document_id: Optional[List[int]]

class GetTopReactions(TLRequest):
    CONSTRUCTOR_ID = 0xBB8125BA
    FIELDS = [
        TLField("limit", "int"),
        TLField("hash", "long"),
    ]
    limit: Optional[int]
    hash: Optional[int]

class GetRecentReactions(TLRequest):
    CONSTRUCTOR_ID = 0x39461DB2
    FIELDS = [
        TLField("limit", "int"),
        TLField("hash", "long"),
    ]
    limit: Optional[int]
    hash: Optional[int]

class ClearRecentReactions(TLRequest):
    CONSTRUCTOR_ID = 0x9DFEEFB4
    FIELDS = []

class GetExtendedMedia(TLRequest):
    CONSTRUCTOR_ID = 0x84F80814
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int", is_vector=True),
    ]
    peer: Optional[TLObject]
    id: Optional[List[int]]

class GetSavedGifs(TLRequest):
    CONSTRUCTOR_ID = 0x5CF09635
    FIELDS = [TLField("hash", "long")]
    hash: Optional[int]

class SaveGif(TLRequest):
    CONSTRUCTOR_ID = 0x327A30CB
    FIELDS = [
        TLField("id", "InputDocument"),
        TLField("unsave", "Bool"),
    ]
    id: Optional[TLObject]
    unsave: Optional[bool]

class GetFavedStickers(TLRequest):
    CONSTRUCTOR_ID = 0x04F1AAA9
    FIELDS = [TLField("hash", "long")]
    hash: Optional[int]

class FaveSticker(TLRequest):
    CONSTRUCTOR_ID = 0xB9FFC55B
    FIELDS = [
        TLField("id", "InputDocument"),
        TLField("unfave", "Bool"),
    ]
    id: Optional[TLObject]
    unfave: Optional[bool]

class GetAllStickers(TLRequest):
    CONSTRUCTOR_ID = 0xB8A0A1A8
    FIELDS = [TLField("hash", "long")]
    hash: Optional[int]

class GetStickers(TLRequest):
    CONSTRUCTOR_ID = 0xD5A5D3A1
    FIELDS = [
        TLField("emoticon", "string"),
        TLField("hash", "long"),
    ]
    emoticon: Optional[str]
    hash: Optional[int]

class InstallStickerSet(TLRequest):
    CONSTRUCTOR_ID = 0xC78FE460
    FIELDS = [
        TLField("stickerset", "InputStickerSet"),
        TLField("archived", "Bool"),
    ]
    stickerset: Optional[TLObject]
    archived: Optional[bool]

class UninstallStickerSet(TLRequest):
    CONSTRUCTOR_ID = 0xF96E55DE
    FIELDS = [TLField("stickerset", "InputStickerSet")]
    stickerset: Optional[TLObject]

class GetFeaturedStickers(TLRequest):
    CONSTRUCTOR_ID = 0x64780B14
    FIELDS = [TLField("hash", "long")]
    hash: Optional[int]

class ReadFeaturedStickers(TLRequest):
    CONSTRUCTOR_ID = 0x5B118126
    FIELDS = [TLField("id", "long", is_vector=True)]
    id: Optional[List[int]]

class GetRecentStickers(TLRequest):
    CONSTRUCTOR_ID = 0x9DA9403B
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("attached", "true", flag_group=0, flag_bit=0),
        TLField("hash", "long"),
    ]
    attached: Optional[bool]
    hash: Optional[int]

class SaveRecentSticker(TLRequest):
    CONSTRUCTOR_ID = 0x392718F8
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("attached", "true", flag_group=0, flag_bit=0),
        TLField("id", "InputDocument"),
        TLField("unsave", "Bool"),
    ]
    attached: Optional[bool]
    id: Optional[TLObject]
    unsave: Optional[bool]

class ClearRecentStickers(TLRequest):
    CONSTRUCTOR_ID = 0x8999602D
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("attached", "true", flag_group=0, flag_bit=0),
    ]
    attached: Optional[bool]

class GetArchivedStickers(TLRequest):
    CONSTRUCTOR_ID = 0x57F17692
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("masks", "true", flag_group=0, flag_bit=0),
        TLField("emojis", "true", flag_group=0, flag_bit=1),
        TLField("offset_id", "long"),
        TLField("limit", "int"),
    ]
    masks: Optional[bool]
    emojis: Optional[bool]
    offset_id: Optional[int]
    limit: Optional[int]

class SearchStickerSets(TLRequest):
    CONSTRUCTOR_ID = 0x35705B8A
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("exclude_featured", "true", flag_group=0, flag_bit=0),
        TLField("q", "string"),
        TLField("hash", "long"),
    ]
    exclude_featured: Optional[bool]
    q: Optional[str]
    hash: Optional[int]

class GetEmojiStickers(TLRequest):
    CONSTRUCTOR_ID = 0xFBFCA18F
    FIELDS = [TLField("hash", "long")]
    hash: Optional[int]

class GetFeaturedEmojiStickers(TLRequest):
    CONSTRUCTOR_ID = 0x0ECF6736
    FIELDS = [TLField("hash", "long")]
    hash: Optional[int]

class GetCommonChats(TLRequest):
    CONSTRUCTOR_ID = 0xE40CA104
    FIELDS = [
        TLField("user_id", "InputUser"),
        TLField("max_id", "long"),
        TLField("limit", "int"),
    ]
    user_id: Optional[TLObject]
    max_id: Optional[int]
    limit: Optional[int]

class GetEmojiKeywordsDifference(TLRequest):
    CONSTRUCTOR_ID = 0x1508B6AF
    FIELDS = [
        TLField("lang_code", "string"),
        TLField("from_version", "int"),
    ]
    lang_code: Optional[str]
    from_version: Optional[int]

class GetAttachMenuBots(TLRequest):
    CONSTRUCTOR_ID = 0x16FCC2CB
    FIELDS = [TLField("hash", "long")]
    hash: Optional[int]

class GetAttachMenuBot(TLRequest):
    CONSTRUCTOR_ID = 0x77216192
    FIELDS = [TLField("bot", "InputUser")]
    bot: Optional[TLObject]

class ToggleBotInAttachMenu(TLRequest):
    CONSTRUCTOR_ID = 0x69F59D69
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("write_allowed", "true", flag_group=0, flag_bit=0),
        TLField("bot", "InputUser"),
        TLField("enabled", "Bool"),
    ]
    write_allowed: Optional[bool]
    bot: Optional[TLObject]
    enabled: Optional[bool]

class RequestWebView(TLRequest):
    CONSTRUCTOR_ID = 0x269DC2C1
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("from_bot_menu", "true", flag_group=0, flag_bit=4),
        TLField("silent", "true", flag_group=0, flag_bit=5),
        TLField("peer", "InputPeer"),
        TLField("bot", "InputUser"),
        TLField("url", "string", flag_group=0, flag_bit=1),
        TLField("start_param", "string", flag_group=0, flag_bit=3),
        TLField("theme_params", "DataJSON", flag_group=0, flag_bit=2),
        TLField("platform", "string"),
        TLField("reply_to", "InputReplyTo", flag_group=0, flag_bit=0),
        TLField("send_as", "InputPeer", flag_group=0, flag_bit=13),
    ]
    from_bot_menu: Optional[bool]
    silent: Optional[bool]
    peer: Optional[TLObject]
    bot: Optional[TLObject]
    url: Optional[str]
    start_param: Optional[str]
    theme_params: Optional[TLObject]
    platform: Optional[str]
    reply_to: Optional[TLObject]
    send_as: Optional[TLObject]

class TranscribeAudio(TLRequest):
    CONSTRUCTOR_ID = 0x269E9A49
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("msg_id", "int"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]

class GetBotApp(TLRequest):
    CONSTRUCTOR_ID = 0x34FDC5C3
    FIELDS = [
        TLField("app", "InputBotApp"),
        TLField("hash", "long"),
    ]
    app: Optional[TLObject]
    hash: Optional[int]

class RequestAppWebView(TLRequest):
    CONSTRUCTOR_ID = 0x8C5A3B3C
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("write_allowed", "true", flag_group=0, flag_bit=0),
        TLField("peer", "InputPeer"),
        TLField("app", "InputBotApp"),
        TLField("start_param", "string", flag_group=0, flag_bit=1),
        TLField("theme_params", "DataJSON", flag_group=0, flag_bit=2),
        TLField("platform", "string"),
    ]
    write_allowed: Optional[bool]
    peer: Optional[TLObject]
    app: Optional[TLObject]
    start_param: Optional[str]
    theme_params: Optional[TLObject]
    platform: Optional[str]
class GetMessagesViews(TLObject):
    CONSTRUCTOR_ID = 0x5784D3E1
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("id", "int", is_vector=True),
        TLField("increment", "Bool"),
    ]
    peer: Optional[TLObject]
    id: Optional[List[int]]
    increment: Optional[bool]

class ImportChatInvite(TLObject):
    CONSTRUCTOR_ID = 0x6C50051C
    FIELDS = [
        TLField("hash", "string"),
    ]
    hash: Optional[str]