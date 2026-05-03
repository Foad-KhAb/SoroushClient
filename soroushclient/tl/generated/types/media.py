# All MessageMedia*, InputMedia*, Photo*, Document*, GeoPoint, etc.
# Already defined above — add remaining ones here:
from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class PhotoEmpty(TLObject):
    CONSTRUCTOR_ID = 0x2331B22D
    FIELDS = [TLField("id", "long")]
    id: Optional[int]

class Photo(TLObject):
    CONSTRUCTOR_ID = 0xFB197A65
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("has_stickers", "true", flag_group=0, flag_bit=0),
        TLField("id", "long"),
        TLField("access_hash", "long"),
        TLField("file_reference", "bytes"),
        TLField("date", "int"),
        TLField("sizes", "PhotoSize", is_vector=True),
        TLField("video_sizes", "VideoSize", flag_group=0, flag_bit=1, is_vector=True),
        TLField("dc_id", "int"),
    ]
    has_stickers: Optional[bool]
    id: Optional[int]
    access_hash: Optional[int]
    file_reference: Optional[bytes]
    date: Optional[int]
    sizes: Optional[List[TLObject]]
    video_sizes: Optional[List[TLObject]]
    dc_id: Optional[int]

class PhotoSizeEmpty(TLObject):
    CONSTRUCTOR_ID = 0x0E17E23C
    FIELDS = [TLField("type", "string")]
    type: Optional[str]

class PhotoSize(TLObject):
    CONSTRUCTOR_ID = 0x75C78E60
    FIELDS = [
        TLField("type", "string"),
        TLField("w", "int"),
        TLField("h", "int"),
        TLField("size", "int"),
    ]
    type: Optional[str]
    w: Optional[int]
    h: Optional[int]
    size: Optional[int]

class PhotoCachedSize(TLObject):
    CONSTRUCTOR_ID = 0x021E1AD6
    FIELDS = [
        TLField("type", "string"),
        TLField("w", "int"),
        TLField("h", "int"),
        TLField("bytes", "bytes"),
    ]
    type: Optional[str]
    w: Optional[int]
    h: Optional[int]
    bytes: Optional[bytes]

class PhotoStrippedSize(TLObject):
    CONSTRUCTOR_ID = 0xE0B0BC2E
    FIELDS = [
        TLField("type", "string"),
        TLField("bytes", "bytes"),
    ]
    type: Optional[str]
    bytes: Optional[bytes]

class PhotoSizeProgressive(TLObject):
    CONSTRUCTOR_ID = 0xFA3EFB95
    FIELDS = [
        TLField("type", "string"),
        TLField("w", "int"),
        TLField("h", "int"),
        TLField("sizes", "int", is_vector=True),
    ]
    type: Optional[str]
    w: Optional[int]
    h: Optional[int]
    sizes: Optional[List[int]]

class PhotoPathSize(TLObject):
    CONSTRUCTOR_ID = 0xD8214D41
    FIELDS = [
        TLField("type", "string"),
        TLField("bytes", "bytes"),
    ]
    type: Optional[str]
    bytes: Optional[bytes]

class GeoPointEmpty(TLObject):
    CONSTRUCTOR_ID = 0x1117DD5F
    FIELDS = []

class GeoPoint(TLObject):
    CONSTRUCTOR_ID = 0xB2A2F663
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("long", "double"),
        TLField("lat", "double"),
        TLField("access_hash", "long"),
        TLField("accuracy_radius", "int", flag_group=0, flag_bit=0),
    ]
    long: Optional[float]
    lat: Optional[float]
    access_hash: Optional[int]
    accuracy_radius: Optional[int]

class InputGeoPointEmpty(TLObject):
    CONSTRUCTOR_ID = 0xE4C123D6
    FIELDS = []

class InputGeoPoint(TLObject):
    CONSTRUCTOR_ID = 0x48222FAF
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("lat", "double"),
        TLField("long", "double"),
        TLField("accuracy_radius", "int", flag_group=0, flag_bit=0),
    ]
    lat: Optional[float]
    long: Optional[float]
    accuracy_radius: Optional[int]

