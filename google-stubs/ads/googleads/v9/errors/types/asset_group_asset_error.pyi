from typing import Any

import proto

__protobuf__: Any

class AssetGroupAssetErrorEnum(proto.Message):
    class AssetGroupAssetError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_RESOURCE: int
        EXPANDABLE_TAGS_NOT_ALLOWED_IN_DESCRIPTION: int
        AD_CUSTOMIZER_NOT_SUPPORTED: int
