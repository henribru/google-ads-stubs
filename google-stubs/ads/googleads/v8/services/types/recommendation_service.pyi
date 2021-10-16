from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v8.common.types import extensions as extensions
from google.ads.googleads.v8.enums.types import keyword_match_type as keyword_match_type

__protobuf__: Any

class GetRecommendationRequest(proto.Message):
    resource_name: Any

class ApplyRecommendationRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any

class ApplyRecommendationOperation(proto.Message):
    class CampaignBudgetParameters(proto.Message):
        new_budget_amount_micros: Any
    class TextAdParameters(proto.Message):
        ad: Any
    class KeywordParameters(proto.Message):
        ad_group: Any
        match_type: Any
        cpc_bid_micros: Any
    class TargetCpaOptInParameters(proto.Message):
        target_cpa_micros: Any
        new_campaign_budget_amount_micros: Any
    class TargetRoasOptInParameters(proto.Message):
        target_roas: Any
        new_campaign_budget_amount_micros: Any
    class CalloutExtensionParameters(proto.Message):
        callout_extensions: Any
    class CallExtensionParameters(proto.Message):
        call_extensions: Any
    class SitelinkExtensionParameters(proto.Message):
        sitelink_extensions: Any
    class MoveUnusedBudgetParameters(proto.Message):
        budget_micros_to_move: Any
    class ResponsiveSearchAdParameters(proto.Message):
        ad: Any
    resource_name: Any
    campaign_budget: Any
    text_ad: Any
    keyword: Any
    target_cpa_opt_in: Any
    target_roas_opt_in: Any
    callout_extension: Any
    call_extension: Any
    sitelink_extension: Any
    move_unused_budget: Any
    responsive_search_ad: Any

class ApplyRecommendationResponse(proto.Message):
    results: Any
    partial_failure_error: Any

class ApplyRecommendationResult(proto.Message):
    resource_name: Any

class DismissRecommendationRequest(proto.Message):
    class DismissRecommendationOperation(proto.Message):
        resource_name: Any
    customer_id: Any
    operations: Any
    partial_failure: Any

class DismissRecommendationResponse(proto.Message):
    class DismissRecommendationResult(proto.Message):
        resource_name: Any
    results: Any
    partial_failure_error: Any
