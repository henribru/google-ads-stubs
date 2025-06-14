import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import served_asset_field_type as gage_served_asset_field_type

__protobuf__: Incomplete

class AssetUsage(proto.Message):
    asset: str
    served_asset_field_type: gage_served_asset_field_type.ServedAssetFieldTypeEnum.ServedAssetFieldType
