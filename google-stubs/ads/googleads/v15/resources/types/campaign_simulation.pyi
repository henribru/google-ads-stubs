from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.simulation import (
    BudgetSimulationPointList,
    CpcBidSimulationPointList,
    TargetCpaSimulationPointList,
    TargetImpressionShareSimulationPointList,
    TargetRoasSimulationPointList,
)
from google.ads.googleads.v15.enums.types.simulation_modification_method import (
    SimulationModificationMethodEnum,
)
from google.ads.googleads.v15.enums.types.simulation_type import SimulationTypeEnum

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
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
