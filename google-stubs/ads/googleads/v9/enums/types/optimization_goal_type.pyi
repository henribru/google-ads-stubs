from typing import Any

import proto

__protobuf__: Any

class OptimizationGoalTypeEnum(proto.Message):
    class OptimizationGoalType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CALL_CLICKS: int
        DRIVING_DIRECTIONS: int
        APP_PRE_REGISTRATION: int
