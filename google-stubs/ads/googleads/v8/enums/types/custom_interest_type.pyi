from typing import Any

import proto

__protobuf__: Any

class CustomInterestTypeEnum(proto.Message):
    class CustomInterestType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CUSTOM_AFFINITY: int
        CUSTOM_INTENT: int
