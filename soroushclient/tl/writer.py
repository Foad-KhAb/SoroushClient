import struct


class TLWriter:
    def __init__(self):
        self._buf = bytearray()

    def write_int(self, v: int, signed=True):
        self._buf += struct.pack("<i" if signed else "<I", v)
        return self

    def write_long(self, v: int, signed=True):
        self._buf += struct.pack("<q" if signed else "<Q", v)
        return self

    def write_bytes(self, data):
        if isinstance(data, str):
            data = data.encode("utf-8")
        n = len(data)
        if n < 254:
            self._buf += bytes([n]) + data
            pad = (-n - 1) % 4
        else:
            self._buf += bytes([254, n & 0xff, (n >> 8) & 0xff, (n >> 16) & 0xff]) + data
            pad = (-n) % 4
        self._buf += bytes(pad)
        return self

    def write_string(self, s: str):
        return self.write_bytes(s.encode("utf-8"))

    def write_raw(self, data: bytes):
        self._buf += data
        return self

    def getvalue(self) -> bytes:
        return bytes(self._buf)
