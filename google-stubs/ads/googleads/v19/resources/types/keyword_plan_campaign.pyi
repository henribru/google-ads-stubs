import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import keyword_plan_network as gage_keyword_plan_network
from typing import MutableSequence

__protobuf__: Incomplete

class KeywordPlanCampaign(proto.Message):
    resource_name: str
    keyword_plan: str
    id: int
    name: str
    language_constants: MutableSequence[str]
    keyword_plan_network: gage_keyword_plan_network.KeywordPlanNetworkEnum.KeywordPlanNetwork
    cpc_bid_micros: int
    geo_targets: MutableSequence['KeywordPlanGeoTarget']

class KeywordPlanGeoTarget(proto.Message):
    geo_target_constant: str
