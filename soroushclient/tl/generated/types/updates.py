# All Update* classes, Updates*, updates.State, updates.Difference*
from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class UpdatesState(TLObject):
    CONSTRUCTOR_ID = 0xA56C2A3E
    FIELDS = [
        TLField("pts", "int"),
        TLField("qts", "int"),
        TLField("date", "int"),
        TLField("seq", "int"),
        TLField("unread_count", "int"),
    ]
    pts: Optional[int]
    qts: Optional[int]
    date: Optional[int]
    seq: Optional[int]
    unread_count: Optional[int]

class UpdatesDifferenceEmpty(TLObject):
    CONSTRUCTOR_ID = 0x5D75A138
    FIELDS = [
        TLField("date", "int"),
        TLField("seq", "int"),
    ]
    date: Optional[int]
    seq: Optional[int]

class UpdatesDifference(TLObject):
    CONSTRUCTOR_ID = 0x00F49CA0
    FIELDS = [
        TLField("new_messages", "Message", is_vector=True),
        TLField("new_encrypted_messages", "EncryptedMessage", is_vector=True),
        TLField("other_updates", "Update", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("state", "updates.State"),
    ]
    new_messages: Optional[List[TLObject]]
    new_encrypted_messages: Optional[List[TLObject]]
    other_updates: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]
    state: Optional[TLObject]

class UpdatesDifferenceSlice(TLObject):
    CONSTRUCTOR_ID = 0xA8FB1981
    FIELDS = [
        TLField("new_messages", "Message", is_vector=True),
        TLField("new_encrypted_messages", "EncryptedMessage", is_vector=True),
        TLField("other_updates", "Update", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("intermediate_state", "updates.State"),
    ]
    new_messages: Optional[List[TLObject]]
    new_encrypted_messages: Optional[List[TLObject]]
    other_updates: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]
    intermediate_state: Optional[TLObject]

class UpdatesDifferenceTooLong(TLObject):
    CONSTRUCTOR_ID = 0x4AFE8F6D
    FIELDS = [TLField("pts", "int")]
    pts: Optional[int]

class UpdatesTooLong(TLObject):
    CONSTRUCTOR_ID = 0xE317AF7E
    FIELDS = []

class UpdateShortMessage(TLObject):
    CONSTRUCTOR_ID = 0x313BC7F8
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("out", "true", flag_group=0, flag_bit=1),
        TLField("mentioned", "true", flag_group=0, flag_bit=4),
        TLField("media_unread", "true", flag_group=0, flag_bit=5),
        TLField("silent", "true", flag_group=0, flag_bit=13),
        TLField("id", "int"),
        TLField("user_id", "long"),
        TLField("message", "string"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
        TLField("date", "int"),
        TLField("fwd_from", "MessageFwdHeader", flag_group=0, flag_bit=2),
        TLField("via_bot_id", "long", flag_group=0, flag_bit=11),
        TLField("reply_to", "MessageReplyHeader", flag_group=0, flag_bit=3),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=7, is_vector=True),
        TLField("ttl_period", "int", flag_group=0, flag_bit=25),
    ]
    out: Optional[bool]
    mentioned: Optional[bool]
    media_unread: Optional[bool]
    silent: Optional[bool]
    id: Optional[int]
    user_id: Optional[int]
    message: Optional[str]
    pts: Optional[int]
    pts_count: Optional[int]
    date: Optional[int]
    fwd_from: Optional[TLObject]
    via_bot_id: Optional[int]
    reply_to: Optional[TLObject]
    entities: Optional[List[TLObject]]
    ttl_period: Optional[int]

class UpdateShortChatMessage(TLObject):
    CONSTRUCTOR_ID = 0x4D6DEEA5
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("out", "true", flag_group=0, flag_bit=1),
        TLField("mentioned", "true", flag_group=0, flag_bit=4),
        TLField("media_unread", "true", flag_group=0, flag_bit=5),
        TLField("silent", "true", flag_group=0, flag_bit=13),
        TLField("id", "int"),
        TLField("from_id", "long"),
        TLField("chat_id", "long"),
        TLField("message", "string"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
        TLField("date", "int"),
        TLField("fwd_from", "MessageFwdHeader", flag_group=0, flag_bit=2),
        TLField("via_bot_id", "long", flag_group=0, flag_bit=11),
        TLField("reply_to", "MessageReplyHeader", flag_group=0, flag_bit=3),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=7, is_vector=True),
        TLField("ttl_period", "int", flag_group=0, flag_bit=25),
    ]
    out: Optional[bool]
    mentioned: Optional[bool]
    media_unread: Optional[bool]
    silent: Optional[bool]
    id: Optional[int]
    from_id: Optional[int]
    chat_id: Optional[int]
    message: Optional[str]
    pts: Optional[int]
    pts_count: Optional[int]
    date: Optional[int]
    fwd_from: Optional[TLObject]
    via_bot_id: Optional[int]
    reply_to: Optional[TLObject]
    entities: Optional[List[TLObject]]
    ttl_period: Optional[int]

class UpdateShort(TLObject):
    CONSTRUCTOR_ID = 0x78D4DEC1
    FIELDS = [
        TLField("update", "Update"),
        TLField("date", "int"),
    ]
    update: Optional[TLObject]
    date: Optional[int]

