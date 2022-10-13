from typing import Any

import proto

from google.ads.googleads.v11.enums.types.asset_set_asset_status import (
    AssetSetAssetStatusEnum,
)

class AssetSetAsset(proto.Message):
    resource_name: str
    asset_set: str
    asset: str
    status: AssetSetAssetStatusEnum.AssetSetAssetStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_set: str = ...,
        asset: str = ...,
        status: AssetSetAssetStatusEnum.AssetSetAssetStatus = ...
    ) -> None: ...
