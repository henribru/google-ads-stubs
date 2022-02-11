from typing import Any

import proto

__protobuf__: Any

class AssetGroupStatusEnum(proto.Message):
    class AssetGroupStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        PAUSED: int
        REMOVED: int
