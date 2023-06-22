from typing import Any

import proto

class ReachPlanErrorEnum(proto.Message):
    class ReachPlanError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_FORECASTABLE_MISSING_RATE = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
