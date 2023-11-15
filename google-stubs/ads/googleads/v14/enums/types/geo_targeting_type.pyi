from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class GeoTargetingTypeEnum(proto.Message):
    class GeoTargetingType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AREA_OF_INTEREST = 2
        LOCATION_OF_PRESENCE = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
