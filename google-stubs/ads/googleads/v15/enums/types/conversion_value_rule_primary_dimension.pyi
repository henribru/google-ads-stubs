from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ConversionValueRulePrimaryDimensionEnum(proto.Message):
    class ConversionValueRulePrimaryDimension(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NO_RULE_APPLIED = 2
        ORIGINAL = 3
        NEW_VS_RETURNING_USER = 4
        GEO_LOCATION = 5
        DEVICE = 6
        AUDIENCE = 7
        MULTIPLE = 8
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
