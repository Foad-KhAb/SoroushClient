# contacts.*
from typing import List, Optional

from soroushclient.tl.base import TLField, TLObject


class ContactsContactsNotModified(TLObject):
    CONSTRUCTOR_ID = 0xB74BA9D2
    FIELDS = []

class ContactsContacts(TLObject):
    CONSTRUCTOR_ID = 0xEAE87E42
    FIELDS = [
        TLField("contacts", "Contact", is_vector=True),
        TLField("saved_count", "int"),
        TLField("users", "User", is_vector=True),
    ]
    contacts: Optional[List[TLObject]]
    saved_count: Optional[int]
    users: Optional[List[TLObject]]

class ContactsImportedContacts(TLObject):
    CONSTRUCTOR_ID = 0x77D01C3B
    FIELDS = [
        TLField("imported", "ImportedContact", is_vector=True),
        TLField("popular_invites", "PopularContact", is_vector=True),
        TLField("retry_contacts", "long", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    imported: Optional[List[TLObject]]
    popular_invites: Optional[List[TLObject]]
    retry_contacts: Optional[List[int]]
    users: Optional[List[TLObject]]

class ContactsBlocked(TLObject):
    CONSTRUCTOR_ID = 0x0ADE1591
    FIELDS = [
        TLField("blocked", "PeerBlocked", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    blocked: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class ContactsBlockedSlice(TLObject):
    CONSTRUCTOR_ID = 0xE1664194
    FIELDS = [
        TLField("count", "int"),
        TLField("blocked", "PeerBlocked", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    count: Optional[int]
    blocked: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class ContactsFound(TLObject):
    CONSTRUCTOR_ID = 0xB3134D9D
    FIELDS = [
        TLField("my_results", "Peer", is_vector=True),
        TLField("results", "Peer", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    my_results: Optional[List[TLObject]]
    results: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class ContactsResolvedPeer(TLObject):
    CONSTRUCTOR_ID = 0x7F077AD9
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    peer: Optional[TLObject]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class ContactsContactBirthdays(TLObject):
    CONSTRUCTOR_ID = 0x114FF30D
    FIELDS = [
        TLField("contacts", "ContactBirthday", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    contacts: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

# messages.*
class MessagesDialogs(TLObject):
    CONSTRUCTOR_ID = 0x15BA6C40
    FIELDS = [
        TLField("dialogs", "Dialog", is_vector=True),
        TLField("messages", "Message", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    dialogs: Optional[List[TLObject]]
    messages: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class MessagesDialogsSlice(TLObject):
    CONSTRUCTOR_ID = 0x71E094F3
    FIELDS = [
        TLField("count", "int"),
        TLField("dialogs", "Dialog", is_vector=True),
        TLField("messages", "Message", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    count: Optional[int]
    dialogs: Optional[List[TLObject]]
    messages: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class MessagesDialogsNotModified(TLObject):
    CONSTRUCTOR_ID = 0xF0E3E596
    FIELDS = [TLField("count", "int")]
    count: Optional[int]

class MessagesMessages(TLObject):
    CONSTRUCTOR_ID = 0x8C718E87
    FIELDS = [
        TLField("messages", "Message", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    messages: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class MessagesMessagesSlice(TLObject):
    CONSTRUCTOR_ID = 0x3A54685E
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("inexact", "true", flag_group=0, flag_bit=1),
        TLField("count", "int"),
        TLField("next_rate", "int", flag_group=0, flag_bit=0),
        TLField("offset_id_offset", "int", flag_group=0, flag_bit=2),
        TLField("messages", "Message", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    inexact: Optional[bool]
    count: Optional[int]
    next_rate: Optional[int]
    offset_id_offset: Optional[int]
    messages: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class MessagesChannelMessages(TLObject):
    CONSTRUCTOR_ID = 0xC776BA4E
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("inexact", "true", flag_group=0, flag_bit=1),
        TLField("pts", "int"),
        TLField("count", "int"),
        TLField("offset_id_offset", "int", flag_group=0, flag_bit=2),
        TLField("messages", "Message", is_vector=True),
        TLField("topics", "ForumTopic", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    inexact: Optional[bool]
    pts: Optional[int]
    count: Optional[int]
    offset_id_offset: Optional[int]
    messages: Optional[List[TLObject]]
    topics: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class MessagesMessagesNotModified(TLObject):
    CONSTRUCTOR_ID = 0x74535F21
    FIELDS = [TLField("count", "int")]
    count: Optional[int]

class MessagesChats(TLObject):
    CONSTRUCTOR_ID = 0x64FF9FD5
    FIELDS = [TLField("chats", "Chat", is_vector=True)]
    chats: Optional[List[TLObject]]

class MessagesChatsSlice(TLObject):
    CONSTRUCTOR_ID = 0x9CD81144
    FIELDS = [
        TLField("count", "int"),
        TLField("chats", "Chat", is_vector=True),
    ]
    count: Optional[int]
    chats: Optional[List[TLObject]]

class MessagesChatFull(TLObject):
    CONSTRUCTOR_ID = 0x05D7903A
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("full_chat", "ChatFull"),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("custom_info", "ChannelFullCustom", flag_group=0, flag_bit=0),
    ]

class MessagesAffectedHistory(TLObject):
    CONSTRUCTOR_ID = 0xB45C69D1
    FIELDS = [
        TLField("pts", "int"),
        TLField("pts_count", "int"),
        TLField("offset", "int"),
    ]
    pts: Optional[int]
    pts_count: Optional[int]
    offset: Optional[int]

class MessagesAffectedMessages(TLObject):
    CONSTRUCTOR_ID = 0x84D19185
    FIELDS = [
        TLField("pts", "int"),
        TLField("pts_count", "int"),
    ]
    pts: Optional[int]
    pts_count: Optional[int]

class MessagesMessageViews(TLObject):
    CONSTRUCTOR_ID = 0xB6C4F543
    FIELDS = [
        TLField("views", "MessageViews", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    views: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class MessagesPeerDialogs(TLObject):
    CONSTRUCTOR_ID = 0x3371C354
    FIELDS = [
        TLField("dialogs", "Dialog", is_vector=True),
        TLField("messages", "Message", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("state", "updates.State"),
    ]
    dialogs: Optional[List[TLObject]]
    messages: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]
    state: Optional[TLObject]

class MessagesPeerSettings(TLObject):
    CONSTRUCTOR_ID = 0x6880B94D
    FIELDS = [
        TLField("settings", "PeerSettings"),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    settings: Optional[TLObject]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class MessagesDialogFilters(TLObject):
    CONSTRUCTOR_ID = 0x2AD93719
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("tags_enabled", "true", flag_group=0, flag_bit=0),
        TLField("filters", "DialogFilter", is_vector=True),
    ]
    tags_enabled: Optional[bool]
    filters: Optional[List[TLObject]]

# users.*
class UsersUserFull(TLObject):
    CONSTRUCTOR_ID = 0x594C64B5
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("full_user", "UserFull"),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("customInfo", "UserFullCustom", flag_group=0, flag_bit=0),
    ]
    full_user: Optional[TLObject]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]
    customInfo: Optional[TLObject]

class UsersSavedMusicNotModified(TLObject):
    CONSTRUCTOR_ID = 0xE3878AA4
    FIELDS = [TLField("count", "int")]
    count: Optional[int]

class UsersSavedMusic(TLObject):
    CONSTRUCTOR_ID = 0x34A2F297
    FIELDS = [
        TLField("count", "int"),
        TLField("documents", "Document", is_vector=True),
    ]
    count: Optional[int]
    documents: Optional[List[TLObject]]

# channels.*
class ChannelsChannelParticipants(TLObject):
    CONSTRUCTOR_ID = 0x9AB0FEAF
    FIELDS = [
        TLField("count", "int"),
        TLField("participants", "ChannelParticipant", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    count: Optional[int]
    participants: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class ChannelsChannelParticipantsNotModified(TLObject):
    CONSTRUCTOR_ID = 0xF0173FE9
    FIELDS = []

class ChannelsChannelParticipant(TLObject):
    CONSTRUCTOR_ID = 0xDFB80317
    FIELDS = [
        TLField("participant", "ChannelParticipant"),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    participant: Optional[TLObject]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class ChannelsSendAsPeers(TLObject):
    CONSTRUCTOR_ID = 0xF496B0C6
    FIELDS = [
        TLField("peers", "SendAsPeer", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    peers: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

# photos.*
class PhotosPhotos(TLObject):
    CONSTRUCTOR_ID = 0x8DCA6AA5
    FIELDS = [
        TLField("photos", "Photo", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    photos: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class PhotosPhotosSlice(TLObject):
    CONSTRUCTOR_ID = 0x15051F54
    FIELDS = [
        TLField("count", "int"),
        TLField("photos", "Photo", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    count: Optional[int]
    photos: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class PhotosPhoto(TLObject):
    CONSTRUCTOR_ID = 0x20212CA8
    FIELDS = [
        TLField("photo", "Photo"),
        TLField("users", "User", is_vector=True),
    ]
    photo: Optional[TLObject]
    users: Optional[List[TLObject]]

# account.*
class AccountPrivacyRules(TLObject):
    CONSTRUCTOR_ID = 0x50A04E45
    FIELDS = [
        TLField("rules", "PrivacyRule", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
    rules: Optional[List[TLObject]]
    chats: Optional[List[TLObject]]
    users: Optional[List[TLObject]]

class AccountSavedMusicIdsNotModified(TLObject):
    CONSTRUCTOR_ID = 0x4FC81D6E
    FIELDS = []

class AccountSavedMusicIds(TLObject):
    CONSTRUCTOR_ID = 0x998D6636
    FIELDS = [TLField("ids", "long", is_vector=True)]
    ids: Optional[List[int]]