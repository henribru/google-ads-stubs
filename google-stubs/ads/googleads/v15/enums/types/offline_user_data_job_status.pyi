from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class OfflineUserDataJobStatusEnum(proto.Message):
    class OfflineUserDataJobStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PENDING = 2
        RUNNING = 3
        SUCCESS = 4
        FAILED = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
