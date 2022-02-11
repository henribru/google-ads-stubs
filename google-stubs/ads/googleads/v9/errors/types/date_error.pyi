from typing import Any

import proto

__protobuf__: Any

class DateErrorEnum(proto.Message):
    class DateError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_FIELD_VALUES_IN_DATE: int
        INVALID_FIELD_VALUES_IN_DATE_TIME: int
        INVALID_STRING_DATE: int
        INVALID_STRING_DATE_TIME_MICROS: int
        INVALID_STRING_DATE_TIME_SECONDS: int
        INVALID_STRING_DATE_TIME_SECONDS_WITH_OFFSET: int
        EARLIER_THAN_MINIMUM_DATE: int
        LATER_THAN_MAXIMUM_DATE: int
        DATE_RANGE_MINIMUM_DATE_LATER_THAN_MAXIMUM_DATE: int
        DATE_RANGE_MINIMUM_AND_MAXIMUM_DATES_BOTH_NULL: int
