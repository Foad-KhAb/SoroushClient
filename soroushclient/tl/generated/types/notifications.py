from typing import Optional

from soroushclient.tl.base import TLField, TLObject


class InputNotifyPeer(TLObject):
    CONSTRUCTOR_ID = 0xB8BC5B0C
    FIELDS = [TLField("peer", "InputPeer")]
    peer: Optional[TLObject]

class InputNotifyUsers(TLObject):
    CONSTRUCTOR_ID = 0x193B4417
    FIELDS = []

class InputNotifyChats(TLObject):
    CONSTRUCTOR_ID = 0x4A95E84E
    FIELDS = []

class InputNotifyBroadcasts(TLObject):
    CONSTRUCTOR_ID = 0xB1DB7C7E
    FIELDS = []

class InputNotifyForumTopic(TLObject):
    CONSTRUCTOR_ID = 0x5C467992
    FIELDS = [
        TLField("peer", "InputPeer"),
        TLField("top_msg_id", "int"),
    ]
    peer: Optional[TLObject]
    top_msg_id: Optional[int]

class InputPeerNotifySettings(TLObject):
    CONSTRUCTOR_ID = 0xCACB6AE2
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("show_previews", "Bool", flag_group=0, flag_bit=0),
        TLField("silent", "Bool", flag_group=0, flag_bit=1),
        TLField("mute_until", "int", flag_group=0, flag_bit=2),
        TLField("sound", "NotificationSound", flag_group=0, flag_bit=3),
        TLField("stories_muted", "Bool", flag_group=0, flag_bit=6),
        TLField("stories_hide_sender", "Bool", flag_group=0, flag_bit=7),
        TLField("stories_sound", "NotificationSound", flag_group=0, flag_bit=8),
    ]
    show_previews: Optional[bool]
    silent: Optional[bool]
    mute_until: Optional[int]
    sound: Optional[TLObject]
    stories_muted: Optional[bool]
    stories_hide_sender: Optional[bool]
    stories_sound: Optional[TLObject]

class PeerNotifySettings(TLObject):
    CONSTRUCTOR_ID = 0x99622C0C
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("show_previews", "Bool", flag_group=0, flag_bit=0),
        TLField("silent", "Bool", flag_group=0, flag_bit=1),
        TLField("mute_until", "int", flag_group=0, flag_bit=2),
        TLField("ios_sound", "NotificationSound", flag_group=0, flag_bit=3),
        TLField("android_sound", "NotificationSound", flag_group=0, flag_bit=4),
        TLField("other_sound", "NotificationSound", flag_group=0, flag_bit=5),
        TLField("stories_muted", "Bool", flag_group=0, flag_bit=6),
        TLField("stories_hide_sender", "Bool", flag_group=0, flag_bit=7),
        TLField("stories_ios_sound", "NotificationSound", flag_group=0, flag_bit=8),
        TLField("stories_android_sound", "NotificationSound", flag_group=0, flag_bit=9),
        TLField("stories_other_sound", "NotificationSound", flag_group=0, flag_bit=10),
    ]
    show_previews: Optional[bool]
    silent: Optional[bool]
    mute_until: Optional[int]
    ios_sound: Optional[TLObject]
    android_sound: Optional[TLObject]
    other_sound: Optional[TLObject]
    stories_muted: Optional[bool]
    stories_hide_sender: Optional[bool]
    stories_ios_sound: Optional[TLObject]
    stories_android_sound: Optional[TLObject]
    stories_other_sound: Optional[TLObject]

class NotifyPeer(TLObject):
    CONSTRUCTOR_ID = 0x9FD40BD8
    FIELDS = [TLField("peer", "Peer")]
    peer: Optional[TLObject]

class NotifyUsers(TLObject):
    CONSTRUCTOR_ID = 0xB4C83B4C
    FIELDS = []

class NotifyChats(TLObject):
    CONSTRUCTOR_ID = 0xC007CEC3
    FIELDS = []

class NotifyBroadcasts(TLObject):
    CONSTRUCTOR_ID = 0xD612E8EF
    FIELDS = []

class NotifyForumTopic(TLObject):
    CONSTRUCTOR_ID = 0x226E6308
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("top_msg_id", "int"),
    ]
    peer: Optional[TLObject]
    top_msg_id: Optional[int]

class NotificationSoundDefault(TLObject):
    CONSTRUCTOR_ID = 0x97E8BEBE
    FIELDS = []

class NotificationSoundNone(TLObject):
    CONSTRUCTOR_ID = 0x6F0C34DF
    FIELDS = []

class NotificationSoundLocal(TLObject):
    CONSTRUCTOR_ID = 0x830B9AE4
    FIELDS = [
        TLField("title", "string"),
        TLField("data", "string"),
    ]
    title: Optional[str]
    data: Optional[str]

class NotificationSoundRingtone(TLObject):
    CONSTRUCTOR_ID = 0xFF6C8049
    FIELDS = [TLField("id", "long")]
    id: Optional[int]