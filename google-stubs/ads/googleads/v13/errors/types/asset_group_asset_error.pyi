from typing import Any

import proto

class AssetGroupAssetErrorEnum(proto.Message):
    class AssetGroupAssetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_RESOURCE = 2
        EXPANDABLE_TAGS_NOT_ALLOWED_IN_DESCRIPTION = 3
        AD_CUSTOMIZER_NOT_SUPPORTED = 4
        HOTEL_PROPERTY_ASSET_NOT_LINKED_TO_CAMPAIGN = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
