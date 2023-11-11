from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class QuotaErrorEnum(proto.Message):
    class QuotaError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RESOURCE_EXHAUSTED = 2
        ACCESS_PROHIBITED = 3
        RESOURCE_TEMPORARILY_EXHAUSTED = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
