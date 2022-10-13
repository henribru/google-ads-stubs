from typing import Any

import proto

from google.ads.googleads.v11.common.types.simulation import (
    CpcBidSimulationPointList,
    PercentCpcBidSimulationPointList,
)
from google.ads.googleads.v11.enums.types.simulation_modification_method import (
    SimulationModificationMethodEnum,
)
from google.ads.googleads.v11.enums.types.simulation_type import SimulationTypeEnum

class AdGroupCriterionSimulation(proto.Message):
    resource_name: str
    ad_group_id: int
    criterion_id: int
    type_: SimulationTypeEnum.SimulationType
    modification_method: SimulationModificationMethodEnum.SimulationModificationMethod
    start_date: str
    end_date: str
    cpc_bid_point_list: CpcBidSimulationPointList
    percent_cpc_bid_point_list: PercentCpcBidSimulationPointList
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_id: int = ...,
        criterion_id: int = ...,
        type_: SimulationTypeEnum.SimulationType = ...,
        modification_method: SimulationModificationMethodEnum.SimulationModificationMethod = ...,
        start_date: str = ...,
        end_date: str = ...,
        cpc_bid_point_list: CpcBidSimulationPointList = ...,
        percent_cpc_bid_point_list: PercentCpcBidSimulationPointList = ...
    ) -> None: ...
