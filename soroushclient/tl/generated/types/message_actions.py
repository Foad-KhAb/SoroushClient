from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class MessageActionEmpty(TLObject):
    CONSTRUCTOR_ID = 3064919984
    FIELDS = []


class MessageActionChatCreate(TLObject):
    CONSTRUCTOR_ID = 3175599021
    FIELDS = [
        TLField("title", "string"),
        TLField("users", "long", is_vector=True),
    ]
    title: Optional[str]
    users: Optional[List[int]]


class MessageActionChatEditTitle(TLObject):
    CONSTRUCTOR_ID = 3047280218
    FIELDS = [TLField("title", "string")]
    title: Optional[str]


class MessageActionChatEditPhoto(TLObject):
    CONSTRUCTOR_ID = 2144015272
    FIELDS = [TLField("photo", "Photo")]
    photo: Optional[TLObject]


class MessageActionChatDeletePhoto(TLObject):
    CONSTRUCTOR_ID = 2514746351
    FIELDS = []


class MessageActionChatAddUser(TLObject):
    CONSTRUCTOR_ID = 365886720
    FIELDS = [TLField("users", "long", is_vector=True)]
    users: Optional[List[int]]


class MessageActionChatDeleteUser(TLObject):
    CONSTRUCTOR_ID = 2755604684
    FIELDS = [TLField("user_id", "long")]
    user_id: Optional[int]


class MessageActionChatJoinedByLink(TLObject):
    CONSTRUCTOR_ID = 51520707
    FIELDS = [TLField("inviter_id", "long")]
    inviter_id: Optional[int]


class MessageActionChannelCreate(TLObject):
    CONSTRUCTOR_ID = 2513611922
    FIELDS = [TLField("title", "string")]
    title: Optional[str]


class MessageActionChatMigrateTo(TLObject):
    CONSTRUCTOR_ID = 3775102866
    FIELDS = [TLField("channel_id", "long")]
    channel_id: Optional[int]


class MessageActionChannelMigrateFrom(TLObject):
    CONSTRUCTOR_ID = 3929622761
    FIELDS = [
        TLField("title", "string"),
        TLField("chat_id", "long"),
    ]
    title: Optional[str]
    chat_id: Optional[int]


class MessageActionPinMessage(TLObject):
    CONSTRUCTOR_ID = 2495428845
    FIELDS = []


class MessageActionHistoryClear(TLObject):
    CONSTRUCTOR_ID = 2679813636
    FIELDS = []


class MessageActionGameScore(TLObject):
    CONSTRUCTOR_ID = 2460428406
    FIELDS = [
        TLField("game_id", "long"),
        TLField("score", "int"),
    ]
    game_id: Optional[int]
    score: Optional[int]


class MessageActionPaymentSentMe(TLObject):
    CONSTRUCTOR_ID = 2402399015
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("recurring_init", "true", flag_group=0, flag_bit=2),
        TLField("recurring_used", "true", flag_group=0, flag_bit=3),
        TLField("currency", "string"),
        TLField("total_amount", "long"),
        TLField("payload", "bytes"),
        TLField("info", "PaymentRequestedInfo", flag_group=0, flag_bit=0),
        TLField("shipping_option_id", "string", flag_group=0, flag_bit=1),
        TLField("charge", "PaymentCharge"),
    ]
    recurring_init: Optional[bool]
    recurring_used: Optional[bool]
    currency: Optional[str]
    total_amount: Optional[int]
    payload: Optional[bytes]
    info: Optional[TLObject]
    shipping_option_id: Optional[str]
    charge: Optional[TLObject]


class MessageActionPaymentSent(TLObject):
    CONSTRUCTOR_ID = 2518040406
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("recurring_init", "true", flag_group=0, flag_bit=2),
        TLField("recurring_used", "true", flag_group=0, flag_bit=3),
        TLField("currency", "string"),
        TLField("total_amount", "long"),
        TLField("invoice_slug", "string", flag_group=0, flag_bit=0),
    ]
    recurring_init: Optional[bool]
    recurring_used: Optional[bool]
    currency: Optional[str]
    total_amount: Optional[int]
    invoice_slug: Optional[str]


