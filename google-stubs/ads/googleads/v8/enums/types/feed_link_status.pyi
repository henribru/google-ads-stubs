from typing import Any

import proto

__protobuf__: Any

class FeedLinkStatusEnum(proto.Message):
    class FeedLinkStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
