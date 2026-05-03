from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class UserTypeNormal(TLObject):
    CONSTRUCTOR_ID = 0xEC35854D
    FIELDS = []

class UserTypeNotify(TLObject):
    CONSTRUCTOR_ID = 0x3EAB4210
    FIELDS = []

class UserTypeBusiness(TLObject):
    CONSTRUCTOR_ID = 0xBB40BF2E
    FIELDS = []

class UserTypeMxb(TLObject):
    CONSTRUCTOR_ID = 0x35168D6A
    FIELDS = [TLField("im_code", "string")]
    im_code: Optional[str]

class UserTypeUnknown(TLObject):
    CONSTRUCTOR_ID = 0xD4D0613D
    FIELDS = []

class UserEmpty(TLObject):
    CONSTRUCTOR_ID = 0xD3BC4B7A
    FIELDS = [TLField("id", "long")]
    id: Optional[int]

class User(TLObject):
    CONSTRUCTOR_ID = 0x274DB727
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("is_self", "true", flag_group=0, flag_bit=10),
        TLField("contact", "true", flag_group=0, flag_bit=11),
        TLField("mutual_contact", "true", flag_group=0, flag_bit=12),
        TLField("deleted", "true", flag_group=0, flag_bit=13),
        TLField("bot", "true", flag_group=0, flag_bit=14),
        TLField("bot_chat_history", "true", flag_group=0, flag_bit=15),
        TLField("bot_nochats", "true", flag_group=0, flag_bit=16),
        TLField("verified", "true", flag_group=0, flag_bit=17),
        TLField("restricted", "true", flag_group=0, flag_bit=18),
        TLField("min", "true", flag_group=0, flag_bit=20),
        TLField("bot_inline_geo", "true", flag_group=0, flag_bit=21),
        TLField("support", "true", flag_group=0, flag_bit=23),
        TLField("scam", "true", flag_group=0, flag_bit=24),
        TLField("apply_min_photo", "true", flag_group=0, flag_bit=25),
        TLField("fake", "true", flag_group=0, flag_bit=26),
        TLField("bot_attach_menu", "true", flag_group=0, flag_bit=27),
        TLField("premium", "true", flag_group=0, flag_bit=28),
        TLField("attach_menu_enabled", "true", flag_group=0, flag_bit=29),
        TLField("flags2", "int", flag_group=1, flag_indicator=True),
        TLField("bot_can_edit", "true", flag_group=1, flag_bit=1),
        TLField("close_friend", "true", flag_group=1, flag_bit=2),
        TLField("stories_hidden", "true", flag_group=1, flag_bit=3),
        TLField("stories_unavailable", "true", flag_group=1, flag_bit=4),
        TLField("id", "long"),
        TLField("access_hash", "long", flag_group=0, flag_bit=0),
        TLField("first_name", "string", flag_group=0, flag_bit=1),
        TLField("last_name", "string", flag_group=0, flag_bit=2),
        TLField("username", "string", flag_group=0, flag_bit=3),
        TLField("phone", "string", flag_group=0, flag_bit=4),
        TLField("photo", "UserProfilePhoto", flag_group=0, flag_bit=5),
        TLField("status", "UserStatus", flag_group=0, flag_bit=6),
        TLField("bot_info_version", "int", flag_group=0, flag_bit=14),
        TLField("restriction_reason", "RestrictionReason", flag_group=0, flag_bit=18, is_vector=True),
        TLField("bot_inline_placeholder", "string", flag_group=0, flag_bit=19),
        TLField("lang_code", "string", flag_group=0, flag_bit=22),
        TLField("emoji_status", "EmojiStatus", flag_group=0, flag_bit=30),
        TLField("usernames", "Username", flag_group=1, flag_bit=0, is_vector=True),
        TLField("stories_max_id", "int", flag_group=1, flag_bit=5),
        TLField("color", "PeerColor", flag_group=1, flag_bit=8),
        TLField("profile_color", "PeerColor", flag_group=1, flag_bit=9),
        TLField("user_type", "UserType"),
    ]
    is_self: Optional[bool]
    contact: Optional[bool]
    mutual_contact: Optional[bool]
    deleted: Optional[bool]
    bot: Optional[bool]
    bot_chat_history: Optional[bool]
    bot_nochats: Optional[bool]
    verified: Optional[bool]
    restricted: Optional[bool]
    min: Optional[bool]
    bot_inline_geo: Optional[bool]
    support: Optional[bool]
    scam: Optional[bool]
    apply_min_photo: Optional[bool]
    fake: Optional[bool]
    bot_attach_menu: Optional[bool]
    premium: Optional[bool]
    attach_menu_enabled: Optional[bool]
    bot_can_edit: Optional[bool]
    close_friend: Optional[bool]
    stories_hidden: Optional[bool]
    stories_unavailable: Optional[bool]
    id: Optional[int]
    access_hash: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    phone: Optional[str]
    photo: Optional[TLObject]
    status: Optional[TLObject]
    bot_info_version: Optional[int]
    restriction_reason: Optional[List[TLObject]]
    bot_inline_placeholder: Optional[str]
    lang_code: Optional[str]
    emoji_status: Optional[TLObject]
    usernames: Optional[List[TLObject]]
    stories_max_id: Optional[int]
    color: Optional[TLObject]
    profile_color: Optional[TLObject]
    user_type: Optional[TLObject]

