from typing import Any

import proto

class FrequencyCapTimeUnitEnum(proto.Message):
    class FrequencyCapTimeUnit(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DAY = 2
        WEEK = 3
        MONTH = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
