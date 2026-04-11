from soroushclient.tl.base import TLField, TLObject


class Channel(TLObject):
    CONSTRUCTOR_ID = 0x8E87CCD8
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("flags2", "int", flag_group=1, flag_indicator=True),
        TLField("creator", "true", flag_group=0, flag_bit=0),
        TLField("left", "true", flag_group=0, flag_bit=2),
        TLField("broadcast", "true", flag_group=0, flag_bit=5),
        TLField("verified", "true", flag_group=0, flag_bit=7),
        TLField("megagroup", "true", flag_group=0, flag_bit=8),
        TLField("restricted", "true", flag_group=0, flag_bit=9),
        TLField("signatures", "true", flag_group=0, flag_bit=11),
        TLField("min", "true", flag_group=0, flag_bit=12),
        TLField("scam", "true", flag_group=0, flag_bit=19),
        TLField("has_link", "true", flag_group=0, flag_bit=20),
        TLField("has_geo", "true", flag_group=0, flag_bit=21),
        TLField("slowmode_enabled", "true", flag_group=0, flag_bit=22),
        TLField("call_active", "true", flag_group=0, flag_bit=23),
        TLField("call_not_empty", "true", flag_group=0, flag_bit=24),
        TLField("fake", "true", flag_group=0, flag_bit=25),
        TLField("gigagroup", "true", flag_group=0, flag_bit=26),
        TLField("noforwards", "true", flag_group=0, flag_bit=27),
        TLField("join_to_send", "true", flag_group=0, flag_bit=28),
        TLField("join_request", "true", flag_group=0, flag_bit=29),
        TLField("forum", "true", flag_group=0, flag_bit=30),
        TLField("stories_hidden", "true", flag_group=1, flag_bit=1),
        TLField("stories_hidden_min", "true", flag_group=1, flag_bit=2),
        TLField("stories_unavailable", "true", flag_group=1, flag_bit=3),
        TLField("id", "long"),
        TLField("access_hash", "long", flag_group=0, flag_bit=13),
        TLField("title", "string"),
        TLField("username", "string", flag_group=0, flag_bit=6),
        TLField("photo", "ChatPhoto"),
        TLField("date", "int"),
        TLField(
            "restriction_reason",
            "RestrictionReason",
            flag_group=0,
            flag_bit=9,
            is_vector=True,
        ),
        TLField("admin_rights", "ChatAdminRights", flag_group=0, flag_bit=14),
        TLField("banned_rights", "ChatBannedRights", flag_group=0, flag_bit=15),
        TLField("default_banned_rights", "ChatBannedRights", flag_group=0, flag_bit=18),
        TLField("participants_count", "int", flag_group=0, flag_bit=17),
        TLField("usernames", "Username", flag_group=1, flag_bit=0, is_vector=True),
        TLField("stories_max_id", "int", flag_group=1, flag_bit=4),
        TLField("color", "PeerColor", flag_group=1, flag_bit=7),
    ]


class ChannelForbidden(TLObject):
    CONSTRUCTOR_ID = 0x17D493D5
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("broadcast", "true", flag_group=0, flag_bit=5),
        TLField("megagroup", "true", flag_group=0, flag_bit=8),
        TLField("id", "long"),
        TLField("access_hash", "long"),
        TLField("title", "string"),
        TLField("until_date", "int", flag_group=0, flag_bit=16),
    ]


class ChannelFull(TLObject):
    CONSTRUCTOR_ID = 0x723027BD
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("can_view_participants", "true", flag_group=0, flag_bit=3),
        TLField("can_set_username", "true", flag_group=0, flag_bit=6),
        TLField("can_set_stickers", "true", flag_group=0, flag_bit=7),
        TLField("hidden_prehistory", "true", flag_group=0, flag_bit=10),
        TLField("can_set_location", "true", flag_group=0, flag_bit=16),
        TLField("has_scheduled", "true", flag_group=0, flag_bit=19),
        TLField("can_view_stats", "true", flag_group=0, flag_bit=20),
        TLField("blocked", "true", flag_group=0, flag_bit=22),
        # second flags word — must be deserialized as its own int in sequence
        TLField("flags2", "int", flag_group=1, flag_indicator=True),
        TLField("can_delete_channel", "true", flag_group=1, flag_bit=0),
        TLField("antispam", "true", flag_group=1, flag_bit=1),
        TLField("participants_hidden", "true", flag_group=1, flag_bit=2),
        TLField("translations_disabled", "true", flag_group=1, flag_bit=3),
        TLField("stories_pinned_available", "true", flag_group=1, flag_bit=5),
        TLField("view_forum_as_messages", "true", flag_group=1, flag_bit=6),
        # non-optional fields
        TLField("id", "long"),
        TLField("about", "string"),
        # optional from flags group 0
        TLField("participants_count", "int", flag_group=0, flag_bit=0),
        TLField("admins_count", "int", flag_group=0, flag_bit=1),
        TLField("kicked_count", "int", flag_group=0, flag_bit=2),
        TLField("banned_count", "int", flag_group=0, flag_bit=2),
        TLField("online_count", "int", flag_group=0, flag_bit=13),
        TLField("read_inbox_max_id", "int"),
        TLField("read_outbox_max_id", "int"),
        TLField("unread_count", "int"),
        TLField("chat_photo", "Photo"),
        TLField("notify_settings", "PeerNotifySettings"),
        TLField("exported_invite", "ChatInviteExported", flag_group=0, flag_bit=23),
        TLField("bot_info", "BotInfo", is_vector=True),  # always present
        TLField("migrated_from_chat_id", "long", flag_group=0, flag_bit=4),
        TLField("migrated_from_max_id", "int", flag_group=0, flag_bit=4),
        TLField("pinned_msg_id", "int", flag_group=0, flag_bit=5),
        TLField("stickerset", "StickerSet", flag_group=0, flag_bit=8),
        TLField("available_min_id", "int", flag_group=0, flag_bit=9),
        TLField("folder_id", "int", flag_group=0, flag_bit=11),
        TLField("linked_chat_id", "long", flag_group=0, flag_bit=14),
        TLField("location", "ChannelLocation", flag_group=0, flag_bit=15),
        TLField("slowmode_seconds", "int", flag_group=0, flag_bit=17),
        TLField("slowmode_next_send_date", "int", flag_group=0, flag_bit=18),
        TLField("stats_dc", "int", flag_group=0, flag_bit=12),
        TLField("pts", "int"),
        TLField("call", "InputGroupCall", flag_group=0, flag_bit=21),
        TLField("ttl_period", "int", flag_group=0, flag_bit=24),
        TLField(
            "pending_suggestions", "string", flag_group=0, flag_bit=25, is_vector=True
        ),
        TLField("groupcall_default_join_as", "Peer", flag_group=0, flag_bit=26),
        TLField("theme_emoticon", "string", flag_group=0, flag_bit=27),
        TLField("requests_pending", "int", flag_group=0, flag_bit=28),
        TLField("recent_requesters", "long", flag_group=0, flag_bit=28, is_vector=True),
        TLField("default_send_as", "Peer", flag_group=0, flag_bit=29),
        TLField("available_reactions", "ChatReactions", flag_group=0, flag_bit=30),
        TLField("stories", "PeerStories", flag_group=1, flag_bit=4),  # flags2.4
    ]
