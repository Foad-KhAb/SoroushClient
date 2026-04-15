from soroushclient.tl.base import TLField, TLRequest


class GetFullChatRequest(TLRequest):
    CONSTRUCTOR_ID = 0xAEB00B34
    FIELDS = [
        TLField("chat_id", "long"),
    ]
