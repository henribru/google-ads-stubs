from typing import Any

import proto

__protobuf__: Any

class DateRangeErrorEnum(proto.Message):
    class DateRangeError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_DATE: int
        START_DATE_AFTER_END_DATE: int
        CANNOT_SET_DATE_TO_PAST: int
        AFTER_MAXIMUM_ALLOWABLE_DATE: int
        CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED: int
