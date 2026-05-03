from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class KeyboardButton(TLObject):
    CONSTRUCTOR_ID = 0xA2FA4880
    FIELDS = [TLField("text", "string")]
    text: Optional[str]


class KeyboardButtonUrl(TLObject):
    CONSTRUCTOR_ID = 0x258AFF05
    FIELDS = [
        TLField("text", "string"),
        TLField("url", "string"),
    ]
    text: Optional[str]
    url: Optional[str]


class KeyboardButtonCallback(TLObject):
    CONSTRUCTOR_ID = 0x35BBDB6B
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("requires_password", "true", flag_group=0, flag_bit=0),
        TLField("text", "string"),
        TLField("data", "bytes"),
    ]
    requires_password: Optional[bool]
    text: Optional[str]
    data: Optional[bytes]


class KeyboardButtonRequestPhone(TLObject):
    CONSTRUCTOR_ID = 0xB16A6C29
    FIELDS = [TLField("text", "string")]
    text: Optional[str]


class KeyboardButtonRequestGeoLocation(TLObject):
    CONSTRUCTOR_ID = 0xFC796B3F
    FIELDS = [TLField("text", "string")]
    text: Optional[str]


class KeyboardButtonSwitchInline(TLObject):
    CONSTRUCTOR_ID = 0x93B9FBB5
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("same_peer", "true", flag_group=0, flag_bit=0),
        TLField("text", "string"),
        TLField("query", "string"),
        TLField("peer_types", "InlineQueryPeerType", flag_group=0, flag_bit=1, is_vector=True),
    ]
    same_peer: Optional[bool]
    text: Optional[str]
    query: Optional[str]
    peer_types: Optional[List[TLObject]]


class KeyboardButtonGame(TLObject):
    CONSTRUCTOR_ID = 0x50F41CCF
    FIELDS = [TLField("text", "string")]
    text: Optional[str]


class KeyboardButtonBuy(TLObject):
    CONSTRUCTOR_ID = 0xAFD93FBB
    FIELDS = [TLField("text", "string")]
    text: Optional[str]


class KeyboardButtonUrlAuth(TLObject):
    CONSTRUCTOR_ID = 0x10B78D29
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("text", "string"),
        TLField("fwd_text", "string", flag_group=0, flag_bit=0),
        TLField("url", "string"),
        TLField("button_id", "int"),
    ]
    text: Optional[str]
    fwd_text: Optional[str]
    url: Optional[str]
    button_id: Optional[int]


class InputKeyboardButtonUrlAuth(TLObject):
    CONSTRUCTOR_ID = 0xD02E7FD4
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("request_write_access", "true", flag_group=0, flag_bit=0),
        TLField("text", "string"),
        TLField("fwd_text", "string", flag_group=0, flag_bit=1),
        TLField("url", "string"),
        TLField("bot", "InputUser"),
    ]
    request_write_access: Optional[bool]
    text: Optional[str]
    fwd_text: Optional[str]
    url: Optional[str]
    bot: Optional[TLObject]


class KeyboardButtonRequestPoll(TLObject):
    CONSTRUCTOR_ID = 0xBBC7515D
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("quiz", "Bool", flag_group=0, flag_bit=0),
        TLField("text", "string"),
    ]
    quiz: Optional[bool]
    text: Optional[str]


class InputKeyboardButtonUserProfile(TLObject):
    CONSTRUCTOR_ID = 0xE988037B
    FIELDS = [
        TLField("text", "string"),
        TLField("user_id", "InputUser"),
    ]
    text: Optional[str]
    user_id: Optional[TLObject]


class KeyboardButtonUserProfile(TLObject):
    CONSTRUCTOR_ID = 0x308660C1
    FIELDS = [
        TLField("text", "string"),
        TLField("user_id", "long"),
    ]
    text: Optional[str]
    user_id: Optional[int]


class KeyboardButtonWebView(TLObject):
    CONSTRUCTOR_ID = 0x13767230
    FIELDS = [
        TLField("text", "string"),
        TLField("url", "string"),
    ]
    text: Optional[str]
    url: Optional[str]


class KeyboardButtonSimpleWebView(TLObject):
    CONSTRUCTOR_ID = 0xA0C0505C
    FIELDS = [
        TLField("text", "string"),
        TLField("url", "string"),
    ]
    text: Optional[str]
    url: Optional[str]


class KeyboardButtonRequestPeer(TLObject):
    CONSTRUCTOR_ID = 0x0D0B468C
    FIELDS = [
        TLField("text", "string"),
        TLField("button_id", "int"),
        TLField("peer_type", "RequestPeerType"),
    ]
    text: Optional[str]
    button_id: Optional[int]
    peer_type: Optional[TLObject]


class KeyboardButtonRow(TLObject):
    CONSTRUCTOR_ID = 0x77608B83
    FIELDS = [TLField("buttons", "KeyboardButton", is_vector=True)]
    buttons: Optional[List[TLObject]]


class ReplyKeyboardHide(TLObject):
    CONSTRUCTOR_ID = 0xA03E5B85
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("selective", "true", flag_group=0, flag_bit=2),
    ]
    selective: Optional[bool]


class ReplyKeyboardForceReply(TLObject):
    CONSTRUCTOR_ID = 0x86B40B08
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("single_use", "true", flag_group=0, flag_bit=1),
        TLField("selective", "true", flag_group=0, flag_bit=2),
        TLField("placeholder", "string", flag_group=0, flag_bit=3),
    ]
    single_use: Optional[bool]
    selective: Optional[bool]
    placeholder: Optional[str]


class ReplyKeyboardMarkup(TLObject):
    CONSTRUCTOR_ID = 0x85DD99D1
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("resize", "true", flag_group=0, flag_bit=0),
        TLField("single_use", "true", flag_group=0, flag_bit=1),
        TLField("selective", "true", flag_group=0, flag_bit=2),
        TLField("persistent", "true", flag_group=0, flag_bit=4),
        TLField("rows", "KeyboardButtonRow", is_vector=True),
        TLField("placeholder", "string", flag_group=0, flag_bit=3),
    ]
    resize: Optional[bool]
    single_use: Optional[bool]
    selective: Optional[bool]
    persistent: Optional[bool]
    rows: Optional[List[TLObject]]
    placeholder: Optional[str]


class ReplyInlineMarkup(TLObject):
    CONSTRUCTOR_ID = 0x48A30254
    FIELDS = [TLField("rows", "KeyboardButtonRow", is_vector=True)]
    rows: Optional[List[TLObject]]