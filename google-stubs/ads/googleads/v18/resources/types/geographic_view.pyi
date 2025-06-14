import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import geo_targeting_type

__protobuf__: Incomplete

class GeographicView(proto.Message):
    resource_name: str
    location_type: geo_targeting_type.GeoTargetingTypeEnum.GeoTargetingType
    country_criterion_id: int
