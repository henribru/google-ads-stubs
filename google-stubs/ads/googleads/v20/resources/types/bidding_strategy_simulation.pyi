import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import simulation
from google.ads.googleads.v20.enums.types import simulation_modification_method, simulation_type

__protobuf__: Incomplete

class BiddingStrategySimulation(proto.Message):
    resource_name: str
    bidding_strategy_id: int
    type_: simulation_type.SimulationTypeEnum.SimulationType
    modification_method: simulation_modification_method.SimulationModificationMethodEnum.SimulationModificationMethod
    start_date: str
    end_date: str
    target_cpa_point_list: simulation.TargetCpaSimulationPointList
    target_roas_point_list: simulation.TargetRoasSimulationPointList
