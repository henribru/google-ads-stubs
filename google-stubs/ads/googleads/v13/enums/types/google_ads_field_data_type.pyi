from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class GoogleAdsFieldDataTypeEnum(proto.Message):
    class GoogleAdsFieldDataType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BOOLEAN = 2
        DATE = 3
        DOUBLE = 4
        ENUM = 5
        FLOAT = 6
        INT32 = 7
        INT64 = 8
        MESSAGE = 9
        RESOURCE_NAME = 10
        STRING = 11
        UINT64 = 12
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
