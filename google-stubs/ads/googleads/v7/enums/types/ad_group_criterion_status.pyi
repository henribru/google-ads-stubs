from typing import Any

import proto

__protobuf__: Any

class AdGroupCriterionStatusEnum(proto.Message):
    class AdGroupCriterionStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        PAUSED: int
        REMOVED: int
