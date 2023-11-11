from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ChangeStatusErrorEnum(proto.Message):
    class ChangeStatusError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        START_DATE_TOO_OLD = 3
        CHANGE_DATE_RANGE_INFINITE = 4
        CHANGE_DATE_RANGE_NEGATIVE = 5
        LIMIT_NOT_SPECIFIED = 6
        INVALID_LIMIT_CLAUSE = 7
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
