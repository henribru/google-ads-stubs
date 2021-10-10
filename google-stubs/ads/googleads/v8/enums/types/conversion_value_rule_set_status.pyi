from typing import Any

import proto

__protobuf__: Any

class ConversionValueRuleSetStatusEnum(proto.Message):
    class ConversionValueRuleSetStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
        PAUSED: int
