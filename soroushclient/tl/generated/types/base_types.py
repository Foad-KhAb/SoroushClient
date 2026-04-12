from soroushclient.tl.base import TLObject


class Chat(TLObject):
    """Abstract base for all chat types (groups, channels, forbidden)."""

    pass


class Peer(TLObject):
    """Abstract base for all Peer types."""

    pass


class InputPeer(TLObject):
    """Abstract base for all InputPeer types."""

    pass
