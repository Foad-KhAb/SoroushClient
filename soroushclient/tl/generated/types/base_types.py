from typing import Optional

from soroushclient.tl.base import TLField, TLObject


class Chat(TLObject):
    """Abstract base for all chat types (groups, channels, forbidden)."""

    pass


class Peer(TLObject):
    """Abstract base for all Peer types."""

    pass


class InputPeer(TLObject):
    """Abstract base for all InputPeer types."""

    pass


class Pong(TLObject):
    CONSTRUCTOR_ID = 0x347773C5
    FIELDS = [
        TLField("msg_id", "long", skip_cid=True),
        TLField("ping_id", "long", skip_cid=True),
    ]

    msg_id: Optional[int]
    ping_id: Optional[int]


class BaseMessage(TLObject):
    """Abstract base for all Message types."""
