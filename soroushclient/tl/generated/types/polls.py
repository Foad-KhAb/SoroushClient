from typing import Optional, List

from soroushclient.tl.base import TLField, TLObject


class PollAnswer(TLObject):
    CONSTRUCTOR_ID = 1823064809
    FIELDS = [
        TLField("text", "string"),
        TLField("option", "bytes"),
    ]
    text: Optional[str]
    option: Optional[bytes]


class Poll(TLObject):
    CONSTRUCTOR_ID = 2262925665
    FIELDS = [
        TLField("id", "long"),
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("closed", "true", flag_group=0, flag_bit=0),
        TLField("public_voters", "true", flag_group=0, flag_bit=1),
        TLField("multiple_choice", "true", flag_group=0, flag_bit=2),
        TLField("quiz", "true", flag_group=0, flag_bit=3),
        TLField("question", "string"),
        TLField("answers", "PollAnswer", is_vector=True),
        TLField("close_period", "int", flag_group=0, flag_bit=4),
        TLField("close_date", "int", flag_group=0, flag_bit=5),
    ]
    id: Optional[int]
    closed: Optional[bool]
    public_voters: Optional[bool]
    multiple_choice: Optional[bool]
    quiz: Optional[bool]
    question: Optional[str]
    answers: Optional[List[TLObject]]
    close_period: Optional[int]
    close_date: Optional[int]


class PollAnswerVoters(TLObject):
    CONSTRUCTOR_ID = 997055186
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("chosen", "true", flag_group=0, flag_bit=0),
        TLField("correct", "true", flag_group=0, flag_bit=1),
        TLField("option", "bytes"),
        TLField("voters", "int"),
    ]
    chosen: Optional[bool]
    correct: Optional[bool]
    option: Optional[bytes]
    voters: Optional[int]


class PollResults(TLObject):
    CONSTRUCTOR_ID = 2061444128
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("min", "true", flag_group=0, flag_bit=0),
        TLField("results", "PollAnswerVoters", flag_group=0, flag_bit=1, is_vector=True),
        TLField("total_voters", "int", flag_group=0, flag_bit=2),
        TLField("recent_voters", "Peer", flag_group=0, flag_bit=3, is_vector=True),
        TLField("solution", "string", flag_group=0, flag_bit=4),
        TLField("solution_entities", "MessageEntity", flag_group=0, flag_bit=4, is_vector=True),
    ]
    min: Optional[bool]
    results: Optional[List[TLObject]]
    total_voters: Optional[int]
    recent_voters: Optional[List[TLObject]]
    solution: Optional[str]
    solution_entities: Optional[List[TLObject]]