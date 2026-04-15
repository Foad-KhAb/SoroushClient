from soroushclient.tl.base import TLField, TLObject


class RpcError(TLObject):
    CONSTRUCTOR_ID = 0x2144CA19
    FIELDS = [TLField("error_code", "int"), TLField("error_message", "string")]
