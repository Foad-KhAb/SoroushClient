from typing import Optional, List

from soroushclient.tl.base import TLObject, TLField


class Config(TLObject):
    CONSTRUCTOR_ID = 0xE8069A50
    FIELDS = [
        TLField("flags", "int", flag_group=0, flag_indicator=True),
        TLField("default_p2p_contacts", "true", flag_group=0, flag_bit=3),
        TLField("preload_featured_stickers", "true", flag_group=0, flag_bit=4),
        TLField("revoke_pm_inbox", "true", flag_group=0, flag_bit=6),
        TLField("blocked_mode", "true", flag_group=0, flag_bit=8),
        TLField("force_try_ipv6", "true", flag_group=0, flag_bit=14),
        TLField("date", "int"),
        TLField("expires", "int"),
        TLField("test_mode", "Bool"),
        TLField("this_dc", "int"),
        TLField("dc_options", "DcOption", is_vector=True),
        TLField("dc_txt_domain_name", "string"),
        TLField("chat_size_max", "int"),
        TLField("megagroup_size_max", "int"),
        TLField("forwarded_count_max", "int"),
        TLField("online_update_period_ms", "int"),
        TLField("offline_blur_timeout_ms", "int"),
        TLField("offline_idle_timeout_ms", "int"),
        TLField("online_cloud_timeout_ms", "int"),
        TLField("notify_cloud_delay_ms", "int"),
        TLField("notify_default_delay_ms", "int"),
        TLField("push_chat_period_ms", "int"),
        TLField("push_chat_limit", "int"),
        TLField("edit_time_limit", "int"),
        TLField("revoke_time_limit", "int"),
        TLField("revoke_pm_time_limit", "int"),
        TLField("rating_e_decay", "int"),
        TLField("stickers_recent_limit", "int"),
        TLField("channels_read_media_period", "int"),
        TLField("tmp_sessions", "int", flag_group=0, flag_bit=0),
        TLField("call_receive_timeout_ms", "int"),
        TLField("call_ring_timeout_ms", "int"),
        TLField("call_connect_timeout_ms", "int"),
        TLField("call_packet_timeout_ms", "int"),
        TLField("me_url_prefix", "string"),
        TLField("me_url_prefixes", "string", is_vector=True),
        TLField("autoupdate_url_prefix", "string", flag_group=0, flag_bit=7),
        TLField("gif_search_username", "string", flag_group=0, flag_bit=9),
        TLField("venue_search_username", "string", flag_group=0, flag_bit=10),
        TLField("img_search_username", "string", flag_group=0, flag_bit=11),
        TLField("static_maps_provider", "string", flag_group=0, flag_bit=12),
        TLField("caption_length_max", "int"),
        TLField("message_length_max", "int"),
        TLField("webfile_dc_id", "int"),
        TLField("suggested_lang_code", "string", flag_group=0, flag_bit=2),
        TLField("lang_pack_version", "int", flag_group=0, flag_bit=2),
        TLField("base_lang_pack_version", "int", flag_group=0, flag_bit=2),
        TLField("reactions_default", "Reaction", flag_group=0, flag_bit=15),
        TLField("autologin_token", "string", flag_group=0, flag_bit=16),
    ]
    default_p2p_contacts: Optional[bool]
    preload_featured_stickers: Optional[bool]
    revoke_pm_inbox: Optional[bool]
    blocked_mode: Optional[bool]
    force_try_ipv6: Optional[bool]
    date: Optional[int]
    expires: Optional[int]
    test_mode: Optional[bool]
    this_dc: Optional[int]
    dc_options: Optional[List[TLObject]]
    dc_txt_domain_name: Optional[str]
    chat_size_max: Optional[int]
    megagroup_size_max: Optional[int]
    forwarded_count_max: Optional[int]
    online_update_period_ms: Optional[int]
    offline_blur_timeout_ms: Optional[int]
    offline_idle_timeout_ms: Optional[int]
    online_cloud_timeout_ms: Optional[int]
    notify_cloud_delay_ms: Optional[int]
    notify_default_delay_ms: Optional[int]
    push_chat_period_ms: Optional[int]
    push_chat_limit: Optional[int]
    edit_time_limit: Optional[int]
    revoke_time_limit: Optional[int]
    revoke_pm_time_limit: Optional[int]
    rating_e_decay: Optional[int]
    stickers_recent_limit: Optional[int]
    channels_read_media_period: Optional[int]
    tmp_sessions: Optional[int]
    call_receive_timeout_ms: Optional[int]
    call_ring_timeout_ms: Optional[int]
    call_connect_timeout_ms: Optional[int]
    call_packet_timeout_ms: Optional[int]
    me_url_prefix: Optional[str]
    me_url_prefixes: Optional[List[str]]
    autoupdate_url_prefix: Optional[str]
    gif_search_username: Optional[str]
    venue_search_username: Optional[str]
    img_search_username: Optional[str]
    static_maps_provider: Optional[str]
    caption_length_max: Optional[int]
    message_length_max: Optional[int]
    webfile_dc_id: Optional[int]
    suggested_lang_code: Optional[str]
    lang_pack_version: Optional[int]
    base_lang_pack_version: Optional[int]
    reactions_default: Optional[TLObject]
    autologin_token: Optional[str]