class DocumentEmpty(TLObject):
    CONSTRUCTOR_ID = 0x36F8C871
    FIELDS = [TLField("id", "long")]
    id: Optional[int]

class Document(TLObject):
    CONSTRUCTOR_ID = 0x8FD4C4D8
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("id", "long"),
        TLField("access_hash", "long"),
        TLField("file_reference", "bytes"),
        TLField("date", "int"),
        TLField("mime_type", "string"),
        TLField("size", "long"),
        TLField("thumbs", "PhotoSize", flag_group=0, flag_bit=0, is_vector=True),
        TLField("video_thumbs", "VideoSize", flag_group=0, flag_bit=1, is_vector=True),
        TLField("dc_id", "int"),
        TLField("attributes", "DocumentAttribute", is_vector=True),
    ]
    id: Optional[int]
    access_hash: Optional[int]
    file_reference: Optional[bytes]
    date: Optional[int]
    mime_type: Optional[str]
    size: Optional[int]
    thumbs: Optional[List[TLObject]]
    video_thumbs: Optional[List[TLObject]]
    dc_id: Optional[int]
    attributes: Optional[List[TLObject]]

class InputDocumentEmpty(TLObject):
    CONSTRUCTOR_ID = 0x72F0EAAE
    FIELDS = []

class InputDocument(TLObject):
    CONSTRUCTOR_ID = 0x1ABFB575
    FIELDS = [
        TLField("id", "long"),
        TLField("access_hash", "long"),
        TLField("file_reference", "bytes"),
    ]
    id: Optional[int]
    access_hash: Optional[int]
    file_reference: Optional[bytes]

class InputPhotoEmpty(TLObject):
    CONSTRUCTOR_ID = 0x1CD7BF0D
    FIELDS = []

class InputPhoto(TLObject):
    CONSTRUCTOR_ID = 0x3BB3B94A
    FIELDS = [
        TLField("id", "long"),
        TLField("access_hash", "long"),
        TLField("file_reference", "bytes"),
    ]
    id: Optional[int]
    access_hash: Optional[int]
    file_reference: Optional[bytes]

class VideoSize(TLObject):
    CONSTRUCTOR_ID = 0xDE33B094
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("type", "string"),
        TLField("w", "int"),
        TLField("h", "int"),
        TLField("size", "int"),
        TLField("video_start_ts", "double", flag_group=0, flag_bit=0),
    ]
    type: Optional[str]
    w: Optional[int]
    h: Optional[int]
    size: Optional[int]
    video_start_ts: Optional[float]

class VideoSizeEmojiMarkup(TLObject):
    CONSTRUCTOR_ID = 0xF85C413C
    FIELDS = [
        TLField("emoji_id", "long"),
        TLField("background_colors", "int", is_vector=True),
    ]
    emoji_id: Optional[int]
    background_colors: Optional[List[int]]

class VideoSizeStickerMarkup(TLObject):
    CONSTRUCTOR_ID = 0x0DA082FE
    FIELDS = [
        TLField("stickerset", "InputStickerSet"),
        TLField("sticker_id", "long"),
        TLField("background_colors", "int", is_vector=True),
    ]
    stickerset: Optional[TLObject]
    sticker_id: Optional[int]
    background_colors: Optional[List[int]]

class WebDocument(TLObject):
    CONSTRUCTOR_ID = 0x1C570ED1
    FIELDS = [
        TLField("url", "string"),
        TLField("access_hash", "long"),
        TLField("size", "int"),
        TLField("mime_type", "string"),
        TLField("attributes", "DocumentAttribute", is_vector=True),
    ]
    url: Optional[str]
    access_hash: Optional[int]
    size: Optional[int]
    mime_type: Optional[str]
    attributes: Optional[List[TLObject]]

class WebDocumentNoProxy(TLObject):
    CONSTRUCTOR_ID = 0xF9C8BCC6
    FIELDS = [
        TLField("url", "string"),
        TLField("size", "int"),
        TLField("mime_type", "string"),
        TLField("attributes", "DocumentAttribute", is_vector=True),
    ]
    url: Optional[str]
    size: Optional[int]
    mime_type: Optional[str]
    attributes: Optional[List[TLObject]]

