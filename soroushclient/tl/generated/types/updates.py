from soroushclient.tl.base import TLField, TLObject


class UpdateNewMessage(TLObject):
    CONSTRUCTOR_ID = 0x1F2B0AFD
    FIELDS = [
        TLField("message", "Message", skip_cid=False),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
    ]


class UpdateMessageID(TLObject):
    CONSTRUCTOR_ID = 0x4E90BFD6
    FIELDS = [
        TLField("id", "int", skip_cid=True),
        TLField("random_id", "long", skip_cid=True),
    ]


class UpdateDeleteMessages(TLObject):
    CONSTRUCTOR_ID = 0xA20DB0E5
    FIELDS = [
        TLField("messages", "int", is_vector=True),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
    ]


class UpdateUserTyping(TLObject):
    CONSTRUCTOR_ID = 0xC01E857F
    FIELDS = [
        TLField("user_id", "long", skip_cid=True),
        TLField("action", "SendMessageAction"),
    ]


class UpdateChatUserTyping(TLObject):
    CONSTRUCTOR_ID = 0x83487AF0
    FIELDS = [
        TLField("chat_id", "long", skip_cid=True),
        TLField("from_id", "Peer"),
        TLField("action", "SendMessageAction"),
    ]


class UpdateChatParticipants(TLObject):
    CONSTRUCTOR_ID = 0x07761198
    FIELDS = [
        TLField("participants", "ChatParticipants"),
    ]


class UpdateUserStatus(TLObject):
    CONSTRUCTOR_ID = 0xE5BDF8DE
    FIELDS = [
        TLField("user_id", "long", skip_cid=True),
        TLField("status", "UserStatus"),
    ]


class UpdateUserName(TLObject):
    CONSTRUCTOR_ID = 0xA7848924
    FIELDS = [
        TLField("user_id", "long", skip_cid=True),
        TLField("first_name", "string", skip_cid=True),
        TLField("last_name", "string", skip_cid=True),
        TLField("usernames", "Username", is_vector=True),
    ]


class UpdateNewAuthorization(TLObject):
    CONSTRUCTOR_ID = 0x8951ABEF
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("unconfirmed", "true", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("hash", "long", skip_cid=True),
        TLField("date", "int", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("device", "string", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("location", "string", flag_group=1, flag_bit=0, skip_cid=True),
    ]


class UpdateDcOptions(TLObject):
    CONSTRUCTOR_ID = 0x8E5E9873
    FIELDS = [
        TLField("dc_options", "DcOption", is_vector=True),
    ]


class UpdateNotifySettings(TLObject):
    CONSTRUCTOR_ID = 0xBEC268EF
    FIELDS = [
        TLField("peer", "NotifyPeer"),
        TLField("notify_settings", "PeerNotifySettings"),
    ]


class UpdateServiceNotification(TLObject):
    CONSTRUCTOR_ID = 0xEBE46819
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("popup", "true", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("invert_media", "true", flag_group=1, flag_bit=2, skip_cid=True),
        TLField("inbox_date", "int", flag_group=1, flag_bit=1, skip_cid=True),
        TLField("type", "string", skip_cid=True),
        TLField("message", "string", skip_cid=True),
        TLField("media", "MessageMedia"),
        TLField("entities", "MessageEntity", is_vector=True),
    ]


class UpdatePrivacy(TLObject):
    CONSTRUCTOR_ID = 0xEE3B272A
    FIELDS = [
        TLField("key", "PrivacyKey"),
        TLField("rules", "PrivacyRule", is_vector=True),
    ]


class UpdateUserPhone(TLObject):
    CONSTRUCTOR_ID = 0x05492A13
    FIELDS = [
        TLField("user_id", "long", skip_cid=True),
        TLField("phone", "string", skip_cid=True),
    ]


class UpdateReadHistoryInbox(TLObject):
    CONSTRUCTOR_ID = 0x9C974FDF
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("folder_id", "int", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("peer", "Peer"),
        TLField("max_id", "int", skip_cid=True),
        TLField("still_unread_count", "int", skip_cid=True),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
    ]


class UpdateReadHistoryOutbox(TLObject):
    CONSTRUCTOR_ID = 0x2F2F21BF
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("max_id", "int", skip_cid=True),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
    ]


class UpdateReadMessagesContents(TLObject):
    CONSTRUCTOR_ID = 0xF8227181
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("messages", "int", is_vector=True),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
        TLField("date", "int", flag_group=1, flag_bit=0, skip_cid=True),
    ]


