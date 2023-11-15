from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ValueRuleSetDimensionEnum(proto.Message):
    class ValueRuleSetDimension(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        GEO_LOCATION = 2
        DEVICE = 3
        AUDIENCE = 4
        NO_CONDITION = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
