from typing import Any

import proto

__protobuf__: Any

class AdGroupAdStatusEnum(proto.Message):
    class AdGroupAdStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        PAUSED: int
        REMOVED: int
