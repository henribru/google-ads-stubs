from google.ads.googleads.v20.common.types.simulation import PercentCpcBidSimulationPointList
from google.ads.googleads.v20.common.types.simulation import CpcBidSimulationPointList
from google.ads.googleads.v20.enums.types.simulation_modification_method import SimulationModificationMethodEnum
from google.ads.googleads.v20.enums.types.simulation_type import SimulationTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., ad_group_id: int = ..., criterion_id: int = ..., type_: SimulationTypeEnum.SimulationType = ..., modification_method: SimulationModificationMethodEnum.SimulationModificationMethod = ..., start_date: str = ..., end_date: str = ..., cpc_bid_point_list: CpcBidSimulationPointList = ..., percent_cpc_bid_point_list: PercentCpcBidSimulationPointList = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "ad_group_id", "criterion_id", "type_", "modification_method", "start_date", "end_date", "cpc_bid_point_list", "percent_cpc_bid_point_list"]) -> bool: ...
