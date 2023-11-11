from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class DatabaseErrorEnum(proto.Message):
    class DatabaseError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CONCURRENT_MODIFICATION = 2
        DATA_CONSTRAINT_VIOLATION = 3
        REQUEST_TOO_LARGE = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
