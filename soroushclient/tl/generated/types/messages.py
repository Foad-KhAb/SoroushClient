from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class Dialog(TLObject):
    CONSTRUCTOR_ID = 0xD58A08C6
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("pinned", "true", flag_group=0, flag_bit=2),
        TLField("unread_mark", "true", flag_group=0, flag_bit=3),
        TLField("view_forum_as_messages", "true", flag_group=0, flag_bit=6),
        TLField("peer", "Peer"),
        TLField("top_message", "int"),
        TLField("read_inbox_max_id", "int"),
        TLField("read_outbox_max_id", "int"),
        TLField("unread_count", "int"),
        TLField("unread_mentions_count", "int"),
        TLField("unread_reactions_count", "int"),
        TLField("notify_settings", "PeerNotifySettings"),
        TLField("pts", "int", flag_group=0, flag_bit=0),
        TLField("draft", "DraftMessage", flag_group=0, flag_bit=1),
        TLField("folder_id", "int", flag_group=0, flag_bit=4),
        TLField("ttl_period", "int", flag_group=0, flag_bit=5),
    ]
    pinned: Optional[bool]
    unread_mark: Optional[bool]
    view_forum_as_messages: Optional[bool]
    peer: Optional[TLObject]
    top_message: Optional[int]
    read_inbox_max_id: Optional[int]
    read_outbox_max_id: Optional[int]
    unread_count: Optional[int]
    unread_mentions_count: Optional[int]
    unread_reactions_count: Optional[int]
    notify_settings: Optional[TLObject]
    pts: Optional[int]
    draft: Optional[TLObject]
    folder_id: Optional[int]
    ttl_period: Optional[int]

class DialogFolder(TLObject):
    CONSTRUCTOR_ID = 0x71BD134C
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("pinned", "true", flag_group=0, flag_bit=2),
        TLField("folder", "Folder"),
        TLField("peer", "Peer"),
        TLField("top_message", "int"),
        TLField("unread_muted_peers_count", "int"),
        TLField("unread_unmuted_peers_count", "int"),
        TLField("unread_muted_messages_count", "int"),
        TLField("unread_unmuted_messages_count", "int"),
    ]
    pinned: Optional[bool]
    folder: Optional[TLObject]
    peer: Optional[TLObject]
    top_message: Optional[int]
    unread_muted_peers_count: Optional[int]
    unread_unmuted_peers_count: Optional[int]
    unread_muted_messages_count: Optional[int]
    unread_unmuted_messages_count: Optional[int]

class MessageEmpty(TLObject):
    CONSTRUCTOR_ID = 0x90A6CA84
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("id", "int"),
        TLField("peer_id", "Peer", flag_group=0, flag_bit=0),
    ]
    id: Optional[int]
    peer_id: Optional[TLObject]

class Message(TLObject):
    CONSTRUCTOR_ID = 0x38116EE0
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("out", "true", flag_group=0, flag_bit=1),
        TLField("mentioned", "true", flag_group=0, flag_bit=4),
        TLField("media_unread", "true", flag_group=0, flag_bit=5),
        TLField("silent", "true", flag_group=0, flag_bit=13),
        TLField("post", "true", flag_group=0, flag_bit=14),
        TLField("from_scheduled", "true", flag_group=0, flag_bit=18),
        TLField("legacy", "true", flag_group=0, flag_bit=19),
        TLField("edit_hide", "true", flag_group=0, flag_bit=21),
        TLField("pinned", "true", flag_group=0, flag_bit=24),
        TLField("noforwards", "true", flag_group=0, flag_bit=26),
        TLField("invert_media", "true", flag_group=0, flag_bit=27),
        TLField("id", "int"),
        TLField("from_id", "Peer", flag_group=0, flag_bit=8),
        TLField("peer_id", "Peer"),
        TLField("fwd_from", "MessageFwdHeader", flag_group=0, flag_bit=2),
        TLField("via_bot_id", "long", flag_group=0, flag_bit=11),
        TLField("reply_to", "MessageReplyHeader", flag_group=0, flag_bit=3),
        TLField("date", "int"),
        TLField("message", "string"),
        TLField("media", "MessageMedia", flag_group=0, flag_bit=9),
        TLField("reply_markup", "ReplyMarkup", flag_group=0, flag_bit=6),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=7, is_vector=True),
        TLField("views", "int", flag_group=0, flag_bit=10),
        TLField("forwards", "int", flag_group=0, flag_bit=10),
        TLField("replies", "MessageReplies", flag_group=0, flag_bit=23),
        TLField("edit_date", "int", flag_group=0, flag_bit=15),
        TLField("post_author", "string", flag_group=0, flag_bit=16),
        TLField("grouped_id", "long", flag_group=0, flag_bit=17),
        TLField("reactions", "MessageReactions", flag_group=0, flag_bit=20),
        TLField("restriction_reason", "RestrictionReason", flag_group=0, flag_bit=22, is_vector=True),
        TLField("ttl_period", "int", flag_group=0, flag_bit=25),
    ]
    out: Optional[bool]
    mentioned: Optional[bool]
    media_unread: Optional[bool]
    silent: Optional[bool]
    post: Optional[bool]
    from_scheduled: Optional[bool]
    legacy: Optional[bool]
    edit_hide: Optional[bool]
    pinned: Optional[bool]
    noforwards: Optional[bool]
    invert_media: Optional[bool]
    id: Optional[int]
    from_id: Optional[TLObject]
    peer_id: Optional[TLObject]
    fwd_from: Optional[TLObject]
    via_bot_id: Optional[int]
    reply_to: Optional[TLObject]
    date: Optional[int]
    message: Optional[str]
    media: Optional[TLObject]
    reply_markup: Optional[TLObject]
    entities: Optional[List[TLObject]]
    views: Optional[int]
    forwards: Optional[int]
    replies: Optional[TLObject]
    edit_date: Optional[int]
    post_author: Optional[str]
    grouped_id: Optional[int]
    reactions: Optional[TLObject]
    restriction_reason: Optional[List[TLObject]]
    ttl_period: Optional[int]

