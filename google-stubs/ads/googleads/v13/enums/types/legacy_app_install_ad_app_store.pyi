from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class LegacyAppInstallAdAppStoreEnum(proto.Message):
    class LegacyAppInstallAdAppStore(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        APPLE_APP_STORE = 2
        GOOGLE_PLAY = 3
        WINDOWS_STORE = 4
        WINDOWS_PHONE_STORE = 5
        CN_APP_STORE = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
