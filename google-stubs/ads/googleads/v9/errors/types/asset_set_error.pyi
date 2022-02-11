from typing import Any

import proto

__protobuf__: Any

class AssetSetErrorEnum(proto.Message):
    class AssetSetError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_ASSET_SET_NAME: int
