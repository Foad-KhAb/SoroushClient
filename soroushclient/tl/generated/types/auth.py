from soroushclient.tl.base import TLObject, TLField


class CodeSettings(TLObject):
    CONSTRUCTOR_ID = 0xad253d78
    FIELDS = [
        TLField("flags",             "int",   flag_group=0, flag_indicator=True),
        TLField("allow_flashcall",   "true",  flag_group=0, flag_bit=0),
        TLField("current_number",    "true",  flag_group=0, flag_bit=1),
        TLField("allow_app_hash",    "true",  flag_group=0, flag_bit=4),
        TLField("allow_missed_call", "true",  flag_group=0, flag_bit=5),
        TLField("logout_tokens",     "bytes", flag_group=0, flag_bit=6, is_vector=True),
        TLField("allow_firebase",    "true",  flag_group=0, flag_bit=7),
        TLField("token",             "string",flag_group=0, flag_bit=8),
        TLField("app_sandbox",       "bool",  flag_group=0, flag_bit=8),
    ]

class SentCodeTypeApp(TLObject):
    CONSTRUCTOR_ID = 0x3dbb5986
    FIELDS = [TLField("length","int")]

class SentCodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 0xc000bba2
    FIELDS = [TLField("length","int")]

class SentCodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 0x5353e5a7
    FIELDS = [TLField("length","int")]

class SentCodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 0xab03c6d9
    FIELDS = [TLField("pattern","string")]
class SentCode(TLObject):
    CONSTRUCTOR_ID = 0x5e002502
    FIELDS = [
        TLField("flags",           "int",  flag_group=0, flag_indicator=True),
        TLField("type",            "SentCodeType"),
        TLField("phone_code_hash", "bytes"),
        TLField("next_type",       "int",  flag_group=0, flag_bit=1),
        TLField("timeout",         "int",  flag_group=0, flag_bit=2),
    ]

class Authorization(TLObject):
    CONSTRUCTOR_ID = 0x2ea2c0d4
    FIELDS = [
        TLField("flags",                   "int",   flag_group=0, flag_indicator=True),
        TLField("setup_password_required", "true",  flag_group=0, flag_bit=1),
        TLField("otherwise_relogin_days",  "int",   flag_group=0, flag_bit=1),
        TLField("tmp_sessions",            "int",   flag_group=0, flag_bit=0),
        TLField("future_auth_token",       "bytes", flag_group=0, flag_bit=2),
        TLField("user",                    "User"),
    ]

class AuthorizationSignUpRequired(TLObject):
    CONSTRUCTOR_ID = 0x44747e9a
    FIELDS = [
        TLField("flags",            "int", flag_group=0, flag_indicator=True),
        TLField("terms_of_service", "TermsOfService", flag_group=0, flag_bit=0),
    ]
