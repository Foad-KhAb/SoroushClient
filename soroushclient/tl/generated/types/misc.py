from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class DataJSON(TLObject):
    CONSTRUCTOR_ID = 0x7D748D04
    FIELDS = [TLField("data", "string")]
    data: Optional[str]

class JSONObjectValue(TLObject):
    CONSTRUCTOR_ID = 0xC0DE1BD9
    FIELDS = [
        TLField("key", "string"),
        TLField("value", "JSONValue"),
    ]
    key: Optional[str]
    value: Optional[TLObject]

class JSONNull(TLObject):
    CONSTRUCTOR_ID = 0x3F6D7B68
    FIELDS = []

class JSONBool(TLObject):
    CONSTRUCTOR_ID = 0xC7345E6A
    FIELDS = [TLField("value", "Bool")]
    value: Optional[bool]

class JSONNumber(TLObject):
    CONSTRUCTOR_ID = 0x2BE0DFA4
    FIELDS = [TLField("value", "double")]
    value: Optional[float]

class JSONString(TLObject):
    CONSTRUCTOR_ID = 0xB71E767A
    FIELDS = [TLField("value", "string")]
    value: Optional[str]

class JSONArray(TLObject):
    CONSTRUCTOR_ID = 0xF7444763
    FIELDS = [TLField("value", "JSONValue", is_vector=True)]
    value: Optional[List[TLObject]]

class JSONObject(TLObject):
    CONSTRUCTOR_ID = 0x99C1D49D
    FIELDS = [TLField("value", "JSONObjectValue", is_vector=True)]
    value: Optional[List[TLObject]]

class TextWithEntities(TLObject):
    CONSTRUCTOR_ID = 0x751F3146
    FIELDS = [
        TLField("text", "string"),
        TLField("entities", "MessageEntity", is_vector=True),
    ]
    text: Optional[str]
    entities: Optional[List[TLObject]]

class DefaultHistoryTTL(TLObject):
    CONSTRUCTOR_ID = 0x43B46B20
    FIELDS = [TLField("period", "int")]
    period: Optional[int]

class ExportedContactToken(TLObject):
    CONSTRUCTOR_ID = 0x41BF109B
    FIELDS = [
        TLField("url", "string"),
        TLField("expires", "int"),
    ]
    url: Optional[str]
    expires: Optional[int]

class WebAuthorization(TLObject):
    CONSTRUCTOR_ID = 0xA6F8F452
    FIELDS = [
        TLField("hash", "long"),
        TLField("bot_id", "long"),
        TLField("domain", "string"),
        TLField("browser", "string"),
        TLField("platform", "string"),
        TLField("date_created", "int"),
        TLField("date_active", "int"),
        TLField("ip", "string"),
        TLField("region", "string"),
    ]
    hash: Optional[int]
    bot_id: Optional[int]
    domain: Optional[str]
    browser: Optional[str]
    platform: Optional[str]
    date_created: Optional[int]
    date_active: Optional[int]
    ip: Optional[str]
    region: Optional[str]

class PopularContact(TLObject):
    CONSTRUCTOR_ID = 0x5CE14175
    FIELDS = [
        TLField("client_id", "long"),
        TLField("importers", "int"),
    ]
    client_id: Optional[int]
    importers: Optional[int]

class InputReportReasonSpam(TLObject):
    CONSTRUCTOR_ID = 0x58DBCAB8
    FIELDS = []

class InputReportReasonViolence(TLObject):
    CONSTRUCTOR_ID = 0x1E22C78D
    FIELDS = []

class InputReportReasonPornography(TLObject):
    CONSTRUCTOR_ID = 0x2E59D922
    FIELDS = []

class InputReportReasonChildAbuse(TLObject):
    CONSTRUCTOR_ID = 0xADF44EE3
    FIELDS = []

class InputReportReasonOther(TLObject):
    CONSTRUCTOR_ID = 0xC1E4A2B1
    FIELDS = []

class InputReportReasonCopyright(TLObject):
    CONSTRUCTOR_ID = 0x9B89F93A
    FIELDS = []

class InputReportReasonGeoIrrelevant(TLObject):
    CONSTRUCTOR_ID = 0xDBD4FEED
    FIELDS = []

class InputReportReasonFake(TLObject):
    CONSTRUCTOR_ID = 0xF5DDD6E7
    FIELDS = []

class InputReportReasonIllegalDrugs(TLObject):
    CONSTRUCTOR_ID = 0x0A8EB2BE
    FIELDS = []

class InputReportReasonPersonalDetails(TLObject):
    CONSTRUCTOR_ID = 0x9EC7863D
    FIELDS = []