class UpdateChannelTooLong(TLObject):
    CONSTRUCTOR_ID = 0x108D941F
    FIELDS = [
        TLField("flags", "", flag_indicator=True, flag_group=0),
        TLField("channel_id", "long", skip_cid=True),
        TLField("pts", "int", flag_group=0, flag_bit=0, skip_cid=True),
    ]


class UpdateChannel(TLObject):
    CONSTRUCTOR_ID = 0x635B4C09
    FIELDS = [
        TLField("channel_id", "long", skip_cid=True),
    ]


class UpdateNewChannelMessage(TLObject):
    CONSTRUCTOR_ID = 0x62BA04D9
    FIELDS = [
        TLField("message", "Message"),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
    ]


class UpdateReadChannelInbox(TLObject):
    CONSTRUCTOR_ID = 0x922E6E10
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("folder_id", "int", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("channel_id", "long", skip_cid=True),
        TLField("max_id", "int", skip_cid=True),
        TLField("still_unread_count", "int", skip_cid=True),
        TLField("pts", "int", skip_cid=True),
    ]


class UpdateDeleteChannelMessages(TLObject):
    CONSTRUCTOR_ID = 0xC32D5B12
    FIELDS = [
        TLField("channel_id", "long", skip_cid=True),
        TLField("messages", "int", is_vector=True),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
    ]


class UpdateChannelMessageViews(TLObject):
    CONSTRUCTOR_ID = 0xF226AC08
    FIELDS = [
        TLField("channel_id", "long", skip_cid=True),
        TLField("id", "int", skip_cid=True),
        TLField("views", "int", skip_cid=True),
    ]


class UpdateEditChannelMessage(TLObject):
    CONSTRUCTOR_ID = 0x1B3F4DF7
    FIELDS = [
        TLField("message", "Message"),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
    ]


class UpdateEditMessage(TLObject):
    CONSTRUCTOR_ID = 0xE40370A3
    FIELDS = [
        TLField("message", "Message"),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
    ]


class UpdateReadChannelOutbox(TLObject):
    CONSTRUCTOR_ID = 0xB75F99A9
    FIELDS = [
        TLField("channel_id", "long", skip_cid=True),
        TLField("max_id", "int", skip_cid=True),
    ]


class UpdateDraftMessage(TLObject):
    CONSTRUCTOR_ID = 0x1B49EC6D
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("peer", "Peer"),
        TLField("top_msg_id", "int", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("draft", "DraftMessage"),
    ]


class UpdateReadFeaturedStickers(TLObject):
    CONSTRUCTOR_ID = 0x571D2742
    FIELDS = []


class UpdateRecentStickers(TLObject):
    CONSTRUCTOR_ID = 0x9A422C20
    FIELDS = []


class UpdateConfig(TLObject):
    CONSTRUCTOR_ID = 0xA229DD06
    FIELDS = []


class UpdatePtsChanged(TLObject):
    CONSTRUCTOR_ID = 0x3354678F
    FIELDS = []


class UpdateChannelWebPage(TLObject):
    CONSTRUCTOR_ID = 0x2F2BA99F
    FIELDS = [
        TLField("channel_id", "long", skip_cid=True),
        TLField("webpage", "WebPage"),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
    ]


class UpdateDialogPinned(TLObject):
    CONSTRUCTOR_ID = 0x6E6FE51C
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("pinned", "true", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("folder_id", "int", flag_group=1, flag_bit=1, skip_cid=True),
        TLField("peer", "DialogPeer"),
    ]


