from typing import Optional, List

from soroushclient.tl.base import TLField, TLObject


class ChatEmpty(TLObject):
    CONSTRUCTOR_ID = 0x29562865
    FIELDS = [TLField("id", "long")]
    id: Optional[int]

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
    creator: Optional[bool]
    left: Optional[bool]
    deactivated: Optional[bool]
    call_active: Optional[bool]
    call_not_empty: Optional[bool]
    noforwards: Optional[bool]
    id: Optional[int]
    title: Optional[str]
    photo: Optional[TLObject]
    participants_count: Optional[int]
    date: Optional[int]
    version: Optional[int]
    migrated_to: Optional[TLObject]
    admin_rights: Optional[TLObject]
    default_banned_rights: Optional[TLObject]

class ChatForbidden(TLObject):
    CONSTRUCTOR_ID = 0x6592A1A7
    FIELDS = [
        TLField("id", "long"),
        TLField("title", "string"),
    ]
    id: Optional[int]
    title: Optional[str]

# Channel class already defined above (kept in chats.py)
class Channel(TLObject):
    CONSTRUCTOR_ID = 0x8E87CCD8
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
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
        TLField("flags2", "int", flag_group=1, flag_indicator=True),
        TLField("stories_hidden", "true", flag_group=1, flag_bit=1),
        TLField("stories_hidden_min", "true", flag_group=1, flag_bit=2),
        TLField("stories_unavailable", "true", flag_group=1, flag_bit=3),
        TLField("id", "long"),
        TLField("access_hash", "long", flag_group=0, flag_bit=13),
        TLField("title", "string"),
        TLField("username", "string", flag_group=0, flag_bit=6),
        TLField("photo", "ChatPhoto"),
        TLField("date", "int"),
        TLField("restriction_reason", "RestrictionReason", flag_group=0, flag_bit=9, is_vector=True),
        TLField("admin_rights", "ChatAdminRights", flag_group=0, flag_bit=14),
        TLField("banned_rights", "ChatBannedRights", flag_group=0, flag_bit=15),
        TLField("default_banned_rights", "ChatBannedRights", flag_group=0, flag_bit=18),
        TLField("participants_count", "int", flag_group=0, flag_bit=17),
        TLField("usernames", "Username", flag_group=1, flag_bit=0, is_vector=True),
        TLField("stories_max_id", "int", flag_group=1, flag_bit=4),
        TLField("color", "PeerColor", flag_group=1, flag_bit=7),
    ]

    creator: Optional[bool]
    left: Optional[bool]
    broadcast: Optional[bool]
    verified: Optional[bool]
    megagroup: Optional[bool]
    restricted: Optional[bool]
    signatures: Optional[bool]
    min: Optional[bool]
    scam: Optional[bool]
    has_link: Optional[bool]
    has_geo: Optional[bool]
    slowmode_enabled: Optional[bool]
    call_active: Optional[bool]
    call_not_empty: Optional[bool]
    fake: Optional[bool]
    gigagroup: Optional[bool]
    noforwards: Optional[bool]
    join_to_send: Optional[bool]
    join_request: Optional[bool]
    forum: Optional[bool]
    stories_hidden: Optional[bool]
    stories_hidden_min: Optional[bool]
    stories_unavailable: Optional[bool]
    id: Optional[int]
    access_hash: Optional[int]
    title: Optional[str]
    username: Optional[str]
    photo: Optional[TLObject]
    date: Optional[int]
    restriction_reason: Optional[List[TLObject]]
    admin_rights: Optional[TLObject]
    banned_rights: Optional[TLObject]
    default_banned_rights: Optional[TLObject]
    participants_count: Optional[int]
    usernames: Optional[List[TLObject]]
    stories_max_id: Optional[int]
    color: Optional[TLObject]

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
    broadcast: Optional[bool]
    megagroup: Optional[bool]
    id: Optional[int]
    access_hash: Optional[int]
    title: Optional[str]
    until_date: Optional[int]

