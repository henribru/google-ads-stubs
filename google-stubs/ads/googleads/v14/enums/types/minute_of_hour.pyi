from typing import Any

import proto

class MinuteOfHourEnum(proto.Message):
    class MinuteOfHour(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ZERO = 2
        FIFTEEN = 3
        THIRTY = 4
        FORTY_FIVE = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