class UpdatePinnedDialogs(TLObject):
    CONSTRUCTOR_ID = 0xFA0F3CA2
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("folder_id", "int", flag_group=1, flag_bit=1, skip_cid=True),
        TLField("order", "DialogPeer", flag_group=1, flag_bit=0, is_vector=True),
    ]


class UpdateSavedGifs(TLObject):
    CONSTRUCTOR_ID = 0x9375341E
    FIELDS = []


class UpdateFavedStickers(TLObject):
    CONSTRUCTOR_ID = 0xE511996D
    FIELDS = []


class UpdateContactsReset(TLObject):
    CONSTRUCTOR_ID = 0x7084A7BE
    FIELDS = []


class UpdateChannelAvailableMessages(TLObject):
    CONSTRUCTOR_ID = 0xB23FC698
    FIELDS = [
        TLField("channel_id", "long", skip_cid=True),
        TLField("available_min_id", "int", skip_cid=True),
    ]


class UpdateDialogUnreadMark(TLObject):
    CONSTRUCTOR_ID = 0xE16459C3
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("unread", "true", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("peer", "DialogPeer"),
    ]


class UpdateMessagePoll(TLObject):
    CONSTRUCTOR_ID = 0xACA1657B
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("poll_id", "long", skip_cid=True),
        TLField("poll", "Poll", flag_group=1, flag_bit=0),
        TLField("results", "PollResults"),
    ]


class UpdateChatDefaultBannedRights(TLObject):
    CONSTRUCTOR_ID = 0x54C01850
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("default_banned_rights", "ChatBannedRights"),
        TLField("version", "int", skip_cid=True),
    ]


class UpdateFolderPeers(TLObject):
    CONSTRUCTOR_ID = 0x19360DC0
    FIELDS = [
        TLField("folder_peers", "FolderPeer", is_vector=True),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
    ]


class UpdatePeerSettings(TLObject):
    CONSTRUCTOR_ID = 0x6A7E7366
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("settings", "PeerSettings"),
    ]


class UpdatePeerLocated(TLObject):
    CONSTRUCTOR_ID = 0xB4AFCFB0
    FIELDS = [
        TLField("peers", "PeerLocated", is_vector=True),
    ]


class UpdateNewScheduledMessage(TLObject):
    CONSTRUCTOR_ID = 0x39A51DFB
    FIELDS = [
        TLField("message", "Message"),
    ]


class UpdateDeleteScheduledMessages(TLObject):
    CONSTRUCTOR_ID = 0x90866CEE
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("messages", "int", is_vector=True),
    ]


class UpdateTheme(TLObject):
    CONSTRUCTOR_ID = 0x8216FBA3
    FIELDS = [
        TLField("theme", "Theme"),
    ]


class UpdateLoginToken(TLObject):
    CONSTRUCTOR_ID = 0x564FE691
    FIELDS = []


class UpdateDialogFilter(TLObject):
    CONSTRUCTOR_ID = 0x26FFDE7D
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("id", "int", skip_cid=True),
        TLField("filter", "DialogFilter", flag_group=1, flag_bit=0),
    ]


class UpdateDialogFilterOrder(TLObject):
    CONSTRUCTOR_ID = 0xA5D72105
    FIELDS = [
        TLField("order", "int", is_vector=True),
    ]


class UpdateDialogFilters(TLObject):
    CONSTRUCTOR_ID = 0x3504914F
    FIELDS = []


class UpdateChannelMessageForwards(TLObject):
    CONSTRUCTOR_ID = 0xD29A27F4
    FIELDS = [
        TLField("channel_id", "long", skip_cid=True),
        TLField("id", "int", skip_cid=True),
        TLField("forwards", "int", skip_cid=True),
    ]


class UpdatePeerBlocked(TLObject):
    CONSTRUCTOR_ID = 0xEBE07752
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("blocked", "true", flag_group=1, flag_bit=0, skip_cid=True),
        TLField(
            "blocked_my_stories_from", "true", flag_group=1, flag_bit=1, skip_cid=True
        ),
        TLField("peer_id", "Peer"),
    ]


