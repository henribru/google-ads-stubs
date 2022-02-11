from typing import Any

import proto

__protobuf__: Any

class AssetSetStatusEnum(proto.Message):
    class AssetSetStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