class UpdatesCombined(TLObject):
    CONSTRUCTOR_ID = 0x725B04C3
    FIELDS = [
        TLField("updates", "Update", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("date", "int"),
        TLField("seq_start", "int"),
        TLField("seq", "int"),
    ]
    updates: Optional[List[TLObject]]
    users: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    date: Optional[int]
    seq_start: Optional[int]
    seq: Optional[int]

class Updates(TLObject):
    CONSTRUCTOR_ID = 0x74AE4240
    FIELDS = [
        TLField("updates", "Update", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("date", "int"),
        TLField("seq", "int"),
    ]
    updates: Optional[List[TLObject]]
    users: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    date: Optional[int]
    seq: Optional[int]

class UpdateShortSentMessage(TLObject):
    CONSTRUCTOR_ID = 0x9015E101
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("out", "true", flag_group=0, flag_bit=1),
        TLField("id", "int"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
        TLField("date", "int"),
        TLField("media", "MessageMedia", flag_group=0, flag_bit=9),
        TLField("entities", "MessageEntity", flag_group=0, flag_bit=7, is_vector=True),
        TLField("ttl_period", "int", flag_group=0, flag_bit=25),
    ]
    out: Optional[bool]
    id: Optional[int]
    pts: Optional[int]
    pts_count: Optional[int]
    date: Optional[int]
    media: Optional[TLObject]
    entities: Optional[List[TLObject]]
    ttl_period: Optional[int]

# Individual Update types (all the updateXxx classes)
class UpdateNewMessage(TLObject):
    CONSTRUCTOR_ID = 0x1F2B0AFD
    FIELDS = [
        TLField("message", "Message"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    message: Optional[TLObject]
    pts: Optional[int]
    pts_count: Optional[int]

class UpdateMessageID(TLObject):
    CONSTRUCTOR_ID = 0x4E90BFD6
    FIELDS = [
        TLField("id", "int"),
        TLField("random_id", "long"),
    ]
    id: Optional[int]
    random_id: Optional[int]

class UpdateDeleteMessages(TLObject):
    CONSTRUCTOR_ID = 0xA20DB0E5
    FIELDS = [
        TLField("messages", "int", is_vector=True),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    messages: Optional[List[int]]
    pts: Optional[int]
    pts_count: Optional[int]

class UpdateUserTyping(TLObject):
    CONSTRUCTOR_ID = 0xC01E857F
    FIELDS = [
        TLField("user_id", "long"),
        TLField("action", "SendMessageAction"),
    ]
    user_id: Optional[int]
    action: Optional[TLObject]

class UpdateChatUserTyping(TLObject):
    CONSTRUCTOR_ID = 0x83487AF0
    FIELDS = [
        TLField("chat_id", "long"),
        TLField("from_id", "Peer"),
        TLField("action", "SendMessageAction"),
    ]
    chat_id: Optional[int]
    from_id: Optional[TLObject]
    action: Optional[TLObject]

class UpdateChatParticipants(TLObject):
    CONSTRUCTOR_ID = 0x07761198
    FIELDS = [TLField("participants", "ChatParticipants")]
    participants: Optional[TLObject]

class UpdateUserStatus(TLObject):
    CONSTRUCTOR_ID = 0xE5BDF8DE
    FIELDS = [
        TLField("user_id", "long"),
        TLField("status", "UserStatus"),
    ]
    user_id: Optional[int]
    status: Optional[TLObject]

class UpdateUserName(TLObject):
    CONSTRUCTOR_ID = 0xA7848924
    FIELDS = [
        TLField("user_id", "long"),
        TLField("first_name", "string"),
        TLField("last_name", "string"),
        TLField("usernames", "Username", is_vector=True),
    ]
    user_id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    usernames: Optional[List[TLObject]]

class UpdateNewChannelMessage(TLObject):
    CONSTRUCTOR_ID = 0x62BA04D9
    FIELDS = [
        TLField("message", "Message"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    message: Optional[TLObject]
    pts: Optional[int]
    pts_count: Optional[int]

class UpdateEditMessage(TLObject):
    CONSTRUCTOR_ID = 0xE40370A3
    FIELDS = [
        TLField("message", "Message"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    message: Optional[TLObject]
    pts: Optional[int]
    pts_count: Optional[int]

class UpdateEditChannelMessage(TLObject):
    CONSTRUCTOR_ID = 0x1B3F4DF7
    FIELDS = [
        TLField("message", "Message"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    message: Optional[TLObject]
    pts: Optional[int]
    pts_count: Optional[int]

class UpdateChannel(TLObject):
    CONSTRUCTOR_ID = 0x635B4C09
    FIELDS = [TLField("channel_id", "long")]
    channel_id: Optional[int]

class UpdateUser(TLObject):
    CONSTRUCTOR_ID = 0x20529438
    FIELDS = [TLField("user_id", "long")]
    user_id: Optional[int]

class UpdateChat(TLObject):
    CONSTRUCTOR_ID = 0xF89A6A4E
    FIELDS = [TLField("chat_id", "long")]
    chat_id: Optional[int]

class UpdateReadHistoryInbox(TLObject):
    CONSTRUCTOR_ID = 0x9C974FDF
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("folder_id", "int", flag_group=0, flag_bit=0),
        TLField("peer", "Peer"),
        TLField("max_id", "int"),
        TLField("still_unread_count", "int"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    folder_id: Optional[int]
    peer: Optional[TLObject]
    max_id: Optional[int]
    still_unread_count: Optional[int]
    pts: Optional[int]
    pts_count: Optional[int]

class UpdateReadHistoryOutbox(TLObject):
    CONSTRUCTOR_ID = 0x2F2F21BF
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("max_id", "int"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    peer: Optional[TLObject]
    max_id: Optional[int]
    pts: Optional[int]
    pts_count: Optional[int]

class UpdateReadChannelInbox(TLObject):
    CONSTRUCTOR_ID = 0x922E6E10
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("folder_id", "int", flag_group=0, flag_bit=0),
        TLField("channel_id", "long"),
        TLField("max_id", "int"),
        TLField("still_unread_count", "int"),
        TLField("pts", "int"),
    ]
    folder_id: Optional[int]
    channel_id: Optional[int]
    max_id: Optional[int]
    still_unread_count: Optional[int]
    pts: Optional[int]

class UpdateDeleteChannelMessages(TLObject):
    CONSTRUCTOR_ID = 0xC32D5B12
    FIELDS = [
        TLField("channel_id", "long"),
        TLField("messages", "int", is_vector=True),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    channel_id: Optional[int]
    messages: Optional[List[int]]
    pts: Optional[int]
    pts_count: Optional[int]

class UpdateChannelMessageViews(TLObject):
    CONSTRUCTOR_ID = 0xF226AC08
    FIELDS = [
        TLField("channel_id", "long"),
        TLField("id", "int"),
        TLField("views", "int"),
    ]
    channel_id: Optional[int]
    id: Optional[int]
    views: Optional[int]

class UpdateNotifySettings(TLObject):
    CONSTRUCTOR_ID = 0xBEC268EF
    FIELDS = [
        TLField("peer", "NotifyPeer"),
        TLField("notify_settings", "PeerNotifySettings"),
    ]
    peer: Optional[TLObject]
    notify_settings: Optional[TLObject]

class UpdatePeerSettings(TLObject):
    CONSTRUCTOR_ID = 0x6A7E7366
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("settings", "PeerSettings"),
    ]
    peer: Optional[TLObject]
    settings: Optional[TLObject]

class UpdatePeerBlocked(TLObject):
    CONSTRUCTOR_ID = 0xEBE07752
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("blocked", "true", flag_group=0, flag_bit=0),
        TLField("blocked_my_stories_from", "true", flag_group=0, flag_bit=1),
        TLField("peer_id", "Peer"),
    ]
    blocked: Optional[bool]
    blocked_my_stories_from: Optional[bool]
    peer_id: Optional[TLObject]

class UpdatePrivacy(TLObject):
    CONSTRUCTOR_ID = 0xEE3B272A
    FIELDS = [
        TLField("key", "PrivacyKey"),
        TLField("rules", "PrivacyRule", is_vector=True),
    ]
    key: Optional[TLObject]
    rules: Optional[List[TLObject]]

class UpdateDcOptions(TLObject):
    CONSTRUCTOR_ID = 0x8E5E9873
    FIELDS = [TLField("dc_options", "DcOption", is_vector=True)]
    dc_options: Optional[List[TLObject]]

class UpdateConfig(TLObject):
    CONSTRUCTOR_ID = 0xA229DD06
    FIELDS = []

class UpdateLoginToken(TLObject):
    CONSTRUCTOR_ID = 0x564FE691
    FIELDS = []

class UpdateAutoSaveSettings(TLObject):
    CONSTRUCTOR_ID = 0xEC05B097
    FIELDS = []

class UpdateTheme(TLObject):
    CONSTRUCTOR_ID = 0x8216FBA3
    FIELDS = [TLField("theme", "Theme")]
    theme: Optional[TLObject]

class UpdatePendingJoinRequests(TLObject):
    CONSTRUCTOR_ID = 0x7063C3DB
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("requests_pending", "int"),
        TLField("recent_requesters", "long", is_vector=True),
    ]
    peer: Optional[TLObject]
    requests_pending: Optional[int]
    recent_requesters: Optional[List[int]]

class UpdateMessageReactions(TLObject):
    CONSTRUCTOR_ID = 0x5E1B3CB8
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "Peer"),
        TLField("msg_id", "int"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=0),
        TLField("reactions", "MessageReactions"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    top_msg_id: Optional[int]
    reactions: Optional[TLObject]

class UpdateStory(TLObject):
    CONSTRUCTOR_ID = 0x75B3B798
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("story", "StoryItem"),
    ]
    peer: Optional[TLObject]
    story: Optional[TLObject]

class UpdateReadStories(TLObject):
    CONSTRUCTOR_ID = 0xF74E932B
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("max_id", "int"),
    ]
    peer: Optional[TLObject]
    max_id: Optional[int]

class UpdateChannelParticipant(TLObject):
    CONSTRUCTOR_ID = 0x985D3ABB
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("via_chatlist", "true", flag_group=0, flag_bit=3),
        TLField("channel_id", "long"),
        TLField("date", "int"),
        TLField("actor_id", "long"),
        TLField("user_id", "long"),
        TLField("prev_participant", "ChannelParticipant", flag_group=0, flag_bit=0),
        TLField("new_participant", "ChannelParticipant", flag_group=0, flag_bit=1),
        TLField("invite", "ExportedChatInvite", flag_group=0, flag_bit=2),
        TLField("qts", "int"),
    ]
    via_chatlist: Optional[bool]
    channel_id: Optional[int]
    date: Optional[int]
    actor_id: Optional[int]
    user_id: Optional[int]
    prev_participant: Optional[TLObject]
    new_participant: Optional[TLObject]
    invite: Optional[TLObject]
    qts: Optional[int]

class UpdateThirdParty(TLObject):
    CONSTRUCTOR_ID = 0x7D2BBA1F
    FIELDS = [TLField("message", "ThirdPartyMessage")]
    message: Optional[TLObject]

class UpdateConferenceCallConnection(TLObject):
    CONSTRUCTOR_ID = 0x9ADDABD6
    FIELDS = [
        TLField("url", "string"),
        TLField("token", "string"),
    ]
    url: Optional[str]
    token: Optional[str]

class UpdateConferenceCall(TLObject):
    CONSTRUCTOR_ID = 0xA7FF4AB2
    FIELDS = [TLField("conference", "conference.ConferenceCall")]
    conference: Optional[TLObject]

class UpdateConferenceCallParticipant(TLObject):
    CONSTRUCTOR_ID = 0x925FEC07
    FIELDS = [
        TLField("conference", "InputConferenceCall"),
        TLField("participants", "ConferenceParticipant", is_vector=True),
        TLField("seq", "int"),
    ]
    conference: Optional[TLObject]
    participants: Optional[List[TLObject]]
    seq: Optional[int]


class UpdateNewAuthorization(TLObject):
    CONSTRUCTOR_ID = 2303831023
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("unconfirmed", "true", flag_group=0, flag_bit=0),
        TLField("hash", "long"),
        TLField("date", "int", flag_group=0, flag_bit=0),
        TLField("device", "string", flag_group=0, flag_bit=0),
        TLField("location", "string", flag_group=0, flag_bit=0),
    ]
    unconfirmed: Optional[bool]
    hash: Optional[int]
    date: Optional[int]
    device: Optional[str]
    location: Optional[str]


class UpdateNewEncryptedMessage(TLObject):
    CONSTRUCTOR_ID = 314359194
    FIELDS = [
        TLField("message", "EncryptedMessage"),
        TLField("qts", "int"),
    ]
    message: Optional[TLObject]
    qts: Optional[int]


class UpdateEncryptedChatTyping(TLObject):
    CONSTRUCTOR_ID = 386986326
    FIELDS = [TLField("chat_id", "int")]
    chat_id: Optional[int]


class UpdateEncryption(TLObject):
    CONSTRUCTOR_ID = 3030575245
    FIELDS = [
        TLField("chat", "EncryptedChat"),
        TLField("date", "int"),
    ]
    chat: Optional[TLObject]
    date: Optional[int]


class UpdateEncryptedMessagesRead(TLObject):
    CONSTRUCTOR_ID = 956179895
    FIELDS = [
        TLField("chat_id", "int"),
        TLField("max_date", "int"),
        TLField("date", "int"),
    ]
    chat_id: Optional[int]
    max_date: Optional[int]
    date: Optional[int]


class UpdateChatParticipantAdd(TLObject):
    CONSTRUCTOR_ID = 1037718609
    FIELDS = [
        TLField("chat_id", "long"),
        TLField("user_id", "long"),
        TLField("inviter_id", "long"),
        TLField("date", "int"),
        TLField("version", "int"),
    ]
    chat_id: Optional[int]
    user_id: Optional[int]
    inviter_id: Optional[int]
    date: Optional[int]
    version: Optional[int]


class UpdateChatParticipantDelete(TLObject):
    CONSTRUCTOR_ID = 3811523959
    FIELDS = [
        TLField("chat_id", "long"),
        TLField("user_id", "long"),
        TLField("version", "int"),
    ]
    chat_id: Optional[int]
    user_id: Optional[int]
    version: Optional[int]



class UpdateServiceNotification(TLObject):
    CONSTRUCTOR_ID = 3957614617
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("popup", "true", flag_group=0, flag_bit=0),
        TLField("invert_media", "true", flag_group=0, flag_bit=2),
        TLField("inbox_date", "int", flag_group=0, flag_bit=1),
        TLField("type", "string"),
        TLField("message", "string"),
        TLField("media", "MessageMedia"),
        TLField("entities", "MessageEntity", is_vector=True),
    ]
    popup: Optional[bool]
    invert_media: Optional[bool]
    inbox_date: Optional[int]
    type: Optional[str]
    message: Optional[str]
    media: Optional[TLObject]
    entities: Optional[List[TLObject]]


class UpdateUserPhone(TLObject):
    CONSTRUCTOR_ID = 88680979
    FIELDS = [
        TLField("user_id", "long"),
        TLField("phone", "string"),
    ]
    user_id: Optional[int]
    phone: Optional[str]



class UpdateWebPage(TLObject):
    CONSTRUCTOR_ID = 2139689491
    FIELDS = [
        TLField("webpage", "WebPage"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    webpage: Optional[TLObject]
    pts: Optional[int]
    pts_count: Optional[int]


class UpdateReadMessagesContents(TLObject):
    CONSTRUCTOR_ID = 4163006849
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("messages", "int", is_vector=True),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
        TLField("date", "int", flag_group=0, flag_bit=0),
    ]
    messages: Optional[List[int]]
    pts: Optional[int]
    pts_count: Optional[int]
    date: Optional[int]


class UpdateChannelTooLong(TLObject):
    CONSTRUCTOR_ID = 277713951
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("channel_id", "long"),
        TLField("pts", "int", flag_group=0, flag_bit=0),
    ]
    channel_id: Optional[int]
    pts: Optional[int]


class UpdateChatParticipantAdmin(TLObject):
    CONSTRUCTOR_ID = 3620364706
    FIELDS = [
        TLField("chat_id", "long"),
        TLField("user_id", "long"),
        TLField("is_admin", "Bool"),
        TLField("version", "int"),
    ]
    chat_id: Optional[int]
    user_id: Optional[int]
    is_admin: Optional[bool]
    version: Optional[int]


class UpdateNewStickerSet(TLObject):
    CONSTRUCTOR_ID = 1753886890
    FIELDS = [TLField("stickerset", "messages.StickerSet")]
    stickerset: Optional[TLObject]


class UpdateStickerSetsOrder(TLObject):
    CONSTRUCTOR_ID = 196268545
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("masks", "true", flag_group=0, flag_bit=0),
        TLField("emojis", "true", flag_group=0, flag_bit=1),
        TLField("order", "long", is_vector=True),
    ]
    masks: Optional[bool]
    emojis: Optional[bool]
    order: Optional[List[int]]


class UpdateStickerSets(TLObject):
    CONSTRUCTOR_ID = 834816008
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("masks", "true", flag_group=0, flag_bit=0),
        TLField("emojis", "true", flag_group=0, flag_bit=1),
    ]
    masks: Optional[bool]
    emojis: Optional[bool]


class UpdateSavedGifs(TLObject):
    CONSTRUCTOR_ID = 2473931806
    FIELDS = []


class UpdateBotInlineQuery(TLObject):
    CONSTRUCTOR_ID = 1232025500
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("query_id", "long"),
        TLField("user_id", "long"),
        TLField("query", "string"),
        TLField("geo", "GeoPoint", flag_group=0, flag_bit=0),
        TLField("peer_type", "InlineQueryPeerType", flag_group=0, flag_bit=1),
        TLField("offset", "string"),
    ]
    query_id: Optional[int]
    user_id: Optional[int]
    query: Optional[str]
    geo: Optional[TLObject]
    peer_type: Optional[TLObject]
    offset: Optional[str]


class UpdateBotInlineSend(TLObject):
    CONSTRUCTOR_ID = 317794823
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("user_id", "long"),
        TLField("query", "string"),
        TLField("geo", "GeoPoint", flag_group=0, flag_bit=0),
        TLField("id", "string"),
        TLField("msg_id", "InputBotInlineMessageID", flag_group=0, flag_bit=1),
    ]
    user_id: Optional[int]
    query: Optional[str]
    geo: Optional[TLObject]
    id: Optional[str]
    msg_id: Optional[TLObject]


class UpdateBotCallbackQuery(TLObject):
    CONSTRUCTOR_ID = 3117401229
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("query_id", "long"),
        TLField("user_id", "long"),
        TLField("peer", "Peer"),
        TLField("msg_id", "int"),
        TLField("chat_instance", "long"),
        TLField("data", "bytes", flag_group=0, flag_bit=0),
        TLField("game_short_name", "string", flag_group=0, flag_bit=1),
    ]
    query_id: Optional[int]
    user_id: Optional[int]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    chat_instance: Optional[int]
    data: Optional[bytes]
    game_short_name: Optional[str]



