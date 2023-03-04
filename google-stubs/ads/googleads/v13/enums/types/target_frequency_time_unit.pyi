from typing import Any

import proto

class TargetFrequencyTimeUnitEnum(proto.Message):
    class TargetFrequencyTimeUnit(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        WEEKLY = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...