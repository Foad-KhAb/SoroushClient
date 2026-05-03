from typing import Optional, List

from soroushclient.tl.base import TLField, TLObject


class ChannelParticipant(TLObject):
    CONSTRUCTOR_ID = 0xC00C07C0
    FIELDS = [
        TLField("user_id", "long"),
        TLField("date", "int"),
    ]
    user_id: Optional[int]
    date: Optional[int]

class ChannelParticipantSelf(TLObject):
    CONSTRUCTOR_ID = 0x35A8BFA7
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("via_request", "true", flag_group=0, flag_bit=0),
        TLField("user_id", "long"),
        TLField("inviter_id", "long"),
        TLField("date", "int"),
    ]
    via_request: Optional[bool]
    user_id: Optional[int]
    inviter_id: Optional[int]
    date: Optional[int]

class ChannelParticipantCreator(TLObject):
    CONSTRUCTOR_ID = 0x2FE601D3
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("user_id", "long"),
        TLField("admin_rights", "ChatAdminRights"),
        TLField("rank", "string", flag_group=0, flag_bit=0),
    ]
    user_id: Optional[int]
    admin_rights: Optional[TLObject]
    rank: Optional[str]

class ChannelParticipantAdmin(TLObject):
    CONSTRUCTOR_ID = 0x34C3BB53
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("can_edit", "true", flag_group=0, flag_bit=0),
        TLField("self", "true", flag_group=0, flag_bit=1),
        TLField("user_id", "long"),
        TLField("inviter_id", "long", flag_group=0, flag_bit=1),
        TLField("promoted_by", "long"),
        TLField("date", "int"),
        TLField("admin_rights", "ChatAdminRights"),
        TLField("rank", "string", flag_group=0, flag_bit=2),
    ]
    can_edit: Optional[bool]
    self: Optional[bool]
    user_id: Optional[int]
    inviter_id: Optional[int]
    promoted_by: Optional[int]
    date: Optional[int]
    admin_rights: Optional[TLObject]
    rank: Optional[str]

class ChannelParticipantBanned(TLObject):
    CONSTRUCTOR_ID = 0x6DF8014E
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("left", "true", flag_group=0, flag_bit=0),
        TLField("peer", "Peer"),
        TLField("kicked_by", "long"),
        TLField("date", "int"),
        TLField("banned_rights", "ChatBannedRights"),
    ]
    left: Optional[bool]
    peer: Optional[TLObject]
    kicked_by: Optional[int]
    date: Optional[int]
    banned_rights: Optional[TLObject]

class ChannelParticipantLeft(TLObject):
    CONSTRUCTOR_ID = 0x1B03F006
    FIELDS = [TLField("peer", "Peer")]
    peer: Optional[TLObject]

class ChannelParticipantsRecent(TLObject):
    CONSTRUCTOR_ID = 0xDE3F3C79
    FIELDS = []

class ChannelParticipantsAdmins(TLObject):
    CONSTRUCTOR_ID = 0xB4608969
    FIELDS = []

class ChannelParticipantsKicked(TLObject):
    CONSTRUCTOR_ID = 0xA3B54985
    FIELDS = [TLField("q", "string")]
    q: Optional[str]

class ChannelParticipantsBots(TLObject):
    CONSTRUCTOR_ID = 0xB0D1865B
    FIELDS = []

class ChannelParticipantsBanned(TLObject):
    CONSTRUCTOR_ID = 0x1427A5E1
    FIELDS = [TLField("q", "string")]
    q: Optional[str]

class ChannelParticipantsSearch(TLObject):
    CONSTRUCTOR_ID = 0x0656AC4B
    FIELDS = [TLField("q", "string")]
    q: Optional[str]

class ChannelParticipantsContacts(TLObject):
    CONSTRUCTOR_ID = 0xBB6AE88D
    FIELDS = [TLField("q", "string")]
    q: Optional[str]

class ChannelParticipantsMentions(TLObject):
    CONSTRUCTOR_ID = 0xE04B5CEB
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("q", "string", flag_group=0, flag_bit=0),
        TLField("top_msg_id", "int", flag_group=0, flag_bit=1),
    ]
    q: Optional[str]
    top_msg_id: Optional[int]

class ChannelMessagesFilterEmpty(TLObject):
    CONSTRUCTOR_ID = 0x94D42EE7
    FIELDS = []

class ChannelMessagesFilter(TLObject):
    CONSTRUCTOR_ID = 0xCD77D957
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("exclude_new_messages", "true", flag_group=0, flag_bit=1),
        TLField("ranges", "MessageRange", is_vector=True),
    ]
    exclude_new_messages: Optional[bool]
    ranges: Optional[List[TLObject]]