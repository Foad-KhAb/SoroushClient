from soroushclient.tl.base import TLObject, TLField


class UserProfilePhotoEmpty(TLObject):
    CONSTRUCTOR_ID = 0x4f11bae1
    FIELDS = []
class UserProfilePhoto(TLObject):
    CONSTRUCTOR_ID = 0x82d1f706
    FIELDS = [
        TLField("flags",         "int",   flag_group=0, flag_indicator=True),
        TLField("has_video",     "true",  flag_group=0, flag_bit=0),
        TLField("personal",      "true",  flag_group=0, flag_bit=2),
        TLField("photo_id",      "long"),
        TLField("stripped_thumb","bytes", flag_group=0, flag_bit=1),
        TLField("dc_id",         "int"),
    ]
class UserDeleted(TLObject):
    CONSTRUCTOR_ID = 0x00000007
    FIELDS = []
class UserStatusEmpty(TLObject):
    CONSTRUCTOR_ID = 0x09d05049
    FIELDS = []

class UserStatusOnline(TLObject):
    CONSTRUCTOR_ID = 0xedb93949
    FIELDS = [TLField("expires", "int")]

class UserStatusOffline(TLObject):
    CONSTRUCTOR_ID = 0x008c703f
    FIELDS = [TLField("was_online", "int")]

class UserStatusRecently(TLObject):
    CONSTRUCTOR_ID = 0xe26f42f1
    FIELDS = []

class UserStatusLastWeek(TLObject):
    CONSTRUCTOR_ID = 0x07bf09fc
    FIELDS = []

class UserStatusLastMonth(TLObject):
    CONSTRUCTOR_ID = 0x77ebc742
    FIELDS = []

class UserTypeNormal(TLObject):
    CONSTRUCTOR_ID = 0xec35854d
    FIELDS = []

class UserTypeNotify(TLObject):
    CONSTRUCTOR_ID = 0x3eab4210
    FIELDS = []

class UserTypeBusiness(TLObject):
    CONSTRUCTOR_ID = 0xbb40bf2e
    FIELDS = []

class UserTypeMxb(TLObject):
    CONSTRUCTOR_ID = 0x35168d6a
    FIELDS = [TLField("im_code", "string")]

class UserTypeUnknown(TLObject):
    CONSTRUCTOR_ID = 0xd4d0613d
    FIELDS = []

class UserTypeNormal2(TLObject):
    """userTypeNormal soroush variant"""
    CONSTRUCTOR_ID = 0x69d5776a
    FIELDS = []
class UserEmpty(TLObject):
    CONSTRUCTOR_ID = 0xd3bc4b7a
    FIELDS = [TLField("id", "long")]

class User(TLObject):
    CONSTRUCTOR_ID = 0x274db727
    FIELDS = [
        TLField("flags",                  "int",    flag_group=0, flag_indicator=True),
        TLField("flags2",                 "int",    flag_group=1, flag_indicator=True),
        TLField("id",                     "long"),
        TLField("access_hash",            "long",   flag_group=0, flag_bit=0),
        TLField("first_name",             "string", flag_group=0, flag_bit=1),
        TLField("last_name",              "string", flag_group=0, flag_bit=2),
        TLField("username",               "string", flag_group=0, flag_bit=3),
        TLField("phone",                  "string", flag_group=0, flag_bit=4),
        TLField("photo",                  "UserProfilePhoto", flag_group=0, flag_bit=5),
        TLField("status",                 "UserStatus",       flag_group=0, flag_bit=6),
        TLField("bot_info_version",       "int",    flag_group=0, flag_bit=14),
        TLField("restriction_reason",     "RestrictionReason", flag_group=0, flag_bit=18, is_vector=True),
        TLField("bot_inline_placeholder", "string", flag_group=0, flag_bit=19),
        TLField("lang_code",              "string", flag_group=0, flag_bit=22),
        TLField("emoji_status",           "EmojiStatus", flag_group=0, flag_bit=30),
        TLField("usernames",              "Username",    flag_group=1, flag_bit=0, is_vector=True),
        TLField("stories_max_id",         "int",    flag_group=1, flag_bit=5),
        TLField("color",                  "PeerColor",   flag_group=1, flag_bit=8),
        TLField("profile_color",          "PeerColor",   flag_group=1, flag_bit=9),
        TLField("user_type",              "UserType"),
        TLField("self_",                  "true",   flag_group=0, flag_bit=10),
        TLField("contact",                "true",   flag_group=0, flag_bit=11),
        TLField("mutual_contact",         "true",   flag_group=0, flag_bit=12),
        TLField("deleted",                "true",   flag_group=0, flag_bit=13),
        TLField("bot",                    "true",   flag_group=0, flag_bit=14),
        TLField("verified",               "true",   flag_group=0, flag_bit=17),
        TLField("restricted",             "true",   flag_group=0, flag_bit=18),
        TLField("scam",                   "true",   flag_group=0, flag_bit=24),
        TLField("fake",                   "true",   flag_group=0, flag_bit=26),
        TLField("premium",                "true",   flag_group=0, flag_bit=28),
        TLField("bot_can_edit",           "true",   flag_group=1, flag_bit=1),
        TLField("close_friend",           "true",   flag_group=1, flag_bit=2),
        TLField("stories_hidden",         "true",   flag_group=1, flag_bit=3),
        TLField("stories_unavailable",    "true",   flag_group=1, flag_bit=4),
    ]
