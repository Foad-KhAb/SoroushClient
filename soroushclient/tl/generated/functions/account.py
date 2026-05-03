from typing import Optional, List

from soroushclient.tl.base import TLRequest, TLField, TLObject


class UpdateProfile(TLRequest):
    CONSTRUCTOR_ID = 0x78515775
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("first_name", "string", flag_group=0, flag_bit=0),
        TLField("last_name", "string", flag_group=0, flag_bit=1),
        TLField("about", "string", flag_group=0, flag_bit=2),
    ]
    first_name: Optional[str]
    last_name: Optional[str]
    about: Optional[str]

class UpdateStatus(TLRequest):
    CONSTRUCTOR_ID = 0x6628562C
    FIELDS = [TLField("offline", "Bool")]
    offline: Optional[bool]

class GetWallPapers(TLRequest):
    CONSTRUCTOR_ID = 0x07967D36
    FIELDS = [TLField("hash", "long")]
    hash: Optional[int]

class ReportPeer(TLRequest):
    CONSTRUCTOR_ID = 0xC5BA3D86
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("reason", "ReportReason"),
        TLField("message", "string"),
    ]
    peer: Optional[TLObject]
    reason: Optional[TLObject]
    message: Optional[str]

class CheckUsername(TLRequest):
    CONSTRUCTOR_ID = 0x2714D86C
    FIELDS = [TLField("username", "string")]
    username: Optional[str]

class UpdateUsername(TLRequest):
    CONSTRUCTOR_ID = 0x3E0BDD7C
    FIELDS = [TLField("username", "string")]
    username: Optional[str]

class GetPrivacy(TLRequest):
    CONSTRUCTOR_ID = 0xDADBC950
    FIELDS = [TLField("key", "InputPrivacyKey")]
    key: Optional[TLObject]

class SetPrivacy(TLRequest):
    CONSTRUCTOR_ID = 0xC9F81CE8
    FIELDS = [
        TLField("key", "InputPrivacyKey"),
        TLField("rules", "InputPrivacyRule", is_vector=True),
    ]
    key: Optional[TLObject]
    rules: Optional[List[TLObject]]

class GetAuthorizations(TLRequest):
    CONSTRUCTOR_ID = 0xE320C158
    FIELDS = []

class ResetAuthorization(TLRequest):
    CONSTRUCTOR_ID = 0xDF77F3BC
    FIELDS = [TLField("hash", "long")]
    hash: Optional[int]

class GetPassword(TLRequest):
    CONSTRUCTOR_ID = 0x548A30F5
    FIELDS = []

class GetPasswordSettings(TLRequest):
    CONSTRUCTOR_ID = 0x9CD4EAF9
    FIELDS = [TLField("password", "InputCheckPasswordSRP")]
    password: Optional[TLObject]

class UpdatePasswordSettings(TLRequest):
    CONSTRUCTOR_ID = 0xA59B102F
    FIELDS = [
        TLField("password", "InputCheckPasswordSRP"),
        TLField("new_settings", "account.PasswordInputSettings"),
    ]
    password: Optional[TLObject]
    new_settings: Optional[TLObject]

class GetNotifySettings(TLRequest):
    CONSTRUCTOR_ID = 0x12B3AD31
    FIELDS = [TLField("peer", "InputNotifyPeer")]
    peer: Optional[TLObject]

class UpdateNotifySettings(TLRequest):
    CONSTRUCTOR_ID = 0x84BE5B93
    FIELDS = [
        TLField("peer", "InputNotifyPeer"),
        TLField("settings", "InputPeerNotifySettings"),
    ]
    peer: Optional[TLObject]
    settings: Optional[TLObject]

class GetNotifyExceptions(TLRequest):
    CONSTRUCTOR_ID = 0x53577479
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("compare_sound", "true", flag_group=0, flag_bit=1),
        TLField("compare_stories", "true", flag_group=0, flag_bit=2),
        TLField("peer", "InputNotifyPeer", flag_group=0, flag_bit=0),
    ]
    compare_sound: Optional[bool]
    compare_stories: Optional[bool]
    peer: Optional[TLObject]

