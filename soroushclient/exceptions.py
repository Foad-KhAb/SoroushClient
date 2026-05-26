class SoroushError(Exception):
    """Base exception for all Soroush errors."""

    pass


class RpcException(SoroushError):
    def __init__(self, error_code: int, error_message: str):
        self.error_code = error_code
        self.error_message = error_message
        super().__init__(f"[{error_code}] {error_message}")


# ── 400 errors ────────────────────────────────────────────────────────────────
class UsernameInvalidError(RpcException):
    pass


class NotFoundError(RpcException):
    pass


class ChannelPrivateError(RpcException):
    pass


# ── 404 errors ────────────────────────────────────────────────────────────────
class UsernameNotOccupiedError(RpcException):
    pass


# ── 420 errors ────────────────────────────────────────────────────────────────
class FloodWaitError(RpcException):
    def __init__(self, error_code: int, error_message: str):
        # extract wait seconds from "FLOOD_WAIT_60"
        parts = error_message.split("_")
        self.wait_seconds = int(parts[-1]) if parts[-1].isdigit() else 0
        super().__init__(error_code, error_message)


# ── mapping ───────────────────────────────────────────────────────────────────
_ERROR_MAP: dict[str, type[RpcException]] = {
    "USERNAME_INVALID": UsernameInvalidError,
    "NOT_FOUND": NotFoundError,
    "USERNAME_NOT_OCCUPIED": UsernameNotOccupiedError,
    "CHANNEL_PRIVATE": ChannelPrivateError,
}


def raise_rpc_error(error_code: int, error_message: str):
    cls = _ERROR_MAP.get(error_message, RpcException)
    # handle FLOOD_WAIT_X pattern
    if error_message.startswith("FLOOD_WAIT_"):
        raise FloodWaitError(error_code, error_message)
    raise cls(error_code, error_message)