class ChatFull(TLObject):
    CONSTRUCTOR_ID = 0xC9D31138
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
        TLField("exported_invite", "ExportedChatInvite", flag_group=0, flag_bit=13),
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
    can_set_username: Optional[bool]
    has_scheduled: Optional[bool]
    translations_disabled: Optional[bool]
    id: Optional[int]
    about: Optional[str]
    participants: Optional[TLObject]
    chat_photo: Optional[TLObject]
    notify_settings: Optional[TLObject]
    exported_invite: Optional[TLObject]
    bot_info: Optional[List[TLObject]]
    pinned_msg_id: Optional[int]
    folder_id: Optional[int]
    call: Optional[TLObject]
    ttl_period: Optional[int]
    groupcall_default_join_as: Optional[TLObject]
    theme_emoticon: Optional[str]
    requests_pending: Optional[int]
    recent_requesters: Optional[List[int]]
    available_reactions: Optional[TLObject]

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
        TLField("flags2", "int", flag_group=1, flag_indicator=True),
        TLField("can_delete_channel", "true", flag_group=1, flag_bit=0),
        TLField("antispam", "true", flag_group=1, flag_bit=1),
        TLField("participants_hidden", "true", flag_group=1, flag_bit=2),
        TLField("translations_disabled", "true", flag_group=1, flag_bit=3),
        TLField("stories_pinned_available", "true", flag_group=1, flag_bit=5),
        TLField("view_forum_as_messages", "true", flag_group=1, flag_bit=6),
        TLField("id", "long"),
        TLField("about", "string"),
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
        TLField("exported_invite", "ExportedChatInvite", flag_group=0, flag_bit=23),
        TLField("bot_info", "BotInfo", is_vector=True),
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
        TLField("pending_suggestions", "string", flag_group=0, flag_bit=25, is_vector=True),
        TLField("groupcall_default_join_as", "Peer", flag_group=0, flag_bit=26),
        TLField("theme_emoticon", "string", flag_group=0, flag_bit=27),
        TLField("requests_pending", "int", flag_group=0, flag_bit=28),
        TLField("recent_requesters", "long", flag_group=0, flag_bit=28, is_vector=True),
        TLField("default_send_as", "Peer", flag_group=0, flag_bit=29),
        TLField("available_reactions", "ChatReactions", flag_group=0, flag_bit=30),
        TLField("stories", "PeerStories", flag_group=1, flag_bit=4),
    ]
    can_view_participants: Optional[bool]
    can_set_username: Optional[bool]
    can_set_stickers: Optional[bool]
    hidden_prehistory: Optional[bool]
    can_set_location: Optional[bool]
    has_scheduled: Optional[bool]
    can_view_stats: Optional[bool]
    blocked: Optional[bool]
    can_delete_channel: Optional[bool]
    antispam: Optional[bool]
    participants_hidden: Optional[bool]
    translations_disabled: Optional[bool]
    stories_pinned_available: Optional[bool]
    view_forum_as_messages: Optional[bool]
    id: Optional[int]
    about: Optional[str]
    participants_count: Optional[int]
    admins_count: Optional[int]
    kicked_count: Optional[int]
    banned_count: Optional[int]
    online_count: Optional[int]
    read_inbox_max_id: Optional[int]
    read_outbox_max_id: Optional[int]
    unread_count: Optional[int]
    chat_photo: Optional[TLObject]
    notify_settings: Optional[TLObject]
    exported_invite: Optional[TLObject]
    bot_info: Optional[List[TLObject]]
    migrated_from_chat_id: Optional[int]
    migrated_from_max_id: Optional[int]
    pinned_msg_id: Optional[int]
    stickerset: Optional[TLObject]
    available_min_id: Optional[int]
    folder_id: Optional[int]
    linked_chat_id: Optional[int]
    location: Optional[TLObject]
    slowmode_seconds: Optional[int]
    slowmode_next_send_date: Optional[int]
    stats_dc: Optional[int]
    pts: Optional[int]
    call: Optional[TLObject]
    ttl_period: Optional[int]
    pending_suggestions: Optional[List[str]]
    groupcall_default_join_as: Optional[TLObject]
    theme_emoticon: Optional[str]
    requests_pending: Optional[int]
    recent_requesters: Optional[List[int]]
    default_send_as: Optional[TLObject]
    available_reactions: Optional[TLObject]
    stories: Optional[TLObject]

class ChatParticipant(TLObject):
    CONSTRUCTOR_ID = 0xC02D4007
    FIELDS = [
        TLField("user_id", "long"),
        TLField("inviter_id", "long"),
        TLField("date", "int"),
    ]
    user_id: Optional[int]
    inviter_id: Optional[int]
    date: Optional[int]

class ChatParticipantCreator(TLObject):
    CONSTRUCTOR_ID = 0xE46BCEE4
    FIELDS = [TLField("user_id", "long")]
    user_id: Optional[int]

class ChatParticipantAdmin(TLObject):
    CONSTRUCTOR_ID = 0xA0933F5B
    FIELDS = [
        TLField("user_id", "long"),
        TLField("inviter_id", "long"),
        TLField("date", "int"),
    ]
    user_id: Optional[int]
    inviter_id: Optional[int]
    date: Optional[int]

