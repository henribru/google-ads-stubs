from typing import Any

import proto

__protobuf__: Any

class AssetSetLinkStatusEnum(proto.Message):
    class AssetSetLinkStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
