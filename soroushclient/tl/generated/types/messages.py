from soroushclient.tl.base import TLField, TLObject


class DraftMessageEmpty(TLObject):
    CONSTRUCTOR_ID = 0x1b0c841a
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("date",  "int", flag_group=0, flag_bit=0),
    ]

class DraftMessage(TLObject):
    CONSTRUCTOR_ID = 0xfd8e711f
    FIELDS = [
        TLField("flags",      "int",    flag_group=0, flag_indicator=True),
        TLField("no_webpage", "true",   flag_group=0, flag_bit=1),
        TLField("reply_to",   "MessageReplyHeader", flag_group=0, flag_bit=4),
        TLField("message",    "string"),
        TLField("entities",   "MessageEntity", flag_group=0, flag_bit=3, is_vector=True),
        TLField("media",      "InputMedia",    flag_group=0, flag_bit=6),
        TLField("date",       "int"),
    ]

class MessageMediaEmpty(TLObject):
    CONSTRUCTOR_ID = 0x3ded6320
    FIELDS = []

class MessageMediaPhoto(TLObject):
    CONSTRUCTOR_ID = 0x695150d7
    FIELDS = [
        TLField("flags",       "int",   flag_group=0, flag_indicator=True),
        TLField("spoiler",     "true",  flag_group=0, flag_bit=3),
        TLField("photo",       "Photo", flag_group=0, flag_bit=0),
        TLField("ttl_seconds", "int",   flag_group=0, flag_bit=2),
    ]

class MessageMediaDocument(TLObject):
    CONSTRUCTOR_ID = 0x4cf4d72d
    FIELDS = [
        TLField("flags",        "int",      flag_group=0, flag_indicator=True),
        TLField("nopremium",    "true",     flag_group=0, flag_bit=3),
        TLField("spoiler",      "true",     flag_group=0, flag_bit=4),
        TLField("document",     "Document", flag_group=0, flag_bit=0),
        TLField("alt_document", "Document", flag_group=0, flag_bit=5),
        TLField("ttl_seconds",  "int",      flag_group=0, flag_bit=2),
    ]

class MessageMediaWebPage(TLObject):
    CONSTRUCTOR_ID = 0xddf10c3b
    FIELDS = [
        TLField("flags",             "int",     flag_group=0, flag_indicator=True),
        TLField("force_large_media", "true",    flag_group=0, flag_bit=0),
        TLField("force_small_media", "true",    flag_group=0, flag_bit=1),
        TLField("manual",            "true",    flag_group=0, flag_bit=3),
        TLField("safe",              "true",    flag_group=0, flag_bit=4),
        TLField("webpage",           "WebPage"),
    ]

class MessageMediaContact(TLObject):
    CONSTRUCTOR_ID = 0x70322949
    FIELDS = [
        TLField("phone_number", "string"),
        TLField("first_name",   "string"),
        TLField("last_name",    "string"),
        TLField("vcard",        "string"),
        TLField("user_id",      "long"),
    ]

class MessageMediaUnsupported(TLObject):
    CONSTRUCTOR_ID = 0x9f84f49e
    FIELDS = []

class MessageMediaGeo(TLObject):
    CONSTRUCTOR_ID = 0x56e0d474
    FIELDS = [TLField("geo", "GeoPoint")]



class MessageFwdHeader(TLObject):
    CONSTRUCTOR_ID = 0x4e4df4bb
    FIELDS = [
        TLField("flags",             "int",    flag_group=0, flag_indicator=True),
        TLField("imported",          "true",   flag_group=0, flag_bit=7),
        TLField("from_id",           "Peer",   flag_group=0, flag_bit=0),
        TLField("from_name",         "string", flag_group=0, flag_bit=5),
        TLField("date",              "int"),
        TLField("channel_post",      "int",    flag_group=0, flag_bit=2),
        TLField("post_author",       "string", flag_group=0, flag_bit=3),
        TLField("saved_from_peer",   "Peer",   flag_group=0, flag_bit=4),
        TLField("saved_from_msg_id", "int",    flag_group=0, flag_bit=4),
        TLField("psa_type",          "string", flag_group=0, flag_bit=11),
    ]

