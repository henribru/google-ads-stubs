from typing import Any

import proto

__protobuf__: Any

class GoalConfigLevelEnum(proto.Message):
    class GoalConfigLevel(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CUSTOMER: int
        CAMPAIGN: int
