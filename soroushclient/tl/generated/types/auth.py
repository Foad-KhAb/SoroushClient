from typing import Optional

from soroushclient.tl.base import TLObject, TLField


class SentCode(TLObject):
    CONSTRUCTOR_ID = 0x5E002502
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("type", "auth.SentCodeType"),
        TLField("phone_code_hash", "string"),
        TLField("next_type", "auth.CodeType", flag_group=0, flag_bit=1),
        TLField("timeout", "int", flag_group=0, flag_bit=2),
    ]
    type: Optional[TLObject]
    phone_code_hash: Optional[str]
    next_type: Optional[TLObject]
    timeout: Optional[int]

class SentCodeSuccess(TLObject):
    CONSTRUCTOR_ID = 0x2390FE44
    FIELDS = [TLField("authorization", "auth.Authorization")]
    authorization: Optional[TLObject]

class SentDeleteAccountCode(TLObject):
    CONSTRUCTOR_ID = 0x92EAdf91
    FIELDS = [
        TLField("type", "auth.SentCodeType"),
        TLField("timeout", "int"),
    ]
    type: Optional[TLObject]
    timeout: Optional[int]

class Authorization(TLObject):
    CONSTRUCTOR_ID = 0x2EA2C0D4
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("setup_password_required", "true", flag_group=0, flag_bit=1),
        TLField("otherwise_relogin_days", "int", flag_group=0, flag_bit=1, skip_cid=True),
        TLField("tmp_sessions", "int", flag_group=0, flag_bit=0, skip_cid=True),
        TLField("future_auth_token", "bytes", flag_group=0, flag_bit=2, skip_cid=True),
        TLField("user", "User"),
    ]
    setup_password_required: Optional[bool]
    otherwise_relogin_days: Optional[int]
    tmp_sessions: Optional[int]
    future_auth_token: Optional[bytes]
    user: Optional[TLObject]

class AuthorizationSignUpRequired(TLObject):
    CONSTRUCTOR_ID = 0x44747E9A
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("terms_of_service", "help.TermsOfService", flag_group=0, flag_bit=0),
    ]
    terms_of_service: Optional[TLObject]

class ExportedAuthorization(TLObject):
    CONSTRUCTOR_ID = 0xB434E2B8
    FIELDS = [
        TLField("id", "long"),
        TLField("bytes", "bytes"),
    ]
    id: Optional[int]
    bytes: Optional[bytes]

class LoggedOut(TLObject):
    CONSTRUCTOR_ID = 0xC3A2835F
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("future_auth_token", "bytes", flag_group=0, flag_bit=0),
    ]
    future_auth_token: Optional[bytes]

class PasswordRecovery(TLObject):
    CONSTRUCTOR_ID = 0x137948A5
    FIELDS = [TLField("email_pattern", "string")]
    email_pattern: Optional[str]

class LoginToken(TLObject):
    CONSTRUCTOR_ID = 0x629F1980
    FIELDS = [
        TLField("expires", "int"),
        TLField("token", "bytes"),
    ]
    expires: Optional[int]
    token: Optional[bytes]

class LoginTokenMigrateTo(TLObject):
    CONSTRUCTOR_ID = 0x068E9916
    FIELDS = [
        TLField("dc_id", "int"),
        TLField("token", "bytes"),
    ]
    dc_id: Optional[int]
    token: Optional[bytes]

class LoginTokenSuccess(TLObject):
    CONSTRUCTOR_ID = 0x390D5C5E
    FIELDS = [TLField("authorization", "auth.Authorization")]
    authorization: Optional[TLObject]

# Code types
class CodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 0x72A3158C
    FIELDS = []

class CodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 0x741CD3E3
    FIELDS = []

class CodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 0x226CCEFB
    FIELDS = []

class CodeTypeMissedCall(TLObject):
    CONSTRUCTOR_ID = 0xD61AD6EE
    FIELDS = []

class CodeTypeFragmentSms(TLObject):
    CONSTRUCTOR_ID = 0x06ED998C
    FIELDS = []

class SentCodeTypeApp(TLObject):
    CONSTRUCTOR_ID = 0x3DBB5986
    FIELDS = [TLField("length", "int")]
    length: Optional[int]

class SentCodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 0xC000BBA2
    FIELDS = [TLField("length", "int")]
    length: Optional[int]

class SentCodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 0x5353E5A7
    FIELDS = [TLField("length", "int")]
    length: Optional[int]

class SentCodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 0xAB03C6D9
    FIELDS = [TLField("pattern", "string")]
    pattern: Optional[str]

class SentCodeTypeMissedCall(TLObject):
    CONSTRUCTOR_ID = 0x82006484
    FIELDS = [
        TLField("prefix", "string"),
        TLField("length", "int"),
    ]
    prefix: Optional[str]
    length: Optional[int]

class SentCodeTypeEmailCode(TLObject):
    CONSTRUCTOR_ID = 0xF450F59B
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("apple_signin_allowed", "true", flag_group=0, flag_bit=0),
        TLField("google_signin_allowed", "true", flag_group=0, flag_bit=1),
        TLField("email_pattern", "string"),
        TLField("length", "int"),
        TLField("reset_available_period", "int", flag_group=0, flag_bit=3),
        TLField("reset_pending_date", "int", flag_group=0, flag_bit=4),
    ]
    apple_signin_allowed: Optional[bool]
    google_signin_allowed: Optional[bool]
    email_pattern: Optional[str]
    length: Optional[int]
    reset_available_period: Optional[int]
    reset_pending_date: Optional[int]

class SentCodeTypeSetUpEmailRequired(TLObject):
    CONSTRUCTOR_ID = 0xA5491DEA
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("apple_signin_allowed", "true", flag_group=0, flag_bit=0),
        TLField("google_signin_allowed", "true", flag_group=0, flag_bit=1),
    ]
    apple_signin_allowed: Optional[bool]
    google_signin_allowed: Optional[bool]

class SentCodeTypeFragmentSms(TLObject):
    CONSTRUCTOR_ID = 0xD9565C39
    FIELDS = [
        TLField("url", "string"),
        TLField("length", "int"),
    ]
    url: Optional[str]
    length: Optional[int]

class SentCodeTypeFirebaseSms(TLObject):
    CONSTRUCTOR_ID = 0xE57B1432
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("nonce", "bytes", flag_group=0, flag_bit=0),
        TLField("receipt", "string", flag_group=0, flag_bit=1),
        TLField("push_timeout", "int", flag_group=0, flag_bit=1),
        TLField("length", "int"),
    ]
    nonce: Optional[bytes]
    receipt: Optional[str]
    push_timeout: Optional[int]
    length: Optional[int]