class MessageReplyHeader(TLObject):
    CONSTRUCTOR_ID = 0xafbc09db
    FIELDS = [
        TLField("flags",             "int",    flag_group=0, flag_indicator=True),
        TLField("reply_to_scheduled","true",   flag_group=0, flag_bit=2),
        TLField("forum_topic",       "true",   flag_group=0, flag_bit=3),
        TLField("quote",             "true",   flag_group=0, flag_bit=9),
        TLField("reply_to_msg_id",   "int",    flag_group=0, flag_bit=4),
        TLField("reply_to_peer_id",  "Peer",   flag_group=0, flag_bit=0),
        TLField("reply_from",        "MessageFwdHeader", flag_group=0, flag_bit=5),
        TLField("reply_media",       "MessageMedia",     flag_group=0, flag_bit=8),
        TLField("reply_to_top_id",   "int",    flag_group=0, flag_bit=1),
        TLField("quote_text",        "string", flag_group=0, flag_bit=6),
        TLField("quote_entities",    "MessageEntity", flag_group=0, flag_bit=7, is_vector=True),
        TLField("quote_offset",      "int",    flag_group=0, flag_bit=10),
    ]

class MessageEntityUnknown(TLObject):
    CONSTRUCTOR_ID = 0xbb92ba95
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityMention(TLObject):
    CONSTRUCTOR_ID = 0xfa04579d
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityHashtag(TLObject):
    CONSTRUCTOR_ID = 0x6f635b0d
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityBotCommand(TLObject):
    CONSTRUCTOR_ID = 0x6cef8ac7
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityUrl(TLObject):
    CONSTRUCTOR_ID = 0x6ed02538
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityEmail(TLObject):
    CONSTRUCTOR_ID = 0x64e475c2
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityBold(TLObject):
    CONSTRUCTOR_ID = 0xbd610bc9
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityItalic(TLObject):
    CONSTRUCTOR_ID = 0x826f8b60
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityCode(TLObject):
    CONSTRUCTOR_ID = 0x28a20571
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityPre(TLObject):
    CONSTRUCTOR_ID = 0x73924be0
    FIELDS = [TLField("offset","int"), TLField("length","int"), TLField("language","string")]

class MessageEntityTextUrl(TLObject):
    CONSTRUCTOR_ID = 0x76a6d327
    FIELDS = [TLField("offset","int"), TLField("length","int"), TLField("url","string")]

class MessageEntityMentionName(TLObject):
    CONSTRUCTOR_ID = 0xdc7b1140
    FIELDS = [TLField("offset","int"), TLField("length","int"), TLField("user_id","long")]

class MessageEntityPhone(TLObject):
    CONSTRUCTOR_ID = 0x9b69e34b
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityCashtag(TLObject):
    CONSTRUCTOR_ID = 0x4c4e743f
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityUnderline(TLObject):
    CONSTRUCTOR_ID = 0x9c4e7e8b
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityStrike(TLObject):
    CONSTRUCTOR_ID = 0xbf0693d4
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntitySpoiler(TLObject):
    CONSTRUCTOR_ID = 0x32ca960f
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityBlockquote(TLObject):
    CONSTRUCTOR_ID = 0xf1ccaaac
    FIELDS = [TLField("offset","int"), TLField("length","int")]

class MessageEntityCustomEmoji(TLObject):
    CONSTRUCTOR_ID = 0xc8cf05f8
    FIELDS = [TLField("offset","int"), TLField("length","int"), TLField("document_id","long")]

class MessageReplies(TLObject):
    CONSTRUCTOR_ID = 0x83d60fc2
    FIELDS = [
        TLField("flags",           "int",  flag_group=0, flag_indicator=True),
        TLField("comments",        "true", flag_group=0, flag_bit=0),
        TLField("replies",         "int"),
        TLField("replies_pts",     "int"),
        TLField("recent_repliers", "Peer", flag_group=0, flag_bit=1, is_vector=True),
        TLField("channel_id",      "long", flag_group=0, flag_bit=0),
        TLField("max_id",          "int",  flag_group=0, flag_bit=2),
        TLField("read_max_id",     "int",  flag_group=0, flag_bit=3),
    ]
class ReactionEmpty(TLObject):
    CONSTRUCTOR_ID = 0x79f5d419
    FIELDS = []

