from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from soroushclient.tl.base import TLField, TLObject
from soroushclient.tl.generated import BaseMessage

if TYPE_CHECKING:
    from soroushclient.tl.generated import Chat, Peer, PeerNotifySettings, User


class DraftMessageEmpty(TLObject):
    CONSTRUCTOR_ID = 0x1B0C841A
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("date", "int", flag_group=0, flag_bit=0),
    ]

    date: Optional[int]


class DraftMessage(TLObject):
    CONSTRUCTOR_ID = 0xFD8E711F
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("no_webpage", "true", flag_group=0, flag_bit=1),
        TLField("reply_to", "MessageReplyHeader", flag_group=0, flag_bit=4),
        TLField("message", "string"),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=3, is_vector=True),
        TLField("media", "InputMedia", flag_group=0, flag_bit=6),
        TLField("date", "int"),
    ]

    no_webpage: Optional[bool]
    reply_to: Optional[TLObject]
    message: Optional[str]
    entities: Optional[List[TLObject]]
    media: Optional[TLObject]
    date: Optional[int]


class MessageMediaEmpty(TLObject):
    CONSTRUCTOR_ID = 0x3DED6320
    FIELDS = []


class MessageMediaPhoto(TLObject):
    CONSTRUCTOR_ID = 0x695150D7
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
    CONSTRUCTOR_ID = 0x4CF4D72D
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
    CONSTRUCTOR_ID = 0xDDF10C3B
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


class MessageMediaContact(TLObject):
    CONSTRUCTOR_ID = 0x70322949
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
    CONSTRUCTOR_ID = 0x9F84F49E
    FIELDS = []


class MessageMediaGeo(TLObject):
    CONSTRUCTOR_ID = 0x56E0D474
    FIELDS = [TLField("geo", "GeoPoint")]

    geo: Optional[TLObject]


class MessageFwdHeader(TLObject):
    CONSTRUCTOR_ID = 0x4E4DF4BB
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
        TLField("psa_type", "string", flag_group=0, flag_bit=11),
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
        TLField(
            "quote_entities", "MessageEntity", flag_group=0, flag_bit=7, is_vector=True
        ),
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


class MessageEntityUnknown(TLObject):
    CONSTRUCTOR_ID = 0xBB92BA95
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityMention(TLObject):
    CONSTRUCTOR_ID = 0xFA04579D
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityHashtag(TLObject):
    CONSTRUCTOR_ID = 0x6F635B0D
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityBotCommand(TLObject):
    CONSTRUCTOR_ID = 0x6CEF8AC7
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityUrl(TLObject):
    CONSTRUCTOR_ID = 0x6ED02538
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityEmail(TLObject):
    CONSTRUCTOR_ID = 0x64E475C2
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityBold(TLObject):
    CONSTRUCTOR_ID = 0xBD610BC9
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityItalic(TLObject):
    CONSTRUCTOR_ID = 0x826F8B60
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityCode(TLObject):
    CONSTRUCTOR_ID = 0x28A20571
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityPre(TLObject):
    CONSTRUCTOR_ID = 0x73924BE0
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
        TLField("language", "string"),
    ]

    offset: Optional[int]
    length: Optional[int]
    language: Optional[str]


class MessageEntityTextUrl(TLObject):
    CONSTRUCTOR_ID = 0x76A6D327
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
        TLField("url", "string"),
    ]

    offset: Optional[int]
    length: Optional[int]
    language: Optional[str]


class MessageEntityMentionName(TLObject):
    CONSTRUCTOR_ID = 0xDC7B1140
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
        TLField("user_id", "long"),
    ]

    offset: Optional[int]
    length: Optional[int]
    language: Optional[str]


class MessageEntityPhone(TLObject):
    CONSTRUCTOR_ID = 0x9B69E34B
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityCashtag(TLObject):
    CONSTRUCTOR_ID = 0x4C4E743F
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityUnderline(TLObject):
    CONSTRUCTOR_ID = 0x9C4E7E8B
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityStrike(TLObject):
    CONSTRUCTOR_ID = 0xBF0693D4
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntitySpoiler(TLObject):
    CONSTRUCTOR_ID = 0x32CA960F
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityBlockquote(TLObject):
    CONSTRUCTOR_ID = 0xF1CCAAAC
    FIELDS = [TLField("offset", "int"), TLField("length", "int")]
    offset: Optional[int]
    length: Optional[int]


