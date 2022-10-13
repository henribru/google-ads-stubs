from typing import Any

import proto

class AssetSetAssetErrorEnum(proto.Message):
    class AssetSetAssetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_ASSET_TYPE = 2
        INVALID_ASSET_SET_TYPE = 3
        DUPLICATE_EXTERNAL_KEY = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
