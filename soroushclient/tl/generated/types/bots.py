from typing import List, Optional

from soroushclient.tl.base import TLField, TLObject


class BotInfo(TLObject):
    CONSTRUCTOR_ID = 0x8F300B57
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("user_id", "long", flag_group=0, flag_bit=0),
        TLField("description", "string", flag_group=0, flag_bit=1),
        TLField("description_photo", "Photo", flag_group=0, flag_bit=4),
        TLField("description_document", "Document", flag_group=0, flag_bit=5),
        TLField("commands", "BotCommand", flag_group=0, flag_bit=2, is_vector=True),
        TLField("menu_button", "BotMenuButton", flag_group=0, flag_bit=3),
    ]
    user_id: Optional[int]
    description: Optional[str]
    description_photo: Optional[TLObject]
    description_document: Optional[TLObject]
    commands: Optional[List[TLObject]]
    menu_button: Optional[TLObject]
