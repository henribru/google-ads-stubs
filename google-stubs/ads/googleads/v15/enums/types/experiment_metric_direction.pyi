from typing import Any

import proto

class ExperimentMetricDirectionEnum(proto.Message):
    class ExperimentMetricDirection(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NO_CHANGE = 2
        INCREASE = 3
        DECREASE = 4
        NO_CHANGE_OR_INCREASE = 5
        NO_CHANGE_OR_DECREASE = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
