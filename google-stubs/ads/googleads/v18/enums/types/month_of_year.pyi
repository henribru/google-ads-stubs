import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class MonthOfYearEnum(proto.Message):
    class MonthOfYear(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        JANUARY = 2
        FEBRUARY = 3
        MARCH = 4
        APRIL = 5
        MAY = 6
        JUNE = 7
        JULY = 8
        AUGUST = 9
        SEPTEMBER = 10
        OCTOBER = 11
        NOVEMBER = 12
        DECEMBER = 13
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