class UpdateInlineBotCallbackQuery(TLObject):
    CONSTRUCTOR_ID = 1763610706
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("query_id", "long"),
        TLField("user_id", "long"),
        TLField("msg_id", "InputBotInlineMessageID"),
        TLField("chat_instance", "long"),
        TLField("data", "bytes", flag_group=0, flag_bit=0),
        TLField("game_short_name", "string", flag_group=0, flag_bit=1),
    ]
    query_id: Optional[int]
    user_id: Optional[int]
    msg_id: Optional[TLObject]
    chat_instance: Optional[int]
    data: Optional[bytes]
    game_short_name: Optional[str]


class UpdateReadChannelOutbox(TLObject):
    CONSTRUCTOR_ID = 3076495785
    FIELDS = [
        TLField("channel_id", "long"),
        TLField("max_id", "int"),
    ]
    channel_id: Optional[int]
    max_id: Optional[int]


class UpdateDraftMessage(TLObject):
    CONSTRUCTOR_ID = 457829485
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "Peer"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=0),
        TLField("draft", "DraftMessage"),
    ]
    peer: Optional[TLObject]
    top_msg_id: Optional[int]
    draft: Optional[TLObject]


class UpdateReadFeaturedStickers(TLObject):
    CONSTRUCTOR_ID = 1461528386
    FIELDS = []