class ChatParticipantsForbidden(TLObject):
    CONSTRUCTOR_ID = 0x8763D3E1
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("chat_id", "long"),
        TLField("self_participant", "ChatParticipant", flag_group=0, flag_bit=0),
    ]
    chat_id: Optional[int]
    self_participant: Optional[TLObject]

class ChatParticipants(TLObject):
    CONSTRUCTOR_ID = 0x3CBC93F8
    FIELDS = [
        TLField("chat_id", "long"),
        TLField("participants", "ChatParticipant", is_vector=True),
        TLField("version", "int"),
    ]
    chat_id: Optional[int]
    participants: Optional[List[TLObject]]
    version: Optional[int]

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
    has_video: Optional[bool]
    photo_id: Optional[int]
    stripped_thumb: Optional[bytes]
    dc_id: Optional[int]

class ChatAdminRights(TLObject):
    CONSTRUCTOR_ID = 0x5FB224D5
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("change_info", "true", flag_group=0, flag_bit=0),
        TLField("post_messages", "true", flag_group=0, flag_bit=1),
        TLField("edit_messages", "true", flag_group=0, flag_bit=2),
        TLField("delete_messages", "true", flag_group=0, flag_bit=3),
        TLField("ban_users", "true", flag_group=0, flag_bit=4),
        TLField("invite_users", "true", flag_group=0, flag_bit=5),
        TLField("pin_messages", "true", flag_group=0, flag_bit=7),
        TLField("add_admins", "true", flag_group=0, flag_bit=9),
        TLField("anonymous", "true", flag_group=0, flag_bit=10),
        TLField("manage_call", "true", flag_group=0, flag_bit=11),
        TLField("other", "true", flag_group=0, flag_bit=12),
        TLField("manage_topics", "true", flag_group=0, flag_bit=13),
        TLField("post_stories", "true", flag_group=0, flag_bit=14),
        TLField("edit_stories", "true", flag_group=0, flag_bit=15),
        TLField("delete_stories", "true", flag_group=0, flag_bit=16),
    ]
    change_info: Optional[bool]
    post_messages: Optional[bool]
    edit_messages: Optional[bool]
    delete_messages: Optional[bool]
    ban_users: Optional[bool]
    invite_users: Optional[bool]
    pin_messages: Optional[bool]
    add_admins: Optional[bool]
    anonymous: Optional[bool]
    manage_call: Optional[bool]
    other: Optional[bool]
    manage_topics: Optional[bool]
    post_stories: Optional[bool]
    edit_stories: Optional[bool]
    delete_stories: Optional[bool]

class ChatBannedRights(TLObject):
    CONSTRUCTOR_ID = 0x9F120418
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("view_messages", "true", flag_group=0, flag_bit=0),
        TLField("send_messages", "true", flag_group=0, flag_bit=1),
        TLField("send_media", "true", flag_group=0, flag_bit=2),
        TLField("send_stickers", "true", flag_group=0, flag_bit=3),
        TLField("send_gifs", "true", flag_group=0, flag_bit=4),
        TLField("send_games", "true", flag_group=0, flag_bit=5),
        TLField("send_inline", "true", flag_group=0, flag_bit=6),
        TLField("embed_links", "true", flag_group=0, flag_bit=7),
        TLField("send_polls", "true", flag_group=0, flag_bit=8),
        TLField("change_info", "true", flag_group=0, flag_bit=10),
        TLField("invite_users", "true", flag_group=0, flag_bit=15),
        TLField("pin_messages", "true", flag_group=0, flag_bit=17),
        TLField("manage_topics", "true", flag_group=0, flag_bit=18),
        TLField("send_photos", "true", flag_group=0, flag_bit=19),
        TLField("send_videos", "true", flag_group=0, flag_bit=20),
        TLField("send_roundvideos", "true", flag_group=0, flag_bit=21),
        TLField("send_audios", "true", flag_group=0, flag_bit=22),
        TLField("send_voices", "true", flag_group=0, flag_bit=23),
        TLField("send_docs", "true", flag_group=0, flag_bit=24),
        TLField("send_plain", "true", flag_group=0, flag_bit=25),
        TLField("until_date", "int"),
    ]
    view_messages: Optional[bool]
    send_messages: Optional[bool]
    send_media: Optional[bool]
    send_stickers: Optional[bool]
    send_gifs: Optional[bool]
    send_games: Optional[bool]
    send_inline: Optional[bool]
    embed_links: Optional[bool]
    send_polls: Optional[bool]
    change_info: Optional[bool]
    invite_users: Optional[bool]
    pin_messages: Optional[bool]
    manage_topics: Optional[bool]
    send_photos: Optional[bool]
    send_videos: Optional[bool]
    send_roundvideos: Optional[bool]
    send_audios: Optional[bool]
    send_voices: Optional[bool]
    send_docs: Optional[bool]
    send_plain: Optional[bool]
    until_date: Optional[int]

