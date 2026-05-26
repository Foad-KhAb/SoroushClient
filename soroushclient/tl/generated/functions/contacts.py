from typing import List, Optional

from soroushclient.tl.base import TLObject, TLField, TLRequest


class GetContacts(TLRequest):
    CONSTRUCTOR_ID = 0x5DD69E12
    FIELDS = [TLField("hash", "long")]
    hash: Optional[int]

class ImportContacts(TLRequest):
    CONSTRUCTOR_ID = 0x2C800BE5
    FIELDS = [TLField("contacts", "InputContact", is_vector=True)]
    contacts: Optional[List[TLObject]]

class DeleteContacts(TLRequest):
    CONSTRUCTOR_ID = 0x096A0E00
    FIELDS = [TLField("id", "InputUser", is_vector=True)]
    id: Optional[List[TLObject]]

class Block(TLRequest):
    CONSTRUCTOR_ID = 0x2E2E8734
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("my_stories_from", "true", flag_group=0, flag_bit=0),
        TLField("id", "InputPeer"),
    ]
    my_stories_from: Optional[bool]
    id: Optional[TLObject]

class Unblock(TLRequest):
    CONSTRUCTOR_ID = 0xB550D328
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("my_stories_from", "true", flag_group=0, flag_bit=0),
        TLField("id", "InputPeer"),
    ]
    my_stories_from: Optional[bool]
    id: Optional[TLObject]

class GetBlocked(TLRequest):
    CONSTRUCTOR_ID = 0x9A868F80
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("my_stories_from", "true", flag_group=0, flag_bit=0),
        TLField("offset", "int"),
        TLField("limit", "int"),
    ]
    my_stories_from: Optional[bool]
    offset: Optional[int]
    limit: Optional[int]

class SearchRequest(TLRequest):
    CONSTRUCTOR_ID = 0x11F812D8
    FIELDS = [
        TLField("q", "string"),
        TLField("limit", "int"),
    ]
    q: Optional[str]
    limit: Optional[int]

class ResolveUsername(TLRequest):
    CONSTRUCTOR_ID = 0xF93CCBA3
    FIELDS = [TLField("username", "string")]
    username: Optional[str]

class ResolvePhone(TLRequest):
    CONSTRUCTOR_ID = 0x8AF94344
    FIELDS = [TLField("phone", "string")]
    phone: Optional[str]

class AddContact(TLRequest):
    CONSTRUCTOR_ID = 0xE8F463D0
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("add_phone_privacy_exception", "true", flag_group=0, flag_bit=0),
        TLField("id", "InputUser"),
        TLField("first_name", "string"),
        TLField("last_name", "string"),
        TLField("phone", "string"),
    ]
    add_phone_privacy_exception: Optional[bool]
    id: Optional[TLObject]
    first_name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]

class EditCloseFriends(TLRequest):
    CONSTRUCTOR_ID = 0xBA6705F0
    FIELDS = [TLField("id", "long", is_vector=True)]
    id: Optional[List[int]]

class GetBirthdays(TLRequest):
    CONSTRUCTOR_ID = 0xDAEDA864
    FIELDS = []