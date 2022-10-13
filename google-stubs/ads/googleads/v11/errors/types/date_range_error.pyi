from typing import Any

import proto

class DateRangeErrorEnum(proto.Message):
    class DateRangeError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_DATE = 2
        START_DATE_AFTER_END_DATE = 3
        CANNOT_SET_DATE_TO_PAST = 4
        AFTER_MAXIMUM_ALLOWABLE_DATE = 5
        CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
