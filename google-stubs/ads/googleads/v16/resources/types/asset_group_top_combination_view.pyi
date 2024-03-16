from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.asset_usage import AssetUsage

_M = TypeVar("_M")

class AssetGroupAssetCombinationData(proto.Message):
    asset_combination_served_assets: MutableSequence[AssetUsage]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset_combination_served_assets: MutableSequence[AssetUsage] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["asset_combination_served_assets"]
    ) -> bool: ...

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
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "asset_group_top_combinations"]
    ) -> bool: ...
