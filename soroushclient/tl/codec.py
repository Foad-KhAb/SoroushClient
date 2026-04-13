# ═══════════════════════════════════════════════════════════
# Serializer
# ═══════════════════════════════════════════════════════════
import logging
from typing import Any, Dict, Type

from soroushclient.tl.base import TLField, TLObject
from soroushclient.tl.reader import TLReader
from soroushclient.tl.writer import TLWriter

logger = logging.getLogger(__name__)


def _serialize(obj: TLObject) -> bytes:
    w = TLWriter()
    w.write_int(obj.CONSTRUCTOR_ID, signed=False)
    flags_map: Dict[int, int] = {}
    for f in obj.FIELDS:
        if f.flag_indicator:
            flags_map[f.flag_group] = 0
    for f in obj.FIELDS:
        if f.flag_indicator or f.flag_bit < 0:
            continue
        val = getattr(obj, f.name, None)
        if val is not None and val is not False:
            flags_map[f.flag_group] = flags_map.get(f.flag_group, 0) | (1 << f.flag_bit)
    for f in obj.FIELDS:
        if f.flag_indicator:
            w.write_int(flags_map.get(f.flag_group, 0), signed=False)
    for f in obj.FIELDS:
        if f.flag_indicator:
            continue
        val = getattr(obj, f.name, None)
        if f.flag_bit >= 0 and not (flags_map.get(f.flag_group, 0) & (1 << f.flag_bit)):
            continue
        _write_field(w, f, val)
    return w.getvalue()


def _write_field(w: TLWriter, f: TLField, val: Any):
    if f.is_vector:
        w.write_int(0x1CB5C415, signed=False)
        w.write_int(len(val))
        for item in val:
            _write_value(w, f.type, item, f.skip_cid)
    else:
        _write_value(w, f.type, val, f.skip_cid)


def _write_value(w: TLWriter, type_: str, val: Any, skip_cid: bool = False):
    if val is None:
        raise ValueError(f"Required field of type '{type_}' is None")
    if type_ == "int":
        w.write_int(val)
    elif type_ == "long":
        w.write_long(val)
    elif type_ == "double":
        w.write_double(val)
    elif type_ == "int128":
        w.write_raw(val if isinstance(val, bytes) else val.to_bytes(16, "little"))
    elif type_ == "int256":
        w.write_raw(val if isinstance(val, bytes) else val.to_bytes(32, "little"))
    elif type_ == "string":
        w.write_string(val)
    elif type_ == "bytes":
        w.write_bytes(val)
    elif type_ in ("bool", "Bool", "true"):
        if not skip_cid:
            w.write_int(0x997275B5 if val else 0xBC799737, signed=False)
    elif isinstance(val, TLObject):
        if skip_cid:
            for f in val.FIELDS:
                if not f.flag_indicator:
                    _write_field(w, f, getattr(val, f.name, None))
        else:
            w.write_raw(val.to_bytes())
    else:
        raise TypeError(f"Cannot serialize type={type_!r} val={val!r}")


# ═══════════════════════════════════════════════════════════
# Deserializer
# ═══════════════════════════════════════════════════════════


def _deserialize(cls: Type[TLObject], r: TLReader) -> TLObject:
    flags_map: Dict[int, int] = {}
    kwargs: Dict[str, Any] = {}
    for f in cls.FIELDS:
        if f.flag_indicator:
            flags_map[f.flag_group] = r.read_int(signed=False)
            continue
        if f.flag_bit >= 0:
            if not (flags_map.get(f.flag_group, 0) & (1 << f.flag_bit)):
                kwargs[f.name] = None
                continue
        try:
            if f.is_vector:
                r.read_int(signed=False)
                count = r.read_int()
                items = []
                for _ in range(count):
                    try:
                        items.append(_read_value(r, f.type, f.skip_cid))
                    except Exception as e:
                        logger.warning(f"[tl] {cls.__name__}.{f.name}[{_}] failed: {e}")
                        import traceback

                        traceback.print_exc()
                        break
                kwargs[f.name] = items
            else:
                kwargs[f.name] = _read_value(r, f.type, f.skip_cid)
        except Exception as e:
            logger.warning(
                f"[tl] Error deserializing {cls.__name__}.{f.name} (type={f.type}) at pos={r._pos}: {e}"
            )
            import traceback

            traceback.print_exc()
            kwargs[f.name] = None
            continue
    for f in cls.FIELDS:
        if f.flag_bit >= 0 and f.type == "true":
            kwargs[f.name] = bool(flags_map.get(f.flag_group, 0) & (1 << f.flag_bit))
    return cls(**kwargs)


def _read_value(r: TLReader, type_: str, skip_cid: bool = False) -> Any:
    if type_ == "int":
        return r.read_int()
    elif type_ == "long":
        return r.read_long()
    elif type_ == "double":
        return r.read_double()
    elif type_ == "int128":
        return r.read_raw(16)
    elif type_ == "int256":
        return r.read_raw(32)
    elif type_ == "string":
        return r.read_string()
    elif type_ == "bytes":
        return r.read_bytes()
    elif type_ in ("bool", "Bool"):
        cid = r.read_int(signed=False)
        return cid == 0x997275B5
    elif type_ == "true":
        return True
    else:
        return TLObject.read_object(r)
