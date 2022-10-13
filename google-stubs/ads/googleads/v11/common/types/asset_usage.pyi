from typing import Any

import proto

from google.ads.googleads.v11.enums.types.served_asset_field_type import (
    ServedAssetFieldTypeEnum,
)

class AssetUsage(proto.Message):
    asset: str
    served_asset_field_type: ServedAssetFieldTypeEnum.ServedAssetFieldType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        asset: str = ...,
        served_asset_field_type: ServedAssetFieldTypeEnum.ServedAssetFieldType = ...
    ) -> None: ...