class MessageActionPhoneCall(TLObject):
    CONSTRUCTOR_ID = 2162236031
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("video", "true", flag_group=0, flag_bit=2),
        TLField("call_id", "long"),
        TLField("reason", "PhoneCallDiscardReason", flag_group=0, flag_bit=0),
        TLField("duration", "int", flag_group=0, flag_bit=1),
    ]
    video: Optional[bool]
    call_id: Optional[int]
    reason: Optional[TLObject]
    duration: Optional[int]


class MessageActionScreenshotTaken(TLObject):
    CONSTRUCTOR_ID = 1200788123
    FIELDS = []


class MessageActionCustomAction(TLObject):
    CONSTRUCTOR_ID = 4209418070
    FIELDS = [TLField("message", "string")]
    message: Optional[str]


class MessageActionBotAllowed(TLObject):
    CONSTRUCTOR_ID = 3306608249
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("attach_menu", "true", flag_group=0, flag_bit=1),
        TLField("from_request", "true", flag_group=0, flag_bit=3),
        TLField("domain", "string", flag_group=0, flag_bit=0),
        TLField("app", "BotApp", flag_group=0, flag_bit=2),
    ]
    attach_menu: Optional[bool]
    from_request: Optional[bool]
    domain: Optional[str]
    app: Optional[TLObject]


class MessageActionSecureValuesSentMe(TLObject):
    CONSTRUCTOR_ID = 455635795
    FIELDS = [
        TLField("values", "SecureValue", is_vector=True),
        TLField("credentials", "SecureCredentialsEncrypted"),
    ]
    values: Optional[List[TLObject]]
    credentials: Optional[TLObject]


class MessageActionSecureValuesSent(TLObject):
    CONSTRUCTOR_ID = 3646710100
    FIELDS = [TLField("types", "SecureValueType", is_vector=True)]
    types: Optional[List[TLObject]]


class MessageActionContactSignUp(TLObject):
    CONSTRUCTOR_ID = 4092747638
    FIELDS = []


class MessageActionGeoProximityReached(TLObject):
    CONSTRUCTOR_ID = 2564871831
    FIELDS = [
        TLField("from_id", "Peer"),
        TLField("to_id", "Peer"),
        TLField("distance", "int"),
    ]
    from_id: Optional[TLObject]
    to_id: Optional[TLObject]
    distance: Optional[int]


class MessageActionGroupCall(TLObject):
    CONSTRUCTOR_ID = 2047704898
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("call", "InputGroupCall"),
        TLField("duration", "int", flag_group=0, flag_bit=0),
    ]
    call: Optional[TLObject]
    duration: Optional[int]


class MessageActionInviteToGroupCall(TLObject):
    CONSTRUCTOR_ID = 1345295095
    FIELDS = [
        TLField("call", "InputGroupCall"),
        TLField("users", "long", is_vector=True),
    ]
    call: Optional[TLObject]
    users: Optional[List[int]]


class MessageActionSetMessagesTTL(TLObject):
    CONSTRUCTOR_ID = 1007897979
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("period", "int"),
        TLField("auto_setting_from", "long", flag_group=0, flag_bit=0),
    ]
    period: Optional[int]
    auto_setting_from: Optional[int]


class MessageActionGroupCallScheduled(TLObject):
    CONSTRUCTOR_ID = 3013637729
    FIELDS = [
        TLField("call", "InputGroupCall"),
        TLField("schedule_date", "int"),
    ]
    call: Optional[TLObject]
    schedule_date: Optional[int]


class MessageActionSetChatTheme(TLObject):
    CONSTRUCTOR_ID = 2860016453
    FIELDS = [TLField("emoticon", "string")]
    emoticon: Optional[str]


class MessageActionChatJoinedByRequest(TLObject):
    CONSTRUCTOR_ID = 3955008459
    FIELDS = []


