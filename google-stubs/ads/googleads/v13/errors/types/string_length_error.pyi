from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class StringLengthErrorEnum(proto.Message):
    class StringLengthError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EMPTY = 4
        TOO_SHORT = 2
        TOO_LONG = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
