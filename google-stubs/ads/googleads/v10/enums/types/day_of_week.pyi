from typing import Any

import proto

class DayOfWeekEnum(proto.Message):
    class DayOfWeek(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MONDAY = 2
        TUESDAY = 3
        WEDNESDAY = 4
        THURSDAY = 5
        FRIDAY = 6
        SATURDAY = 7
        SUNDAY = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
