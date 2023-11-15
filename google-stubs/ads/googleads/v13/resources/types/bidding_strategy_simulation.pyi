from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.common.types.simulation import (
    TargetCpaSimulationPointList,
    TargetRoasSimulationPointList,
)
from google.ads.googleads.v13.enums.types.simulation_modification_method import (
    SimulationModificationMethodEnum,
)
from google.ads.googleads.v13.enums.types.simulation_type import SimulationTypeEnum

_M = TypeVar("_M")

class BiddingStrategySimulation(proto.Message):
    resource_name: str
    bidding_strategy_id: int
    type_: SimulationTypeEnum.SimulationType
    modification_method: SimulationModificationMethodEnum.SimulationModificationMethod
    start_date: str
    end_date: str
    target_cpa_point_list: TargetCpaSimulationPointList
    target_roas_point_list: TargetRoasSimulationPointList
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        bidding_strategy_id: int = ...,
        type_: SimulationTypeEnum.SimulationType = ...,
        modification_method: SimulationModificationMethodEnum.SimulationModificationMethod = ...,
        start_date: str = ...,
        end_date: str = ...,
        target_cpa_point_list: TargetCpaSimulationPointList = ...,
        target_roas_point_list: TargetRoasSimulationPointList = ...
    ) -> None: ...
