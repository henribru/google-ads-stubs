from typing import Any

import proto

__protobuf__: Any

class CustomConversionGoalStatusEnum(proto.Message):
    class CustomConversionGoalStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
