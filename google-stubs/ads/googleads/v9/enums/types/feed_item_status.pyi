from typing import Any

import proto

__protobuf__: Any

class FeedItemStatusEnum(proto.Message):
    class FeedItemStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
