from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v15.common.types.asset_usage import AssetUsage

class AssetGroupAssetCombinationData(proto.Message):
    asset_combination_served_assets: MutableSequence[AssetUsage]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        asset_combination_served_assets: MutableSequence[AssetUsage] = ...
    ) -> None: ...

class AssetGroupTopCombinationView(proto.Message):
    resource_name: str
    asset_group_top_combinations: MutableSequence[AssetGroupAssetCombinationData]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_group_top_combinations: MutableSequence[
            AssetGroupAssetCombinationData
        ] = ...
    ) -> None: ...