class UserProfilePhotoEmpty(TLObject):
    CONSTRUCTOR_ID = 0x4F11BAE1
    FIELDS = []

class UserProfilePhoto(TLObject):
    CONSTRUCTOR_ID = 0x82D1F706
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("has_video", "true", flag_group=0, flag_bit=0),
        TLField("personal", "true", flag_group=0, flag_bit=2),
        TLField("photo_id", "long"),
        TLField("stripped_thumb", "bytes", flag_group=0, flag_bit=1),
        TLField("dc_id", "int"),
    ]
    has_video: Optional[bool]
    personal: Optional[bool]
    photo_id: Optional[int]
    stripped_thumb: Optional[bytes]
    dc_id: Optional[int]

class UserStatusEmpty(TLObject):
    CONSTRUCTOR_ID = 0x09D05049
    FIELDS = []

class UserStatusOnline(TLObject):
    CONSTRUCTOR_ID = 0xEDB93949
    FIELDS = [TLField("expires", "int")]
    expires: Optional[int]

class UserStatusOffline(TLObject):
    CONSTRUCTOR_ID = 0x008C703F
    FIELDS = [TLField("was_online", "int")]
    was_online: Optional[int]

class UserStatusRecently(TLObject):
    CONSTRUCTOR_ID = 0xE26F42F1
    FIELDS = []

class UserStatusLastWeek(TLObject):
    CONSTRUCTOR_ID = 0x07BF09FC
    FIELDS = []

class UserStatusLastMonth(TLObject):
    CONSTRUCTOR_ID = 0x77EBC742
    FIELDS = []

