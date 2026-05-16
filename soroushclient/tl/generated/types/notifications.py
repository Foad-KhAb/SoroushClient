from soroushclient.tl.base import TLField, TLObject


class NotificationSoundDefault(TLObject):
    CONSTRUCTOR_ID = 0x97E8BEBE
    FIELDS = []


class NotificationSoundNone(TLObject):
    CONSTRUCTOR_ID = 0x6F0C34DF
    FIELDS = []


class NotificationSoundLocal(TLObject):
    CONSTRUCTOR_ID = 0x830B9AE4
    FIELDS = [TLField("title", "string"), TLField("data", "string")]


class NotificationSoundRingtone(TLObject):
    CONSTRUCTOR_ID = 0x59753BC0
    FIELDS = [TLField("id", "long")]