class MessageEntityCustomEmoji(TLObject):
    CONSTRUCTOR_ID = 0xC8CF05F8
    FIELDS = [
        TLField("offset", "int"),
        TLField("length", "int"),
        TLField("document_id", "long"),
    ]
    offset: Optional[int]
    length: Optional[int]
    document_id: Optional[int]


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


class ReactionEmpty(TLObject):
    CONSTRUCTOR_ID = 0x79F5D419
    FIELDS = []


class ReactionEmoji(TLObject):
    CONSTRUCTOR_ID = 0x1B2286BE
    FIELDS = [TLField("emoticon", "string")]
    emoticon: Optional[str]


class ReactionCustomEmoji(TLObject):
    CONSTRUCTOR_ID = 0x8935FC73
    FIELDS = [TLField("document_id", "long")]
    document_id: Optional[int]


class ReactionCount(TLObject):
    CONSTRUCTOR_ID = 0xA3D1CB80
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("chosen_order", "int", flag_group=0, flag_bit=0),
        TLField("reaction", "Reaction"),
        TLField("count", "int"),
    ]

    chosen_order: Optional[int]
    reaction: Optional[TLObject]
    count: Optional[int]


class MessageReactions(TLObject):
    CONSTRUCTOR_ID = 0x4F2B9479
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("min", "true", flag_group=0, flag_bit=0),
        TLField("can_see_list", "true", flag_group=0, flag_bit=2),
        TLField("reactions_as_tags", "true", flag_group=0, flag_bit=3),
        TLField("results", "ReactionCount", is_vector=True),
        TLField(
            "recent_reactions",
            "MessagePeerReaction",
            flag_group=0,
            flag_bit=1,
            is_vector=True,
        ),
    ]

    min: Optional[bool]
    can_see_list: Optional[bool]
    reactions_as_tags: Optional[bool]
    results: Optional[List[TLObject]]
    recent_reactions: Optional[List[TLObject]]


class MessageEmpty(TLObject):
    CONSTRUCTOR_ID = 0x90A6CA84
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("id", "int"),
        TLField("peer_id", "Peer", flag_group=0, flag_bit=0),
    ]

    id: Optional[int]
    peer_id: Optional[Peer]


class Message(BaseMessage):
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
        TLField(
            "restriction_reason",
            "RestrictionReason",
            flag_group=0,
            flag_bit=22,
            is_vector=True,
        ),
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


class MessageActionEmpty(TLObject):
    CONSTRUCTOR_ID = 0xB6AEF7B0
    FIELDS = []


class MessageActionChatCreate(TLObject):
    CONSTRUCTOR_ID = 0xBD47CBAD
    FIELDS = [TLField("title", "string"), TLField("users", "long", is_vector=True)]

    title: Optional[str]
    users: Optional[List[int]]


class MessageActionChatEditTitle(TLObject):
    CONSTRUCTOR_ID = 0xB5A1CE5A
    FIELDS = [TLField("title", "string")]

    title: Optional[str]


class MessageActionChatAddUser(TLObject):
    CONSTRUCTOR_ID = 0x15CEFD00
    FIELDS = [TLField("users", "long", is_vector=True)]
    users: Optional[List[int]]


class MessageActionChatDeleteUser(TLObject):
    CONSTRUCTOR_ID = 0xA43F30CC
    FIELDS = [TLField("user_id", "long")]
    users: Optional[List[int]]


class MessageActionChannelCreate(TLObject):
    CONSTRUCTOR_ID = 0x95D2AC92
    FIELDS = [TLField("title", "string")]
    title: Optional[str]


class MessageActionPinMessage(TLObject):
    CONSTRUCTOR_ID = 0x94BD38ED
    FIELDS = []


class MessageActionHistoryClear(TLObject):
    CONSTRUCTOR_ID = 0x9FBAB604
    FIELDS = []


class MessageActionContactSignUp(TLObject):
    CONSTRUCTOR_ID = 0xF3F25F76
    FIELDS = []


class MessageActionChatJoinedByLink(TLObject):
    CONSTRUCTOR_ID = 0x031224C3
    FIELDS = [TLField("inviter_id", "long")]
    inviter_id: Optional[int]


class MessageActionChatMigrateTo(TLObject):
    CONSTRUCTOR_ID = 0xE1037F92
    FIELDS = [TLField("channel_id", "long")]
    channel_id: Optional[int]


class MessageActionChannelMigrateFrom(TLObject):
    CONSTRUCTOR_ID = 0xEA3948E9
    FIELDS = [TLField("title", "string"), TLField("chat_id", "long")]

    title: Optional[str]
    chat_id: Optional[int]