class UpdateRecentStickers(TLObject):
    CONSTRUCTOR_ID = 2588027936
    FIELDS = []


class UpdatePtsChanged(TLObject):
    CONSTRUCTOR_ID = 861169551
    FIELDS = []


class UpdateChannelWebPage(TLObject):
    CONSTRUCTOR_ID = 791390623
    FIELDS = [
        TLField("channel_id", "long"),
        TLField("webpage", "WebPage"),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    channel_id: Optional[int]
    webpage: Optional[TLObject]
    pts: Optional[int]
    pts_count: Optional[int]


class UpdateDialogPinned(TLObject):
    CONSTRUCTOR_ID = 1852826908
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("pinned", "true", flag_group=0, flag_bit=0),
        TLField("folder_id", "int", flag_group=0, flag_bit=1),
        TLField("peer", "DialogPeer"),
    ]
    pinned: Optional[bool]
    folder_id: Optional[int]
    peer: Optional[TLObject]


class UpdatePinnedDialogs(TLObject):
    CONSTRUCTOR_ID = 4195302562
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("folder_id", "int", flag_group=0, flag_bit=1),
        TLField("order", "DialogPeer", flag_group=0, flag_bit=0, is_vector=True),
    ]
    folder_id: Optional[int]
    order: Optional[List[TLObject]]


