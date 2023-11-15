from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class NullErrorEnum(proto.Message):
    class NullError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NULL_CONTENT = 2
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
