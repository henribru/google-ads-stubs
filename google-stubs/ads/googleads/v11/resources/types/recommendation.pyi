import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import (
    criteria as criteria,
    extensions as extensions,
)
from google.ads.googleads.v11.enums.types import (
    keyword_match_type as keyword_match_type,
    recommendation_type as recommendation_type,
    target_cpa_opt_in_recommendation_goal as target_cpa_opt_in_recommendation_goal,
)

__protobuf__: Incomplete

class Recommendation(proto.Message):
    class RecommendationImpact(proto.Message):
        base_metrics: Incomplete
        potential_metrics: Incomplete

    class RecommendationMetrics(proto.Message):
        impressions: Incomplete
        clicks: Incomplete
        cost_micros: Incomplete
        conversions: Incomplete
        video_views: Incomplete

    class CampaignBudgetRecommendation(proto.Message):
        class CampaignBudgetRecommendationOption(proto.Message):
            budget_amount_micros: Incomplete
            impact: Incomplete
        current_budget_amount_micros: Incomplete
        recommended_budget_amount_micros: Incomplete
        budget_options: Incomplete

    class KeywordRecommendation(proto.Message):
        keyword: Incomplete
        recommended_cpc_bid_micros: Incomplete

    class TextAdRecommendation(proto.Message):
        ad: Incomplete
        creation_date: Incomplete
        auto_apply_date: Incomplete

    class TargetCpaOptInRecommendation(proto.Message):
        class TargetCpaOptInRecommendationOption(proto.Message):
            goal: Incomplete
            target_cpa_micros: Incomplete
            required_campaign_budget_amount_micros: Incomplete
            impact: Incomplete
        options: Incomplete
        recommended_target_cpa_micros: Incomplete

    class MaximizeConversionsOptInRecommendation(proto.Message):
        recommended_budget_amount_micros: Incomplete

    class EnhancedCpcOptInRecommendation(proto.Message): ...
    class SearchPartnersOptInRecommendation(proto.Message): ...

    class MaximizeClicksOptInRecommendation(proto.Message):
        recommended_budget_amount_micros: Incomplete

    class OptimizeAdRotationRecommendation(proto.Message): ...

    class CalloutExtensionRecommendation(proto.Message):
        recommended_extensions: Incomplete

    class SitelinkExtensionRecommendation(proto.Message):
        recommended_extensions: Incomplete

    class CallExtensionRecommendation(proto.Message):
        recommended_extensions: Incomplete

    class KeywordMatchTypeRecommendation(proto.Message):
        keyword: Incomplete
        recommended_match_type: Incomplete

    class MoveUnusedBudgetRecommendation(proto.Message):
        excess_campaign_budget: Incomplete
        budget_recommendation: Incomplete

    class TargetRoasOptInRecommendation(proto.Message):
        recommended_target_roas: Incomplete
        required_campaign_budget_amount_micros: Incomplete

    class ResponsiveSearchAdAssetRecommendation(proto.Message):
        current_ad: Incomplete
        recommended_assets: Incomplete

    class ResponsiveSearchAdImproveAdStrengthRecommendation(proto.Message):
        current_ad: Incomplete
        recommended_ad: Incomplete

    class ResponsiveSearchAdRecommendation(proto.Message):
        ad: Incomplete

    class UseBroadMatchKeywordRecommendation(proto.Message):
        keyword: Incomplete
        suggested_keywords_count: Incomplete
        campaign_keywords_count: Incomplete
        campaign_uses_shared_budget: Incomplete
        required_campaign_budget_amount_micros: Incomplete

    class UpgradeSmartShoppingCampaignToPerformanceMaxRecommendation(proto.Message):
        merchant_id: Incomplete
        sales_country_code: Incomplete

    class DisplayExpansionOptInRecommendation(proto.Message): ...
    class UpgradeLocalCampaignToPerformanceMaxRecommendation(proto.Message): ...
    resource_name: Incomplete
    type_: Incomplete
    impact: Incomplete
    campaign_budget: Incomplete
    campaign: Incomplete
    ad_group: Incomplete
    dismissed: Incomplete
    campaign_budget_recommendation: Incomplete
    forecasting_campaign_budget_recommendation: Incomplete
    keyword_recommendation: Incomplete
    text_ad_recommendation: Incomplete
    target_cpa_opt_in_recommendation: Incomplete
    maximize_conversions_opt_in_recommendation: Incomplete
    enhanced_cpc_opt_in_recommendation: Incomplete
    search_partners_opt_in_recommendation: Incomplete
    maximize_clicks_opt_in_recommendation: Incomplete
    optimize_ad_rotation_recommendation: Incomplete
    callout_extension_recommendation: Incomplete
    sitelink_extension_recommendation: Incomplete
    call_extension_recommendation: Incomplete
    keyword_match_type_recommendation: Incomplete
    move_unused_budget_recommendation: Incomplete
    target_roas_opt_in_recommendation: Incomplete
    responsive_search_ad_recommendation: Incomplete
    marginal_roi_campaign_budget_recommendation: Incomplete
    use_broad_match_keyword_recommendation: Incomplete
    responsive_search_ad_asset_recommendation: Incomplete
    upgrade_smart_shopping_campaign_to_performance_max_recommendation: Incomplete
    responsive_search_ad_improve_ad_strength_recommendation: Incomplete
    display_expansion_opt_in_recommendation: Incomplete
    upgrade_local_campaign_to_performance_max_recommendation: Incomplete
