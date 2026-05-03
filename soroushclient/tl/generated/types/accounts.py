from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class AccountDaysTTL(TLObject):
    CONSTRUCTOR_ID = 0xB8D0AFDF
    FIELDS = [TLField("days", "int")]
    days: Optional[int]

class AccountAuthorizations(TLObject):
    CONSTRUCTOR_ID = 0x4BFF8EA0
    FIELDS = [
        TLField("authorization_ttl_days", "int"),
        TLField("authorizations", "Authorization", is_vector=True),
    ]
    authorization_ttl_days: Optional[int]
    authorizations: Optional[List[TLObject]]

class AccountPassword(TLObject):
    CONSTRUCTOR_ID = 0x957B50FB
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("has_recovery", "true", flag_group=0, flag_bit=0),
        TLField("has_secure_values", "true", flag_group=0, flag_bit=1),
        TLField("has_password", "true", flag_group=0, flag_bit=2),
        TLField("current_algo", "PasswordKdfAlgo", flag_group=0, flag_bit=2),
        TLField("srp_B", "bytes", flag_group=0, flag_bit=2),
        TLField("srp_id", "long", flag_group=0, flag_bit=2),
        TLField("hint", "string", flag_group=0, flag_bit=3),
        TLField("email_unconfirmed_pattern", "string", flag_group=0, flag_bit=4),
        TLField("new_algo", "PasswordKdfAlgo"),
        TLField("new_secure_algo", "SecurePasswordKdfAlgo"),
        TLField("secure_random", "bytes"),
        TLField("pending_reset_date", "int", flag_group=0, flag_bit=5),
        TLField("login_email_pattern", "string", flag_group=0, flag_bit=6),
    ]
    has_recovery: Optional[bool]
    has_secure_values: Optional[bool]
    has_password: Optional[bool]
    current_algo: Optional[TLObject]
    srp_B: Optional[bytes]
    srp_id: Optional[int]
    hint: Optional[str]
    email_unconfirmed_pattern: Optional[str]
    new_algo: Optional[TLObject]
    new_secure_algo: Optional[TLObject]
    secure_random: Optional[bytes]
    pending_reset_date: Optional[int]
    login_email_pattern: Optional[str]

class AccountPasswordSettings(TLObject):
    CONSTRUCTOR_ID = 0x9A5C33E5
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("email", "string", flag_group=0, flag_bit=0),
        TLField("secure_settings", "SecureSecretSettings", flag_group=0, flag_bit=1),
    ]
    email: Optional[str]
    secure_settings: Optional[TLObject]

class AccountPasswordInputSettings(TLObject):
    CONSTRUCTOR_ID = 0xC23727C9
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("new_algo", "PasswordKdfAlgo", flag_group=0, flag_bit=0),
        TLField("new_password_hash", "bytes", flag_group=0, flag_bit=0),
        TLField("hint", "string", flag_group=0, flag_bit=0),
        TLField("email", "string", flag_group=0, flag_bit=1),
        TLField("new_secure_settings", "SecureSecretSettings", flag_group=0, flag_bit=2),
    ]
    new_algo: Optional[TLObject]
    new_password_hash: Optional[bytes]
    hint: Optional[str]
    email: Optional[str]
    new_secure_settings: Optional[TLObject]

class AccountTmpPassword(TLObject):
    CONSTRUCTOR_ID = 0xDB64FD34
    FIELDS = [
        TLField("tmp_password", "bytes"),
        TLField("valid_until", "int"),
    ]
    tmp_password: Optional[bytes]
    valid_until: Optional[int]

