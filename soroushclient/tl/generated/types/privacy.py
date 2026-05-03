from typing import Optional, List

from soroushclient.tl.base import TLField, TLObject


class InputPrivacyKeyStatusTimestamp(TLObject):
    CONSTRUCTOR_ID = 0x4F96CB18
    FIELDS = []

class InputPrivacyKeyChatInvite(TLObject):
    CONSTRUCTOR_ID = 0xBDFB0426
    FIELDS = []

class InputPrivacyKeyPhoneCall(TLObject):
    CONSTRUCTOR_ID = 0xFABADC5F
    FIELDS = []

class InputPrivacyKeyPhoneP2P(TLObject):
    CONSTRUCTOR_ID = 0xDB9E70D2
    FIELDS = []

class InputPrivacyKeyForwards(TLObject):
    CONSTRUCTOR_ID = 0xA4DD4C08
    FIELDS = []

class InputPrivacyKeyProfilePhoto(TLObject):
    CONSTRUCTOR_ID = 0x5719BACC
    FIELDS = []

class InputPrivacyKeyPhoneNumber(TLObject):
    CONSTRUCTOR_ID = 0x0352DAFA
    FIELDS = []

class InputPrivacyKeyAddedByPhone(TLObject):
    CONSTRUCTOR_ID = 0xD1219BDD
    FIELDS = []

class InputPrivacyKeyVoiceMessages(TLObject):
    CONSTRUCTOR_ID = 0xAEE69D68
    FIELDS = []

class InputPrivacyKeyAbout(TLObject):
    CONSTRUCTOR_ID = 0x3823CC40
    FIELDS = []

class InputPrivacyKeyReceiveMessage(TLObject):
    CONSTRUCTOR_ID = 0xE5207388
    FIELDS = []

class InputPrivacyKeyGender(TLObject):
    CONSTRUCTOR_ID = 0x9ECCED02
    FIELDS = []

class InputPrivacyKeyBirthday(TLObject):
    CONSTRUCTOR_ID = 0xD65A11CC
    FIELDS = []

class PrivacyKeyStatusTimestamp(TLObject):
    CONSTRUCTOR_ID = 0xBC2EAB30
    FIELDS = []

class PrivacyKeyChatInvite(TLObject):
    CONSTRUCTOR_ID = 0x500E6DFA
    FIELDS = []

class PrivacyKeyPhoneCall(TLObject):
    CONSTRUCTOR_ID = 0x3D662B7B
    FIELDS = []

class PrivacyKeyPhoneP2P(TLObject):
    CONSTRUCTOR_ID = 0x39491CC8
    FIELDS = []

class PrivacyKeyForwards(TLObject):
    CONSTRUCTOR_ID = 0x69EC56A3
    FIELDS = []

class PrivacyKeyProfilePhoto(TLObject):
    CONSTRUCTOR_ID = 0x96151FED
    FIELDS = []

class PrivacyKeyPhoneNumber(TLObject):
    CONSTRUCTOR_ID = 0xD19AE46D
    FIELDS = []

class PrivacyKeyAddedByPhone(TLObject):
    CONSTRUCTOR_ID = 0x42FFD42B
    FIELDS = []

class PrivacyKeyVoiceMessages(TLObject):
    CONSTRUCTOR_ID = 0x0697F414
    FIELDS = []

class PrivacyKeyAbout(TLObject):
    CONSTRUCTOR_ID = 0xA486B761
    FIELDS = []

class PrivacyKeyReceiveMessage(TLObject):
    CONSTRUCTOR_ID = 0x84FBC6FF
    FIELDS = []

class PrivacyKeyGender(TLObject):
    CONSTRUCTOR_ID = 0x5D5201B6
    FIELDS = []

class PrivacyKeyBirthday(TLObject):
    CONSTRUCTOR_ID = 0x2000A518
    FIELDS = []

class InputPrivacyValueAllowContacts(TLObject):
    CONSTRUCTOR_ID = 0x0D09E07B
    FIELDS = []

class InputPrivacyValueAllowAll(TLObject):
    CONSTRUCTOR_ID = 0x184B35CE
    FIELDS = []

class InputPrivacyValueAllowUsers(TLObject):
    CONSTRUCTOR_ID = 0x131CC67F
    FIELDS = [TLField("users", "InputUser", is_vector=True)]
    users: Optional[List[TLObject]]

class InputPrivacyValueDisallowContacts(TLObject):
    CONSTRUCTOR_ID = 0x0BA52007
    FIELDS = []

class InputPrivacyValueDisallowAll(TLObject):
    CONSTRUCTOR_ID = 0xD66B66C9
    FIELDS = []

