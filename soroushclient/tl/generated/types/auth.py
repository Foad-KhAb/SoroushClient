from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from soroushclient.tl.base import TLField, TLObject

if TYPE_CHECKING:
    from soroushclient.tl.generated import User


class CodeSettings(TLObject):
    CONSTRUCTOR_ID = 0xAD253D78
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("allow_flashcall", "true", flag_group=0, flag_bit=0),
        TLField("current_number", "true", flag_group=0, flag_bit=1),
        TLField("allow_app_hash", "true", flag_group=0, flag_bit=4),
        TLField("allow_missed_call", "true", flag_group=0, flag_bit=5),
        TLField("logout_tokens", "bytes", flag_group=0, flag_bit=6, is_vector=True),
        TLField("allow_firebase", "true", flag_group=0, flag_bit=7),
        TLField("token", "string", flag_group=0, flag_bit=8),
        TLField("app_sandbox", "bool", flag_group=0, flag_bit=8),
    ]
    allow_flashcall: Optional[bool]
    current_number: Optional[bool]
    allow_app_hash: Optional[bool]
    allow_missed_call: Optional[bool]
    logout_tokens: Optional[bytes]
    allow_firebase: Optional[bool]
    token: Optional[bytes]
    app_sandbox: Optional[bool]


class SentCodeTypeApp(TLObject):
    CONSTRUCTOR_ID = 0x3DBB5986
    FIELDS = [TLField("length", "int")]
    length: int


class SentCodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 0xC000BBA2
    FIELDS = [TLField("length", "int")]
    length: int


class SentCodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 0x5353E5A7
    FIELDS = [TLField("length", "int")]
    length: int


class SentCodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 0xAB03C6D9
    FIELDS = [TLField("pattern", "string")]
    pattern: str


class SentCode(TLObject):
    CONSTRUCTOR_ID = 0x5E002502
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("type", "SentCodeType"),
        TLField("phone_code_hash", "bytes"),
        TLField("next_type", "int", flag_group=0, flag_bit=1),
        TLField("timeout", "int", flag_group=0, flag_bit=2),
    ]
    type: Optional[int]
    phone_code_hash: Optional[bytes]
    next_type: Optional[int]
    timeout: Optional[int]


class Authorization(TLObject):
    CONSTRUCTOR_ID = 0x2EA2C0D4
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("setup_password_required", "true", flag_group=0, flag_bit=1),
        TLField("otherwise_relogin_days", "int", flag_group=0, flag_bit=1),
        TLField("tmp_sessions", "int", flag_group=0, flag_bit=0),
        TLField("future_auth_token", "bytes", flag_group=0, flag_bit=2),
        TLField("user", "User"),
    ]
    setup_password_required: Optional[bool]
    otherwise_relogin_days: Optional[int]
    tmp_sessions: Optional[int]
    future_auth_token: Optional[bytes]
    user: Optional[User]


class AuthorizationSignUpRequired(TLObject):
    CONSTRUCTOR_ID = 0x44747E9A
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("terms_of_service", "TermsOfService", flag_group=0, flag_bit=0),
    ]
class AuthCodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 0x72A3158C
    FIELDS = []


class AuthCodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 0x741CD3E3
    FIELDS = []


class AuthCodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 0x226CCEFB
    FIELDS = []


class AuthCodeTypeMissedCall(TLObject):
    CONSTRUCTOR_ID = 0xD61AD6EE
    FIELDS = []


class AuthCodeTypeFragmentSms(TLObject):
    CONSTRUCTOR_ID = 0x06ED998C
    FIELDS = []


class AuthSentCodeTypeApp(TLObject):
    CONSTRUCTOR_ID = 0x3DBB5986
    FIELDS = [
        TLField("length", "int"),
    ]

    length: Optional[int]


class AuthSentCodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 0xC000BBA2
    FIELDS = [
        TLField("length", "int"),
    ]

    length: Optional[int]


class AuthSentCodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 0x5353E5A7
    FIELDS = [
        TLField("length", "int"),
    ]

    length: Optional[int]


class AuthSentCodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 0xAB03C6D9
    FIELDS = [
        TLField("pattern", "string"),
    ]

    pattern: Optional[str]


class AuthSentCodeTypeMissedCall(TLObject):
    CONSTRUCTOR_ID = 0x82006484
    FIELDS = [
        TLField("prefix", "string"),
        TLField("length", "int"),
    ]

    prefix: Optional[str]
    length: Optional[int]


class AuthSentCodeTypeEmailCode(TLObject):
    CONSTRUCTOR_ID = 0xF450235F
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


class AuthSentCodeTypeSetUpEmailRequired(TLObject):
    CONSTRUCTOR_ID = 0xA5491DEA
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("apple_signin_allowed", "true", flag_group=0, flag_bit=0),
        TLField("google_signin_allowed", "true", flag_group=0, flag_bit=1),
    ]

    apple_signin_allowed: Optional[bool]
    google_signin_allowed: Optional[bool]


class AuthSentCodeTypeFragmentSms(TLObject):
    CONSTRUCTOR_ID = 0xD9565C39
    FIELDS = [
        TLField("url", "string"),
        TLField("length", "int"),
    ]

    url: Optional[str]
    length: Optional[int]


class AuthSentCodeTypeFirebaseSms(TLObject):
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


class MessagesBotCallbackAnswer(TLObject):
    CONSTRUCTOR_ID = 0x36585EA4
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("alert", "true", flag_group=0, flag_bit=1),
        TLField("has_url", "true", flag_group=0, flag_bit=3),
        TLField("native_ui", "true", flag_group=0, flag_bit=4),
        TLField("message", "string", flag_group=0, flag_bit=0),
        TLField("url", "string", flag_group=0, flag_bit=2),
        TLField("cache_time", "int"),
    ]

    alert: Optional[bool]
    has_url: Optional[bool]
    native_ui: Optional[bool]
    message: Optional[str]
    url: Optional[str]
    cache_time: Optional[int]