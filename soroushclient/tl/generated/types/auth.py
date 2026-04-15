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