class Folder(TLObject):
    CONSTRUCTOR_ID = 0xFF544E65
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("autofill_new_broadcasts", "true", flag_group=0, flag_bit=0),
        TLField("autofill_public_groups", "true", flag_group=0, flag_bit=1),
        TLField("autofill_new_correspondents", "true", flag_group=0, flag_bit=2),
        TLField("id", "int"),
        TLField("title", "string"),
        TLField("photo", "ChatPhoto", flag_group=0, flag_bit=3),
    ]
    autofill_new_broadcasts: Optional[bool]
    autofill_public_groups: Optional[bool]
    autofill_new_correspondents: Optional[bool]
    id: Optional[int]
    title: Optional[str]
    photo: Optional[TLObject]

class InputFolderPeer(TLObject):
    CONSTRUCTOR_ID = 0xFBD2C296
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("folder_id", "int"),
    ]
    peer: Optional[TLObject]
    folder_id: Optional[int]

class FolderPeer(TLObject):
    CONSTRUCTOR_ID = 0xE9BAA668
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("folder_id", "int"),
    ]
    peer: Optional[TLObject]
    folder_id: Optional[int]

class InputDialogPeer(TLObject):
    CONSTRUCTOR_ID = 0xFCAAFEB7
    FIELDS = [TLField("peer", "InputPeer")]
    peer: Optional[TLObject]

class InputDialogPeerFolder(TLObject):
    CONSTRUCTOR_ID = 0x64600527
    FIELDS = [TLField("folder_id", "int")]
    folder_id: Optional[int]

class DialogPeer(TLObject):
    CONSTRUCTOR_ID = 0xE56DBF05
    FIELDS = [TLField("peer", "Peer")]
    peer: Optional[TLObject]

class DialogPeerFolder(TLObject):
    CONSTRUCTOR_ID = 0x514519E2
    FIELDS = [TLField("folder_id", "int")]
    folder_id: Optional[int]

class DialogFilter(TLObject):
    CONSTRUCTOR_ID = 0x5FB5523B
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("contacts", "true", flag_group=0, flag_bit=0),
        TLField("non_contacts", "true", flag_group=0, flag_bit=1),
        TLField("groups", "true", flag_group=0, flag_bit=2),
        TLField("broadcasts", "true", flag_group=0, flag_bit=3),
        TLField("bots", "true", flag_group=0, flag_bit=4),
        TLField("exclude_muted", "true", flag_group=0, flag_bit=11),
        TLField("exclude_read", "true", flag_group=0, flag_bit=12),
        TLField("exclude_archived", "true", flag_group=0, flag_bit=13),
        TLField("id", "int"),
        TLField("title", "string"),
        TLField("emoticon", "string", flag_group=0, flag_bit=25),
        TLField("color", "int", flag_group=0, flag_bit=27),
        TLField("pinned_peers", "InputPeer", is_vector=True),
        TLField("include_peers", "InputPeer", is_vector=True),
        TLField("exclude_peers", "InputPeer", is_vector=True),
    ]
    contacts: Optional[bool]
    non_contacts: Optional[bool]
    groups: Optional[bool]
    broadcasts: Optional[bool]
    bots: Optional[bool]
    exclude_muted: Optional[bool]
    exclude_read: Optional[bool]
    exclude_archived: Optional[bool]
    id: Optional[int]
    title: Optional[str]
    emoticon: Optional[str]
    color: Optional[int]
    pinned_peers: Optional[List[TLObject]]
    include_peers: Optional[List[TLObject]]
    exclude_peers: Optional[List[TLObject]]

class DialogFilterDefault(TLObject):
    CONSTRUCTOR_ID = 0x363293AE
    FIELDS = []

class DialogFilterChatlist(TLObject):
    CONSTRUCTOR_ID = 0xD64A04A8
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("has_my_invites", "true", flag_group=0, flag_bit=26),
        TLField("id", "int"),
        TLField("title", "string"),
        TLField("emoticon", "string", flag_group=0, flag_bit=25),
        TLField("pinned_peers", "InputPeer", is_vector=True),
        TLField("include_peers", "InputPeer", is_vector=True),
    ]
    has_my_invites: Optional[bool]
    id: Optional[int]
    title: Optional[str]
    emoticon: Optional[str]
    pinned_peers: Optional[List[TLObject]]
    include_peers: Optional[List[TLObject]]

class DialogFilterSuggested(TLObject):
    CONSTRUCTOR_ID = 0x77744D4A
    FIELDS = [
        TLField("filter", "DialogFilter"),
        TLField("description", "string"),
    ]
    filter: Optional[TLObject]
    description: Optional[str]

class PeerColor(TLObject):
    CONSTRUCTOR_ID = 0xB54B5ACF
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("color", "int", flag_group=0, flag_bit=0),
        TLField("background_emoji_id", "long", flag_group=0, flag_bit=1),
    ]
    color: Optional[int]
    background_emoji_id: Optional[int]

class Timezone(TLObject):
    CONSTRUCTOR_ID = 0xFF9289F5
    FIELDS = [
        TLField("id", "string"),
        TLField("name", "string"),
        TLField("utc_offset", "int"),
    ]
    id: Optional[str]
    name: Optional[str]
    utc_offset: Optional[int]

