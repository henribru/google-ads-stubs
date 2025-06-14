import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import geo_target_constant_status

__protobuf__: Incomplete

class GeoTargetConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    country_code: str
    target_type: str
    status: geo_target_constant_status.GeoTargetConstantStatusEnum.GeoTargetConstantStatus
    canonical_name: str
    parent_geo_target: str
