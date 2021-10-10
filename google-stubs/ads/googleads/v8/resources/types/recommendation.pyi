from typing import Any

import proto

from google.ads.googleads.v8.common.types import (
    criteria as criteria,
    extensions as extensions,
)
from google.ads.googleads.v8.enums.types import (
    keyword_match_type as keyword_match_type,
    recommendation_type as recommendation_type,
    target_cpa_opt_in_recommendation_goal as target_cpa_opt_in_recommendation_goal,
)

__protobuf__: Any

class Recommendation(proto.Message):
    class RecommendationImpact(proto.Message):
        base_metrics: Any
        potential_metrics: Any
    class RecommendationMetrics(proto.Message):
        impressions: Any
        clicks: Any
        cost_micros: Any
        conversions: Any
        video_views: Any
    class CampaignBudgetRecommendation(proto.Message):
        class CampaignBudgetRecommendationOption(proto.Message):
            budget_amount_micros: Any
            impact: Any
        current_budget_amount_micros: Any
        recommended_budget_amount_micros: Any
        budget_options: Any
    class KeywordRecommendation(proto.Message):
        keyword: Any
        recommended_cpc_bid_micros: Any
    class MaximizeConversionsOptInRecommendation(proto.Message):
        recommended_budget_amount_micros: Any
    class CalloutExtensionRecommendation(proto.Message):
        recommended_extensions: Any
    class TextAdRecommendation(proto.Message):
        ad: Any
        creation_date: Any
        auto_apply_date: Any
    class MoveUnusedBudgetRecommendation(proto.Message):
        excess_campaign_budget: Any
        budget_recommendation: Any
    class TargetCpaOptInRecommendation(proto.Message):
        class TargetCpaOptInRecommendationOption(proto.Message):
            goal: Any
            target_cpa_micros: Any
            required_campaign_budget_amount_micros: Any
            impact: Any
        options: Any
        recommended_target_cpa_micros: Any
    class KeywordMatchTypeRecommendation(proto.Message):
        keyword: Any
        recommended_match_type: Any
    class EnhancedCpcOptInRecommendation(proto.Message): ...
    class SearchPartnersOptInRecommendation(proto.Message): ...
    class CallExtensionRecommendation(proto.Message):
        recommended_extensions: Any
    class TargetRoasOptInRecommendation(proto.Message):
        recommended_target_roas: Any
        required_campaign_budget_amount_micros: Any
    class ResponsiveSearchAdRecommendation(proto.Message):
        ad: Any
    class MaximizeClicksOptInRecommendation(proto.Message):
        recommended_budget_amount_micros: Any
    class OptimizeAdRotationRecommendation(proto.Message): ...
    class SitelinkExtensionRecommendation(proto.Message):
        recommended_extensions: Any
    resource_name: Any
    type_: Any
    impact: Any
    campaign_budget: Any
    campaign: Any
    ad_group: Any
    dismissed: Any
    campaign_budget_recommendation: Any
    forecasting_campaign_budget_recommendation: Any
    keyword_recommendation: Any
    text_ad_recommendation: Any
    target_cpa_opt_in_recommendation: Any
    maximize_conversions_opt_in_recommendation: Any
    enhanced_cpc_opt_in_recommendation: Any
    search_partners_opt_in_recommendation: Any
    maximize_clicks_opt_in_recommendation: Any
    optimize_ad_rotation_recommendation: Any
    callout_extension_recommendation: Any
    sitelink_extension_recommendation: Any
    call_extension_recommendation: Any
    keyword_match_type_recommendation: Any
    move_unused_budget_recommendation: Any
    target_roas_opt_in_recommendation: Any
    responsive_search_ad_recommendation: Any
    marginal_roi_campaign_budget_recommendation: Any
