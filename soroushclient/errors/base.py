from soroushclient.tl.base import TLObject, TLField


class RpcError(TLObject):
    CONSTRUCTOR_ID = 0x2144ca19
    FIELDS = [TLField("error_code","int"), TLField("error_message","string")]