class UpdateEmojiStatus(TLRequest):
    CONSTRUCTOR_ID = 0xFBD3DE6B
    FIELDS = [TLField("emoji_status", "EmojiStatus")]
    emoji_status: Optional[TLObject]

class GetRecentEmojiStatuses(TLRequest):
    CONSTRUCTOR_ID = 0x0F578105
    FIELDS = [TLField("hash", "long")]
    hash: Optional[int]

class ReorderUsernames(TLRequest):
    CONSTRUCTOR_ID = 0xEF500EAB
    FIELDS = [TLField("order", "string", is_vector=True)]
    order: Optional[List[str]]

class ToggleUsername(TLRequest):
    CONSTRUCTOR_ID = 0x58D6B376
    FIELDS = [
        TLField("username", "string"),
        TLField("active", "Bool"),
    ]
    username: Optional[str]
    active: Optional[bool]

class UpdateGender(TLRequest):
    CONSTRUCTOR_ID = 0x7374F514
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("gender", "Gender", flag_group=0, flag_bit=0),
    ]
    gender: Optional[TLObject]

class GetGlobalPrivacySettings(TLRequest):
    CONSTRUCTOR_ID = 0xEB2B4CF6
    FIELDS = []

class SetGlobalPrivacySettings(TLRequest):
    CONSTRUCTOR_ID = 0x1EDAAAC2
    FIELDS = [TLField("settings", "GlobalPrivacySettings")]
    settings: Optional[TLObject]

class SetAuthorizationTTL(TLRequest):
    CONSTRUCTOR_ID = 0xBF899AA0
    FIELDS = [TLField("authorization_ttl_days", "int")]
    authorization_ttl_days: Optional[int]

class ChangeAuthorizationSettings(TLRequest):
    CONSTRUCTOR_ID = 0x40F48462
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("confirmed", "true", flag_group=0, flag_bit=3),
        TLField("hash", "long"),
        TLField("encrypted_requests_disabled", "Bool", flag_group=0, flag_bit=0),
        TLField("call_requests_disabled", "Bool", flag_group=0, flag_bit=1),
    ]
    confirmed: Optional[bool]
    hash: Optional[int]
    encrypted_requests_disabled: Optional[bool]
    call_requests_disabled: Optional[bool]

class UpdateBirthday(TLRequest):
    CONSTRUCTOR_ID = 0xCC6E0C11
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("birthday", "Birthday", flag_group=0, flag_bit=0),
    ]
    birthday: Optional[TLObject]

class SaveMusic(TLRequest):
    CONSTRUCTOR_ID = 0xB26732A9
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("unsave", "true", flag_group=0, flag_bit=0),
        TLField("id", "InputDocument"),
        TLField("after_id", "InputDocument", flag_group=0, flag_bit=1),
    ]
    unsave: Optional[bool]
    id: Optional[TLObject]
    after_id: Optional[TLObject]

class SetMainProfileTab(TLRequest):
    CONSTRUCTOR_ID = 0x5DEE78B0
    FIELDS = [TLField("tab", "ProfileTab")]
    tab: Optional[TLObject]

class GetSavedMusicIds(TLRequest):
    CONSTRUCTOR_ID = 0xE09D5FAF
    FIELDS = [TLField("hash", "long")]
    hash: Optional[int]

class UpdatePersonalChannel(TLRequest):
    CONSTRUCTOR_ID = 0xD94305E0
    FIELDS = [TLField("channel", "InputChannel")]
    channel: Optional[TLObject]

class UpdateBusinessWorkHours(TLRequest):
    CONSTRUCTOR_ID = 0x4B00E066
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("business_work_hours", "BusinessWorkHours", flag_group=0, flag_bit=0),
    ]
    business_work_hours: Optional[TLObject]