class StatsURL(TLObject):
    CONSTRUCTOR_ID = 0x47A971E0
    FIELDS = [TLField("url", "string")]
    url: Optional[str]

class SavedPhoneContact(TLObject):
    CONSTRUCTOR_ID = 0x1142BD56
    FIELDS = [
        TLField("phone", "string"),
        TLField("first_name", "string"),
        TLField("last_name", "string"),
        TLField("date", "int"),
    ]
    phone: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    date: Optional[int]

class ExportedStoryLink(TLObject):
    CONSTRUCTOR_ID = 0x3FC9053B
    FIELDS = [TLField("link", "string")]
    link: Optional[str]

class ExportedMessageLink(TLObject):
    CONSTRUCTOR_ID = 0x5DAB1AF4
    FIELDS = [
        TLField("link", "string"),
        TLField("html", "string"),
    ]
    link: Optional[str]
    html: Optional[str]

class ExportedChatlistInvite(TLObject):
    CONSTRUCTOR_ID = 0x0C5181AC
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("title", "string"),
        TLField("url", "string"),
        TLField("peers", "Peer", is_vector=True),
    ]
    title: Optional[str]
    url: Optional[str]
    peers: Optional[List[TLObject]]

class InputChatlistDialogFilter(TLObject):
    CONSTRUCTOR_ID = 0xF3E0DA33
    FIELDS = [TLField("filter_id", "int")]
    filter_id: Optional[int]

class BotVerification(TLObject):
    CONSTRUCTOR_ID = 0xF93CD45C
    FIELDS = [
        TLField("bot_id", "long"),
        TLField("icon", "long"),
        TLField("description", "string"),
    ]
    bot_id: Optional[int]
    icon: Optional[int]
    description: Optional[str]

class DisallowedGiftsSettings(TLObject):
    CONSTRUCTOR_ID = 0x71F276C4
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("disallow_unlimited_stargifts", "true", flag_group=0, flag_bit=0),
        TLField("disallow_limited_stargifts", "true", flag_group=0, flag_bit=1),
        TLField("disallow_unique_stargifts", "true", flag_group=0, flag_bit=2),
        TLField("disallow_premium_gifts", "true", flag_group=0, flag_bit=3),
    ]
    disallow_unlimited_stargifts: Optional[bool]
    disallow_limited_stargifts: Optional[bool]
    disallow_unique_stargifts: Optional[bool]
    disallow_premium_gifts: Optional[bool]

class StarRefProgram(TLObject):
    CONSTRUCTOR_ID = 0xDD0C66F2
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("bot_id", "long"),
        TLField("commission_permille", "int"),
        TLField("duration_months", "int", flag_group=0, flag_bit=0),
        TLField("end_date", "int", flag_group=0, flag_bit=1),
        TLField("daily_revenue_per_user", "StarsAmount", flag_group=0, flag_bit=2),
    ]
    bot_id: Optional[int]
    commission_permille: Optional[int]
    duration_months: Optional[int]
    end_date: Optional[int]
    daily_revenue_per_user: Optional[TLObject]

class StarsRating(TLObject):
    CONSTRUCTOR_ID = 0x1B0E4F07
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("level", "int"),
        TLField("current_level_stars", "long"),
        TLField("stars", "long"),
        TLField("next_level_stars", "long", flag_group=0, flag_bit=0),
    ]
    level: Optional[int]
    current_level_stars: Optional[int]
    stars: Optional[int]
    next_level_stars: Optional[int]

class StarsAmount(TLObject):
    CONSTRUCTOR_ID = 0xBBB6B4A3
    FIELDS = [
        TLField("amount", "long"),
        TLField("nanos", "int"),
    ]
    amount: Optional[int]
    nanos: Optional[int]

class StarsTonAmount(TLObject):
    CONSTRUCTOR_ID = 0x74AEE3E0
    FIELDS = [TLField("amount", "long")]
    amount: Optional[int]

class ProfileTabPosts(TLObject):
    CONSTRUCTOR_ID = 0xB98CD696
    FIELDS = []

class ProfileTabGifts(TLObject):
    CONSTRUCTOR_ID = 0x4D4BD46A
    FIELDS = []

class ProfileTabMedia(TLObject):
    CONSTRUCTOR_ID = 0x72C64955
    FIELDS = []

class ProfileTabFiles(TLObject):
    CONSTRUCTOR_ID = 0xAB339C00
    FIELDS = []

class ProfileTabMusic(TLObject):
    CONSTRUCTOR_ID = 0x9F27D26E
    FIELDS = []

class ProfileTabVoice(TLObject):
    CONSTRUCTOR_ID = 0xE477092E
    FIELDS = []

class ProfileTabLinks(TLObject):
    CONSTRUCTOR_ID = 0xD3656499
    FIELDS = []

class ProfileTabGifs(TLObject):
    CONSTRUCTOR_ID = 0xA2C0F695
    FIELDS = []