from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.simulation import (
    CpcBidSimulationPointList,
    PercentCpcBidSimulationPointList,
)
from google.ads.googleads.v15.enums.types.simulation_modification_method import (
    SimulationModificationMethodEnum,
)
from google.ads.googleads.v15.enums.types.simulation_type import SimulationTypeEnum

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
