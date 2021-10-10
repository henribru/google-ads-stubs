from typing import Any

import proto

__protobuf__: Any

class KeywordPlanCampaign(proto.Message):
    resource_name: Any
    keyword_plan: Any
    id: Any
    name: Any
    language_constants: Any
    keyword_plan_network: Any
    cpc_bid_micros: Any
    geo_targets: Any

class KeywordPlanGeoTarget(proto.Message):
    geo_target_constant: Any
