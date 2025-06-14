import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import asset_usage
from typing import MutableSequence

__protobuf__: Incomplete

class AdGroupAdAssetCombinationView(proto.Message):
    resource_name: str
    served_assets: MutableSequence[asset_usage.AssetUsage]
    enabled: bool
