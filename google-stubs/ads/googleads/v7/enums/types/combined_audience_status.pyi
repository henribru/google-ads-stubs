from typing import Any

import proto

__protobuf__: Any

class CombinedAudienceStatusEnum(proto.Message):
    class CombinedAudienceStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
