from soroushclient.tl.base import TLField, TLRequest


class GetFullChatRequest(TLRequest):
    CONSTRUCTOR_ID = 0xaeb00b34
    FIELDS = [
        TLField("chat_id", "long"),
    ]
