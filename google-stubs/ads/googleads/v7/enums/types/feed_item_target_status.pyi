from typing import Any

import proto

__protobuf__: Any

class FeedItemTargetStatusEnum(proto.Message):
    class FeedItemTargetStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