class MessageService(TLObject):
    CONSTRUCTOR_ID = 0x2B085862
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("out", "true", flag_group=0, flag_bit=1),
        TLField("mentioned", "true", flag_group=0, flag_bit=4),
        TLField("media_unread", "true", flag_group=0, flag_bit=5),
        TLField("silent", "true", flag_group=0, flag_bit=13),
        TLField("post", "true", flag_group=0, flag_bit=14),
        TLField("legacy", "true", flag_group=0, flag_bit=19),
        TLField("id", "int"),
        TLField("from_id", "Peer", flag_group=0, flag_bit=8),
        TLField("peer_id", "Peer"),
        TLField("reply_to", "MessageReplyHeader", flag_group=0, flag_bit=3),
        TLField("date", "int"),
        TLField("action", "MessageAction"),
        TLField("ttl_period", "int", flag_group=0, flag_bit=25),
    ]
    out: Optional[bool]
    mentioned: Optional[bool]
    media_unread: Optional[bool]
    silent: Optional[bool]
    post: Optional[bool]
    legacy: Optional[bool]
    id: Optional[int]
    from_id: Optional[TLObject]
    peer_id: Optional[TLObject]
    reply_to: Optional[TLObject]
    date: Optional[int]
    action: Optional[TLObject]
    ttl_period: Optional[int]

class MessageFwdHeader(TLObject):
    CONSTRUCTOR_ID = 0x5F777DCE
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("imported", "true", flag_group=0, flag_bit=7),
        TLField("from_id", "Peer", flag_group=0, flag_bit=0),
        TLField("from_name", "string", flag_group=0, flag_bit=5),
        TLField("date", "int"),
        TLField("channel_post", "int", flag_group=0, flag_bit=2),
        TLField("post_author", "string", flag_group=0, flag_bit=3),
        TLField("saved_from_peer", "Peer", flag_group=0, flag_bit=4),
        TLField("saved_from_msg_id", "int", flag_group=0, flag_bit=4),
        TLField("psa_type", "string", flag_group=0, flag_bit=6),
    ]
    imported: Optional[bool]
    from_id: Optional[TLObject]
    from_name: Optional[str]
    date: Optional[int]
    channel_post: Optional[int]
    post_author: Optional[str]
    saved_from_peer: Optional[TLObject]
    saved_from_msg_id: Optional[int]
    psa_type: Optional[str]

