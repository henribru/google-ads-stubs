from typing import Any

import proto

__protobuf__: Any

class CustomizerValueStatusEnum(proto.Message):
    class CustomizerValueStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
