from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.simulation import (
    CpcBidSimulationPointList,
    CpvBidSimulationPointList,
    TargetCpaSimulationPointList,
    TargetRoasSimulationPointList,
)
from google.ads.googleads.v14.enums.types.simulation_modification_method import (
    SimulationModificationMethodEnum,
)
from google.ads.googleads.v14.enums.types.simulation_type import SimulationTypeEnum

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        ad_group_id: int = ...,
        type_: SimulationTypeEnum.SimulationType = ...,
        modification_method: SimulationModificationMethodEnum.SimulationModificationMethod = ...,
        start_date: str = ...,
        end_date: str = ...,
        cpc_bid_point_list: CpcBidSimulationPointList = ...,
        cpv_bid_point_list: CpvBidSimulationPointList = ...,
        target_cpa_point_list: TargetCpaSimulationPointList = ...,
        target_roas_point_list: TargetRoasSimulationPointList = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "ad_group_id",
            "type_",
            "modification_method",
            "start_date",
            "end_date",
            "cpc_bid_point_list",
            "cpv_bid_point_list",
            "target_cpa_point_list",
            "target_roas_point_list",
        ],
    ) -> bool: ...
