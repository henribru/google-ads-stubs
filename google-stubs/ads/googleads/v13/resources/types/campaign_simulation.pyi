from typing import Any

import proto

from google.ads.googleads.v13.common.types.simulation import (
    BudgetSimulationPointList,
    CpcBidSimulationPointList,
    TargetCpaSimulationPointList,
    TargetImpressionShareSimulationPointList,
    TargetRoasSimulationPointList,
)
from google.ads.googleads.v13.enums.types.simulation_modification_method import (
    SimulationModificationMethodEnum,
)
from google.ads.googleads.v13.enums.types.simulation_type import SimulationTypeEnum

class CampaignSimulation(proto.Message):
    resource_name: str
    campaign_id: int
    type_: SimulationTypeEnum.SimulationType
    modification_method: SimulationModificationMethodEnum.SimulationModificationMethod
    start_date: str
    end_date: str
    cpc_bid_point_list: CpcBidSimulationPointList
    target_cpa_point_list: TargetCpaSimulationPointList
    target_roas_point_list: TargetRoasSimulationPointList
    target_impression_share_point_list: TargetImpressionShareSimulationPointList
    budget_point_list: BudgetSimulationPointList
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_id: int = ...,
        type_: SimulationTypeEnum.SimulationType = ...,
        modification_method: SimulationModificationMethodEnum.SimulationModificationMethod = ...,
        start_date: str = ...,
        end_date: str = ...,
        cpc_bid_point_list: CpcBidSimulationPointList = ...,
        target_cpa_point_list: TargetCpaSimulationPointList = ...,
        target_roas_point_list: TargetRoasSimulationPointList = ...,
        target_impression_share_point_list: TargetImpressionShareSimulationPointList = ...,
        budget_point_list: BudgetSimulationPointList = ...
    ) -> None: ...
