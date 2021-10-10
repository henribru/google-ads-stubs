from typing import Any

import proto

__protobuf__: Any

class ConversionCustomVariableStatusEnum(proto.Message):
    class ConversionCustomVariableStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ACTIVATION_NEEDED: int
        ENABLED: int
        PAUSED: int
