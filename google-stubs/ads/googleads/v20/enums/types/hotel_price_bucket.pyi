import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class HotelPriceBucketEnum(proto.Message):
    class HotelPriceBucket(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOWEST_UNIQUE = 2
        LOWEST_TIED = 3
        NOT_LOWEST = 4
        ONLY_PARTNER_SHOWN = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