class UpdateChannelUserTyping(TLObject):
    CONSTRUCTOR_ID = 0x8C88C923
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("channel_id", "long", skip_cid=True),
        TLField("top_msg_id", "int", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("from_id", "Peer"),
        TLField("action", "SendMessageAction"),
    ]


class UpdatePinnedMessages(TLObject):
    CONSTRUCTOR_ID = 0xED85EAB5
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("pinned", "true", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("peer", "Peer"),
        TLField("messages", "int", is_vector=True),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
    ]


class UpdatePinnedChannelMessages(TLObject):
    CONSTRUCTOR_ID = 0x5BB98608
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("pinned", "true", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("channel_id", "long", skip_cid=True),
        TLField("messages", "int", is_vector=True),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
    ]


class UpdateChat(TLObject):
    CONSTRUCTOR_ID = 0xF89A6A4E
    FIELDS = [
        TLField("chat_id", "long", skip_cid=True),
    ]


class UpdateGroupCall(TLObject):
    CONSTRUCTOR_ID = 0x14B24500
    FIELDS = [
        TLField("chat_id", "long", skip_cid=True),
        TLField("call", "GroupCall"),
    ]


class UpdatePeerHistoryTTL(TLObject):
    CONSTRUCTOR_ID = 0xBB9BB9A5
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("peer", "Peer"),
        TLField("ttl_period", "int", flag_group=1, flag_bit=0, skip_cid=True),
    ]


class UpdateUser(TLObject):
    CONSTRUCTOR_ID = 0x20529438
    FIELDS = [
        TLField("user_id", "long", skip_cid=True),
    ]


class UpdateAutoSaveSettings(TLObject):
    CONSTRUCTOR_ID = 0xEC05B097
    FIELDS = []


class UpdateStory(TLObject):
    CONSTRUCTOR_ID = 0x75B3B798
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("story", "StoryItem"),
    ]


class UpdateReadStories(TLObject):
    CONSTRUCTOR_ID = 0xF74E932B
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("max_id", "int", skip_cid=True),
    ]


class UpdateStoryID(TLObject):
    CONSTRUCTOR_ID = 0x1BF335B9
    FIELDS = [
        TLField("id", "int", skip_cid=True),
        TLField("random_id", "long", skip_cid=True),
    ]


class UpdateUserEmojiStatus(TLObject):
    CONSTRUCTOR_ID = 0x28373599
    FIELDS = [
        TLField("user_id", "long", skip_cid=True),
        TLField("emoji_status", "EmojiStatus"),
    ]


class UpdateRecentEmojiStatuses(TLObject):
    CONSTRUCTOR_ID = 0x30F443DB
    FIELDS = []


class UpdateRecentReactions(TLObject):
    CONSTRUCTOR_ID = 0x6F7863F4
    FIELDS = []


class UpdateMessageReactions(TLObject):
    CONSTRUCTOR_ID = 0x5E1B3CB8
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("peer", "Peer"),
        TLField("msg_id", "int", skip_cid=True),
        TLField("top_msg_id", "int", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("reactions", "MessageReactions"),
    ]


class UpdateAttachMenuBots(TLObject):
    CONSTRUCTOR_ID = 0x17B7A20B
    FIELDS = []


class UpdateReadFeaturedEmojiStickers(TLObject):
    CONSTRUCTOR_ID = 0xFB4C496C
    FIELDS = []


class UpdateChannelPinnedTopic(TLObject):
    CONSTRUCTOR_ID = 0x192EFBE3
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("pinned", "true", flag_group=1, flag_bit=0, skip_cid=True),
        TLField("channel_id", "long", skip_cid=True),
        TLField("topic_id", "int", skip_cid=True),
    ]


class UpdateChannelPinnedTopics(TLObject):
    CONSTRUCTOR_ID = 0xFE198602
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("channel_id", "long", skip_cid=True),
        TLField("order", "int", flag_group=1, flag_bit=0, is_vector=True),
    ]