class ReactionEmoji(TLObject):
    CONSTRUCTOR_ID = 0x1b2286be
    FIELDS = [TLField("emoticon", "string")]

class ReactionCustomEmoji(TLObject):
    CONSTRUCTOR_ID = 0x8935fc73
    FIELDS = [TLField("document_id", "long")]

class ReactionCount(TLObject):
    CONSTRUCTOR_ID = 0xa3d1cb80
    FIELDS = [
        TLField("flags",        "int",  flag_group=0, flag_indicator=True),
        TLField("chosen_order", "int",  flag_group=0, flag_bit=0),
        TLField("reaction",     "Reaction"),
        TLField("count",        "int"),
    ]

class MessageReactions(TLObject):
    CONSTRUCTOR_ID = 0x4f2b9479
    FIELDS = [
        TLField("flags",              "int",  flag_group=0, flag_indicator=True),
        TLField("min",                "true", flag_group=0, flag_bit=0),
        TLField("can_see_list",       "true", flag_group=0, flag_bit=2),
        TLField("reactions_as_tags",  "true", flag_group=0, flag_bit=3),
        TLField("results",            "ReactionCount", is_vector=True),
        TLField("recent_reactions",   "MessagePeerReaction", flag_group=0, flag_bit=1, is_vector=True),
    ]

class MessageEmpty(TLObject):
    CONSTRUCTOR_ID = 0x90a6ca84
    FIELDS = [
        TLField("flags",   "int",  flag_group=0, flag_indicator=True),
        TLField("id",      "int"),
        TLField("peer_id", "Peer", flag_group=0, flag_bit=0),
    ]

class Message(TLObject):
    CONSTRUCTOR_ID = 0x38116ee0
    FIELDS = [
        TLField("flags",              "int",  flag_group=0, flag_indicator=True),
        TLField("out",                "true", flag_group=0, flag_bit=1),
        TLField("mentioned",          "true", flag_group=0, flag_bit=4),
        TLField("media_unread",       "true", flag_group=0, flag_bit=5),
        TLField("silent",             "true", flag_group=0, flag_bit=13),
        TLField("post",               "true", flag_group=0, flag_bit=14),
        TLField("from_scheduled",     "true", flag_group=0, flag_bit=18),
        TLField("legacy",             "true", flag_group=0, flag_bit=19),
        TLField("edit_hide",          "true", flag_group=0, flag_bit=21),
        TLField("pinned",             "true", flag_group=0, flag_bit=24),
        TLField("noforwards",         "true", flag_group=0, flag_bit=26),
        TLField("invert_media",       "true", flag_group=0, flag_bit=27),
        TLField("id",                 "int"),
        TLField("from_id",            "Peer", flag_group=0, flag_bit=8),
        TLField("peer_id",            "Peer"),
        TLField("fwd_from",           "MessageFwdHeader",  flag_group=0, flag_bit=2),
        TLField("via_bot_id",         "long", flag_group=0, flag_bit=11),
        TLField("reply_to",           "MessageReplyHeader",flag_group=0, flag_bit=3),
        TLField("date",               "int"),
        TLField("message",            "string"),
        TLField("media",              "MessageMedia",  flag_group=0, flag_bit=9),
        TLField("reply_markup",       "ReplyMarkup",   flag_group=0, flag_bit=6),
        TLField("entities",           "MessageEntity", flag_group=0, flag_bit=7, is_vector=True),
        TLField("views",              "int",  flag_group=0, flag_bit=10),
        TLField("forwards",           "int",  flag_group=0, flag_bit=10),
        TLField("replies",            "MessageReplies",  flag_group=0, flag_bit=23),
        TLField("edit_date",          "int",  flag_group=0, flag_bit=15),
        TLField("post_author",        "string", flag_group=0, flag_bit=16),
        TLField("grouped_id",         "long", flag_group=0, flag_bit=17),
        TLField("reactions",          "MessageReactions", flag_group=0, flag_bit=20),
        TLField("restriction_reason", "RestrictionReason", flag_group=0, flag_bit=22, is_vector=True),
        TLField("ttl_period",         "int",  flag_group=0, flag_bit=25),
    ]

