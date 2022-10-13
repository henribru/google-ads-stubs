from typing import Any

import proto

from google.ads.googleads.v10.common.types.simulation import (
    BidModifierSimulationPointList,
)
from google.ads.googleads.v10.enums.types.simulation_modification_method import (
    SimulationModificationMethodEnum,
)
from google.ads.googleads.v10.enums.types.simulation_type import SimulationTypeEnum

class CampaignCriterionSimulation(proto.Message):
    resource_name: str
    campaign_id: int
    criterion_id: int
    type_: SimulationTypeEnum.SimulationType
    modification_method: SimulationModificationMethodEnum.SimulationModificationMethod
    start_date: str
    end_date: str
    bid_modifier_point_list: BidModifierSimulationPointList
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_id: int = ...,
        criterion_id: int = ...,
        type_: SimulationTypeEnum.SimulationType = ...,
        modification_method: SimulationModificationMethodEnum.SimulationModificationMethod = ...,
        start_date: str = ...,
        end_date: str = ...,
        bid_modifier_point_list: BidModifierSimulationPointList = ...
    ) -> None: ...
