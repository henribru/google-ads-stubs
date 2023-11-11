from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ContextErrorEnum(proto.Message):
    class ContextError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPERATION_NOT_PERMITTED_FOR_CONTEXT = 2
        OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
