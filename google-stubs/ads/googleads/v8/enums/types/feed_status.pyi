from typing import Any

import proto

__protobuf__: Any

class FeedStatusEnum(proto.Message):
    class FeedStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
