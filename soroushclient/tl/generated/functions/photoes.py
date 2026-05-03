from typing import Optional, List

from soroushclient.tl.base import TLRequest, TLField, TLObject


class UpdateProfilePhoto(TLRequest):
    CONSTRUCTOR_ID = 0x09E82039
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("fallback", "true", flag_group=0, flag_bit=0),
        TLField("bot", "InputUser", flag_group=0, flag_bit=1),
        TLField("id", "InputPhoto"),
    ]
    fallback: Optional[bool]
    bot: Optional[TLObject]
    id: Optional[TLObject]

class UploadProfilePhoto(TLRequest):
    CONSTRUCTOR_ID = 0x0388A3B5
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("fallback", "true", flag_group=0, flag_bit=3),
        TLField("bot", "InputUser", flag_group=0, flag_bit=5),
        TLField("file", "InputFile", flag_group=0, flag_bit=0),
        TLField("video", "InputFile", flag_group=0, flag_bit=1),
        TLField("video_start_ts", "double", flag_group=0, flag_bit=2),
        TLField("video_emoji_markup", "VideoSize", flag_group=0, flag_bit=4),
    ]
    fallback: Optional[bool]
    bot: Optional[TLObject]
    file: Optional[TLObject]
    video: Optional[TLObject]
    video_start_ts: Optional[float]
    video_emoji_markup: Optional[TLObject]

class DeletePhotos(TLRequest):
    CONSTRUCTOR_ID = 0x87CF7F2F
    FIELDS = [TLField("id", "InputPhoto", is_vector=True)]
    id: Optional[List[TLObject]]

class GetUserPhotos(TLRequest):
    CONSTRUCTOR_ID = 0x91CD32A8
    FIELDS = [
        TLField("user_id", "InputUser"),
        TLField("offset", "int"),
        TLField("max_id", "long"),
        TLField("limit", "int"),
    ]
    user_id: Optional[TLObject]
    offset: Optional[int]
    max_id: Optional[int]
    limit: Optional[int]