from typing import Any

import proto

__protobuf__: Any

class CustomAudienceStatusEnum(proto.Message):
    class CustomAudienceStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
