from typing import Any

import proto

__protobuf__: Any

class ReachPlanErrorEnum(proto.Message):
    class ReachPlanError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NOT_FORECASTABLE_MISSING_RATE: int
