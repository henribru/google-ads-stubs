import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import asset_set_type as gage_asset_set_type

__protobuf__: Incomplete

class AssetSetTypeView(proto.Message):
    resource_name: str
    asset_set_type: gage_asset_set_type.AssetSetTypeEnum.AssetSetType
