import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import asset_field_type, asset_source as gage_asset_source

__protobuf__: Incomplete

class CampaignAggregateAssetView(proto.Message):
    resource_name: str
    campaign: str
    asset: str
    asset_source: gage_asset_source.AssetSourceEnum.AssetSource
    field_type: asset_field_type.AssetFieldTypeEnum.AssetFieldType
