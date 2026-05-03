from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class CodeSettings(TLObject):
    CONSTRUCTOR_ID = 0xAD253D78
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("allow_flashcall", "true", flag_group=0, flag_bit=0),
        TLField("current_number", "true", flag_group=0, flag_bit=1),
        TLField("allow_app_hash", "true", flag_group=0, flag_bit=4),
        TLField("allow_missed_call", "true", flag_group=0, flag_bit=5),
        TLField("allow_firebase", "true", flag_group=0, flag_bit=7),
        TLField("logout_tokens", "bytes", flag_group=0, flag_bit=6, is_vector=True),
        TLField("token", "string", flag_group=0, flag_bit=8),
        TLField("app_sandbox", "Bool", flag_group=0, flag_bit=8),
    ]
    allow_flashcall: Optional[bool]
    current_number: Optional[bool]
    allow_app_hash: Optional[bool]
    allow_missed_call: Optional[bool]
    allow_firebase: Optional[bool]
    logout_tokens: Optional[List[bytes]]
    token: Optional[str]
    app_sandbox: Optional[bool]

class WallPaperSettings(TLObject):
    CONSTRUCTOR_ID = 0x1DC1BCA4
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("blur", "true", flag_group=0, flag_bit=1),
        TLField("motion", "true", flag_group=0, flag_bit=2),
        TLField("background_color", "int", flag_group=0, flag_bit=0),
        TLField("second_background_color", "int", flag_group=0, flag_bit=4),
        TLField("third_background_color", "int", flag_group=0, flag_bit=5),
        TLField("fourth_background_color", "int", flag_group=0, flag_bit=6),
        TLField("intensity", "int", flag_group=0, flag_bit=3),
        TLField("rotation", "int", flag_group=0, flag_bit=4),
    ]
    blur: Optional[bool]
    motion: Optional[bool]
    background_color: Optional[int]
    second_background_color: Optional[int]
    third_background_color: Optional[int]
    fourth_background_color: Optional[int]
    intensity: Optional[int]
    rotation: Optional[int]

class AutoDownloadSettings(TLObject):
    CONSTRUCTOR_ID = 0xBAA57628
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("disabled", "true", flag_group=0, flag_bit=0),
        TLField("video_preload_large", "true", flag_group=0, flag_bit=1),
        TLField("audio_preload_next", "true", flag_group=0, flag_bit=2),
        TLField("phonecalls_less_data", "true", flag_group=0, flag_bit=3),
        TLField("stories_preload", "true", flag_group=0, flag_bit=4),
        TLField("photo_size_max", "int"),
        TLField("video_size_max", "long"),
        TLField("file_size_max", "long"),
        TLField("video_upload_maxbitrate", "int"),
        TLField("small_queue_active_operations_max", "int"),
        TLField("large_queue_active_operations_max", "int"),
    ]
    disabled: Optional[bool]
    video_preload_large: Optional[bool]
    audio_preload_next: Optional[bool]
    phonecalls_less_data: Optional[bool]
    stories_preload: Optional[bool]
    photo_size_max: Optional[int]
    video_size_max: Optional[int]
    file_size_max: Optional[int]
    video_upload_maxbitrate: Optional[int]
    small_queue_active_operations_max: Optional[int]
    large_queue_active_operations_max: Optional[int]

class AutoSaveSettings(TLObject):
    CONSTRUCTOR_ID = 0xC84834CE
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("photos", "true", flag_group=0, flag_bit=0),
        TLField("videos", "true", flag_group=0, flag_bit=1),
        TLField("video_max_size", "long", flag_group=0, flag_bit=2),
    ]
    photos: Optional[bool]
    videos: Optional[bool]
    video_max_size: Optional[int]

class AutoSaveException(TLObject):
    CONSTRUCTOR_ID = 0x81602D47
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("settings", "AutoSaveSettings"),
    ]
    peer: Optional[TLObject]
    settings: Optional[TLObject]

class InputThemeSettings(TLObject):
    CONSTRUCTOR_ID = 0x8FDE504F
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("message_colors_animated", "true", flag_group=0, flag_bit=2),
        TLField("base_theme", "BaseTheme"),
        TLField("accent_color", "int"),
        TLField("outbox_accent_color", "int", flag_group=0, flag_bit=3),
        TLField("message_colors", "int", flag_group=0, flag_bit=0, is_vector=True),
        TLField("wallpaper", "InputWallPaper", flag_group=0, flag_bit=1),
        TLField("wallpaper_settings", "WallPaperSettings", flag_group=0, flag_bit=1),
    ]
    message_colors_animated: Optional[bool]
    base_theme: Optional[TLObject]
    accent_color: Optional[int]
    outbox_accent_color: Optional[int]
    message_colors: Optional[List[int]]
    wallpaper: Optional[TLObject]
    wallpaper_settings: Optional[TLObject]

class ThemeSettings(TLObject):
    CONSTRUCTOR_ID = 0xFA58B6D4
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("message_colors_animated", "true", flag_group=0, flag_bit=2),
        TLField("base_theme", "BaseTheme"),
        TLField("accent_color", "int"),
        TLField("outbox_accent_color", "int", flag_group=0, flag_bit=3),
        TLField("message_colors", "int", flag_group=0, flag_bit=0, is_vector=True),
        TLField("wallpaper", "WallPaper", flag_group=0, flag_bit=1),
    ]
    message_colors_animated: Optional[bool]
    base_theme: Optional[TLObject]
    accent_color: Optional[int]
    outbox_accent_color: Optional[int]
    message_colors: Optional[List[int]]
    wallpaper: Optional[TLObject]