class UserFull(TLObject):
    CONSTRUCTOR_ID = 0xC577B5AD
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("blocked", "true", flag_group=0, flag_bit=0),
        TLField("phone_calls_available", "true", flag_group=0, flag_bit=4),
        TLField("phone_calls_private", "true", flag_group=0, flag_bit=5),
        TLField("can_pin_message", "true", flag_group=0, flag_bit=7),
        TLField("has_scheduled", "true", flag_group=0, flag_bit=12),
        TLField("video_calls_available", "true", flag_group=0, flag_bit=13),
        TLField("voice_messages_forbidden", "true", flag_group=0, flag_bit=20),
        TLField("translations_disabled", "true", flag_group=0, flag_bit=23),
        TLField("stories_pinned_available", "true", flag_group=0, flag_bit=26),
        TLField("blocked_my_stories_from", "true", flag_group=0, flag_bit=27),
        TLField("wallpaper_overridden", "true", flag_group=0, flag_bit=28),
        TLField("contact_require_premium", "true", flag_group=0, flag_bit=29),
        TLField("read_dates_private", "true", flag_group=0, flag_bit=30),
        TLField("flags2", "int", flag_group=1, flag_indicator=True),
        TLField("sponsored_enabled", "true", flag_group=1, flag_bit=7),
        TLField("can_view_revenue", "true", flag_group=1, flag_bit=9),
        TLField("bot_can_manage_emoji_status", "true", flag_group=1, flag_bit=10),
        TLField("display_gifts_button", "true", flag_group=1, flag_bit=16),
        TLField("id", "long"),
        TLField("about", "string", flag_group=0, flag_bit=1),
        TLField("settings", "PeerSettings"),
        TLField("personal_photo", "Photo", flag_group=0, flag_bit=21),
        TLField("profile_photo", "Photo", flag_group=0, flag_bit=2),
        TLField("fallback_photo", "Photo", flag_group=0, flag_bit=22),
        TLField("notify_settings", "PeerNotifySettings"),
        TLField("bot_info", "BotInfo", flag_group=0, flag_bit=3),
        TLField("pinned_msg_id", "int", flag_group=0, flag_bit=6),
        TLField("common_chats_count", "int"),
        TLField("folder_id", "int", flag_group=0, flag_bit=11),
        TLField("ttl_period", "int", flag_group=0, flag_bit=14),
        TLField("theme", "ChatTheme", flag_group=0, flag_bit=15),
        TLField("private_forward_name", "string", flag_group=0, flag_bit=16),
        TLField("bot_group_admin_rights", "ChatAdminRights", flag_group=0, flag_bit=17),
        TLField("bot_broadcast_admin_rights", "ChatAdminRights", flag_group=0, flag_bit=18),
        TLField("wallpaper", "WallPaper", flag_group=0, flag_bit=24),
        TLField("stories", "PeerStories", flag_group=0, flag_bit=25),
        TLField("business_work_hours", "BusinessWorkHours", flag_group=1, flag_bit=0),
        TLField("business_location", "BusinessLocation", flag_group=1, flag_bit=1),
        TLField("business_greeting_message", "BusinessGreetingMessage", flag_group=1, flag_bit=2),
        TLField("business_away_message", "BusinessAwayMessage", flag_group=1, flag_bit=3),
        TLField("business_intro", "BusinessIntro", flag_group=1, flag_bit=4),
        TLField("birthday", "Birthday", flag_group=1, flag_bit=5),
        TLField("personal_channel_id", "long", flag_group=1, flag_bit=6),
        TLField("personal_channel_message", "int", flag_group=1, flag_bit=6),
        TLField("stargifts_count", "int", flag_group=1, flag_bit=8),
        TLField("starref_program", "StarRefProgram", flag_group=1, flag_bit=11),
        TLField("bot_verification", "BotVerification", flag_group=1, flag_bit=12),
        TLField("send_paid_messages_stars", "long", flag_group=1, flag_bit=14),
        TLField("disallowed_gifts", "DisallowedGiftsSettings", flag_group=1, flag_bit=15),
        TLField("stars_rating", "StarsRating", flag_group=1, flag_bit=17),
        TLField("stars_my_pending_rating", "StatsRating", flag_group=1, flag_bit=18),
        TLField("stars_my_pending_rating_date", "int", flag_group=1, flag_bit=18),
        TLField("main_tab", "ProfileTab", flag_group=1, flag_bit=20),
        TLField("saved_music", "Document", flag_group=1, flag_bit=21),
    ]
    blocked: Optional[bool]
    phone_calls_available: Optional[bool]
    phone_calls_private: Optional[bool]
    can_pin_message: Optional[bool]
    has_scheduled: Optional[bool]
    video_calls_available: Optional[bool]
    voice_messages_forbidden: Optional[bool]
    translations_disabled: Optional[bool]
    stories_pinned_available: Optional[bool]
    blocked_my_stories_from: Optional[bool]
    wallpaper_overridden: Optional[bool]
    contact_require_premium: Optional[bool]
    read_dates_private: Optional[bool]
    sponsored_enabled: Optional[bool]
    can_view_revenue: Optional[bool]
    bot_can_manage_emoji_status: Optional[bool]
    display_gifts_button: Optional[bool]
    id: Optional[int]
    about: Optional[str]
    settings: Optional[TLObject]
    personal_photo: Optional[TLObject]
    profile_photo: Optional[TLObject]
    fallback_photo: Optional[TLObject]
    notify_settings: Optional[TLObject]
    bot_info: Optional[TLObject]
    pinned_msg_id: Optional[int]
    common_chats_count: Optional[int]
    folder_id: Optional[int]
    ttl_period: Optional[int]
    theme: Optional[TLObject]
    private_forward_name: Optional[str]
    bot_group_admin_rights: Optional[TLObject]
    bot_broadcast_admin_rights: Optional[TLObject]
    wallpaper: Optional[TLObject]
    stories: Optional[TLObject]
    business_work_hours: Optional[TLObject]
    business_location: Optional[TLObject]
    business_greeting_message: Optional[TLObject]
    business_away_message: Optional[TLObject]
    business_intro: Optional[TLObject]
    birthday: Optional[TLObject]
    personal_channel_id: Optional[int]
    personal_channel_message: Optional[int]
    stargifts_count: Optional[int]
    starref_program: Optional[TLObject]
    bot_verification: Optional[TLObject]
    send_paid_messages_stars: Optional[int]
    disallowed_gifts: Optional[TLObject]
    stars_rating: Optional[TLObject]
    stars_my_pending_rating: Optional[TLObject]
    stars_my_pending_rating_date: Optional[int]
    main_tab: Optional[TLObject]
    saved_music: Optional[TLObject]

