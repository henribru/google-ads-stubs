import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v10.common.types import extensions as extensions
from google.ads.googleads.v10.enums.types import (
    keyword_match_type as keyword_match_type,
)

__protobuf__: Incomplete

class ApplyRecommendationRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete

class ApplyRecommendationOperation(proto.Message):
    class CampaignBudgetParameters(proto.Message):
        new_budget_amount_micros: Incomplete

    class TextAdParameters(proto.Message):
        ad: Incomplete

    class KeywordParameters(proto.Message):
        ad_group: Incomplete
        match_type: Incomplete
        cpc_bid_micros: Incomplete

    class TargetCpaOptInParameters(proto.Message):
        target_cpa_micros: Incomplete
        new_campaign_budget_amount_micros: Incomplete

    class TargetRoasOptInParameters(proto.Message):
        target_roas: Incomplete
        new_campaign_budget_amount_micros: Incomplete

    class CalloutExtensionParameters(proto.Message):
        callout_extensions: Incomplete

    class CallExtensionParameters(proto.Message):
        call_extensions: Incomplete

    class SitelinkExtensionParameters(proto.Message):
        sitelink_extensions: Incomplete

    class MoveUnusedBudgetParameters(proto.Message):
        budget_micros_to_move: Incomplete

    class ResponsiveSearchAdAssetParameters(proto.Message):
        updated_ad: Incomplete

    class ResponsiveSearchAdParameters(proto.Message):
        ad: Incomplete

    class UseBroadMatchKeywordParameters(proto.Message):
        new_budget_amount_micros: Incomplete
    resource_name: Incomplete
    campaign_budget: Incomplete
    text_ad: Incomplete
    keyword: Incomplete
    target_cpa_opt_in: Incomplete
    target_roas_opt_in: Incomplete
    callout_extension: Incomplete
    call_extension: Incomplete
    sitelink_extension: Incomplete
    move_unused_budget: Incomplete
    responsive_search_ad: Incomplete
    use_broad_match_keyword: Incomplete
    responsive_search_ad_asset: Incomplete

class ApplyRecommendationResponse(proto.Message):
    results: Incomplete
    partial_failure_error: Incomplete

class ApplyRecommendationResult(proto.Message):
    resource_name: Incomplete

class DismissRecommendationRequest(proto.Message):
    class DismissRecommendationOperation(proto.Message):
        resource_name: Incomplete
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete

class DismissRecommendationResponse(proto.Message):
    class DismissRecommendationResult(proto.Message):
        resource_name: Incomplete
    results: Incomplete
    partial_failure_error: Incomplete
