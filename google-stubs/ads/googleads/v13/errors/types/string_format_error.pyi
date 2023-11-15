from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class StringFormatErrorEnum(proto.Message):
    class StringFormatError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ILLEGAL_CHARS = 2
        INVALID_FORMAT = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