class MessageService(TLObject):
    CONSTRUCTOR_ID = 0x2b085862
    FIELDS = [
        TLField("flags",     "int",  flag_group=0, flag_indicator=True),
        TLField("out",       "true", flag_group=0, flag_bit=1),
        TLField("mentioned", "true", flag_group=0, flag_bit=4),
        TLField("silent",    "true", flag_group=0, flag_bit=13),
        TLField("post",      "true", flag_group=0, flag_bit=14),
        TLField("legacy",    "true", flag_group=0, flag_bit=19),
        TLField("id",        "int"),
        TLField("from_id",   "Peer", flag_group=0, flag_bit=8),
        TLField("peer_id",   "Peer"),
        TLField("reply_to",  "MessageReplyHeader", flag_group=0, flag_bit=3),
        TLField("date",      "int"),
        TLField("action",    "MessageAction"),
        TLField("ttl_period","int",  flag_group=0, flag_bit=25),
    ]

class MessageActionEmpty(TLObject):
    CONSTRUCTOR_ID = 0xb6aef7b0
    FIELDS = []

class MessageActionChatCreate(TLObject):
    CONSTRUCTOR_ID = 0xbd47cbad
    FIELDS = [TLField("title","string"), TLField("users","long",is_vector=True)]

class MessageActionChatEditTitle(TLObject):
    CONSTRUCTOR_ID = 0xb5a1ce5a
    FIELDS = [TLField("title","string")]

class MessageActionChatAddUser(TLObject):
    CONSTRUCTOR_ID = 0x15cefd00
    FIELDS = [TLField("users","long",is_vector=True)]

class MessageActionChatDeleteUser(TLObject):
    CONSTRUCTOR_ID = 0xa43f30cc
    FIELDS = [TLField("user_id","long")]

class MessageActionChannelCreate(TLObject):
    CONSTRUCTOR_ID = 0x95d2ac92
    FIELDS = [TLField("title","string")]

class MessageActionPinMessage(TLObject):
    CONSTRUCTOR_ID = 0x94bd38ed
    FIELDS = []

class MessageActionHistoryClear(TLObject):
    CONSTRUCTOR_ID = 0x9fbab604
    FIELDS = []

class MessageActionContactSignUp(TLObject):
    CONSTRUCTOR_ID = 0xf3f25f76
    FIELDS = []

class MessageActionChatJoinedByLink(TLObject):
    CONSTRUCTOR_ID = 0x031224c3
    FIELDS = [TLField("inviter_id","long")]

class MessageActionChatMigrateTo(TLObject):
    CONSTRUCTOR_ID = 0xe1037f92
    FIELDS = [TLField("channel_id","long")]

class MessageActionChannelMigrateFrom(TLObject):
    CONSTRUCTOR_ID = 0xea3948e9
    FIELDS = [TLField("title","string"), TLField("chat_id","long")]

class MessageActionCustomAction(TLObject):
    CONSTRUCTOR_ID = 0xfae69f56
    FIELDS = [TLField("message","string")]

class MessageActionSetMessagesTTL(TLObject):
    CONSTRUCTOR_ID = 0x3c134d7b
    FIELDS = [
        TLField("flags",             "int",  flag_group=0, flag_indicator=True),
        TLField("period",            "int"),
        TLField("auto_setting_from", "long", flag_group=0, flag_bit=0),
    ]

class MessageActionTopicCreate(TLObject):
    CONSTRUCTOR_ID = 0x0d999256
    FIELDS = [
        TLField("flags",        "int",  flag_group=0, flag_indicator=True),
        TLField("title",        "string"),
        TLField("icon_color",   "int"),
        TLField("icon_emoji_id","long", flag_group=0, flag_bit=0),
    ]

class MessageActionContactReturned(TLObject):
    CONSTRUCTOR_ID = 0x1e47f27a
    FIELDS = []

class MessageActionGiftPremium(TLObject):
    CONSTRUCTOR_ID = 0xc83d6aec
    FIELDS = [
        TLField("flags",          "int",    flag_group=0, flag_indicator=True),
        TLField("currency",       "string"),
        TLField("amount",         "long"),
        TLField("months",         "int"),
        TLField("crypto_currency","string", flag_group=0, flag_bit=0),
        TLField("crypto_amount",  "long",   flag_group=0, flag_bit=0),
    ]

