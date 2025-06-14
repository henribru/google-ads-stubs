import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import placement_type as gage_placement_type

__protobuf__: Incomplete

class PerformanceMaxPlacementView(proto.Message):
    resource_name: str
    placement: str
    display_name: str
    target_url: str
    placement_type: gage_placement_type.PlacementTypeEnum.PlacementType
