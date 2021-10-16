from typing import Any

import proto

__protobuf__: Any

class AssetLinkStatusEnum(proto.Message):
    class AssetLinkStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
        PAUSED: int