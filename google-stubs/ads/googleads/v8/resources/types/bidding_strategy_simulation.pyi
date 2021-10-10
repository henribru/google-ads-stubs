from typing import Any

import proto

from google.ads.googleads.v8.common.types import simulation as simulation
from google.ads.googleads.v8.enums.types import (
    simulation_modification_method as simulation_modification_method,
    simulation_type as simulation_type,
)

__protobuf__: Any

class BiddingStrategySimulation(proto.Message):
    resource_name: Any
    bidding_strategy_id: Any
    type_: Any
    modification_method: Any
    start_date: Any
    end_date: Any
    target_cpa_point_list: Any
    target_roas_point_list: Any
