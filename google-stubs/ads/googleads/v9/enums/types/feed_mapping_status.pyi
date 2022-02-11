from typing import Any

import proto

__protobuf__: Any

class FeedMappingStatusEnum(proto.Message):
    class FeedMappingStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