class MessageActionWebViewDataSentMe(TLObject):
    CONSTRUCTOR_ID = 1205698681
    FIELDS = [
        TLField("text", "string"),
        TLField("data", "string"),
    ]
    text: Optional[str]
    data: Optional[str]


class MessageActionWebViewDataSent(TLObject):
    CONSTRUCTOR_ID = 3032714421
    FIELDS = [TLField("text", "string")]
    text: Optional[str]


class MessageActionGiftPremium(TLObject):
    CONSTRUCTOR_ID = 3359468268
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("currency", "string"),
        TLField("amount", "long"),
        TLField("months", "int"),
        TLField("crypto_currency", "string", flag_group=0, flag_bit=0),
        TLField("crypto_amount", "long", flag_group=0, flag_bit=0),
    ]
    currency: Optional[str]
    amount: Optional[int]
    months: Optional[int]
    crypto_currency: Optional[str]
    crypto_amount: Optional[int]


class MessageActionTopicCreate(TLObject):
    CONSTRUCTOR_ID = 228168278
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("title", "string"),
        TLField("icon_color", "int"),
        TLField("icon_emoji_id", "long", flag_group=0, flag_bit=0),
    ]
    title: Optional[str]
    icon_color: Optional[int]
    icon_emoji_id: Optional[int]


class MessageActionTopicEdit(TLObject):
    CONSTRUCTOR_ID = 3230943264
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("title", "string", flag_group=0, flag_bit=0),
        TLField("icon_emoji_id", "long", flag_group=0, flag_bit=1),
        TLField("closed", "Bool", flag_group=0, flag_bit=2),
        TLField("hidden", "Bool", flag_group=0, flag_bit=3),
    ]
    title: Optional[str]
    icon_emoji_id: Optional[int]
    closed: Optional[bool]
    hidden: Optional[bool]


class MessageActionSuggestProfilePhoto(TLObject):
    CONSTRUCTOR_ID = 1474192222
    FIELDS = [TLField("photo", "Photo")]
    photo: Optional[TLObject]


class MessageActionRequestedPeer(TLObject):
    CONSTRUCTOR_ID = 4269225053
    FIELDS = [
        TLField("button_id", "int"),
        TLField("peer", "Peer"),
    ]
    button_id: Optional[int]
    peer: Optional[TLObject]


class MessageActionSetChatWallPaper(TLObject):
    CONSTRUCTOR_ID = 1348510708
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("same", "true", flag_group=0, flag_bit=0),
        TLField("for_both", "true", flag_group=0, flag_bit=1),
        TLField("wallpaper", "WallPaper"),
    ]
    same: Optional[bool]
    for_both: Optional[bool]
    wallpaper: Optional[TLObject]


class MessageActionGiftCode(TLObject):
    CONSTRUCTOR_ID = 3536837390
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("via_giveaway", "true", flag_group=0, flag_bit=0),
        TLField("unclaimed", "true", flag_group=0, flag_bit=2),
        TLField("boost_peer", "Peer", flag_group=0, flag_bit=1),
        TLField("months", "int"),
        TLField("slug", "string"),
    ]
    via_giveaway: Optional[bool]
    unclaimed: Optional[bool]
    boost_peer: Optional[TLObject]
    months: Optional[int]
    slug: Optional[str]


class MessageActionGiveawayLaunch(TLObject):
    CONSTRUCTOR_ID = 858499565
    FIELDS = []


class MessageActionGiveawayResults(TLObject):
    CONSTRUCTOR_ID = 715107781
    FIELDS = [
        TLField("winners_count", "int"),
        TLField("unclaimed_count", "int"),
    ]
    winners_count: Optional[int]
    unclaimed_count: Optional[int]


class MessageActionContactReturned(TLObject):
    CONSTRUCTOR_ID = 508031610
    FIELDS = []

class MessageActionProtectedMessage(TLObject):
    CONSTRUCTOR_ID = 0xB8257746
    FIELDS = [
        TLField("id", "string", skip_cid=True),
    ]