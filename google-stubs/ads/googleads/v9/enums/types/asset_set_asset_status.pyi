from typing import Any

import proto

__protobuf__: Any

class AssetSetAssetStatusEnum(proto.Message):
    class AssetSetAssetStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
