from typing import Any

import proto

class OptimizationGoalTypeEnum(proto.Message):
    class OptimizationGoalType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CALL_CLICKS = 2
        DRIVING_DIRECTIONS = 3
        APP_PRE_REGISTRATION = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
