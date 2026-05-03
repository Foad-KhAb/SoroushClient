from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class BusinessAwayMessage(TLObject):
    CONSTRUCTOR_ID = 0xEF156A5C
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("offline_only", "true", flag_group=0, flag_bit=0),
        TLField("shortcut_id", "int"),
        TLField("schedule", "BusinessAwayMessageSchedule"),
        TLField("recipients", "BusinessRecipients"),
    ]
    offline_only: Optional[bool]
    shortcut_id: Optional[int]
    schedule: Optional[TLObject]
    recipients: Optional[TLObject]

class BusinessGreetingMessage(TLObject):
    CONSTRUCTOR_ID = 0xE519ABAB
    FIELDS = [
        TLField("shortcut_id", "int"),
        TLField("recipients", "BusinessRecipients"),
        TLField("no_activity_days", "int"),
    ]
    shortcut_id: Optional[int]
    recipients: Optional[TLObject]
    no_activity_days: Optional[int]

class BusinessIntro(TLObject):
    CONSTRUCTOR_ID = 0x5A0A066D
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("title", "string"),
        TLField("description", "string"),
        TLField("sticker", "Document", flag_group=0, flag_bit=0),
    ]
    title: Optional[str]
    description: Optional[str]
    sticker: Optional[TLObject]

class BusinessLocation(TLObject):
    CONSTRUCTOR_ID = 0xAC5C1AF7
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("geo_point", "GeoPoint", flag_group=0, flag_bit=0),
        TLField("address", "string"),
    ]
    geo_point: Optional[TLObject]
    address: Optional[str]

class BusinessWorkHours(TLObject):
    CONSTRUCTOR_ID = 0x8C92B098
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("open_now", "true", flag_group=0, flag_bit=0),
        TLField("timezone_id", "string"),
        TLField("weekly_open", "BusinessWeeklyOpen", is_vector=True),
    ]
    open_now: Optional[bool]
    timezone_id: Optional[str]
    weekly_open: Optional[List[TLObject]]

class BusinessAwayMessageScheduleAlways(TLObject):
    CONSTRUCTOR_ID = 0xC9B9E2B9
    FIELDS = []

class BusinessAwayMessageScheduleOutsideWorkHours(TLObject):
    CONSTRUCTOR_ID = 0xC3F2F501
    FIELDS = []

class BusinessAwayMessageScheduleCustom(TLObject):
    CONSTRUCTOR_ID = 0xCC4D9ECC
    FIELDS = [
        TLField("start_date", "int"),
        TLField("end_date", "int"),
    ]
    start_date: Optional[int]
    end_date: Optional[int]

class BusinessRecipients(TLObject):
    CONSTRUCTOR_ID = 0x21108FF7
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("existing_chats", "true", flag_group=0, flag_bit=0),
        TLField("new_chats", "true", flag_group=0, flag_bit=1),
        TLField("contacts", "true", flag_group=0, flag_bit=2),
        TLField("non_contacts", "true", flag_group=0, flag_bit=3),
        TLField("exclude_selected", "true", flag_group=0, flag_bit=5),
        TLField("users", "long", flag_group=0, flag_bit=4, is_vector=True),
    ]
    existing_chats: Optional[bool]
    new_chats: Optional[bool]
    contacts: Optional[bool]
    non_contacts: Optional[bool]
    exclude_selected: Optional[bool]
    users: Optional[List[int]]

class BusinessWeeklyOpen(TLObject):
    CONSTRUCTOR_ID = 0x120B1AB9
    FIELDS = [
        TLField("start_minute", "int"),
        TLField("end_minute", "int"),
    ]
    start_minute: Optional[int]
    end_minute: Optional[int]