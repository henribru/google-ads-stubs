from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.criteria import KeywordInfo
from google.ads.googleads.v14.enums.types.app_bidding_goal import AppBiddingGoalEnum
from google.ads.googleads.v14.enums.types.keyword_match_type import KeywordMatchTypeEnum
from google.ads.googleads.v14.enums.types.recommendation_type import (
    RecommendationTypeEnum,
)
from google.ads.googleads.v14.enums.types.shopping_add_products_to_campaign_recommendation_enum import (
    ShoppingAddProductsToCampaignRecommendationEnum,
)
from google.ads.googleads.v14.enums.types.target_cpa_opt_in_recommendation_goal import (
    TargetCpaOptInRecommendationGoalEnum,
)
from google.ads.googleads.v14.resources.types.ad import Ad
from google.ads.googleads.v14.resources.types.asset import Asset

_M = TypeVar("_M")

class Recommendation(proto.Message):
    class CallAssetRecommendation(proto.Message):
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: NoReturn
        ) -> bool: ...

    class CalloutAssetRecommendation(proto.Message):
        recommended_campaign_callout_assets: MutableSequence[Asset]
        recommended_customer_callout_assets: MutableSequence[Asset]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            recommended_campaign_callout_assets: MutableSequence[Asset] = ...,
            recommended_customer_callout_assets: MutableSequence[Asset] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "recommended_campaign_callout_assets",
                "recommended_customer_callout_assets",
            ],
        ) -> bool: ...

    class CampaignBudget(proto.Message):
        current_amount_micros: int
        recommended_new_amount_micros: int
        new_start_date: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            current_amount_micros: int = ...,
            recommended_new_amount_micros: int = ...,
            new_start_date: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "current_amount_micros",
                "recommended_new_amount_micros",
                "new_start_date",
            ],
        ) -> bool: ...

    class CampaignBudgetRecommendation(proto.Message):
        class CampaignBudgetRecommendationOption(proto.Message):
            budget_amount_micros: int
            impact: Recommendation.RecommendationImpact
            def __init__(
                self: _M,
                mapping: _M | Mapping | google.protobuf.message.Message | None = None,
                *,
                ignore_unknown_fields: bool = False,
                budget_amount_micros: int = ...,
                impact: Recommendation.RecommendationImpact = ...,
            ) -> None: ...
            def __contains__(  # type: ignore[override]
                self, key: Literal["budget_amount_micros", "impact"]
            ) -> bool: ...

        current_budget_amount_micros: int
        recommended_budget_amount_micros: int
        budget_options: MutableSequence[
            Recommendation.CampaignBudgetRecommendation.CampaignBudgetRecommendationOption
        ]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            current_budget_amount_micros: int = ...,
            recommended_budget_amount_micros: int = ...,
            budget_options: MutableSequence[
                Recommendation.CampaignBudgetRecommendation.CampaignBudgetRecommendationOption
            ] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "current_budget_amount_micros",
                "recommended_budget_amount_micros",
                "budget_options",
            ],
        ) -> bool: ...

    class DisplayExpansionOptInRecommendation(proto.Message):
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: NoReturn
        ) -> bool: ...

    class DynamicImageExtensionOptInRecommendation(proto.Message):
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: NoReturn
        ) -> bool: ...

    class EnhancedCpcOptInRecommendation(proto.Message):
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: NoReturn
        ) -> bool: ...

    class ForecastingSetTargetRoasRecommendation(proto.Message):
        recommended_target_roas: float
        campaign_budget: Recommendation.CampaignBudget
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            recommended_target_roas: float = ...,
            campaign_budget: Recommendation.CampaignBudget = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["recommended_target_roas", "campaign_budget"]
        ) -> bool: ...

    class ImprovePerformanceMaxAdStrengthRecommendation(proto.Message):
        asset_group: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            asset_group: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["asset_group"]
        ) -> bool: ...

    class KeywordMatchTypeRecommendation(proto.Message):
        keyword: KeywordInfo
        recommended_match_type: KeywordMatchTypeEnum.KeywordMatchType
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            keyword: KeywordInfo = ...,
            recommended_match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["keyword", "recommended_match_type"]
        ) -> bool: ...

    class KeywordRecommendation(proto.Message):
        class SearchTerm(proto.Message):
            text: str
            estimated_weekly_search_count: int
            def __init__(
                self: _M,
                mapping: _M | Mapping | google.protobuf.message.Message | None = None,
                *,
                ignore_unknown_fields: bool = False,
                text: str = ...,
                estimated_weekly_search_count: int = ...,
            ) -> None: ...
            def __contains__(  # type: ignore[override]
                self, key: Literal["text", "estimated_weekly_search_count"]
            ) -> bool: ...

        keyword: KeywordInfo
        search_terms: MutableSequence[Recommendation.KeywordRecommendation.SearchTerm]
        recommended_cpc_bid_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            keyword: KeywordInfo = ...,
            search_terms: MutableSequence[
                Recommendation.KeywordRecommendation.SearchTerm
            ] = ...,
            recommended_cpc_bid_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["keyword", "search_terms", "recommended_cpc_bid_micros"]
        ) -> bool: ...

    class LowerTargetRoasRecommendation(proto.Message):
        target_adjustment: Recommendation.TargetAdjustmentInfo
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_adjustment: Recommendation.TargetAdjustmentInfo = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["target_adjustment"]
        ) -> bool: ...

    class MaximizeClicksOptInRecommendation(proto.Message):
        recommended_budget_amount_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            recommended_budget_amount_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["recommended_budget_amount_micros"]
        ) -> bool: ...

    class MaximizeConversionsOptInRecommendation(proto.Message):
        recommended_budget_amount_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            recommended_budget_amount_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["recommended_budget_amount_micros"]
        ) -> bool: ...

    class MerchantInfo(proto.Message):
        id: int
        name: str
        multi_client: bool
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            id: int = ...,
            name: str = ...,
            multi_client: bool = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["id", "name", "multi_client"]
        ) -> bool: ...

    class MigrateDynamicSearchAdsCampaignToPerformanceMaxRecommendation(proto.Message):
        apply_link: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            apply_link: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["apply_link"]
        ) -> bool: ...

    class MoveUnusedBudgetRecommendation(proto.Message):
        excess_campaign_budget: str
        budget_recommendation: Recommendation.CampaignBudgetRecommendation
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            excess_campaign_budget: str = ...,
            budget_recommendation: Recommendation.CampaignBudgetRecommendation = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["excess_campaign_budget", "budget_recommendation"]
        ) -> bool: ...

    class OptimizeAdRotationRecommendation(proto.Message):
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: NoReturn
        ) -> bool: ...

    class PerformanceMaxOptInRecommendation(proto.Message):
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: NoReturn
        ) -> bool: ...

    class RaiseTargetCpaBidTooLowRecommendation(proto.Message):
        recommended_target_multiplier: float
        average_target_cpa_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            recommended_target_multiplier: float = ...,
            average_target_cpa_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal["recommended_target_multiplier", "average_target_cpa_micros"],
        ) -> bool: ...

    class RaiseTargetCpaRecommendation(proto.Message):
        target_adjustment: Recommendation.TargetAdjustmentInfo
        app_bidding_goal: AppBiddingGoalEnum.AppBiddingGoal
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_adjustment: Recommendation.TargetAdjustmentInfo = ...,
            app_bidding_goal: AppBiddingGoalEnum.AppBiddingGoal = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["target_adjustment", "app_bidding_goal"]
        ) -> bool: ...

    class RecommendationImpact(proto.Message):
        base_metrics: Recommendation.RecommendationMetrics
        potential_metrics: Recommendation.RecommendationMetrics
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            base_metrics: Recommendation.RecommendationMetrics = ...,
            potential_metrics: Recommendation.RecommendationMetrics = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["base_metrics", "potential_metrics"]
        ) -> bool: ...

    class RecommendationMetrics(proto.Message):
        impressions: float
        clicks: float
        cost_micros: int
        conversions: float
        video_views: float
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            impressions: float = ...,
            clicks: float = ...,
            cost_micros: int = ...,
            conversions: float = ...,
            video_views: float = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "impressions", "clicks", "cost_micros", "conversions", "video_views"
            ],
        ) -> bool: ...

    class ResponsiveSearchAdAssetRecommendation(proto.Message):
        current_ad: Ad
        recommended_assets: Ad
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            current_ad: Ad = ...,
            recommended_assets: Ad = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["current_ad", "recommended_assets"]
        ) -> bool: ...

    class ResponsiveSearchAdImproveAdStrengthRecommendation(proto.Message):
        current_ad: Ad
        recommended_ad: Ad
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            current_ad: Ad = ...,
            recommended_ad: Ad = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["current_ad", "recommended_ad"]
        ) -> bool: ...

    class ResponsiveSearchAdRecommendation(proto.Message):
        ad: Ad
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            ad: Ad = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["ad"]
        ) -> bool: ...

    class SearchPartnersOptInRecommendation(proto.Message):
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: NoReturn
        ) -> bool: ...

    class ShoppingAddProductsToCampaignRecommendation(proto.Message):
        merchant: Recommendation.MerchantInfo
        feed_label: str
        reason: ShoppingAddProductsToCampaignRecommendationEnum.Reason
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            merchant: Recommendation.MerchantInfo = ...,
            feed_label: str = ...,
            reason: ShoppingAddProductsToCampaignRecommendationEnum.Reason = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["merchant", "feed_label", "reason"]
        ) -> bool: ...

    class ShoppingFixDisapprovedProductsRecommendation(proto.Message):
        merchant: Recommendation.MerchantInfo
        feed_label: str
        products_count: int
        disapproved_products_count: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            merchant: Recommendation.MerchantInfo = ...,
            feed_label: str = ...,
            products_count: int = ...,
            disapproved_products_count: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "merchant", "feed_label", "products_count", "disapproved_products_count"
            ],
        ) -> bool: ...

    class ShoppingMerchantCenterAccountSuspensionRecommendation(proto.Message):
        merchant: Recommendation.MerchantInfo
        feed_label: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            merchant: Recommendation.MerchantInfo = ...,
            feed_label: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["merchant", "feed_label"]
        ) -> bool: ...

    class ShoppingMigrateRegularShoppingCampaignOffersToPerformanceMaxRecommendation(
        proto.Message
    ):
        merchant: Recommendation.MerchantInfo
        feed_label: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            merchant: Recommendation.MerchantInfo = ...,
            feed_label: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["merchant", "feed_label"]
        ) -> bool: ...

    class ShoppingOfferAttributeRecommendation(proto.Message):
        merchant: Recommendation.MerchantInfo
        feed_label: str
        offers_count: int
        demoted_offers_count: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            merchant: Recommendation.MerchantInfo = ...,
            feed_label: str = ...,
            offers_count: int = ...,
            demoted_offers_count: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "merchant", "feed_label", "offers_count", "demoted_offers_count"
            ],
        ) -> bool: ...

    class ShoppingTargetAllOffersRecommendation(proto.Message):
        merchant: Recommendation.MerchantInfo
        untargeted_offers_count: int
        feed_label: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            merchant: Recommendation.MerchantInfo = ...,
            untargeted_offers_count: int = ...,
            feed_label: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["merchant", "untargeted_offers_count", "feed_label"]
        ) -> bool: ...

    class SitelinkAssetRecommendation(proto.Message):
        recommended_campaign_sitelink_assets: MutableSequence[Asset]
        recommended_customer_sitelink_assets: MutableSequence[Asset]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            recommended_campaign_sitelink_assets: MutableSequence[Asset] = ...,
            recommended_customer_sitelink_assets: MutableSequence[Asset] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "recommended_campaign_sitelink_assets",
                "recommended_customer_sitelink_assets",
            ],
        ) -> bool: ...

    class TargetAdjustmentInfo(proto.Message):
        shared_set: str
        recommended_target_multiplier: float
        current_average_target_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            shared_set: str = ...,
            recommended_target_multiplier: float = ...,
            current_average_target_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "shared_set",
                "recommended_target_multiplier",
                "current_average_target_micros",
            ],
        ) -> bool: ...

    class TargetCpaOptInRecommendation(proto.Message):
        class TargetCpaOptInRecommendationOption(proto.Message):
            goal: TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal
            target_cpa_micros: int
            required_campaign_budget_amount_micros: int
            impact: Recommendation.RecommendationImpact
            def __init__(
                self: _M,
                mapping: _M | Mapping | google.protobuf.message.Message | None = None,
                *,
                ignore_unknown_fields: bool = False,
                goal: TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal = ...,
                target_cpa_micros: int = ...,
                required_campaign_budget_amount_micros: int = ...,
                impact: Recommendation.RecommendationImpact = ...,
            ) -> None: ...
            def __contains__(  # type: ignore[override]
                self,
                key: Literal[
                    "goal",
                    "target_cpa_micros",
                    "required_campaign_budget_amount_micros",
                    "impact",
                ],
            ) -> bool: ...

        options: MutableSequence[
            Recommendation.TargetCpaOptInRecommendation.TargetCpaOptInRecommendationOption
        ]
        recommended_target_cpa_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            options: MutableSequence[
                Recommendation.TargetCpaOptInRecommendation.TargetCpaOptInRecommendationOption
            ] = ...,
            recommended_target_cpa_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["options", "recommended_target_cpa_micros"]
        ) -> bool: ...

    class TargetRoasOptInRecommendation(proto.Message):
        recommended_target_roas: float
        required_campaign_budget_amount_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            recommended_target_roas: float = ...,
            required_campaign_budget_amount_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "recommended_target_roas", "required_campaign_budget_amount_micros"
            ],
        ) -> bool: ...

    class TextAdRecommendation(proto.Message):
        ad: Ad
        creation_date: str
        auto_apply_date: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            ad: Ad = ...,
            creation_date: str = ...,
            auto_apply_date: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["ad", "creation_date", "auto_apply_date"]
        ) -> bool: ...

    class UpgradeLocalCampaignToPerformanceMaxRecommendation(proto.Message):
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: NoReturn
        ) -> bool: ...

    class UpgradeSmartShoppingCampaignToPerformanceMaxRecommendation(proto.Message):
        merchant_id: int
        sales_country_code: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            merchant_id: int = ...,
            sales_country_code: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["merchant_id", "sales_country_code"]
        ) -> bool: ...

    class UseBroadMatchKeywordRecommendation(proto.Message):
        keyword: MutableSequence[KeywordInfo]
        suggested_keywords_count: int
        campaign_keywords_count: int
        campaign_uses_shared_budget: bool
        required_campaign_budget_amount_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            keyword: MutableSequence[KeywordInfo] = ...,
            suggested_keywords_count: int = ...,
            campaign_keywords_count: int = ...,
            campaign_uses_shared_budget: bool = ...,
            required_campaign_budget_amount_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "keyword",
                "suggested_keywords_count",
                "campaign_keywords_count",
                "campaign_uses_shared_budget",
                "required_campaign_budget_amount_micros",
            ],
        ) -> bool: ...

    resource_name: str
    type_: RecommendationTypeEnum.RecommendationType
    impact: Recommendation.RecommendationImpact
    campaign_budget: str
    campaign: str
    ad_group: str
    dismissed: bool
    campaigns: MutableSequence[str]
    campaign_budget_recommendation: Recommendation.CampaignBudgetRecommendation
    forecasting_campaign_budget_recommendation: (
        Recommendation.CampaignBudgetRecommendation
    )
    keyword_recommendation: Recommendation.KeywordRecommendation
    text_ad_recommendation: Recommendation.TextAdRecommendation
    target_cpa_opt_in_recommendation: Recommendation.TargetCpaOptInRecommendation
    maximize_conversions_opt_in_recommendation: (
        Recommendation.MaximizeConversionsOptInRecommendation
    )
    enhanced_cpc_opt_in_recommendation: Recommendation.EnhancedCpcOptInRecommendation
    search_partners_opt_in_recommendation: (
        Recommendation.SearchPartnersOptInRecommendation
    )
    maximize_clicks_opt_in_recommendation: (
        Recommendation.MaximizeClicksOptInRecommendation
    )
    optimize_ad_rotation_recommendation: Recommendation.OptimizeAdRotationRecommendation
    keyword_match_type_recommendation: Recommendation.KeywordMatchTypeRecommendation
    move_unused_budget_recommendation: Recommendation.MoveUnusedBudgetRecommendation
    target_roas_opt_in_recommendation: Recommendation.TargetRoasOptInRecommendation
    responsive_search_ad_recommendation: Recommendation.ResponsiveSearchAdRecommendation
    marginal_roi_campaign_budget_recommendation: (
        Recommendation.CampaignBudgetRecommendation
    )
    use_broad_match_keyword_recommendation: (
        Recommendation.UseBroadMatchKeywordRecommendation
    )
    responsive_search_ad_asset_recommendation: (
        Recommendation.ResponsiveSearchAdAssetRecommendation
    )
    upgrade_smart_shopping_campaign_to_performance_max_recommendation: (
        Recommendation.UpgradeSmartShoppingCampaignToPerformanceMaxRecommendation
    )
    responsive_search_ad_improve_ad_strength_recommendation: (
        Recommendation.ResponsiveSearchAdImproveAdStrengthRecommendation
    )
    display_expansion_opt_in_recommendation: (
        Recommendation.DisplayExpansionOptInRecommendation
    )
    upgrade_local_campaign_to_performance_max_recommendation: (
        Recommendation.UpgradeLocalCampaignToPerformanceMaxRecommendation
    )
    raise_target_cpa_bid_too_low_recommendation: (
        Recommendation.RaiseTargetCpaBidTooLowRecommendation
    )
    forecasting_set_target_roas_recommendation: (
        Recommendation.ForecastingSetTargetRoasRecommendation
    )
    callout_asset_recommendation: Recommendation.CalloutAssetRecommendation
    sitelink_asset_recommendation: Recommendation.SitelinkAssetRecommendation
    call_asset_recommendation: Recommendation.CallAssetRecommendation
    shopping_add_age_group_recommendation: (
        Recommendation.ShoppingOfferAttributeRecommendation
    )
    shopping_add_color_recommendation: (
        Recommendation.ShoppingOfferAttributeRecommendation
    )
    shopping_add_gender_recommendation: (
        Recommendation.ShoppingOfferAttributeRecommendation
    )
    shopping_add_gtin_recommendation: (
        Recommendation.ShoppingOfferAttributeRecommendation
    )
    shopping_add_more_identifiers_recommendation: (
        Recommendation.ShoppingOfferAttributeRecommendation
    )
    shopping_add_size_recommendation: (
        Recommendation.ShoppingOfferAttributeRecommendation
    )
    shopping_add_products_to_campaign_recommendation: (
        Recommendation.ShoppingAddProductsToCampaignRecommendation
    )
    shopping_fix_disapproved_products_recommendation: (
        Recommendation.ShoppingFixDisapprovedProductsRecommendation
    )
    shopping_target_all_offers_recommendation: (
        Recommendation.ShoppingTargetAllOffersRecommendation
    )
    shopping_fix_suspended_merchant_center_account_recommendation: (
        Recommendation.ShoppingMerchantCenterAccountSuspensionRecommendation
    )
    shopping_fix_merchant_center_account_suspension_warning_recommendation: (
        Recommendation.ShoppingMerchantCenterAccountSuspensionRecommendation
    )
    shopping_migrate_regular_shopping_campaign_offers_to_performance_max_recommendation: Recommendation.ShoppingMigrateRegularShoppingCampaignOffersToPerformanceMaxRecommendation
    dynamic_image_extension_opt_in_recommendation: (
        Recommendation.DynamicImageExtensionOptInRecommendation
    )
    raise_target_cpa_recommendation: Recommendation.RaiseTargetCpaRecommendation
    lower_target_roas_recommendation: Recommendation.LowerTargetRoasRecommendation
    performance_max_opt_in_recommendation: (
        Recommendation.PerformanceMaxOptInRecommendation
    )
    improve_performance_max_ad_strength_recommendation: (
        Recommendation.ImprovePerformanceMaxAdStrengthRecommendation
    )
    migrate_dynamic_search_ads_campaign_to_performance_max_recommendation: (
        Recommendation.MigrateDynamicSearchAdsCampaignToPerformanceMaxRecommendation
    )
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        type_: RecommendationTypeEnum.RecommendationType = ...,
        impact: Recommendation.RecommendationImpact = ...,
        campaign_budget: str = ...,
        campaign: str = ...,
        ad_group: str = ...,
        dismissed: bool = ...,
        campaigns: MutableSequence[str] = ...,
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
        keyword_match_type_recommendation: Recommendation.KeywordMatchTypeRecommendation = ...,
        move_unused_budget_recommendation: Recommendation.MoveUnusedBudgetRecommendation = ...,
        target_roas_opt_in_recommendation: Recommendation.TargetRoasOptInRecommendation = ...,
        responsive_search_ad_recommendation: Recommendation.ResponsiveSearchAdRecommendation = ...,
        marginal_roi_campaign_budget_recommendation: Recommendation.CampaignBudgetRecommendation = ...,
        use_broad_match_keyword_recommendation: Recommendation.UseBroadMatchKeywordRecommendation = ...,
        responsive_search_ad_asset_recommendation: Recommendation.ResponsiveSearchAdAssetRecommendation = ...,
        upgrade_smart_shopping_campaign_to_performance_max_recommendation: Recommendation.UpgradeSmartShoppingCampaignToPerformanceMaxRecommendation = ...,
        responsive_search_ad_improve_ad_strength_recommendation: Recommendation.ResponsiveSearchAdImproveAdStrengthRecommendation = ...,
        display_expansion_opt_in_recommendation: Recommendation.DisplayExpansionOptInRecommendation = ...,
        upgrade_local_campaign_to_performance_max_recommendation: Recommendation.UpgradeLocalCampaignToPerformanceMaxRecommendation = ...,
        raise_target_cpa_bid_too_low_recommendation: Recommendation.RaiseTargetCpaBidTooLowRecommendation = ...,
        forecasting_set_target_roas_recommendation: Recommendation.ForecastingSetTargetRoasRecommendation = ...,
        callout_asset_recommendation: Recommendation.CalloutAssetRecommendation = ...,
        sitelink_asset_recommendation: Recommendation.SitelinkAssetRecommendation = ...,
        call_asset_recommendation: Recommendation.CallAssetRecommendation = ...,
        shopping_add_age_group_recommendation: Recommendation.ShoppingOfferAttributeRecommendation = ...,
        shopping_add_color_recommendation: Recommendation.ShoppingOfferAttributeRecommendation = ...,
        shopping_add_gender_recommendation: Recommendation.ShoppingOfferAttributeRecommendation = ...,
        shopping_add_gtin_recommendation: Recommendation.ShoppingOfferAttributeRecommendation = ...,
        shopping_add_more_identifiers_recommendation: Recommendation.ShoppingOfferAttributeRecommendation = ...,
        shopping_add_size_recommendation: Recommendation.ShoppingOfferAttributeRecommendation = ...,
        shopping_add_products_to_campaign_recommendation: Recommendation.ShoppingAddProductsToCampaignRecommendation = ...,
        shopping_fix_disapproved_products_recommendation: Recommendation.ShoppingFixDisapprovedProductsRecommendation = ...,
        shopping_target_all_offers_recommendation: Recommendation.ShoppingTargetAllOffersRecommendation = ...,
        shopping_fix_suspended_merchant_center_account_recommendation: Recommendation.ShoppingMerchantCenterAccountSuspensionRecommendation = ...,
        shopping_fix_merchant_center_account_suspension_warning_recommendation: Recommendation.ShoppingMerchantCenterAccountSuspensionRecommendation = ...,
        shopping_migrate_regular_shopping_campaign_offers_to_performance_max_recommendation: Recommendation.ShoppingMigrateRegularShoppingCampaignOffersToPerformanceMaxRecommendation = ...,
        dynamic_image_extension_opt_in_recommendation: Recommendation.DynamicImageExtensionOptInRecommendation = ...,
        raise_target_cpa_recommendation: Recommendation.RaiseTargetCpaRecommendation = ...,
        lower_target_roas_recommendation: Recommendation.LowerTargetRoasRecommendation = ...,
        performance_max_opt_in_recommendation: Recommendation.PerformanceMaxOptInRecommendation = ...,
        improve_performance_max_ad_strength_recommendation: Recommendation.ImprovePerformanceMaxAdStrengthRecommendation = ...,
        migrate_dynamic_search_ads_campaign_to_performance_max_recommendation: Recommendation.MigrateDynamicSearchAdsCampaignToPerformanceMaxRecommendation = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "type_",
            "impact",
            "campaign_budget",
            "campaign",
            "ad_group",
            "dismissed",
            "campaigns",
            "campaign_budget_recommendation",
            "forecasting_campaign_budget_recommendation",
            "keyword_recommendation",
            "text_ad_recommendation",
            "target_cpa_opt_in_recommendation",
            "maximize_conversions_opt_in_recommendation",
            "enhanced_cpc_opt_in_recommendation",
            "search_partners_opt_in_recommendation",
            "maximize_clicks_opt_in_recommendation",
            "optimize_ad_rotation_recommendation",
            "keyword_match_type_recommendation",
            "move_unused_budget_recommendation",
            "target_roas_opt_in_recommendation",
            "responsive_search_ad_recommendation",
            "marginal_roi_campaign_budget_recommendation",
            "use_broad_match_keyword_recommendation",
            "responsive_search_ad_asset_recommendation",
            "upgrade_smart_shopping_campaign_to_performance_max_recommendation",
            "responsive_search_ad_improve_ad_strength_recommendation",
            "display_expansion_opt_in_recommendation",
            "upgrade_local_campaign_to_performance_max_recommendation",
            "raise_target_cpa_bid_too_low_recommendation",
            "forecasting_set_target_roas_recommendation",
            "callout_asset_recommendation",
            "sitelink_asset_recommendation",
            "call_asset_recommendation",
            "shopping_add_age_group_recommendation",
            "shopping_add_color_recommendation",
            "shopping_add_gender_recommendation",
            "shopping_add_gtin_recommendation",
            "shopping_add_more_identifiers_recommendation",
            "shopping_add_size_recommendation",
            "shopping_add_products_to_campaign_recommendation",
            "shopping_fix_disapproved_products_recommendation",
            "shopping_target_all_offers_recommendation",
            "shopping_fix_suspended_merchant_center_account_recommendation",
            "shopping_fix_merchant_center_account_suspension_warning_recommendation",
            "shopping_migrate_regular_shopping_campaign_offers_to_performance_max_recommendation",
            "dynamic_image_extension_opt_in_recommendation",
            "raise_target_cpa_recommendation",
            "lower_target_roas_recommendation",
            "performance_max_opt_in_recommendation",
            "improve_performance_max_ad_strength_recommendation",
            "migrate_dynamic_search_ads_campaign_to_performance_max_recommendation",
        ],
    ) -> bool: ...