class UpdateBotWebhookJSON(TLObject):
    CONSTRUCTOR_ID = 2199371971
    FIELDS = [TLField("data", "DataJSON")]
    data: Optional[TLObject]


class UpdateBotWebhookJSONQuery(TLObject):
    CONSTRUCTOR_ID = 2610053286
    FIELDS = [
        TLField("query_id", "long"),
        TLField("data", "DataJSON"),
        TLField("timeout", "int"),
    ]
    query_id: Optional[int]
    data: Optional[TLObject]
    timeout: Optional[int]


class UpdateBotShippingQuery(TLObject):
    CONSTRUCTOR_ID = 3048144253
    FIELDS = [
        TLField("query_id", "long"),
        TLField("user_id", "long"),
        TLField("payload", "bytes"),
        TLField("shipping_address", "PostAddress"),
    ]
    query_id: Optional[int]
    user_id: Optional[int]
    payload: Optional[bytes]
    shipping_address: Optional[TLObject]


class UpdateBotPrecheckoutQuery(TLObject):
    CONSTRUCTOR_ID = 2359990934
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("query_id", "long"),
        TLField("user_id", "long"),
        TLField("payload", "bytes"),
        TLField("info", "PaymentRequestedInfo", flag_group=0, flag_bit=0),
        TLField("shipping_option_id", "string", flag_group=0, flag_bit=1),
        TLField("currency", "string"),
        TLField("total_amount", "long"),
    ]
    query_id: Optional[int]
    user_id: Optional[int]
    payload: Optional[bytes]
    info: Optional[TLObject]
    shipping_option_id: Optional[str]
    currency: Optional[str]
    total_amount: Optional[int]


