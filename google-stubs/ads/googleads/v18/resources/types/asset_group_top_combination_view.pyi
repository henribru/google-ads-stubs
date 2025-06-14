from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.asset_usage import AssetUsage
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AssetGroupAssetCombinationData(proto.Message):
    asset_combination_served_assets: MutableSequence[AssetUsage]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, asset_combination_served_assets: MutableSequence[AssetUsage] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["asset_combination_served_assets"]) -> bool: ...
class AssetGroupTopCombinationView(proto.Message):
    resource_name: str
    asset_group_top_combinations: MutableSequence[AssetGroupAssetCombinationData]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., asset_group_top_combinations: MutableSequence[AssetGroupAssetCombinationData] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "asset_group_top_combinations"]) -> bool: ...
