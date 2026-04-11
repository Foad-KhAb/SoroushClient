import hashlib


def generate_key_iv(auth_key: bytes, msg_key: bytes, client: bool):
    x     = 0 if client else 8
    sha_a = hashlib.sha256(msg_key + auth_key[x:x + 36]).digest()
    sha_b = hashlib.sha256(auth_key[x + 40:x + 76] + msg_key).digest()
    key   = sha_a[:8]  + sha_b[8:24]  + sha_a[24:32]
    iv    = sha_b[:8]  + sha_a[8:24]  + sha_b[24:32]
    return key, iv
