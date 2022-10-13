from typing import Any

import proto

from google.ads.googleads.v10.common.types.simulation import (
    CpcBidSimulationPointList,
    CpvBidSimulationPointList,
    TargetCpaSimulationPointList,
    TargetRoasSimulationPointList,
)
from google.ads.googleads.v10.enums.types.simulation_modification_method import (
    SimulationModificationMethodEnum,
)
from google.ads.googleads.v10.enums.types.simulation_type import SimulationTypeEnum

class AdGroupSimulation(proto.Message):
    resource_name: str
    ad_group_id: int
    type_: SimulationTypeEnum.SimulationType
    modification_method: SimulationModificationMethodEnum.SimulationModificationMethod
    start_date: str
    end_date: str
    cpc_bid_point_list: CpcBidSimulationPointList
    cpv_bid_point_list: CpvBidSimulationPointList
    target_cpa_point_list: TargetCpaSimulationPointList
    target_roas_point_list: TargetRoasSimulationPointList
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_id: int = ...,
        type_: SimulationTypeEnum.SimulationType = ...,
        modification_method: SimulationModificationMethodEnum.SimulationModificationMethod = ...,
        start_date: str = ...,
        end_date: str = ...,
        cpc_bid_point_list: CpcBidSimulationPointList = ...,
        cpv_bid_point_list: CpvBidSimulationPointList = ...,
        target_cpa_point_list: TargetCpaSimulationPointList = ...,
        target_roas_point_list: TargetRoasSimulationPointList = ...
    ) -> None: ...
