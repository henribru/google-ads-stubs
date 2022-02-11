from typing import Any

import proto

__protobuf__: Any

class SharedSetStatusEnum(proto.Message):
    class SharedSetStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