class InputWebDocument(TLObject):
    CONSTRUCTOR_ID = 0x9BED434D
    FIELDS = [
        TLField("url", "string"),
        TLField("size", "int"),
        TLField("mime_type", "string"),
        TLField("attributes", "DocumentAttribute", is_vector=True),
    ]
    url: Optional[str]
    size: Optional[int]
    mime_type: Optional[str]
    attributes: Optional[List[TLObject]]

class FileHash(TLObject):
    CONSTRUCTOR_ID = 0xF39B035C
    FIELDS = [
        TLField("offset", "long"),
        TLField("limit", "int"),
        TLField("hash", "bytes"),
    ]
    offset: Optional[int]
    limit: Optional[int]
    hash: Optional[bytes]

class InputFile(TLObject):
    CONSTRUCTOR_ID = 0xF52FF27F
    FIELDS = [
        TLField("id", "long"),
        TLField("parts", "int"),
        TLField("name", "string"),
        TLField("md5_checksum", "string"),
    ]
    id: Optional[int]
    parts: Optional[int]
    name: Optional[str]
    md5_checksum: Optional[str]

class InputFileBig(TLObject):
    CONSTRUCTOR_ID = 0xFA4F0BB5
    FIELDS = [
        TLField("id", "long"),
        TLField("parts", "int"),
        TLField("name", "string"),
    ]
    id: Optional[int]
    parts: Optional[int]
    name: Optional[str]
class MessageMediaEmpty(TLObject):
    CONSTRUCTOR_ID = 1038967584
    FIELDS = []


class MessageMediaPhoto(TLObject):
    CONSTRUCTOR_ID = 1766936791
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("spoiler", "true", flag_group=0, flag_bit=3),
        TLField("photo", "Photo", flag_group=0, flag_bit=0),
        TLField("ttl_seconds", "int", flag_group=0, flag_bit=2),
    ]
    spoiler: Optional[bool]
    photo: Optional[TLObject]
    ttl_seconds: Optional[int]


class MessageMediaGeo(TLObject):
    CONSTRUCTOR_ID = 1457575028
    FIELDS = [TLField("geo", "GeoPoint")]
    geo: Optional[TLObject]


class MessageMediaContact(TLObject):
    CONSTRUCTOR_ID = 1882335561
    FIELDS = [
        TLField("phone_number", "string"),
        TLField("first_name", "string"),
        TLField("last_name", "string"),
        TLField("vcard", "string"),
        TLField("user_id", "long"),
    ]
    phone_number: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    vcard: Optional[str]
    user_id: Optional[int]


class MessageMediaUnsupported(TLObject):
    CONSTRUCTOR_ID = 2676290718
    FIELDS = []


class MessageMediaDocument(TLObject):
    CONSTRUCTOR_ID = 1291114285
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("nopremium", "true", flag_group=0, flag_bit=3),
        TLField("spoiler", "true", flag_group=0, flag_bit=4),
        TLField("document", "Document", flag_group=0, flag_bit=0),
        TLField("alt_document", "Document", flag_group=0, flag_bit=5),
        TLField("ttl_seconds", "int", flag_group=0, flag_bit=2),
    ]
    nopremium: Optional[bool]
    spoiler: Optional[bool]
    document: Optional[TLObject]
    alt_document: Optional[TLObject]
    ttl_seconds: Optional[int]


class MessageMediaWebPage(TLObject):
    CONSTRUCTOR_ID = 3723562043
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("force_large_media", "true", flag_group=0, flag_bit=0),
        TLField("force_small_media", "true", flag_group=0, flag_bit=1),
        TLField("manual", "true", flag_group=0, flag_bit=3),
        TLField("safe", "true", flag_group=0, flag_bit=4),
        TLField("webpage", "WebPage"),
    ]
    force_large_media: Optional[bool]
    force_small_media: Optional[bool]
    manual: Optional[bool]
    safe: Optional[bool]
    webpage: Optional[TLObject]


