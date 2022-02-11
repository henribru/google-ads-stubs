from typing import Any

import proto

__protobuf__: Any

class SearchTermTargetingStatusEnum(proto.Message):
    class SearchTermTargetingStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADDED: int
        EXCLUDED: int
        ADDED_EXCLUDED: int
        NONE: int
