from typing import Any

import proto

from google.ads.googleads.v10.common.types.criteria import KeywordInfo
from google.ads.googleads.v10.common.types.extensions import (
    CallFeedItem,
    CalloutFeedItem,
    SitelinkFeedItem,
)
from google.ads.googleads.v10.enums.types.keyword_match_type import KeywordMatchTypeEnum
from google.ads.googleads.v10.enums.types.recommendation_type import (
    RecommendationTypeEnum,
)
from google.ads.googleads.v10.enums.types.target_cpa_opt_in_recommendation_goal import (
    TargetCpaOptInRecommendationGoalEnum,
)
from google.ads.googleads.v10.resources.types.ad import Ad

class Recommendation(proto.Message):
    class CallExtensionRecommendation(proto.Message):
        recommended_extensions: list[CallFeedItem]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            recommended_extensions: list[CallFeedItem] = ...,
        ) -> None: ...

    class CalloutExtensionRecommendation(proto.Message):
        recommended_extensions: list[CalloutFeedItem]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            recommended_extensions: list[CalloutFeedItem] = ...,
        ) -> None: ...

    class CampaignBudgetRecommendation(proto.Message):
        class CampaignBudgetRecommendationOption(proto.Message):
            budget_amount_micros: int
            impact: Recommendation.RecommendationImpact
            def __init__(
                self,
                mapping: Any | None = ...,
                *,
                ignore_unknown_fields: bool = ...,
                budget_amount_micros: int = ...,
                impact: Recommendation.RecommendationImpact = ...,
            ) -> None: ...
        current_budget_amount_micros: int
        recommended_budget_amount_micros: int
        budget_options: list[
            Recommendation.CampaignBudgetRecommendation.CampaignBudgetRecommendationOption
        ]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            current_budget_amount_micros: int = ...,
            recommended_budget_amount_micros: int = ...,
            budget_options: list[
                Recommendation.CampaignBudgetRecommendation.CampaignBudgetRecommendationOption
            ] = ...,
        ) -> None: ...

    class EnhancedCpcOptInRecommendation(proto.Message):
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
        ) -> None: ...
        ...

    class KeywordMatchTypeRecommendation(proto.Message):
        keyword: KeywordInfo
        recommended_match_type: KeywordMatchTypeEnum.KeywordMatchType
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            keyword: KeywordInfo = ...,
            recommended_match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
        ) -> None: ...

    class KeywordRecommendation(proto.Message):
        keyword: KeywordInfo
        recommended_cpc_bid_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            keyword: KeywordInfo = ...,
            recommended_cpc_bid_micros: int = ...,
        ) -> None: ...

    class MaximizeClicksOptInRecommendation(proto.Message):
        recommended_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            recommended_budget_amount_micros: int = ...,
        ) -> None: ...

    class MaximizeConversionsOptInRecommendation(proto.Message):
        recommended_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            recommended_budget_amount_micros: int = ...,
        ) -> None: ...

    class MoveUnusedBudgetRecommendation(proto.Message):
        excess_campaign_budget: str
        budget_recommendation: Recommendation.CampaignBudgetRecommendation
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            excess_campaign_budget: str = ...,
            budget_recommendation: Recommendation.CampaignBudgetRecommendation = ...,
        ) -> None: ...

    class OptimizeAdRotationRecommendation(proto.Message):
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
        ) -> None: ...
        ...

    class RecommendationImpact(proto.Message):
        base_metrics: Recommendation.RecommendationMetrics
        potential_metrics: Recommendation.RecommendationMetrics
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            base_metrics: Recommendation.RecommendationMetrics = ...,
            potential_metrics: Recommendation.RecommendationMetrics = ...,
        ) -> None: ...

    class RecommendationMetrics(proto.Message):
        impressions: float
        clicks: float
        cost_micros: int
        conversions: float
        video_views: float
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            impressions: float = ...,
            clicks: float = ...,
            cost_micros: int = ...,
            conversions: float = ...,
            video_views: float = ...,
        ) -> None: ...

    class ResponsiveSearchAdAssetRecommendation(proto.Message):
        current_ad: Ad
        recommended_assets: Ad
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            current_ad: Ad = ...,
            recommended_assets: Ad = ...,
        ) -> None: ...

    class ResponsiveSearchAdRecommendation(proto.Message):
        ad: Ad
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            ad: Ad = ...,
        ) -> None: ...

    class SearchPartnersOptInRecommendation(proto.Message):
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
        ) -> None: ...
        ...

    class SitelinkExtensionRecommendation(proto.Message):
        recommended_extensions: list[SitelinkFeedItem]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            recommended_extensions: list[SitelinkFeedItem] = ...,
        ) -> None: ...

    class TargetCpaOptInRecommendation(proto.Message):
        class TargetCpaOptInRecommendationOption(proto.Message):
            goal: TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal
            target_cpa_micros: int
            required_campaign_budget_amount_micros: int
            impact: Recommendation.RecommendationImpact
            def __init__(
                self,
                mapping: Any | None = ...,
                *,
                ignore_unknown_fields: bool = ...,
                goal: TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal = ...,
                target_cpa_micros: int = ...,
                required_campaign_budget_amount_micros: int = ...,
                impact: Recommendation.RecommendationImpact = ...,
            ) -> None: ...
        options: list[
            Recommendation.TargetCpaOptInRecommendation.TargetCpaOptInRecommendationOption
        ]
        recommended_target_cpa_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            options: list[
                Recommendation.TargetCpaOptInRecommendation.TargetCpaOptInRecommendationOption
            ] = ...,
            recommended_target_cpa_micros: int = ...,
        ) -> None: ...

    class TargetRoasOptInRecommendation(proto.Message):
        recommended_target_roas: float
        required_campaign_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            recommended_target_roas: float = ...,
            required_campaign_budget_amount_micros: int = ...,
        ) -> None: ...

    class TextAdRecommendation(proto.Message):
        ad: Ad
        creation_date: str
        auto_apply_date: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            ad: Ad = ...,
            creation_date: str = ...,
            auto_apply_date: str = ...,
        ) -> None: ...

    class UseBroadMatchKeywordRecommendation(proto.Message):
        keyword: list[KeywordInfo]
        suggested_keywords_count: int
        campaign_keywords_count: int
        campaign_uses_shared_budget: bool
        required_campaign_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            keyword: list[KeywordInfo] = ...,
            suggested_keywords_count: int = ...,
            campaign_keywords_count: int = ...,
            campaign_uses_shared_budget: bool = ...,
            required_campaign_budget_amount_micros: int = ...,
        ) -> None: ...
    resource_name: str
    type_: RecommendationTypeEnum.RecommendationType
    impact: Recommendation.RecommendationImpact
    campaign_budget: str
    campaign: str
    ad_group: str
    dismissed: bool
    campaign_budget_recommendation: Recommendation.CampaignBudgetRecommendation
    forecasting_campaign_budget_recommendation: Recommendation.CampaignBudgetRecommendation
    keyword_recommendation: Recommendation.KeywordRecommendation
    text_ad_recommendation: Recommendation.TextAdRecommendation
    target_cpa_opt_in_recommendation: Recommendation.TargetCpaOptInRecommendation
    maximize_conversions_opt_in_recommendation: Recommendation.MaximizeConversionsOptInRecommendation
    enhanced_cpc_opt_in_recommendation: Recommendation.EnhancedCpcOptInRecommendation
    search_partners_opt_in_recommendation: Recommendation.SearchPartnersOptInRecommendation
    maximize_clicks_opt_in_recommendation: Recommendation.MaximizeClicksOptInRecommendation
    optimize_ad_rotation_recommendation: Recommendation.OptimizeAdRotationRecommendation
    callout_extension_recommendation: Recommendation.CalloutExtensionRecommendation
    sitelink_extension_recommendation: Recommendation.SitelinkExtensionRecommendation
    call_extension_recommendation: Recommendation.CallExtensionRecommendation
    keyword_match_type_recommendation: Recommendation.KeywordMatchTypeRecommendation
    move_unused_budget_recommendation: Recommendation.MoveUnusedBudgetRecommendation
    target_roas_opt_in_recommendation: Recommendation.TargetRoasOptInRecommendation
    responsive_search_ad_recommendation: Recommendation.ResponsiveSearchAdRecommendation
    marginal_roi_campaign_budget_recommendation: Recommendation.CampaignBudgetRecommendation
    use_broad_match_keyword_recommendation: Recommendation.UseBroadMatchKeywordRecommendation
    responsive_search_ad_asset_recommendation: Recommendation.ResponsiveSearchAdAssetRecommendation
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        type_: RecommendationTypeEnum.RecommendationType = ...,
        impact: Recommendation.RecommendationImpact = ...,
        campaign_budget: str = ...,
        campaign: str = ...,
        ad_group: str = ...,
        dismissed: bool = ...,
        campaign_budget_recommendation: Recommendation.CampaignBudgetRecommendation = ...,
        forecasting_campaign_budget_recommendation: Recommendation.CampaignBudgetRecommendation = ...,
        keyword_recommendation: Recommendation.KeywordRecommendation = ...,
        text_ad_recommendation: Recommendation.TextAdRecommendation = ...,
        target_cpa_opt_in_recommendation: Recommendation.TargetCpaOptInRecommendation = ...,
        maximize_conversions_opt_in_recommendation: Recommendation.MaximizeConversionsOptInRecommendation = ...,
        enhanced_cpc_opt_in_recommendation: Recommendation.EnhancedCpcOptInRecommendation = ...,
        search_partners_opt_in_recommendation: Recommendation.SearchPartnersOptInRecommendation = ...,
        maximize_clicks_opt_in_recommendation: Recommendation.MaximizeClicksOptInRecommendation = ...,
        optimize_ad_rotation_recommendation: Recommendation.OptimizeAdRotationRecommendation = ...,
        callout_extension_recommendation: Recommendation.CalloutExtensionRecommendation = ...,
        sitelink_extension_recommendation: Recommendation.SitelinkExtensionRecommendation = ...,
        call_extension_recommendation: Recommendation.CallExtensionRecommendation = ...,
        keyword_match_type_recommendation: Recommendation.KeywordMatchTypeRecommendation = ...,
        move_unused_budget_recommendation: Recommendation.MoveUnusedBudgetRecommendation = ...,
        target_roas_opt_in_recommendation: Recommendation.TargetRoasOptInRecommendation = ...,
        responsive_search_ad_recommendation: Recommendation.ResponsiveSearchAdRecommendation = ...,
        marginal_roi_campaign_budget_recommendation: Recommendation.CampaignBudgetRecommendation = ...,
        use_broad_match_keyword_recommendation: Recommendation.UseBroadMatchKeywordRecommendation = ...,
        responsive_search_ad_asset_recommendation: Recommendation.ResponsiveSearchAdAssetRecommendation = ...,
    ) -> None: ...