class ChatOnlines(TLObject):
    CONSTRUCTOR_ID = 0xF041E250
    FIELDS = [TLField("onlines", "int")]
    onlines: Optional[int]

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
    revoked: Optional[bool]
    permanent: Optional[bool]
    request_needed: Optional[bool]
    link: Optional[str]
    links: Optional[List[str]]
    admin_id: Optional[int]
    date: Optional[int]
    start_date: Optional[int]
    expire_date: Optional[int]
    usage_limit: Optional[int]
    usage: Optional[int]
    requested: Optional[int]
    title: Optional[str]

class ChatInvitePublicJoinRequests(TLObject):
    CONSTRUCTOR_ID = 0xED107AB7
    FIELDS = []

class ChatInviteAlready(TLObject):
    CONSTRUCTOR_ID = 0x5A686D7C
    FIELDS = [TLField("chat", "Chat")]
    chat: Optional[TLObject]

class ChatInvite(TLObject):
    CONSTRUCTOR_ID = 0xCDE0EC40
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("channel", "true", flag_group=0, flag_bit=0),
        TLField("broadcast", "true", flag_group=0, flag_bit=1),
        TLField("public", "true", flag_group=0, flag_bit=2),
        TLField("megagroup", "true", flag_group=0, flag_bit=3),
        TLField("request_needed", "true", flag_group=0, flag_bit=6),
        TLField("verified", "true", flag_group=0, flag_bit=7),
        TLField("scam", "true", flag_group=0, flag_bit=8),
        TLField("fake", "true", flag_group=0, flag_bit=9),
        TLField("title", "string"),
        TLField("about", "string", flag_group=0, flag_bit=5),
        TLField("photo", "Photo"),
        TLField("participants_count", "int"),
        TLField("participants", "User", flag_group=0, flag_bit=4, is_vector=True),
        TLField("color", "int"),
    ]
    channel: Optional[bool]
    broadcast: Optional[bool]
    public: Optional[bool]
    megagroup: Optional[bool]
    request_needed: Optional[bool]
    verified: Optional[bool]
    scam: Optional[bool]
    fake: Optional[bool]
    title: Optional[str]
    about: Optional[str]
    photo: Optional[TLObject]
    participants_count: Optional[int]
    participants: Optional[List[TLObject]]
    color: Optional[int]

class ChatInvitePeek(TLObject):
    CONSTRUCTOR_ID = 0x61695CB0
    FIELDS = [
        TLField("chat", "Chat"),
        TLField("expires", "int"),
    ]
    chat: Optional[TLObject]
    expires: Optional[int]

class ChatInviteImporter(TLObject):
    CONSTRUCTOR_ID = 0x8C5ADFD9
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("requested", "true", flag_group=0, flag_bit=0),
        TLField("via_chatlist", "true", flag_group=0, flag_bit=3),
        TLField("user_id", "long"),
        TLField("date", "int"),
        TLField("about", "string", flag_group=0, flag_bit=2),
        TLField("approved_by", "long", flag_group=0, flag_bit=1),
    ]
    requested: Optional[bool]
    via_chatlist: Optional[bool]
    user_id: Optional[int]
    date: Optional[int]
    about: Optional[str]
    approved_by: Optional[int]

class ChatAdminWithInvites(TLObject):
    CONSTRUCTOR_ID = 0xF2ECEF23
    FIELDS = [
        TLField("admin_id", "long"),
        TLField("invites_count", "int"),
        TLField("revoked_invites_count", "int"),
    ]
    admin_id: Optional[int]
    invites_count: Optional[int]
    revoked_invites_count: Optional[int]

class ChatTheme(TLObject):
    CONSTRUCTOR_ID = 0xC3DFFC04
    FIELDS = [TLField("emoticon", "string")]
    emoticon: Optional[str]

class ChatThemeUniqueGift(TLObject):
    CONSTRUCTOR_ID = 0x3458F9C8
    FIELDS = [
        TLField("gift", "StarGift"),
        TLField("theme_settings", "ThemeSettings", is_vector=True),
    ]
    gift: Optional[TLObject]
    theme_settings: Optional[List[TLObject]]

class ChannelLocation(TLObject):
    CONSTRUCTOR_ID = 0x209B82DB
    FIELDS = [
        TLField("geo_point", "GeoPoint"),
        TLField("address", "string"),
    ]
    geo_point: Optional[TLObject]
    address: Optional[str]

class ChannelLocationEmpty(TLObject):
    CONSTRUCTOR_ID = 0xBFB5AD8B
    FIELDS = []