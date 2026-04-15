from soroushclient.tl.base import TLField, TLRequest
from soroushclient.tl.generated.types.auth import Authorization, SentCode


class SendCodeRequest(TLRequest):
    CONSTRUCTOR_ID = 0xA677244F
    RESPONSE_TYPE = SentCode
    FIELDS = [
        TLField("phone_number", "string"),
        TLField("api_id", "int"),
        TLField("api_hash", "string"),
        TLField("settings", "CodeSettings"),
    ]


class SignInRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8D52A951
    RESPONSE_TYPE = Authorization
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("phone_number", "string"),
        TLField("phone_code_hash", "bytes"),
        TLField("phone_code", "string", flag_group=0, flag_bit=0),
        TLField("email_verification", "EmailVerification", flag_group=0, flag_bit=1),
    ]


class SignUpRequest(TLRequest):
    CONSTRUCTOR_ID = 0x80EEE427
    RESPONSE_TYPE = Authorization
    FIELDS = [
        TLField("phone_number", "string"),
        TLField("phone_code_hash", "bytes"),
        TLField("first_name", "string"),
        TLField("last_name", "string"),
    ]


class LogOutRequest(TLRequest):
    CONSTRUCTOR_ID = 0x3E72BA19
    FIELDS = []
