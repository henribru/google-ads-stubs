import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import asset_field_type

__protobuf__: Incomplete

class AssetFieldTypeView(proto.Message):
    resource_name: str
    field_type: asset_field_type.AssetFieldTypeEnum.AssetFieldType
