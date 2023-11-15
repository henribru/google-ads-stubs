from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class BatchJobStatusEnum(proto.Message):
    class BatchJobStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PENDING = 2
        RUNNING = 3
        DONE = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
