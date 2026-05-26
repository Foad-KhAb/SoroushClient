from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField, TLRequest


class SendCode(TLRequest):
    CONSTRUCTOR_ID = 0xA677244F
    FIELDS = [
        TLField("phone_number", "string"),
        TLField("api_id", "int"),
        TLField("api_hash", "string"),
        TLField("settings", "CodeSettings"),
    ]
    phone_number: Optional[str]
    api_id: Optional[int]
    api_hash: Optional[str]
    settings: Optional[TLObject]

class SignUp(TLRequest):
    CONSTRUCTOR_ID = 0x80EEE427
    FIELDS = [
        TLField("phone_number", "string"),
        TLField("phone_code_hash", "string"),
        TLField("first_name", "string"),
        TLField("last_name", "string"),
    ]
    phone_number: Optional[str]
    phone_code_hash: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]

class SignIn(TLRequest):
    CONSTRUCTOR_ID = 0x8D52A951
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("phone_number", "string"),
        TLField("phone_code_hash", "string"),
        TLField("phone_code", "string", flag_group=0, flag_bit=0),
        TLField("email_verification", "EmailVerification", flag_group=0, flag_bit=1),
    ]
    phone_number: Optional[str]
    phone_code_hash: Optional[str]
    phone_code: Optional[str]
    email_verification: Optional[TLObject]

class LogOut(TLRequest):
    CONSTRUCTOR_ID = 0x3E72BA19
    FIELDS = []

class ResetAuthorizations(TLRequest):
    CONSTRUCTOR_ID = 0x9FAB0D1A
    FIELDS = []

class ExportAuthorization(TLRequest):
    CONSTRUCTOR_ID = 0xE5BFFFCD
    FIELDS = [TLField("dc_id", "int")]
    dc_id: Optional[int]

class ImportAuthorization(TLRequest):
    CONSTRUCTOR_ID = 0xA57A7DAD
    FIELDS = [
        TLField("id", "long"),
        TLField("bytes", "bytes"),
    ]
    id: Optional[int]
    bytes: Optional[bytes]

class ResendCode(TLRequest):
    CONSTRUCTOR_ID = 0x3EF1A9BF
    FIELDS = [
        TLField("phone_number", "string"),
        TLField("phone_code_hash", "string"),
    ]
    phone_number: Optional[str]
    phone_code_hash: Optional[str]

class CancelCode(TLRequest):
    CONSTRUCTOR_ID = 0x1F040578
    FIELDS = [
        TLField("phone_number", "string"),
        TLField("phone_code_hash", "string"),
    ]
    phone_number: Optional[str]
    phone_code_hash: Optional[str]

class ExportLoginToken(TLRequest):
    CONSTRUCTOR_ID = 0xB7E085FE
    FIELDS = [
        TLField("api_id", "int"),
        TLField("api_hash", "string"),
        TLField("except_ids", "long", is_vector=True),
    ]
    api_id: Optional[int]
    api_hash: Optional[str]
    except_ids: Optional[List[int]]

class ImportLoginToken(TLRequest):
    CONSTRUCTOR_ID = 0x95AC5CE4
    FIELDS = [TLField("token", "bytes")]
    token: Optional[bytes]

class SendDeleteAccountCode(TLRequest):
    CONSTRUCTOR_ID = 0x7FB3DDC0
    FIELDS = []

class ResendDeleteAccountCode(TLRequest):
    CONSTRUCTOR_ID = 0x633A65A0
    FIELDS = []

class DeleteAccount(TLRequest):
    CONSTRUCTOR_ID = 0x441A1EC2
    FIELDS = [TLField("delete_account_code", "string")]
    delete_account_code: Optional[str]