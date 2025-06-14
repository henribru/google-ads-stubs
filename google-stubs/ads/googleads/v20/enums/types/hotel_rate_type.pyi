import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class HotelRateTypeEnum(proto.Message):
    class HotelRateType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNAVAILABLE = 2
        PUBLIC_RATE = 3
        QUALIFIED_RATE = 4
        PRIVATE_RATE = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
