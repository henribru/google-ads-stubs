from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class TimeTypeEnum(proto.Message):
    class TimeType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOW = 2
        FOREVER = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