class UpdatePhoneCall(TLObject):
    CONSTRUCTOR_ID = 2869914398
    FIELDS = [TLField("phone_call", "PhoneCall")]
    phone_call: Optional[TLObject]


class UpdateLangPackTooLong(TLObject):
    CONSTRUCTOR_ID = 1180041828
    FIELDS = [TLField("lang_code", "string")]
    lang_code: Optional[str]


class UpdateLangPack(TLObject):
    CONSTRUCTOR_ID = 1442983757
    FIELDS = [TLField("difference", "LangPackDifference")]
    difference: Optional[TLObject]


class UpdateFavedStickers(TLObject):
    CONSTRUCTOR_ID = 3843135853
    FIELDS = []


class UpdateChannelReadMessagesContents(TLObject):
    CONSTRUCTOR_ID = 3928556893
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("channel_id", "long"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=0),
        TLField("messages", "int", is_vector=True),
    ]
    channel_id: Optional[int]
    top_msg_id: Optional[int]
    messages: Optional[List[int]]


class UpdateContactsReset(TLObject):
    CONSTRUCTOR_ID = 1887741886
    FIELDS = []


class UpdateChannelAvailableMessages(TLObject):
    CONSTRUCTOR_ID = 2990524056
    FIELDS = [
        TLField("channel_id", "long"),
        TLField("available_min_id", "int"),
    ]
    channel_id: Optional[int]
    available_min_id: Optional[int]


class UpdateDialogUnreadMark(TLObject):
    CONSTRUCTOR_ID = 3781450179
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("unread", "true", flag_group=0, flag_bit=0),
        TLField("peer", "DialogPeer"),
    ]
    unread: Optional[bool]
    peer: Optional[TLObject]


class UpdateMessagePoll(TLObject):
    CONSTRUCTOR_ID = 2896258427
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("poll_id", "long"),
        TLField("poll", "Poll", flag_group=0, flag_bit=0),
        TLField("results", "PollResults"),
    ]
    poll_id: Optional[int]
    poll: Optional[TLObject]
    results: Optional[TLObject]


class UpdateChatDefaultBannedRights(TLObject):
    CONSTRUCTOR_ID = 1421875280
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("default_banned_rights", "ChatBannedRights"),
        TLField("version", "int"),
    ]
    peer: Optional[TLObject]
    default_banned_rights: Optional[TLObject]
    version: Optional[int]


class UpdateFolderPeers(TLObject):
    CONSTRUCTOR_ID = 422972864
    FIELDS = [
        TLField("folder_peers", "FolderPeer", is_vector=True),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    folder_peers: Optional[List[TLObject]]
    pts: Optional[int]
    pts_count: Optional[int]

class UpdatePeerLocated(TLObject):
    CONSTRUCTOR_ID = 3031420848
    FIELDS = [TLField("peers", "PeerLocated", is_vector=True)]
    peers: Optional[List[TLObject]]


class UpdateNewScheduledMessage(TLObject):
    CONSTRUCTOR_ID = 967122427
    FIELDS = [TLField("message", "Message")]
    message: Optional[TLObject]


class UpdateDeleteScheduledMessages(TLObject):
    CONSTRUCTOR_ID = 2424728814
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("messages", "int", is_vector=True),
    ]
    peer: Optional[TLObject]
    messages: Optional[List[int]]


class UpdateGeoLiveViewed(TLObject):
    CONSTRUCTOR_ID = 2267003193
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("msg_id", "int"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]



class UpdateMessagePollVote(TLObject):
    CONSTRUCTOR_ID = 619974263
    FIELDS = [
        TLField("poll_id", "long"),
        TLField("peer", "Peer"),
        TLField("options", "bytes", is_vector=True),
        TLField("qts", "int"),
    ]
    poll_id: Optional[int]
    peer: Optional[TLObject]
    options: Optional[List[bytes]]
    qts: Optional[int]


class UpdateDialogFilter(TLObject):
    CONSTRUCTOR_ID = 654302845
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("id", "int"),
        TLField("filter", "DialogFilter", flag_group=0, flag_bit=0),
    ]
    id: Optional[int]
    filter: Optional[TLObject]


class UpdateDialogFilterOrder(TLObject):
    CONSTRUCTOR_ID = 2782339333
    FIELDS = [TLField("order", "int", is_vector=True)]
    order: Optional[List[int]]


