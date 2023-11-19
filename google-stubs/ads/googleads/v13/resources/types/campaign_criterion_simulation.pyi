from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v13.common.types.simulation import (
    BidModifierSimulationPointList,
)
from google.ads.googleads.v13.enums.types.simulation_modification_method import (
    SimulationModificationMethodEnum,
)
from google.ads.googleads.v13.enums.types.simulation_type import SimulationTypeEnum

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign_id: int = ...,
        criterion_id: int = ...,
        type_: SimulationTypeEnum.SimulationType = ...,
        modification_method: SimulationModificationMethodEnum.SimulationModificationMethod = ...,
        start_date: str = ...,
        end_date: str = ...,
        bid_modifier_point_list: BidModifierSimulationPointList = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "campaign_id", "criterion_id", "type_", "modification_method", "start_date", "end_date", "bid_modifier_point_list"]) -> bool: ...  # type: ignore[override]
