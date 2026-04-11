from soroushclient.tl.base import TLField, TLObject


class NotificationSoundDefault(TLObject):
    CONSTRUCTOR_ID = 0x97e8bebe
    FIELDS = []

class NotificationSoundNone(TLObject):
    CONSTRUCTOR_ID = 0x6f0c34df
    FIELDS = []

class NotificationSoundLocal(TLObject):
    CONSTRUCTOR_ID = 0x830b9ae4
    FIELDS = [TLField("title", "string"), TLField("data", "string")]

class NotificationSoundRingtone(TLObject):
    CONSTRUCTOR_ID = 0x59753bc0
    FIELDS = [TLField("id", "long")]