class MessageReplyHeader(TLObject):
    CONSTRUCTOR_ID = 0xAFBC09DB
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("reply_to_scheduled", "true", flag_group=0, flag_bit=2),
        TLField("forum_topic", "true", flag_group=0, flag_bit=3),
        TLField("quote", "true", flag_group=0, flag_bit=9),
        TLField("reply_to_msg_id", "int", flag_group=0, flag_bit=4),
        TLField("reply_to_peer_id", "Peer", flag_group=0, flag_bit=0),
        TLField("reply_from", "MessageFwdHeader", flag_group=0, flag_bit=5),
        TLField("reply_media", "MessageMedia", flag_group=0, flag_bit=8),
        TLField("reply_to_top_id", "int", flag_group=0, flag_bit=1),
        TLField("quote_text", "string", flag_group=0, flag_bit=6),
        TLField("quote_entities", "MessageEntity", flag_group=0, flag_bit=7, is_vector=True),
        TLField("quote_offset", "int", flag_group=0, flag_bit=10),
    ]
    reply_to_scheduled: Optional[bool]
    forum_topic: Optional[bool]
    quote: Optional[bool]
    reply_to_msg_id: Optional[int]
    reply_to_peer_id: Optional[TLObject]
    reply_from: Optional[TLObject]
    reply_media: Optional[TLObject]
    reply_to_top_id: Optional[int]
    quote_text: Optional[str]
    quote_entities: Optional[List[TLObject]]
    quote_offset: Optional[int]

class MessageReplyStoryHeader(TLObject):
    CONSTRUCTOR_ID = 0x9C98BFC1
    FIELDS = [
        TLField("user_id", "long"),
        TLField("story_id", "int"),
    ]
    user_id: Optional[int]
    story_id: Optional[int]

class MessageReplies(TLObject):
    CONSTRUCTOR_ID = 0x83D60FC2
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("comments", "true", flag_group=0, flag_bit=0),
        TLField("replies", "int"),
        TLField("replies_pts", "int"),
        TLField("recent_repliers", "Peer", flag_group=0, flag_bit=1, is_vector=True),
        TLField("channel_id", "long", flag_group=0, flag_bit=0),
        TLField("max_id", "int", flag_group=0, flag_bit=2),
        TLField("read_max_id", "int", flag_group=0, flag_bit=3),
    ]
    comments: Optional[bool]
    replies: Optional[int]
    replies_pts: Optional[int]
    recent_repliers: Optional[List[TLObject]]
    channel_id: Optional[int]
    max_id: Optional[int]
    read_max_id: Optional[int]

class MessageViews(TLObject):
    CONSTRUCTOR_ID = 0x455B853D
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("views", "int", flag_group=0, flag_bit=0),
        TLField("forwards", "int", flag_group=0, flag_bit=1),
        TLField("replies", "MessageReplies", flag_group=0, flag_bit=2),
    ]
    views: Optional[int]
    forwards: Optional[int]
    replies: Optional[TLObject]

class MessageReactions(TLObject):
    CONSTRUCTOR_ID = 0x4F2B9479
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("min", "true", flag_group=0, flag_bit=0),
        TLField("can_see_list", "true", flag_group=0, flag_bit=2),
        TLField("results", "ReactionCount", is_vector=True),
        TLField("recent_reactions", "MessagePeerReaction", flag_group=0, flag_bit=1, is_vector=True),
    ]
    min: Optional[bool]
    can_see_list: Optional[bool]
    results: Optional[List[TLObject]]
    recent_reactions: Optional[List[TLObject]]

class MessagePeerReaction(TLObject):
    CONSTRUCTOR_ID = 0x8C79B63C
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("big", "true", flag_group=0, flag_bit=0),
        TLField("unread", "true", flag_group=0, flag_bit=1),
        TLField("my", "true", flag_group=0, flag_bit=2),
        TLField("peer_id", "Peer"),
        TLField("date", "int"),
        TLField("reaction", "Reaction"),
    ]
    big: Optional[bool]
    unread: Optional[bool]
    my: Optional[bool]
    peer_id: Optional[TLObject]
    date: Optional[int]
    reaction: Optional[TLObject]

class MessagePeerVote(TLObject):
    CONSTRUCTOR_ID = 0xB6CC2D5C
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("option", "bytes"),
        TLField("date", "int"),
    ]
    peer: Optional[TLObject]
    option: Optional[bytes]
    date: Optional[int]

class MessagePeerVoteInputOption(TLObject):
    CONSTRUCTOR_ID = 0x74CDA504
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("date", "int"),
    ]
    peer: Optional[TLObject]
    date: Optional[int]

class MessagePeerVoteMultiple(TLObject):
    CONSTRUCTOR_ID = 0x4628F6E6
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("options", "bytes", is_vector=True),
        TLField("date", "int"),
    ]
    peer: Optional[TLObject]
    options: Optional[List[bytes]]
    date: Optional[int]

class MessageExtendedMediaPreview(TLObject):
    CONSTRUCTOR_ID = 0xAD628CC8
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("w", "int", flag_group=0, flag_bit=0),
        TLField("h", "int", flag_group=0, flag_bit=0),
        TLField("thumb", "PhotoSize", flag_group=0, flag_bit=1),
        TLField("video_duration", "int", flag_group=0, flag_bit=2),
    ]
    w: Optional[int]
    h: Optional[int]
    thumb: Optional[TLObject]
    video_duration: Optional[int]

