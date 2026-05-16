import logging
from dataclasses import dataclass
from typing import Dict, List, Optional, Type

from soroushclient.tl.reader import TLReader

logger = logging.getLogger(__name__)


@dataclass
class TLField:
    name: str
    type: str
    flag_group: int = 0
    flag_bit: int = -1
    flag_indicator: bool = False
    is_vector: bool = False
    skip_cid: bool = False


class TLObject:
    CONSTRUCTOR_ID: int = 0
    FIELDS: List[TLField] = []
    _registry: Dict[int, "Type[TLObject]"] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.CONSTRUCTOR_ID:
            TLObject._registry[cls.CONSTRUCTOR_ID] = cls

    def __init__(self, **kwargs):
        for f in self.FIELDS:
            if not f.flag_indicator:
                setattr(self, f.name, kwargs.get(f.name))

    @classmethod
    def from_reader(cls, r: TLReader) -> "TLObject":
        from soroushclient.tl.codec import _deserialize

        return _deserialize(cls, r)

    def to_bytes(self) -> bytes:
        from soroushclient.tl.codec import _serialize

        return _serialize(self)

    def to_dict(self) -> dict:
        d = {"_": self.__class__.__name__}
        for f in self.FIELDS:
            if not f.flag_indicator:
                d[f.name] = getattr(self, f.name, None)
        return d

    def __repr__(self):
        parts = ", ".join(
            f"{f.name}={getattr(self, f.name, None)!r}"
            for f in self.FIELDS
            if not f.flag_indicator
        )
        return f"{self.__class__.__name__}({parts})"

    @staticmethod
    def read_object(r: TLReader) -> "TLObject":
        cid = r.read_int(signed=False)
        cls = TLObject._registry.get(cid)
        if cls is None:
            raise ValueError(f"Unknown constructor id={cid} at pos={r._pos}")
        try:
            return cls.from_reader(r)
        except Exception as e:
            raise ValueError(f"Failed to parse cid={cid}: {e}") from e

    @staticmethod
    def read_object_with_cid(cid: int, r: TLReader) -> "TLObject":
        cls = TLObject._registry.get(cid)
        if cls is None:
            return UnknownObject(cid)
        try:
            return cls.from_reader(r)
        except Exception as e:
            return UnknownObject(cid, error=str(e))


class UnknownObject(TLObject):
    def __init__(self, cid: int, error: Optional[str] = None):
        super().__init__()
        self.cid = cid
        self.error = error

    def __repr__(self):
        return f"UnknownObject(cid={self.cid:#010x}, error={self.error!r})"


class TLRequest(TLObject):
    RESPONSE_TYPE: Type[TLObject] = None

    def parse_response(self, cid: int, r: TLReader):
        cls = TLObject._registry.get(cid)
        if cls is None:
            logger.warning(f"[tl] Unknown response constructor: {cid:#010x}")
            return UnknownObject(cid)
        return cls.from_reader(r)