class MessageActionCustomAction(TLObject):
    CONSTRUCTOR_ID = 0xFAE69F56
    FIELDS = [TLField("message", "string")]
    message: Optional[str]


class MessageActionSetMessagesTTL(TLObject):
    CONSTRUCTOR_ID = 0x3C134D7B
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("period", "int"),
        TLField("auto_setting_from", "long", flag_group=0, flag_bit=0),
    ]

    period: Optional[int]
    auto_setting_from: Optional[int]


class MessageActionTopicCreate(TLObject):
    CONSTRUCTOR_ID = 0x0D999256
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("title", "string"),
        TLField("icon_color", "int"),
        TLField("icon_emoji_id", "long", flag_group=0, flag_bit=0),
    ]

    title: Optional[str]
    icon_color: Optional[int]
    icon_emoji_id: Optional[int]


class MessageActionContactReturned(TLObject):
    CONSTRUCTOR_ID = 0x1E47F27A
    FIELDS = []


class MessageActionGiftPremium(TLObject):
    CONSTRUCTOR_ID = 0xC83D6AEC
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("currency", "string"),
        TLField("amount", "long"),
        TLField("months", "int"),
        TLField("crypto_currency", "string", flag_group=0, flag_bit=0),
        TLField("crypto_amount", "long", flag_group=0, flag_bit=0),
    ]


class Messages(BaseMessage):
    CONSTRUCTOR_ID = 0x8C718E87
    FIELDS = [
        TLField("messages", "Message", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]


class MessagesSlice(BaseMessage):
    CONSTRUCTOR_ID = 0x3A54F328
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("inexact", "true", flag_group=1, flag_bit=1),
        TLField("count", "int", skip_cid=True),
        TLField("next_rate", "int", flag_group=1, flag_bit=0),
        TLField("offset_id_offset", "int", flag_group=1, flag_bit=2),
        TLField("messages", "Message", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]


class ForumTopic(TLObject):
    CONSTRUCTOR_ID = 0x71701DA9
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("my", "true", flag_group=0, flag_bit=1),
        TLField("closed", "true", flag_group=0, flag_bit=2),
        TLField("pinned", "true", flag_group=0, flag_bit=3),
        TLField("short", "true", flag_group=0, flag_bit=5),
        TLField("hidden", "true", flag_group=0, flag_bit=6),
        TLField("id", "int"),
        TLField("date", "int"),
        TLField("title", "string"),
        TLField("icon_color", "int"),
        TLField("icon_emoji_id", "long", flag_group=0, flag_bit=0),
        TLField("top_message", "int"),
        TLField("read_inbox_max_id", "int"),
        TLField("read_outbox_max_id", "int"),
        TLField("unread_count", "int"),
        TLField("unread_mentions_count", "int"),
        TLField("unread_reactions_count", "int"),
        TLField("from_id", "Peer"),
        TLField("notify_settings", "PeerNotifySettings"),
        TLField("draft", "DraftMessage", flag_group=0, flag_bit=4),
    ]

    my: Optional[bool]
    closed: Optional[bool]
    pinned: Optional[bool]
    short: Optional[bool]
    hidden: Optional[bool]
    id: Optional[int]
    date: Optional[int]
    title: Optional[str]
    icon_color: Optional[int]
    icon_emoji_id: Optional[int]
    top_message: Optional[int]
    read_inbox_max_id: Optional[int]
    read_outbox_max_id: Optional[int]
    unread_count: Optional[int]
    unread_mentions_count: Optional[int]
    unread_reactions_count: Optional[int]
    from_id: Optional[Peer]
    notify_settings: Optional[PeerNotifySettings]
    draft: Optional[DraftMessage]


class ChannelMessages(TLObject):
    CONSTRUCTOR_ID = 0xC776BA4E
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("inexact", "true", flag_group=0, flag_bit=1),
        TLField("pts", "int", skip_cid=True),
        TLField("count", "int", skip_cid=True),
        TLField("offset_id_offset", "int", flag_group=0, flag_bit=2),
        TLField("messages", "Message", is_vector=True),
        TLField("topics", "ForumTopic", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]


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
    replies: Optional[MessageReplies]


class MessagesMessageViews(TLObject):
    CONSTRUCTOR_ID = 0xB6C4F543
    FIELDS = [
        TLField("views", "MessageViews", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]

    views: Optional[List[MessageViews]]
    chats: Optional[List[Chat]]
    users: Optional[List[User]]
