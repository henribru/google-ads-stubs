from google.ads.googleads.v23.common.types.simulation import BudgetSimulationPointList
from google.ads.googleads.v23.common.types.simulation import TargetImpressionShareSimulationPointList
from google.ads.googleads.v23.common.types.simulation import TargetRoasSimulationPointList
from google.ads.googleads.v23.common.types.simulation import TargetCpaSimulationPointList
from google.ads.googleads.v23.common.types.simulation import CpcBidSimulationPointList
from google.ads.googleads.v23.enums.types.simulation_modification_method import SimulationModificationMethodEnum
from google.ads.googleads.v23.enums.types.simulation_type import SimulationTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., campaign_id: int = ..., type_: SimulationTypeEnum.SimulationType = ..., modification_method: SimulationModificationMethodEnum.SimulationModificationMethod = ..., start_date: str = ..., end_date: str = ..., cpc_bid_point_list: CpcBidSimulationPointList = ..., target_cpa_point_list: TargetCpaSimulationPointList = ..., target_roas_point_list: TargetRoasSimulationPointList = ..., target_impression_share_point_list: TargetImpressionShareSimulationPointList = ..., budget_point_list: BudgetSimulationPointList = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "campaign_id", "type_", "modification_method", "start_date", "end_date", "cpc_bid_point_list", "target_cpa_point_list", "target_roas_point_list", "target_impression_share_point_list", "budget_point_list"]) -> bool: ...
