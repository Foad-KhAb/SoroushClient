import struct


class TLReader:
    def __init__(self, data: bytes):
        self._data = data
        self._pos = 0

    def read_int(self, signed=True) -> int:
        v = struct.unpack_from("<i" if signed else "<I", self._data, self._pos)[0]
        self._pos += 4
        return v

    def read_long(self, signed=True) -> int:
        v = struct.unpack_from("<q" if signed else "<Q", self._data, self._pos)[0]
        self._pos += 8
        return v

    def read_bytes(self) -> bytes:
        first = self._data[self._pos]
        if first < 254:
            n = first
            self._pos += 1
            data = self._data[self._pos : self._pos + n]
            self._pos += n
            self._pos += (-n - 1) % 4
        else:
            n = (
                self._data[self._pos + 1]
                | (self._data[self._pos + 2] << 8)
                | (self._data[self._pos + 3] << 16)
            )
            self._pos += 4
            data = self._data[self._pos : self._pos + n]
            self._pos += n
            self._pos += (-n) % 4
        return data

    def read_string(self) -> str:
        return self.read_bytes().decode("utf-8")

    def read_raw(self, n: int) -> bytes:
        data = self._data[self._pos : self._pos + n]
        self._pos += n
        return data

    def read_double(self) -> float:
        import struct

        v = struct.unpack_from("<d", self._data, self._pos)[0]
        self._pos += 8
        return v

    @property
    def remaining(self) -> int:
        return len(self._data) - self._pos