class UserFullCustom(TLObject):
    CONSTRUCTOR_ID = 0x1828494E
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("gender", "Gender", flag_group=0, flag_bit=0),
    ]
    gender: Optional[TLObject]

class GenderFemale(TLObject):
    CONSTRUCTOR_ID = 0xD6A1F9FF
    FIELDS = []

class GenderMale(TLObject):
    CONSTRUCTOR_ID = 0x5B79DA8A
    FIELDS = []

class Username(TLObject):
    CONSTRUCTOR_ID = 0xB4073647
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("editable", "true", flag_group=0, flag_bit=0),
        TLField("active", "true", flag_group=0, flag_bit=1),
        TLField("username", "string"),
    ]
    editable: Optional[bool]
    active: Optional[bool]
    username: Optional[str]

class Contact(TLObject):
    CONSTRUCTOR_ID = 0x145ADE0B
    FIELDS = [
        TLField("user_id", "long"),
        TLField("mutual", "Bool"),
    ]
    user_id: Optional[int]
    mutual: Optional[bool]

class ImportedContact(TLObject):
    CONSTRUCTOR_ID = 0xC13E3C50
    FIELDS = [
        TLField("user_id", "long"),
        TLField("client_id", "long"),
    ]
    user_id: Optional[int]
    client_id: Optional[int]

class ContactStatus(TLObject):
    CONSTRUCTOR_ID = 0x16D9703B
    FIELDS = [
        TLField("user_id", "long"),
        TLField("status", "UserStatus"),
    ]
    user_id: Optional[int]
    status: Optional[TLObject]

class InputPhoneContact(TLObject):
    CONSTRUCTOR_ID = 0xF392B7F4
    FIELDS = [
        TLField("client_id", "long"),
        TLField("phone", "string"),
        TLField("first_name", "string"),
        TLField("last_name", "string"),
    ]
    client_id: Optional[int]
    phone: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]

class PeerBlocked(TLObject):
    CONSTRUCTOR_ID = 0xE8FD8014
    FIELDS = [
        TLField("peer_id", "Peer"),
        TLField("date", "int"),
    ]
    peer_id: Optional[TLObject]
    date: Optional[int]

class Birthday(TLObject):
    CONSTRUCTOR_ID = 0x6C8E1E06
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("year_hidden", "true", flag_group=0, flag_bit=30),
        TLField("day", "int"),
        TLField("month", "int"),
        TLField("year", "int", flag_group=0, flag_bit=0),
    ]
    year_hidden: Optional[bool]
    day: Optional[int]
    month: Optional[int]
    year: Optional[int]

class ContactBirthday(TLObject):
    CONSTRUCTOR_ID = 0x1D998733
    FIELDS = [
        TLField("contact_id", "long"),
        TLField("birthday", "Birthday"),
    ]
    contact_id: Optional[int]
    birthday: Optional[TLObject]

class ReadParticipantDate(TLObject):
    CONSTRUCTOR_ID = 0x4A4FF172
    FIELDS = [
        TLField("user_id", "long"),
        TLField("date", "int"),
    ]
    user_id: Optional[int]
    date: Optional[int]

class SendAsPeer(TLObject):
    CONSTRUCTOR_ID = 0xB81C7034
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("premium_required", "true", flag_group=0, flag_bit=0),
        TLField("peer", "Peer"),
    ]
    premium_required: Optional[bool]
    peer: Optional[TLObject]