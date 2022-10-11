import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import simulation as simulation
from google.ads.googleads.v11.enums.types import (
    simulation_modification_method as simulation_modification_method,
    simulation_type as simulation_type,
)

__protobuf__: Incomplete

class AdGroupCriterionSimulation(proto.Message):
    resource_name: Incomplete
    ad_group_id: Incomplete
    criterion_id: Incomplete
    type_: Incomplete
    modification_method: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    cpc_bid_point_list: Incomplete
    percent_cpc_bid_point_list: Incomplete
