from soroushclient.tl.base import TLField, TLObject


class ChatPhotoEmpty(TLObject):
    CONSTRUCTOR_ID = 0x37C1011C
    FIELDS = []


class ChatPhoto(TLObject):
    CONSTRUCTOR_ID = 0x1C6E1C11
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("has_video", "true", flag_group=0, flag_bit=0),
        TLField("photo_id", "long"),
        TLField("stripped_thumb", "bytes", flag_group=0, flag_bit=1),
        TLField("dc_id", "int"),
    ]


class ChatEmpty(TLObject):
    CONSTRUCTOR_ID = 0x29562865
    FIELDS = [TLField("id", "long")]


class Chat(TLObject):
    CONSTRUCTOR_ID = 0x41CBF256
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("creator", "true", flag_group=0, flag_bit=0),
        TLField("left", "true", flag_group=0, flag_bit=2),
        TLField("deactivated", "true", flag_group=0, flag_bit=5),
        TLField("call_active", "true", flag_group=0, flag_bit=23),
        TLField("call_not_empty", "true", flag_group=0, flag_bit=24),
        TLField("noforwards", "true", flag_group=0, flag_bit=25),
        TLField("id", "long"),
        TLField("title", "string"),
        TLField("photo", "ChatPhoto"),
        TLField("participants_count", "int"),
        TLField("date", "int"),
        TLField("version", "int"),
        TLField("migrated_to", "InputChannel", flag_group=0, flag_bit=6),
        TLField("admin_rights", "ChatAdminRights", flag_group=0, flag_bit=14),
        TLField("default_banned_rights", "ChatBannedRights", flag_group=0, flag_bit=18),
    ]


class ChatForbidden(TLObject):
    CONSTRUCTOR_ID = 0x6592A1A7
    FIELDS = [TLField("id", "long"), TLField("title", "string")]


class ChatReactionsNone(TLObject):
    CONSTRUCTOR_ID = 0xEAFC32BC
    FIELDS = []


class ChatParticipant(TLObject):
    CONSTRUCTOR_ID = 0xC02D4007
    FIELDS = [
        TLField("user_id", "long"),
        TLField("inviter_id", "long"),
        TLField("date", "int"),
    ]


class ChatParticipantCreator(TLObject):
    CONSTRUCTOR_ID = 0xE46BCEE4
    FIELDS = [
        TLField("user_id", "long"),
    ]


class ChatParticipantAdmin(TLObject):
    CONSTRUCTOR_ID = 0xA0933F5B
    FIELDS = [
        TLField("user_id", "long"),
        TLField("inviter_id", "long"),
        TLField("date", "int"),
    ]


class ChatReactionsAll(TLObject):
    CONSTRUCTOR_ID = 0x52928BCA
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("allow_custom", "true", flag_group=0, flag_bit=0),
    ]


class ChatReactionsSome(TLObject):
    CONSTRUCTOR_ID = 0x661D4037
    FIELDS = [
        TLField("reactions", "Reaction", is_vector=True),
    ]


class ChatReactionsDisabled(TLObject):
    CONSTRUCTOR_ID = 0x75C1F53B
    FIELDS = []


class ChatParticipantsForbidden(TLObject):
    CONSTRUCTOR_ID = 0x8763D3E1
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("chat_id", "long"),
        TLField("self_participant", "ChatParticipant", flag_group=0, flag_bit=0),
    ]


class ChatParticipants(TLObject):
    CONSTRUCTOR_ID = 0x3CBC93F8
    FIELDS = [
        TLField("chat_id", "long"),
        TLField("participants", "ChatParticipant", is_vector=True),
        TLField("version", "int"),
    ]


class ChatInviteExported(TLObject):
    CONSTRUCTOR_ID = 0x3F423924
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("revoked", "true", flag_group=0, flag_bit=0),
        TLField("permanent", "true", flag_group=0, flag_bit=5),
        TLField("request_needed", "true", flag_group=0, flag_bit=6),
        TLField("link", "string"),
        TLField("links", "string", is_vector=True),
        TLField("admin_id", "long"),
        TLField("date", "int"),
        TLField("start_date", "int", flag_group=0, flag_bit=4),
        TLField("expire_date", "int", flag_group=0, flag_bit=1),
        TLField("usage_limit", "int", flag_group=0, flag_bit=2),
        TLField("usage", "int", flag_group=0, flag_bit=3),
        TLField("requested", "int", flag_group=0, flag_bit=7),
        TLField("title", "string", flag_group=0, flag_bit=8),
    ]


class ChatFull(TLObject):
    CONSTRUCTOR_ID = 0xD18EE226
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("can_set_username", "true", flag_group=0, flag_bit=7),
        TLField("has_scheduled", "true", flag_group=0, flag_bit=8),
        TLField("translations_disabled", "true", flag_group=0, flag_bit=19),
        TLField("id", "long"),
        TLField("about", "string"),
        TLField("participants", "ChatParticipants"),
        TLField("chat_photo", "Photo", flag_group=0, flag_bit=2),
        TLField("notify_settings", "PeerNotifySettings"),
        TLField("exported_invite", "ChatInviteExported", flag_group=0, flag_bit=13),
        TLField("bot_info", "BotInfo", flag_group=0, flag_bit=3, is_vector=True),
        TLField("pinned_msg_id", "int", flag_group=0, flag_bit=6),
        TLField("folder_id", "int", flag_group=0, flag_bit=11),
        TLField("call", "InputGroupCall", flag_group=0, flag_bit=12),
        TLField("ttl_period", "int", flag_group=0, flag_bit=14),
        TLField("groupcall_default_join_as", "Peer", flag_group=0, flag_bit=15),
        TLField("theme_emoticon", "string", flag_group=0, flag_bit=16),
        TLField("requests_pending", "int", flag_group=0, flag_bit=17),
        TLField("recent_requesters", "long", flag_group=0, flag_bit=17, is_vector=True),
        TLField("available_reactions", "ChatReactions", flag_group=0, flag_bit=18),
    ]


class ExportedChatInviteResult(TLObject):
    CONSTRUCTOR_ID = 0x1871BE50
    FIELDS = [
        TLField("invite", "ChatInviteExported"),
        TLField("users", "User", is_vector=True),
    ]


class ExportedChatInviteReplaced(TLObject):
    CONSTRUCTOR_ID = 0x222600EF
    FIELDS = [
        TLField("invite", "ChatInviteExported"),
        TLField("new_invite", "ChatInviteExported"),
        TLField("users", "User", is_vector=True),
    ]


class MessagesChatFull(TLObject):
    CONSTRUCTOR_ID = 0xE5D7D19C
    FIELDS = [
        TLField("full_chat", "ChatFull"),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]


class ExportedChatInvites(TLObject):
    CONSTRUCTOR_ID = 0xBDC62DCC
    FIELDS = [
        TLField("count", "int"),
        TLField("invites", "ChatInviteExported", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
