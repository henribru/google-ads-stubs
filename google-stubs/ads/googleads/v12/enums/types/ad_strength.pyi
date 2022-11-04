from typing import Any

import proto

class AdStrengthEnum(proto.Message):
    class AdStrength(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PENDING = 2
        NO_ADS = 3
        POOR = 4
        AVERAGE = 5
        GOOD = 6
        EXCELLENT = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
