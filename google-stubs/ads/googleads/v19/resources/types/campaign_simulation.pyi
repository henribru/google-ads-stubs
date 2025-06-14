import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import simulation
from google.ads.googleads.v19.enums.types import simulation_modification_method, simulation_type

__protobuf__: Incomplete

class CampaignSimulation(proto.Message):
    resource_name: str
    campaign_id: int
    type_: simulation_type.SimulationTypeEnum.SimulationType
    modification_method: simulation_modification_method.SimulationModificationMethodEnum.SimulationModificationMethod
    start_date: str
    end_date: str
    cpc_bid_point_list: simulation.CpcBidSimulationPointList
    target_cpa_point_list: simulation.TargetCpaSimulationPointList
    target_roas_point_list: simulation.TargetRoasSimulationPointList
    target_impression_share_point_list: simulation.TargetImpressionShareSimulationPointList
    budget_point_list: simulation.BudgetSimulationPointList
