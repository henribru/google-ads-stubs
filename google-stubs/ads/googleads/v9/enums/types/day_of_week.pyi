from typing import Any

import proto

__protobuf__: Any

class DayOfWeekEnum(proto.Message):
    class DayOfWeek(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MONDAY: int
        TUESDAY: int
        WEDNESDAY: int
        THURSDAY: int
        FRIDAY: int
        SATURDAY: int
        SUNDAY: int
