from typing import Any

import proto

__protobuf__: Any

class FeedItemSetStatusEnum(proto.Message):
    class FeedItemSetStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
