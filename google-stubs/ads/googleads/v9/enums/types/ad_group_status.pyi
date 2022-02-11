from typing import Any

import proto

__protobuf__: Any

class AdGroupStatusEnum(proto.Message):
    class AdGroupStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        PAUSED: int
        REMOVED: int
