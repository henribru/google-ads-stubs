import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import asset_set_asset_status

__protobuf__: Incomplete

class AssetSetAsset(proto.Message):
    resource_name: str
    asset_set: str
    asset: str
    status: asset_set_asset_status.AssetSetAssetStatusEnum.AssetSetAssetStatus
