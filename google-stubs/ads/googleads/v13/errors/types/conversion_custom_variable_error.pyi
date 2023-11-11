from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ConversionCustomVariableErrorEnum(proto.Message):
    class ConversionCustomVariableError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_NAME = 2
        DUPLICATE_TAG = 3
        RESERVED_TAG = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
