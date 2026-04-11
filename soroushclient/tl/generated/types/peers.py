from soroushclient.tl.base import TLField, TLObject


class PeerUser(TLObject):
    CONSTRUCTOR_ID = 0x59511722
    FIELDS = [TLField("user_id", "long")]


class PeerChat(TLObject):
    CONSTRUCTOR_ID = 0x36C6019A
    FIELDS = [TLField("chat_id", "long")]


class PeerChannel(TLObject):
    CONSTRUCTOR_ID = 0xA2A5371E
    FIELDS = [TLField("channel_id", "long")]


class PeerColor(TLObject):
    CONSTRUCTOR_ID = 0xB54B5ACF
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("color", "int", flag_group=0, flag_bit=0),
    ]


class PeerNotifySettings(TLObject):
    CONSTRUCTOR_ID = 0x99622C0C
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("show_previews", "bool", flag_group=0, flag_bit=0),
        TLField("silent", "bool", flag_group=0, flag_bit=1),
        TLField("mute_until", "int", flag_group=0, flag_bit=2),
        TLField("ios_sound", "NotificationSound", flag_group=0, flag_bit=3),
        TLField("android_sound", "NotificationSound", flag_group=0, flag_bit=4),
        TLField("other_sound", "NotificationSound", flag_group=0, flag_bit=5),
        TLField("stories_muted", "bool", flag_group=0, flag_bit=6),
        TLField("stories_hide_sender", "bool", flag_group=0, flag_bit=7),
        TLField("stories_ios_sound", "NotificationSound", flag_group=0, flag_bit=8),
        TLField("stories_android_sound", "NotificationSound", flag_group=0, flag_bit=9),
        TLField("stories_other_sound", "NotificationSound", flag_group=0, flag_bit=10),
    ]
