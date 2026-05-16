from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from soroushclient.tl.generated import Chat

if TYPE_CHECKING:
    from soroushclient.tl.generated.types.inputs import InputChannel

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


class ChatEmpty(Chat):
    CONSTRUCTOR_ID = 0x29562865
    FIELDS = [
        TLField("id", "long", skip_cid=True),
    ]

    id: Optional[int]


class GroupChat(Chat):
    CONSTRUCTOR_ID = 0x41CBF256
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("creator", "true", flag_group=1, flag_bit=0),
        TLField("left", "true", flag_group=1, flag_bit=2),
        TLField("deactivated", "true", flag_group=1, flag_bit=5),
        TLField("call_active", "true", flag_group=1, flag_bit=23),
        TLField("call_not_empty", "true", flag_group=1, flag_bit=24),
        TLField("noforwards", "true", flag_group=1, flag_bit=25),
        TLField("id", "long", skip_cid=True),
        TLField("title", "string", skip_cid=True),
        TLField("photo", "ChatPhoto"),
        TLField("participants_count", "int", skip_cid=True),
        TLField("date", "int", skip_cid=True),
        TLField("version", "int", skip_cid=True),
        TLField("migrated_to", "InputChannel", flag_group=1, flag_bit=6),
        TLField("admin_rights", "ChatAdminRights", flag_group=1, flag_bit=14),
        TLField("default_banned_rights", "ChatBannedRights", flag_group=1, flag_bit=18),
    ]

    creator: Optional[bool]
    left: Optional[bool]
    deactivated: Optional[bool]
    call_active: Optional[bool]
    call_not_empty: Optional[bool]
    noforwards: Optional[bool]
    id: Optional[int]
    title: Optional[str]
    photo: Optional[ChatPhoto]
    participants_count: Optional[int]
    date: Optional[int]
    version: Optional[int]
    migrated_to: Optional[InputChannel]
    admin_rights: Optional[ChatAdminRights]
    default_banned_rights: Optional[ChatBannedRights]


class ChatForbidden(Chat):
    CONSTRUCTOR_ID = 0x6592A1A7  # 1704108455
    FIELDS = [
        TLField("id", "long", skip_cid=True),
        TLField("title", "string", skip_cid=True),
    ]

    id: Optional[int]
    title: Optional[str]


class RestrictionReason(TLObject):
    CONSTRUCTOR_ID = 0xD072ACB4
    FIELDS = [
        TLField("platform", "string", skip_cid=True),
        TLField("reason", "string", skip_cid=True),
        TLField("text", "string", skip_cid=True),
    ]

    platform: Optional[str]
    reason: Optional[str]
    text: Optional[str]
