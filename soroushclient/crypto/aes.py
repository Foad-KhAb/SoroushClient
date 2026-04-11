from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from soroushclient.crypto.utils import xor


def _aes_ecb(key: bytes, block: bytes, encrypt: bool) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    op = cipher.encryptor() if encrypt else cipher.decryptor()
    return op.update(block) + op.finalize()


def aes_ige_encrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    if len(data) % 16:
        data += bytes(16 - len(data) % 16)
    iv_o, iv_i = iv[0:16], iv[16:32]
    out = bytearray()
    for i in range(0, len(data), 16):
        plain = data[i : i + 16]
        cipher = xor(_aes_ecb(key, xor(plain, iv_o), True), iv_i)
        out += cipher
        iv_i, iv_o = plain, cipher
    return bytes(out)


def aes_ige_decrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    if len(data) % 16:
        data += bytes(16 - len(data) % 16)
    iv_o, iv_i = iv[0:16], iv[16:32]
    out = bytearray()
    for i in range(0, len(data), 16):
        cipher = data[i : i + 16]
        plain = xor(_aes_ecb(key, xor(cipher, iv_i), False), iv_o)
        out += plain
        iv_o, iv_i = cipher, plain
    return bytes(out)


def aes_ctr(key: bytes, iv: bytes):
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    return cipher.encryptor()