class UpdateDialogFilters(TLObject):
    CONSTRUCTOR_ID = 889491791
    FIELDS = []


class UpdatePhoneCallSignalingData(TLObject):
    CONSTRUCTOR_ID = 643940105
    FIELDS = [
        TLField("phone_call_id", "long"),
        TLField("data", "bytes"),
    ]
    phone_call_id: Optional[int]
    data: Optional[bytes]


class UpdateChannelMessageForwards(TLObject):
    CONSTRUCTOR_ID = 3533318132
    FIELDS = [
        TLField("channel_id", "long"),
        TLField("id", "int"),
        TLField("forwards", "int"),
    ]
    channel_id: Optional[int]
    id: Optional[int]
    forwards: Optional[int]


class UpdateReadChannelDiscussionInbox(TLObject):
    CONSTRUCTOR_ID = 3601962310
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("channel_id", "long"),
        TLField("top_msg_id", "int"),
        TLField("read_max_id", "int"),
        TLField("broadcast_id", "long", flag_group=0, flag_bit=0),
        TLField("broadcast_post", "int", flag_group=0, flag_bit=0),
    ]
    channel_id: Optional[int]
    top_msg_id: Optional[int]
    read_max_id: Optional[int]
    broadcast_id: Optional[int]
    broadcast_post: Optional[int]


class UpdateReadChannelDiscussionOutbox(TLObject):
    CONSTRUCTOR_ID = 1767677564
    FIELDS = [
        TLField("channel_id", "long"),
        TLField("top_msg_id", "int"),
        TLField("read_max_id", "int"),
    ]
    channel_id: Optional[int]
    top_msg_id: Optional[int]
    read_max_id: Optional[int]


class UpdateChannelUserTyping(TLObject):
    CONSTRUCTOR_ID = 2357774627
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("channel_id", "long"),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=0),
        TLField("from_id", "Peer"),
        TLField("action", "SendMessageAction"),
    ]
    channel_id: Optional[int]
    top_msg_id: Optional[int]
    from_id: Optional[TLObject]
    action: Optional[TLObject]


class UpdatePinnedMessages(TLObject):
    CONSTRUCTOR_ID = 3984976565
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("pinned", "true", flag_group=0, flag_bit=0),
        TLField("peer", "Peer"),
        TLField("messages", "int", is_vector=True),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    pinned: Optional[bool]
    peer: Optional[TLObject]
    messages: Optional[List[int]]
    pts: Optional[int]
    pts_count: Optional[int]


class UpdatePinnedChannelMessages(TLObject):
    CONSTRUCTOR_ID = 1538885128
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("pinned", "true", flag_group=0, flag_bit=0),
        TLField("channel_id", "long"),
        TLField("messages", "int", is_vector=True),
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    pinned: Optional[bool]
    channel_id: Optional[int]
    messages: Optional[List[int]]
    pts: Optional[int]
    pts_count: Optional[int]


class UpdateGroupCallParticipants(TLObject):
    CONSTRUCTOR_ID = 4075543374
    FIELDS = [
        TLField("call", "InputGroupCall"),
        TLField("participants", "GroupCallParticipant", is_vector=True),
        TLField("version", "int"),
    ]
    call: Optional[TLObject]
    participants: Optional[List[TLObject]]
    version: Optional[int]


class UpdateGroupCall(TLObject):
    CONSTRUCTOR_ID = 347227392
    FIELDS = [
        TLField("chat_id", "long"),
        TLField("call", "GroupCall"),
    ]
    chat_id: Optional[int]
    call: Optional[TLObject]


class UpdatePeerHistoryTTL(TLObject):
    CONSTRUCTOR_ID = 3147544997
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("peer", "Peer"),
        TLField("ttl_period", "int", flag_group=0, flag_bit=0),
    ]
    peer: Optional[TLObject]
    ttl_period: Optional[int]


class UpdateChatParticipant(TLObject):
    CONSTRUCTOR_ID = 3498534458
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("chat_id", "long"),
        TLField("date", "int"),
        TLField("actor_id", "long"),
        TLField("user_id", "long"),
        TLField("prev_participant", "ChatParticipant", flag_group=0, flag_bit=0),
        TLField("new_participant", "ChatParticipant", flag_group=0, flag_bit=1),
        TLField("invite", "ExportedChatInvite", flag_group=0, flag_bit=2),
        TLField("qts", "int"),
    ]
    chat_id: Optional[int]
    date: Optional[int]
    actor_id: Optional[int]
    user_id: Optional[int]
    prev_participant: Optional[TLObject]
    new_participant: Optional[TLObject]
    invite: Optional[TLObject]
    qts: Optional[int]


class UpdateBotStopped(TLObject):
    CONSTRUCTOR_ID = 3297184329
    FIELDS = [
        TLField("user_id", "long"),
        TLField("date", "int"),
        TLField("stopped", "Bool"),
        TLField("qts", "int"),
    ]
    user_id: Optional[int]
    date: Optional[int]
    stopped: Optional[bool]
    qts: Optional[int]


class UpdateGroupCallConnection(TLObject):
    CONSTRUCTOR_ID = 192428418
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("presentation", "true", flag_group=0, flag_bit=0),
        TLField("params", "DataJSON"),
    ]
    presentation: Optional[bool]
    params: Optional[TLObject]


class UpdateBotCommands(TLObject):
    CONSTRUCTOR_ID = 1299263278
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("bot_id", "long"),
        TLField("commands", "BotCommand", is_vector=True),
    ]
    peer: Optional[TLObject]
    bot_id: Optional[int]
    commands: Optional[List[TLObject]]


