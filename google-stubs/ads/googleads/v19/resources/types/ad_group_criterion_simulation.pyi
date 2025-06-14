import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import simulation
from google.ads.googleads.v19.enums.types import simulation_modification_method, simulation_type

__protobuf__: Incomplete

class AdGroupCriterionSimulation(proto.Message):
    resource_name: str
    ad_group_id: int
    criterion_id: int
    type_: simulation_type.SimulationTypeEnum.SimulationType
    modification_method: simulation_modification_method.SimulationModificationMethodEnum.SimulationModificationMethod
    start_date: str
    end_date: str
    cpc_bid_point_list: simulation.CpcBidSimulationPointList
    percent_cpc_bid_point_list: simulation.PercentCpcBidSimulationPointList