class AccountWebAuthorizations(TLObject):
    CONSTRUCTOR_ID = 0xED56C9FC
    FIELDS = [
        TLField("authorizations", "WebAuthorization", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    authorizations: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class AccountContentSettings(TLObject):
    CONSTRUCTOR_ID = 0x57E28221
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("sensitive_enabled", "true", flag_group=0, flag_bit=0),
        TLField("sensitive_can_change", "true", flag_group=0, flag_bit=1),
    ]
    sensitive_enabled: Optional[bool]
    sensitive_can_change: Optional[bool]

class AccountAutoDownloadSettings(TLObject):
    CONSTRUCTOR_ID = 0x63CACF26
    FIELDS = [
        TLField("low", "AutoDownloadSettings"),
        TLField("medium", "AutoDownloadSettings"),
        TLField("high", "AutoDownloadSettings"),
    ]
    low: Optional[TLObject]
    medium: Optional[TLObject]
    high: Optional[TLObject]

class AccountAutoSaveSettings(TLObject):
    CONSTRUCTOR_ID = 0x4C3E069D
    FIELDS = [
        TLField("users_settings", "AutoSaveSettings"),
        TLField("chats_settings", "AutoSaveSettings"),
        TLField("broadcasts_settings", "AutoSaveSettings"),
        TLField("exceptions", "AutoSaveException", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    users_settings: Optional[TLObject]
    chats_settings: Optional[TLObject]
    broadcasts_settings: Optional[TLObject]
    exceptions: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class AccountWallPapersNotModified(TLObject):
    CONSTRUCTOR_ID = 0x1C199183
    FIELDS = []

class AccountWallPapers(TLObject):
    CONSTRUCTOR_ID = 0xCDC3858C
    FIELDS = [
        TLField("hash", "long"),
        TLField("wallpapers", "WallPaper", is_vector=True),
    ]
    hash: Optional[int]
    wallpapers: Optional[List[TLObject]]

class AccountThemesNotModified(TLObject):
    CONSTRUCTOR_ID = 0xF41EB622
    FIELDS = []

class AccountThemes(TLObject):
    CONSTRUCTOR_ID = 0x9A3D8C6D
    FIELDS = [
        TLField("hash", "long"),
        TLField("themes", "Theme", is_vector=True),
    ]
    hash: Optional[int]
    themes: Optional[List[TLObject]]

class AccountEmojiStatusesNotModified(TLObject):
    CONSTRUCTOR_ID = 0xD08CE645
    FIELDS = []

class AccountEmojiStatuses(TLObject):
    CONSTRUCTOR_ID = 0x90C467D1
    FIELDS = [
        TLField("hash", "long"),
        TLField("statuses", "EmojiStatus", is_vector=True),
    ]
    hash: Optional[int]
    statuses: Optional[List[TLObject]]

class AccountSavedRingtonesNotModified(TLObject):
    CONSTRUCTOR_ID = 0xFBF6E8B1
    FIELDS = []

class AccountSavedRingtones(TLObject):
    CONSTRUCTOR_ID = 0xC1E92CC5
    FIELDS = [
        TLField("hash", "long"),
        TLField("ringtones", "Document", is_vector=True),
    ]
    hash: Optional[int]
    ringtones: Optional[List[TLObject]]

class AccountSavedRingtone(TLObject):
    CONSTRUCTOR_ID = 0xB7263F6D
    FIELDS = []

class AccountSavedRingtoneConverted(TLObject):
    CONSTRUCTOR_ID = 0x1F307EB7
    FIELDS = [TLField("document", "Document")]
    document: Optional[TLObject]

class AccountResetPasswordFailedWait(TLObject):
    CONSTRUCTOR_ID = 0xE3779861
    FIELDS = [TLField("retry_date", "int")]
    retry_date: Optional[int]

class AccountResetPasswordRequestedWait(TLObject):
    CONSTRUCTOR_ID = 0xE9EFFC7D
    FIELDS = [TLField("until_date", "int")]
    until_date: Optional[int]

class AccountResetPasswordOk(TLObject):
    CONSTRUCTOR_ID = 0xE926D63E
    FIELDS = []

class AccountTakeout(TLObject):
    CONSTRUCTOR_ID = 0x4DBA4501
    FIELDS = [TLField("id", "long")]
    id: Optional[int]

class AccountSentEmailCode(TLObject):
    CONSTRUCTOR_ID = 0x811F854F
    FIELDS = [
        TLField("email_pattern", "string"),
        TLField("length", "int"),
    ]
    email_pattern: Optional[str]
    length: Optional[int]

class AccountEmailVerified(TLObject):
    CONSTRUCTOR_ID = 0x2B96CD1B
    FIELDS = [TLField("email", "string")]
    email: Optional[str]

class AccountEmailVerifiedLogin(TLObject):
    CONSTRUCTOR_ID = 0xE1BB0D61
    FIELDS = [
        TLField("email", "string"),
        TLField("sent_code", "auth.SentCode"),
    ]
    email: Optional[str]
    sent_code: Optional[TLObject]

class AccountSavedMusicIdsNotModified(TLObject):
    CONSTRUCTOR_ID = 0x4FC81D6E
    FIELDS = []

class AccountSavedMusicIds(TLObject):
    CONSTRUCTOR_ID = 0x998D6636
    FIELDS = [TLField("ids", "long", is_vector=True)]
    ids: Optional[List[int]]

class AccountAuthorizationForm(TLObject):
    CONSTRUCTOR_ID = 0xAD2E1CD8
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("required_types", "SecureRequiredType", is_vector=True),
        TLField("values", "SecureValue", is_vector=True),
        TLField("errors", "SecureValueError", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("privacy_policy_url", "string", flag_group=0, flag_bit=0),
    ]
    required_types: Optional[List[TLObject]]
    values: Optional[List[TLObject]]
    errors: Optional[List[TLObject]]
    users: Optional[List[TLObject]]
    privacy_policy_url: Optional[str]