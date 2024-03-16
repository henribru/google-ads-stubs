from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.simulation import (
    CpcBidSimulationPointList,
    PercentCpcBidSimulationPointList,
)
from google.ads.googleads.v16.enums.types.simulation_modification_method import (
    SimulationModificationMethodEnum,
)
from google.ads.googleads.v16.enums.types.simulation_type import SimulationTypeEnum

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
        percent_cpc_bid_point_list: PercentCpcBidSimulationPointList = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "ad_group_id",
            "criterion_id",
            "type_",
            "modification_method",
            "start_date",
            "end_date",
            "cpc_bid_point_list",
            "percent_cpc_bid_point_list",
        ],
    ) -> bool: ...
