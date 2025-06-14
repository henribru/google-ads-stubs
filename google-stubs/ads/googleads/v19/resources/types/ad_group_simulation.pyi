import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import simulation
from google.ads.googleads.v19.enums.types import simulation_modification_method, simulation_type

__protobuf__: Incomplete

class AdGroupSimulation(proto.Message):
    resource_name: str
    ad_group_id: int
    type_: simulation_type.SimulationTypeEnum.SimulationType
    modification_method: simulation_modification_method.SimulationModificationMethodEnum.SimulationModificationMethod
    start_date: str
    end_date: str
    cpc_bid_point_list: simulation.CpcBidSimulationPointList
    cpv_bid_point_list: simulation.CpvBidSimulationPointList
    target_cpa_point_list: simulation.TargetCpaSimulationPointList
    target_roas_point_list: simulation.TargetRoasSimulationPointList
