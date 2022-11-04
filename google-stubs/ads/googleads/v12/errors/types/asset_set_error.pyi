from typing import Any

import proto

class AssetSetErrorEnum(proto.Message):
    class AssetSetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_ASSET_SET_NAME = 2
        INVALID_PARENT_ASSET_SET_TYPE = 3
        ASSET_SET_SOURCE_INCOMPATIBLE_WITH_PARENT_ASSET_SET = 4
        ASSET_SET_TYPE_CANNOT_BE_LINKED_TO_CUSTOMER = 5
        INVALID_CHAIN_IDS = 6
        LOCATION_SYNC_ASSET_SET_DOES_NOT_SUPPORT_RELATIONSHIP_TYPE = 7
        NOT_UNIQUE_ENABLED_LOCATION_SYNC_TYPED_ASSET_SET = 8
        INVALID_PLACE_IDS = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