class UpdateBotChatInviteRequester(TLObject):
    CONSTRUCTOR_ID = 299870598
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("date", "int"),
        TLField("user_id", "long"),
        TLField("about", "string"),
        TLField("invite", "ExportedChatInvite"),
        TLField("qts", "int"),
    ]
    peer: Optional[TLObject]
    date: Optional[int]
    user_id: Optional[int]
    about: Optional[str]
    invite: Optional[TLObject]
    qts: Optional[int]


class UpdateAttachMenuBots(TLObject):
    CONSTRUCTOR_ID = 397910539
    FIELDS = []


class UpdateWebViewResultSent(TLObject):
    CONSTRUCTOR_ID = 361936797
    FIELDS = [TLField("query_id", "long")]
    query_id: Optional[int]


class UpdateBotMenuButton(TLObject):
    CONSTRUCTOR_ID = 347625491
    FIELDS = [
        TLField("bot_id", "long"),
        TLField("button", "BotMenuButton"),
    ]
    bot_id: Optional[int]
    button: Optional[TLObject]


class UpdateSavedRingtones(TLObject):
    CONSTRUCTOR_ID = 1960361625
    FIELDS = []


class UpdateTranscribedAudio(TLObject):
    CONSTRUCTOR_ID = 8703322
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("pending", "true", flag_group=0, flag_bit=0),
        TLField("peer", "Peer"),
        TLField("msg_id", "int"),
        TLField("transcription_id", "long"),
        TLField("text", "string"),
    ]
    pending: Optional[bool]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    transcription_id: Optional[int]
    text: Optional[str]


class UpdateReadFeaturedEmojiStickers(TLObject):
    CONSTRUCTOR_ID = 4216080748
    FIELDS = []


class UpdateUserEmojiStatus(TLObject):
    CONSTRUCTOR_ID = 674706841
    FIELDS = [
        TLField("user_id", "long"),
        TLField("emoji_status", "EmojiStatus"),
    ]
    user_id: Optional[int]
    emoji_status: Optional[TLObject]


class UpdateRecentEmojiStatuses(TLObject):
    CONSTRUCTOR_ID = 821314523
    FIELDS = []


class UpdateRecentReactions(TLObject):
    CONSTRUCTOR_ID = 1870160884
    FIELDS = []


class UpdateMoveStickerSetToTop(TLObject):
    CONSTRUCTOR_ID = 2264715141
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("masks", "true", flag_group=0, flag_bit=0),
        TLField("emojis", "true", flag_group=0, flag_bit=1),
        TLField("stickerset", "long"),
    ]
    masks: Optional[bool]
    emojis: Optional[bool]
    stickerset: Optional[int]


class UpdateMessageExtendedMedia(TLObject):
    CONSTRUCTOR_ID = 1517529484
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("msg_id", "int"),
        TLField("extended_media", "MessageExtendedMedia"),
    ]
    peer: Optional[TLObject]
    msg_id: Optional[int]
    extended_media: Optional[TLObject]


class UpdateChannelPinnedTopic(TLObject):
    CONSTRUCTOR_ID = 422509539
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("pinned", "true", flag_group=0, flag_bit=0),
        TLField("channel_id", "long"),
        TLField("topic_id", "int"),
    ]
    pinned: Optional[bool]
    channel_id: Optional[int]
    topic_id: Optional[int]


class UpdateChannelPinnedTopics(TLObject):
    CONSTRUCTOR_ID = 4263085570
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("channel_id", "long"),
        TLField("order", "int", flag_group=0, flag_bit=0, is_vector=True),
    ]
    channel_id: Optional[int]
    order: Optional[List[int]]


class UpdateGroupInvitePrivacyForbidden(TLObject):
    CONSTRUCTOR_ID = 3438316246
    FIELDS = [TLField("user_id", "long")]
    user_id: Optional[int]


class UpdateStoryID(TLObject):
    CONSTRUCTOR_ID = 468923833
    FIELDS = [
        TLField("id", "int"),
        TLField("random_id", "long"),
    ]
    id: Optional[int]
    random_id: Optional[int]


class UpdateStoriesStealthMode(TLObject):
    CONSTRUCTOR_ID = 738741697
    FIELDS = [TLField("stealth_mode", "StoriesStealthMode")]
    stealth_mode: Optional[TLObject]


class UpdateSentStoryReaction(TLObject):
    CONSTRUCTOR_ID = 2103604867
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("story_id", "int"),
        TLField("reaction", "Reaction"),
    ]
    peer: Optional[TLObject]
    story_id: Optional[int]
    reaction: Optional[TLObject]


class UpdateBotChatBoost(TLObject):
    CONSTRUCTOR_ID = 2421019804
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("boost", "Boost"),
        TLField("qts", "int"),
    ]
    peer: Optional[TLObject]
    boost: Optional[TLObject]
    qts: Optional[int]


class UpdateChannelViewForumAsMessages(TLObject):
    CONSTRUCTOR_ID = 129403168
    FIELDS = [
        TLField("channel_id", "long"),
        TLField("enabled", "Bool"),
    ]
    channel_id: Optional[int]
    enabled: Optional[bool]


class UpdatePeerWallpaper(TLObject):
    CONSTRUCTOR_ID = 2923368477
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("wallpaper_overridden", "true", flag_group=0, flag_bit=1),
        TLField("peer", "Peer"),
        TLField("wallpaper", "WallPaper", flag_group=0, flag_bit=0),
    ]
    wallpaper_overridden: Optional[bool]
    peer: Optional[TLObject]
    wallpaper: Optional[TLObject]