from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class LocationGroupRadiusUnitsEnum(proto.Message):
    class LocationGroupRadiusUnits(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        METERS = 2
        MILES = 3
        MILLI_MILES = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