class MessageMediaVenue(TLObject):
    CONSTRUCTOR_ID = 784356159
    FIELDS = [
        TLField("geo", "GeoPoint"),
        TLField("title", "string"),
        TLField("address", "string"),
        TLField("provider", "string"),
        TLField("venue_id", "string"),
        TLField("venue_type", "string"),
    ]
    geo: Optional[TLObject]
    title: Optional[str]
    address: Optional[str]
    provider: Optional[str]
    venue_id: Optional[str]
    venue_type: Optional[str]


class MessageMediaGame(TLObject):
    CONSTRUCTOR_ID = 4256272392
    FIELDS = [TLField("game", "Game")]
    game: Optional[TLObject]


class MessageMediaInvoice(TLObject):
    CONSTRUCTOR_ID = 4138027219
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("shipping_address_requested", "true", flag_group=0, flag_bit=1),
        TLField("test", "true", flag_group=0, flag_bit=3),
        TLField("title", "string"),
        TLField("description", "string"),
        TLField("photo", "WebDocument", flag_group=0, flag_bit=0),
        TLField("receipt_msg_id", "int", flag_group=0, flag_bit=2),
        TLField("currency", "string"),
        TLField("total_amount", "long"),
        TLField("start_param", "string"),
        TLField("extended_media", "MessageExtendedMedia", flag_group=0, flag_bit=4),
    ]
    shipping_address_requested: Optional[bool]
    test: Optional[bool]
    title: Optional[str]
    description: Optional[str]
    photo: Optional[TLObject]
    receipt_msg_id: Optional[int]
    currency: Optional[str]
    total_amount: Optional[int]
    start_param: Optional[str]
    extended_media: Optional[TLObject]


class MessageMediaGeoLive(TLObject):
    CONSTRUCTOR_ID = 3108030054
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("geo", "GeoPoint"),
        TLField("heading", "int", flag_group=0, flag_bit=0),
        TLField("period", "int"),
        TLField("proximity_notification_radius", "int", flag_group=0, flag_bit=1),
    ]
    geo: Optional[TLObject]
    heading: Optional[int]
    period: Optional[int]
    proximity_notification_radius: Optional[int]


class MessageMediaPoll(TLObject):
    CONSTRUCTOR_ID = 1272375192
    FIELDS = [
        TLField("poll", "Poll"),
        TLField("results", "PollResults"),
    ]
    poll: Optional[TLObject]
    results: Optional[TLObject]


class MessageMediaDice(TLObject):
    CONSTRUCTOR_ID = 1065280907
    FIELDS = [
        TLField("value", "int"),
        TLField("emoticon", "string"),
    ]
    value: Optional[int]
    emoticon: Optional[str]


class MessageMediaStory(TLObject):
    CONSTRUCTOR_ID = 1758159491
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("via_mention", "true", flag_group=0, flag_bit=1),
        TLField("peer", "Peer"),
        TLField("id", "int"),
        TLField("story", "StoryItem", flag_group=0, flag_bit=0),
    ]
    via_mention: Optional[bool]
    peer: Optional[TLObject]
    id: Optional[int]
    story: Optional[TLObject]


class MessageMediaGiveaway(TLObject):
    CONSTRUCTOR_ID = 1478887012
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("only_new_subscribers", "true", flag_group=0, flag_bit=0),
        TLField("channels", "long", is_vector=True),
        TLField("countries_iso2", "string", flag_group=0, flag_bit=1, is_vector=True),
        TLField("quantity", "int"),
        TLField("months", "int"),
        TLField("until_date", "int"),
    ]
    only_new_subscribers: Optional[bool]
    channels: Optional[List[int]]
    countries_iso2: Optional[List[str]]
    quantity: Optional[int]
    months: Optional[int]
    until_date: Optional[int]


class MessageMediaPayment(TLObject):
    CONSTRUCTOR_ID = 48213848
    FIELDS = [
        TLField("payment_id", "long"),
        TLField("multimedia", "MessageMedia", is_vector=True),
    ]
    payment_id: Optional[int]
    multimedia: Optional[List[TLObject]]