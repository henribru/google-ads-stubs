from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class DataDrivenModelStatusEnum(proto.Message):
    class DataDrivenModelStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AVAILABLE = 2
        STALE = 3
        EXPIRED = 4
        NEVER_GENERATED = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
