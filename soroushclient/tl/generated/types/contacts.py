from soroushclient.tl.base import TLField, TLObject


class Found(TLObject):
    CONSTRUCTOR_ID = 0xB3134D9D
    FIELDS = [
        TLField("my_results", "Peer", is_vector=True),
        TLField("results", "Peer", is_vector=True),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]


class ResolvedPeer(TLObject):
    CONSTRUCTOR_ID = 0x7F077AD9
    FIELDS = [
        TLField("peer", "Peer"),
        TLField("chats", "Chat", is_vector=True),
        TLField("users", "User", is_vector=True),
    ]
