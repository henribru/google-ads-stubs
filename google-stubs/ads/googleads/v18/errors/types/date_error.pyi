from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class DateErrorEnum(proto.Message):
    class DateError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_FIELD_VALUES_IN_DATE = 2
        INVALID_FIELD_VALUES_IN_DATE_TIME = 3
        INVALID_STRING_DATE = 4
        INVALID_STRING_DATE_TIME_MICROS = 6
        INVALID_STRING_DATE_TIME_SECONDS = 11
        INVALID_STRING_DATE_TIME_SECONDS_WITH_OFFSET = 12
        EARLIER_THAN_MINIMUM_DATE = 7
        LATER_THAN_MAXIMUM_DATE = 8
        DATE_RANGE_MINIMUM_DATE_LATER_THAN_MAXIMUM_DATE = 9
        DATE_RANGE_MINIMUM_AND_MAXIMUM_DATES_BOTH_NULL = 10

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
