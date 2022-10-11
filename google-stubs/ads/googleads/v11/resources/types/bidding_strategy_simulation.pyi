import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import simulation as simulation
from google.ads.googleads.v11.enums.types import (
    simulation_modification_method as simulation_modification_method,
    simulation_type as simulation_type,
)

__protobuf__: Incomplete

class BiddingStrategySimulation(proto.Message):
    resource_name: Incomplete
    bidding_strategy_id: Incomplete
    type_: Incomplete
    modification_method: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    target_cpa_point_list: Incomplete
    target_roas_point_list: Incomplete