class UpdateChannelViewForumAsMessages(TLObject):
    CONSTRUCTOR_ID = 0x07B68920
    FIELDS = [
        TLField("channel_id", "long", skip_cid=True),
        TLField("enabled", "Bool"),
    ]


class UpdatePeerWallpaper(TLObject):
    CONSTRUCTOR_ID = 0xAE3F101D
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField(
            "wallpaper_overridden", "true", flag_group=1, flag_bit=1, skip_cid=True
        ),
        TLField("peer", "Peer"),
        TLField("wallpaper", "WallPaper", flag_group=1, flag_bit=0),
    ]


# ── Updates containers ─────────────────────────────────────────────────────────


class UpdatesTooLong(TLObject):
    CONSTRUCTOR_ID = 0xE317AF7E
    FIELDS = []


class UpdateShort(TLObject):
    CONSTRUCTOR_ID = 0x78D4DEC1
    FIELDS = [
        TLField("update", "Update"),
        TLField("date", "int", skip_cid=True),
    ]


class UpdatesCombined(TLObject):
    CONSTRUCTOR_ID = 0x725B04C3
    FIELDS = [
        TLField("updates", "Update", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("date", "int", skip_cid=True),
        TLField("seq_start", "int", skip_cid=True),
        TLField("seq", "int", skip_cid=True),
    ]


class UpdateShortSentMessage(TLObject):
    CONSTRUCTOR_ID = 0x9015E101
    FIELDS = [
        TLField("flags", "", flag_indicator=True),
        TLField("out", "true", flag_group=1, flag_bit=1, skip_cid=True),
        TLField("id", "int", skip_cid=True),
        TLField("pts", "int", skip_cid=True),
        TLField("pts_count", "int", skip_cid=True),
        TLField("date", "int", skip_cid=True),
        TLField("media", "MessageMedia", flag_group=1, flag_bit=9),
        TLField("entities", "MessageEntity", flag_group=1, flag_bit=7, is_vector=True),
        TLField("ttl_period", "int", flag_group=1, flag_bit=25, skip_cid=True),
    ]


# ── updates.State / updates.Difference ────────────────────────────────────────


class UpdatesState(TLObject):
    CONSTRUCTOR_ID = 0xA56C2A3E
    FIELDS = [
        TLField("pts", "int", skip_cid=True),
        TLField("qts", "int", skip_cid=True),
        TLField("date", "int", skip_cid=True),
        TLField("seq", "int", skip_cid=True),
        TLField("unread_count", "int", skip_cid=True),
    ]


class UpdatesDifferenceEmpty(TLObject):
    CONSTRUCTOR_ID = 0x5D75A138
    FIELDS = [
        TLField("date", "int", skip_cid=True),
        TLField("seq", "int", skip_cid=True),
    ]


class UpdatesDifference(TLObject):
    CONSTRUCTOR_ID = 0x00F49CA0
    FIELDS = [
        TLField("new_messages", "Message", is_vector=True),
        TLField("new_encrypted_messages", "EncryptedMessage", is_vector=True),
        TLField("other_updates", "Update", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("state", "updates.State"),
    ]


class UpdatesDifferenceSlice(TLObject):
    CONSTRUCTOR_ID = 0xA8FB1981
    FIELDS = [
        TLField("new_messages", "Message", is_vector=True),
        TLField("new_encrypted_messages", "EncryptedMessage", is_vector=True),
        TLField("other_updates", "Update", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("intermediate_state", "updates.State"),
    ]


class UpdatesDifferenceTooLong(TLObject):
    CONSTRUCTOR_ID = 0x4AFE8F6D
    FIELDS = [
        TLField("pts", "int", skip_cid=True),
    ]


class Updates(TLObject):
    CONSTRUCTOR_ID = 0x74AE4240
    FIELDS = [
        TLField("updates", "Update", is_vector=True),
        TLField("users", "User", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("date", "int", skip_cid=True),
        TLField("seq", "int", skip_cid=True),
    ]
