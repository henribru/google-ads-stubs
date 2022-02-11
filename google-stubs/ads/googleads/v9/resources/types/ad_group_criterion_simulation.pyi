from typing import Any

import proto

from google.ads.googleads.v9.common.types import simulation as simulation
from google.ads.googleads.v9.enums.types import (
    simulation_modification_method as simulation_modification_method,
    simulation_type as simulation_type,
)

__protobuf__: Any

class AdGroupCriterionSimulation(proto.Message):
    resource_name: Any
    ad_group_id: Any
    criterion_id: Any
    type_: Any
    modification_method: Any
    start_date: Any
    end_date: Any
    cpc_bid_point_list: Any
    percent_cpc_bid_point_list: Any
