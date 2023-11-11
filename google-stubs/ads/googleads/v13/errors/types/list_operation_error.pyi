from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ListOperationErrorEnum(proto.Message):
    class ListOperationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        REQUIRED_FIELD_MISSING = 7
        DUPLICATE_VALUES = 8
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