class MessageExtendedMedia(TLObject):
    CONSTRUCTOR_ID = 0xEE479C64
    FIELDS = [TLField("media", "MessageMedia")]
    media: Optional[TLObject]

class DraftMessageEmpty(TLObject):
    CONSTRUCTOR_ID = 0x1B0C841A
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("date", "int", flag_group=0, flag_bit=0),
    ]
    date: Optional[int]

class DraftMessage(TLObject):
    CONSTRUCTOR_ID = 0x3FCCF7EF
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("no_webpage", "true", flag_group=0, flag_bit=1),
        TLField("invert_media", "true", flag_group=0, flag_bit=6),
        TLField("reply_to", "InputReplyTo", flag_group=0, flag_bit=4),
        TLField("message", "string"),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=3, is_vector=True),
        TLField("media", "InputMedia", flag_group=0, flag_bit=5),
        TLField("date", "int"),
    ]
    no_webpage: Optional[bool]
    invert_media: Optional[bool]
    reply_to: Optional[TLObject]
    message: Optional[str]
    entities: Optional[List[TLObject]]
    media: Optional[TLObject]
    date: Optional[int]

class InputReplyToMessage(TLObject):
    CONSTRUCTOR_ID = 0x22C0F6D5
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("reply_to_msg_id", "int"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=0),
        TLField("reply_to_peer_id", "InputPeer", flag_group=0, flag_bit=1),
        TLField("quote_text", "string", flag_group=0, flag_bit=2),
        TLField("quote_entities", "MessageEntity", flag_group=0, flag_bit=3, is_vector=True),
        TLField("quote_offset", "int", flag_group=0, flag_bit=4),
    ]
    reply_to_msg_id: Optional[int]
    top_msg_id: Optional[int]
    reply_to_peer_id: Optional[TLObject]
    quote_text: Optional[str]
    quote_entities: Optional[List[TLObject]]
    quote_offset: Optional[int]

class InputReplyToStory(TLObject):
    CONSTRUCTOR_ID = 0x15B0F283
    FIELDS = [
        TLField("user_id", "InputUser"),
        TLField("story_id", "int"),
    ]
    user_id: Optional[TLObject]
    story_id: Optional[int]

class InputMessageID(TLObject):
    CONSTRUCTOR_ID = 0xA676A322
    FIELDS = [TLField("id", "int")]
    id: Optional[int]

class InputMessageReplyTo(TLObject):
    CONSTRUCTOR_ID = 0xBAD88395
    FIELDS = [TLField("id", "int")]
    id: Optional[int]

class InputMessagePinned(TLObject):
    CONSTRUCTOR_ID = 0x86872538
    FIELDS = []

class InputMessageCallbackQuery(TLObject):
    CONSTRUCTOR_ID = 0xACFA1A7E
    FIELDS = [
        TLField("id", "int"),
        TLField("query_id", "long"),
    ]
    id: Optional[int]
    query_id: Optional[int]

class InputSingleMedia(TLObject):
    CONSTRUCTOR_ID = 0x1CC6E91F
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("media", "InputMedia"),
        TLField("random_id", "long"),
        TLField("message", "string"),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=0, is_vector=True),
    ]
    media: Optional[TLObject]
    random_id: Optional[int]
    message: Optional[str]
    entities: Optional[List[TLObject]]

class ReceivedNotifyMessage(TLObject):
    CONSTRUCTOR_ID = 0xA384B779
    FIELDS = [
        TLField("id", "int"),
        TLField("flags", "int"),
    ]
    id: Optional[int]
    flags: Optional[int]

class MessageRange(TLObject):
    CONSTRUCTOR_ID = 0x0AE30253
    FIELDS = [
        TLField("min_id", "int"),
        TLField("max_id", "int"),
    ]
    min_id: Optional[int]
    max_id: Optional[int]


class MessageMediaEmpty(TLObject):
    CONSTRUCTOR_ID = 1038967584  # 0x3DED6320 in standard, different here

class MessageMediaPhoto(TLObject):
    CONSTRUCTOR_ID = 1766936791  # 0x6950E6D7 — Soroush specific
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("spoiler", "true", flag_group=0, flag_bit=3),
        TLField("photo", "Photo", flag_group=0, flag_bit=0),
        TLField("ttl_seconds", "int", flag_group=0, flag_bit=2),
    ]
    spoiler: Optional[bool]
    photo: Optional[TLObject]
    ttl_seconds: Optional[int]

