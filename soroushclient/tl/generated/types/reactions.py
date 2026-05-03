from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class ReactionEmpty(TLObject):
    CONSTRUCTOR_ID = 0x79F5D419
    FIELDS = []

class ReactionEmoji(TLObject):
    CONSTRUCTOR_ID = 0x1B2286B8
    FIELDS = [TLField("emoticon", "string")]
    emoticon: Optional[str]

class ReactionCustomEmoji(TLObject):
    CONSTRUCTOR_ID = 0x8935FC73
    FIELDS = [TLField("document_id", "long")]
    document_id: Optional[int]

class ReactionCount(TLObject):
    CONSTRUCTOR_ID = 0xA3D1CB80
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("chosen_order", "int", flag_group=0, flag_bit=0),
        TLField("reaction", "Reaction"),
        TLField("count", "int"),
    ]
    chosen_order: Optional[int]
    reaction: Optional[TLObject]
    count: Optional[int]

class ChatReactionsNone(TLObject):
    CONSTRUCTOR_ID = 0xEAFC32BC
    FIELDS = []

class ChatReactionsAll(TLObject):
    CONSTRUCTOR_ID = 0x52928BCA
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("allow_custom", "true", flag_group=0, flag_bit=0),
    ]
    allow_custom: Optional[bool]

class ChatReactionsSome(TLObject):
    CONSTRUCTOR_ID = 0x661D4037
    FIELDS = [TLField("reactions", "Reaction", is_vector=True)]
    reactions: Optional[List[TLObject]]

class ChatReactionsDisabled(TLObject):
    CONSTRUCTOR_ID = 0x75C1F53B
    FIELDS = []

class AvailableReaction(TLObject):
    CONSTRUCTOR_ID = 0xC077EC01
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("inactive", "true", flag_group=0, flag_bit=0),
        TLField("premium", "true", flag_group=0, flag_bit=2),
        TLField("reaction", "string"),
        TLField("title", "string"),
        TLField("static_icon", "Document"),
        TLField("appear_animation", "Document"),
        TLField("select_animation", "Document"),
        TLField("activate_animation", "Document"),
        TLField("effect_animation", "Document"),
        TLField("around_animation", "Document", flag_group=0, flag_bit=1),
        TLField("center_icon", "Document", flag_group=0, flag_bit=1),
    ]
    inactive: Optional[bool]
    premium: Optional[bool]
    reaction: Optional[str]
    title: Optional[str]
    static_icon: Optional[TLObject]
    appear_animation: Optional[TLObject]
    select_animation: Optional[TLObject]
    activate_animation: Optional[TLObject]
    effect_animation: Optional[TLObject]
    around_animation: Optional[TLObject]
    center_icon: Optional[TLObject]