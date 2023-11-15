from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class HotelPriceBucketEnum(proto.Message):
    class HotelPriceBucket(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOWEST_UNIQUE = 2
        LOWEST_TIED = 3
        NOT_LOWEST = 4
        ONLY_PARTNER_SHOWN = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