class MessageMediaDocument(TLObject):
    CONSTRUCTOR_ID = 1291114285  # 0x4CF4D72D in standard, different here
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("nopremium", "true", flag_group=0, flag_bit=3),
        TLField("spoiler", "true", flag_group=0, flag_bit=4),
        TLField("document", "Document", flag_group=0, flag_bit=0),
        TLField("alt_document", "Document", flag_group=0, flag_bit=5),
        TLField("ttl_seconds", "int", flag_group=0, flag_bit=2),
    ]
    nopremium: Optional[bool]
    spoiler: Optional[bool]
    document: Optional[TLObject]
    alt_document: Optional[TLObject]
    ttl_seconds: Optional[int]

class MessageMediaWebPage(TLObject):
    CONSTRUCTOR_ID = 3723562043  # different from standard
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("force_large_media", "true", flag_group=0, flag_bit=0),
        TLField("force_small_media", "true", flag_group=0, flag_bit=1),
        TLField("manual", "true", flag_group=0, flag_bit=3),
        TLField("safe", "true", flag_group=0, flag_bit=4),
        TLField("webpage", "WebPage"),
    ]
    force_large_media: Optional[bool]
    force_small_media: Optional[bool]
    manual: Optional[bool]
    safe: Optional[bool]
    webpage: Optional[TLObject]

class MessageMediaGeo(TLObject):
    CONSTRUCTOR_ID = 1457575028
    FIELDS = [TLField("geo", "GeoPoint")]
    geo: Optional[TLObject]

class MessageMediaContact(TLObject):
    CONSTRUCTOR_ID = 1882335561
    FIELDS = [
        TLField("phone_number", "string"),
        TLField("first_name", "string"),
        TLField("last_name", "string"),
        TLField("vcard", "string"),
        TLField("user_id", "long"),
    ]
    phone_number: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    vcard: Optional[str]
    user_id: Optional[int]

class MessageMediaUnsupported(TLObject):
    CONSTRUCTOR_ID = 2676290718
    FIELDS = []

class MessageEntityUnknown(TLObject):
    CONSTRUCTOR_ID = 3146955413
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityMention(TLObject):
    CONSTRUCTOR_ID = 4194588573
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityHashtag(TLObject):
    CONSTRUCTOR_ID = 1868782349
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityBotCommand(TLObject):
    CONSTRUCTOR_ID = 1827637959
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityUrl(TLObject):
    CONSTRUCTOR_ID = 1859134776
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityEmail(TLObject):
    CONSTRUCTOR_ID = 1692693954
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityBold(TLObject):
    CONSTRUCTOR_ID = 3177253833
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityItalic(TLObject):
    CONSTRUCTOR_ID = 2188348256
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityCode(TLObject):
    CONSTRUCTOR_ID = 681706865
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityPre(TLObject):
    CONSTRUCTOR_ID = 1938967520
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
        TLField("language", "string"),
    ]
    offset: Optional[int]
    length: Optional[int]
    language: Optional[str]


class MessageEntityTextUrl(TLObject):
    CONSTRUCTOR_ID = 1990644519
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
        TLField("url", "string"),
    ]
    offset: Optional[int]
    length: Optional[int]
    url: Optional[str]


class MessageEntityMentionName(TLObject):
    CONSTRUCTOR_ID = 3699052864
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
        TLField("user_id", "long"),
    ]
    offset: Optional[int]
    length: Optional[int]
    user_id: Optional[int]


class InputMessageEntityMentionName(TLObject):
    CONSTRUCTOR_ID = 546203849
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
        TLField("user_id", "InputUser"),
    ]
    offset: Optional[int]
    length: Optional[int]
    user_id: Optional[TLObject]


class MessageEntityPhone(TLObject):
    CONSTRUCTOR_ID = 2607407947
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityCashtag(TLObject):
    CONSTRUCTOR_ID = 1280209983
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityUnderline(TLObject):
    CONSTRUCTOR_ID = 2622389899
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityStrike(TLObject):
    CONSTRUCTOR_ID = 3204879316
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityBankCard(TLObject):
    CONSTRUCTOR_ID = 1981704948
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntitySpoiler(TLObject):
    CONSTRUCTOR_ID = 852137487
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityCustomEmoji(TLObject):
    CONSTRUCTOR_ID = 3369010680
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
        TLField("document_id", "long"),
    ]
    offset: Optional[int]
    length: Optional[int]
    document_id: Optional[int]


class MessageEntityBlockquote(TLObject):
    CONSTRUCTOR_ID = 34469328
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
    ]
    offset: Optional[int]
    length: Optional[int]