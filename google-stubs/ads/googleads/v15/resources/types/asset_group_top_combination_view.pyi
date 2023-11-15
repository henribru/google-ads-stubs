from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.asset_usage import AssetUsage

_M = TypeVar("_M")

class AssetGroupAssetCombinationData(proto.Message):
    asset_combination_served_assets: MutableSequence[AssetUsage]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset_combination_served_assets: MutableSequence[AssetUsage] = ...
    ) -> None: ...

class AssetGroupTopCombinationView(proto.Message):
    resource_name: str
    asset_group_top_combinations: MutableSequence[AssetGroupAssetCombinationData]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        asset_group_top_combinations: MutableSequence[
            AssetGroupAssetCombinationData
        ] = ...
    ) -> None: ...
