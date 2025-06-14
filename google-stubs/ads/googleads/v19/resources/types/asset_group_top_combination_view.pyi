import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import asset_usage
from typing import MutableSequence

__protobuf__: Incomplete

class AssetGroupTopCombinationView(proto.Message):
    resource_name: str
    asset_group_top_combinations: MutableSequence['AssetGroupAssetCombinationData']

class AssetGroupAssetCombinationData(proto.Message):
    asset_combination_served_assets: MutableSequence[asset_usage.AssetUsage]
