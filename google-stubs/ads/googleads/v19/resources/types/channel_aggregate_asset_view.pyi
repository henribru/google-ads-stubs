import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import advertising_channel_type as gage_advertising_channel_type, asset_field_type, asset_source as gage_asset_source

__protobuf__: Incomplete

class ChannelAggregateAssetView(proto.Message):
    resource_name: str
    advertising_channel_type: gage_advertising_channel_type.AdvertisingChannelTypeEnum.AdvertisingChannelType
    asset: str
    asset_source: gage_asset_source.AssetSourceEnum.AssetSource
    field_type: asset_field_type.AssetFieldTypeEnum.AssetFieldType
