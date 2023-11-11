from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CustomerStatusEnum(proto.Message):
    class CustomerStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENABLED = 2
        CANCELED = 3
        SUSPENDED = 4
        CLOSED = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
