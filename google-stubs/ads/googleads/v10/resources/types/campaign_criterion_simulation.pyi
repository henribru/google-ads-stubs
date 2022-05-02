import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.common.types import simulation as simulation
from google.ads.googleads.v10.enums.types import (
    simulation_modification_method as simulation_modification_method,
    simulation_type as simulation_type,
)

__protobuf__: Incomplete

class CampaignCriterionSimulation(proto.Message):
    resource_name: Incomplete
    campaign_id: Incomplete
    criterion_id: Incomplete
    type_: Incomplete
    modification_method: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    bid_modifier_point_list: Incomplete
