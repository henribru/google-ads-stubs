from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class PriceExtensionPriceQualifierEnum(proto.Message):
    class PriceExtensionPriceQualifier(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FROM = 2
        UP_TO = 3
        AVERAGE = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