class InputPrivacyValueDisallowUsers(TLObject):
    CONSTRUCTOR_ID = 0x90110467
    FIELDS = [TLField("users", "InputUser", is_vector=True)]
    users: Optional[List[TLObject]]

class InputPrivacyValueAllowChatParticipants(TLObject):
    CONSTRUCTOR_ID = 0x840649CF
    FIELDS = [TLField("chats", "long", is_vector=True)]
    chats: Optional[List[int]]

class InputPrivacyValueDisallowChatParticipants(TLObject):
    CONSTRUCTOR_ID = 0xE94F0F86
    FIELDS = [TLField("chats", "long", is_vector=True)]
    chats: Optional[List[int]]

class InputPrivacyValueAllowCloseFriends(TLObject):
    CONSTRUCTOR_ID = 0x2F453E49
    FIELDS = []

class PrivacyValueAllowContacts(TLObject):
    CONSTRUCTOR_ID = 0xFFFE1BAC
    FIELDS = []

class PrivacyValueAllowAll(TLObject):
    CONSTRUCTOR_ID = 0x65427B82
    FIELDS = []

class PrivacyValueAllowUsers(TLObject):
    CONSTRUCTOR_ID = 0xB8905FB2
    FIELDS = [TLField("users", "long", is_vector=True)]
    users: Optional[List[int]]

class PrivacyValueDisallowContacts(TLObject):
    CONSTRUCTOR_ID = 0xF888FA1A
    FIELDS = []

class PrivacyValueDisallowAll(TLObject):
    CONSTRUCTOR_ID = 0x8B73E763
    FIELDS = []

class PrivacyValueDisallowUsers(TLObject):
    CONSTRUCTOR_ID = 0xE4621141
    FIELDS = [TLField("users", "long", is_vector=True)]
    users: Optional[List[int]]

class PrivacyValueAllowChatParticipants(TLObject):
    CONSTRUCTOR_ID = 0x6B134E8E
    FIELDS = [TLField("chats", "long", is_vector=True)]
    chats: Optional[List[int]]

class PrivacyValueDisallowChatParticipants(TLObject):
    CONSTRUCTOR_ID = 0x41C87565
    FIELDS = [TLField("chats", "long", is_vector=True)]
    chats: Optional[List[int]]

class PrivacyValueAllowCloseFriends(TLObject):
    CONSTRUCTOR_ID = 0xF7E8D89B
    FIELDS = []

class RestrictionReason(TLObject):
    CONSTRUCTOR_ID = 0xD072ACB4
    FIELDS = [
        TLField("platform", "string"),
        TLField("reason", "string"),
        TLField("text", "string"),
    ]
    platform: Optional[str]
    reason: Optional[str]
    text: Optional[str]

class PeerSettings(TLObject):
    CONSTRUCTOR_ID = 0xA518110D
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("report_spam", "true", flag_group=0, flag_bit=0),
        TLField("add_contact", "true", flag_group=0, flag_bit=1),
        TLField("block_contact", "true", flag_group=0, flag_bit=2),
        TLField("share_contact", "true", flag_group=0, flag_bit=3),
        TLField("need_contacts_exception", "true", flag_group=0, flag_bit=4),
        TLField("report_geo", "true", flag_group=0, flag_bit=5),
        TLField("autoarchived", "true", flag_group=0, flag_bit=7),
        TLField("invite_members", "true", flag_group=0, flag_bit=8),
        TLField("request_chat_broadcast", "true", flag_group=0, flag_bit=10),
        TLField("geo_distance", "int", flag_group=0, flag_bit=6),
        TLField("request_chat_title", "string", flag_group=0, flag_bit=9),
        TLField("request_chat_date", "int", flag_group=0, flag_bit=9),
    ]
    report_spam: Optional[bool]
    add_contact: Optional[bool]
    block_contact: Optional[bool]
    share_contact: Optional[bool]
    need_contacts_exception: Optional[bool]
    report_geo: Optional[bool]
    autoarchived: Optional[bool]
    invite_members: Optional[bool]
    request_chat_broadcast: Optional[bool]
    geo_distance: Optional[int]
    request_chat_title: Optional[str]
    request_chat_date: Optional[int]

class GlobalPrivacySettings(TLObject):
    CONSTRUCTOR_ID = 0x734C4CCB
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("archive_and_mute_new_noncontact_peers", "true", flag_group=0, flag_bit=0),
        TLField("keep_archived_unmuted", "true", flag_group=0, flag_bit=1),
        TLField("keep_archived_folders", "true", flag_group=0, flag_bit=2),
    ]
    archive_and_mute_new_noncontact_peers: Optional[bool]
    keep_archived_unmuted: Optional[bool]
    keep_archived_folders: Optional[bool]