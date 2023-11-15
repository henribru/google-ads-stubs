from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AsyncActionStatusEnum(proto.Message):
    class AsyncActionStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_STARTED = 2
        IN_PROGRESS = 3
        COMPLETED = 4
        FAILED = 5
        COMPLETED_WITH_WARNING = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
