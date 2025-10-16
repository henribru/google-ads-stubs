from google.ads.googleads.v19.common.types.simulation import TargetRoasSimulationPointList
from google.ads.googleads.v19.common.types.simulation import TargetCpaSimulationPointList
from google.ads.googleads.v19.enums.types.simulation_modification_method import SimulationModificationMethodEnum
from google.ads.googleads.v19.enums.types.simulation_type import SimulationTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., bidding_strategy_id: int = ..., type_: SimulationTypeEnum.SimulationType = ..., modification_method: SimulationModificationMethodEnum.SimulationModificationMethod = ..., start_date: str = ..., end_date: str = ..., target_cpa_point_list: TargetCpaSimulationPointList = ..., target_roas_point_list: TargetRoasSimulationPointList = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "bidding_strategy_id", "type_", "modification_method", "start_date", "end_date", "target_cpa_point_list", "target_roas_point_list"]) -> bool: ...
