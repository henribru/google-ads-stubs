from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class SkAdNetworkCoarseConversionValueEnum(proto.Message):
    class SkAdNetworkCoarseConversionValue(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNAVAILABLE = 2
        LOW = 3
        MEDIUM = 4
        HIGH = 5
        NONE = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
