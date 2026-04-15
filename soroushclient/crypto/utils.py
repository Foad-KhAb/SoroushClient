import hashlib


def sha1(data: bytes) -> bytes:
    return hashlib.sha1(data).digest()


def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def xor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def _int_to_bytes(n: int, length: int) -> bytes:
    return n.to_bytes(length, "big")


def _bytes_to_int(b: bytes) -> int:
    return int.from_bytes(b, "big")
