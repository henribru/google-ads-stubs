from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.common.types.criteria import KeywordInfo
from google.ads.googleads.v15.common.types.dates import DateRange
from google.ads.googleads.v15.common.types.keyword_plan_common import (
    HistoricalMetricsOptions,
    KeywordAnnotations,
    KeywordPlanAggregateMetricResults,
    KeywordPlanAggregateMetrics,
    KeywordPlanHistoricalMetrics,
)
from google.ads.googleads.v15.enums.types.keyword_match_type import KeywordMatchTypeEnum
from google.ads.googleads.v15.enums.types.keyword_plan_keyword_annotation import (
    KeywordPlanKeywordAnnotationEnum,
)
from google.ads.googleads.v15.enums.types.keyword_plan_network import (
    KeywordPlanNetworkEnum,
)

_M = TypeVar("_M")

class AdGroupKeywordSuggestion(proto.Message):
    keyword_text: str
    suggested_keyword_text: str
    suggested_match_type: KeywordMatchTypeEnum.KeywordMatchType
    suggested_ad_group: str
    suggested_campaign: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_text: str = ...,
        suggested_keyword_text: str = ...,
        suggested_match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
        suggested_ad_group: str = ...,
        suggested_campaign: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "keyword_text",
            "suggested_keyword_text",
            "suggested_match_type",
            "suggested_ad_group",
            "suggested_campaign",
        ],
    ) -> bool: ...

class BiddableKeyword(proto.Message):
    keyword: KeywordInfo
    max_cpc_bid_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword: KeywordInfo = ...,
        max_cpc_bid_micros: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["keyword", "max_cpc_bid_micros"]
    ) -> bool: ...

class CampaignToForecast(proto.Message):
    class CampaignBiddingStrategy(proto.Message):
        manual_cpc_bidding_strategy: ManualCpcBiddingStrategy
        maximize_clicks_bidding_strategy: MaximizeClicksBiddingStrategy
        maximize_conversions_bidding_strategy: MaximizeConversionsBiddingStrategy
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            manual_cpc_bidding_strategy: ManualCpcBiddingStrategy = ...,
            maximize_clicks_bidding_strategy: MaximizeClicksBiddingStrategy = ...,
            maximize_conversions_bidding_strategy: MaximizeConversionsBiddingStrategy = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "manual_cpc_bidding_strategy",
                "maximize_clicks_bidding_strategy",
                "maximize_conversions_bidding_strategy",
            ],
        ) -> bool: ...

    language_constants: MutableSequence[str]
    geo_modifiers: MutableSequence[CriterionBidModifier]
    keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetwork
    negative_keywords: MutableSequence[KeywordInfo]
    bidding_strategy: CampaignToForecast.CampaignBiddingStrategy
    conversion_rate: float
    ad_groups: MutableSequence[ForecastAdGroup]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        language_constants: MutableSequence[str] = ...,
        geo_modifiers: MutableSequence[CriterionBidModifier] = ...,
        keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetwork = ...,
        negative_keywords: MutableSequence[KeywordInfo] = ...,
        bidding_strategy: CampaignToForecast.CampaignBiddingStrategy = ...,
        conversion_rate: float = ...,
        ad_groups: MutableSequence[ForecastAdGroup] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "language_constants",
            "geo_modifiers",
            "keyword_plan_network",
            "negative_keywords",
            "bidding_strategy",
            "conversion_rate",
            "ad_groups",
        ],
    ) -> bool: ...

class CriterionBidModifier(proto.Message):
    geo_target_constant: str
    bid_modifier: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        geo_target_constant: str = ...,
        bid_modifier: float = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["geo_target_constant", "bid_modifier"]
    ) -> bool: ...

class ForecastAdGroup(proto.Message):
    max_cpc_bid_micros: int
    biddable_keywords: MutableSequence[BiddableKeyword]
    negative_keywords: MutableSequence[KeywordInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        max_cpc_bid_micros: int = ...,
        biddable_keywords: MutableSequence[BiddableKeyword] = ...,
        negative_keywords: MutableSequence[KeywordInfo] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["max_cpc_bid_micros", "biddable_keywords", "negative_keywords"],
    ) -> bool: ...

class GenerateAdGroupThemesRequest(proto.Message):
    customer_id: str
    keywords: MutableSequence[str]
    ad_groups: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        keywords: MutableSequence[str] = ...,
        ad_groups: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "keywords", "ad_groups"]
    ) -> bool: ...

class GenerateAdGroupThemesResponse(proto.Message):
    ad_group_keyword_suggestions: MutableSequence[AdGroupKeywordSuggestion]
    unusable_ad_groups: MutableSequence[UnusableAdGroup]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ad_group_keyword_suggestions: MutableSequence[AdGroupKeywordSuggestion] = ...,
        unusable_ad_groups: MutableSequence[UnusableAdGroup] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["ad_group_keyword_suggestions", "unusable_ad_groups"]
    ) -> bool: ...

class GenerateKeywordForecastMetricsRequest(proto.Message):
    customer_id: str
    currency_code: str
    forecast_period: DateRange
    campaign: CampaignToForecast
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        currency_code: str = ...,
        forecast_period: DateRange = ...,
        campaign: CampaignToForecast = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["customer_id", "currency_code", "forecast_period", "campaign"],
    ) -> bool: ...

class GenerateKeywordForecastMetricsResponse(proto.Message):
    campaign_forecast_metrics: KeywordForecastMetrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        campaign_forecast_metrics: KeywordForecastMetrics = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["campaign_forecast_metrics"]
    ) -> bool: ...

class GenerateKeywordHistoricalMetricsRequest(proto.Message):
    customer_id: str
    keywords: MutableSequence[str]
    language: str
    include_adult_keywords: bool
    geo_target_constants: MutableSequence[str]
    keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetwork
    aggregate_metrics: KeywordPlanAggregateMetrics
    historical_metrics_options: HistoricalMetricsOptions
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        keywords: MutableSequence[str] = ...,
        language: str = ...,
        include_adult_keywords: bool = ...,
        geo_target_constants: MutableSequence[str] = ...,
        keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetwork = ...,
        aggregate_metrics: KeywordPlanAggregateMetrics = ...,
        historical_metrics_options: HistoricalMetricsOptions = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "keywords",
            "language",
            "include_adult_keywords",
            "geo_target_constants",
            "keyword_plan_network",
            "aggregate_metrics",
            "historical_metrics_options",
        ],
    ) -> bool: ...

class GenerateKeywordHistoricalMetricsResponse(proto.Message):
    results: MutableSequence[GenerateKeywordHistoricalMetricsResult]
    aggregate_metric_results: KeywordPlanAggregateMetricResults
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[GenerateKeywordHistoricalMetricsResult] = ...,
        aggregate_metric_results: KeywordPlanAggregateMetricResults = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["results", "aggregate_metric_results"]
    ) -> bool: ...

class GenerateKeywordHistoricalMetricsResult(proto.Message):
    text: str
    close_variants: MutableSequence[str]
    keyword_metrics: KeywordPlanHistoricalMetrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        text: str = ...,
        close_variants: MutableSequence[str] = ...,
        keyword_metrics: KeywordPlanHistoricalMetrics = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["text", "close_variants", "keyword_metrics"]
    ) -> bool: ...

class GenerateKeywordIdeaResponse(proto.Message):
    results: MutableSequence[GenerateKeywordIdeaResult]
    aggregate_metric_results: KeywordPlanAggregateMetricResults
    next_page_token: str
    total_size: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[GenerateKeywordIdeaResult] = ...,
        aggregate_metric_results: KeywordPlanAggregateMetricResults = ...,
        next_page_token: str = ...,
        total_size: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "results", "aggregate_metric_results", "next_page_token", "total_size"
        ],
    ) -> bool: ...

class GenerateKeywordIdeaResult(proto.Message):
    text: str
    keyword_idea_metrics: KeywordPlanHistoricalMetrics
    keyword_annotations: KeywordAnnotations
    close_variants: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        text: str = ...,
        keyword_idea_metrics: KeywordPlanHistoricalMetrics = ...,
        keyword_annotations: KeywordAnnotations = ...,
        close_variants: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "text", "keyword_idea_metrics", "keyword_annotations", "close_variants"
        ],
    ) -> bool: ...

class GenerateKeywordIdeasRequest(proto.Message):
    customer_id: str
    language: str
    geo_target_constants: MutableSequence[str]
    include_adult_keywords: bool
    page_token: str
    page_size: int
    keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetwork
    keyword_annotation: MutableSequence[
        KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation
    ]
    aggregate_metrics: KeywordPlanAggregateMetrics
    historical_metrics_options: HistoricalMetricsOptions
    keyword_and_url_seed: KeywordAndUrlSeed
    keyword_seed: KeywordSeed
    url_seed: UrlSeed
    site_seed: SiteSeed
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        language: str = ...,
        geo_target_constants: MutableSequence[str] = ...,
        include_adult_keywords: bool = ...,
        page_token: str = ...,
        page_size: int = ...,
        keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetwork = ...,
        keyword_annotation: MutableSequence[
            KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation
        ] = ...,
        aggregate_metrics: KeywordPlanAggregateMetrics = ...,
        historical_metrics_options: HistoricalMetricsOptions = ...,
        keyword_and_url_seed: KeywordAndUrlSeed = ...,
        keyword_seed: KeywordSeed = ...,
        url_seed: UrlSeed = ...,
        site_seed: SiteSeed = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "language",
            "geo_target_constants",
            "include_adult_keywords",
            "page_token",
            "page_size",
            "keyword_plan_network",
            "keyword_annotation",
            "aggregate_metrics",
            "historical_metrics_options",
            "keyword_and_url_seed",
            "keyword_seed",
            "url_seed",
            "site_seed",
        ],
    ) -> bool: ...

class KeywordAndUrlSeed(proto.Message):
    url: str
    keywords: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        url: str = ...,
        keywords: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["url", "keywords"]
    ) -> bool: ...

class KeywordForecastMetrics(proto.Message):
    impressions: float
    click_through_rate: float
    average_cpc_micros: int
    clicks: float
    cost_micros: int
    conversions: float
    conversion_rate: float
    average_cpa_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        impressions: float = ...,
        click_through_rate: float = ...,
        average_cpc_micros: int = ...,
        clicks: float = ...,
        cost_micros: int = ...,
        conversions: float = ...,
        conversion_rate: float = ...,
        average_cpa_micros: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "impressions",
            "click_through_rate",
            "average_cpc_micros",
            "clicks",
            "cost_micros",
            "conversions",
            "conversion_rate",
            "average_cpa_micros",
        ],
    ) -> bool: ...

class KeywordSeed(proto.Message):
    keywords: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keywords: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["keywords"]
    ) -> bool: ...

class ManualCpcBiddingStrategy(proto.Message):
    daily_budget_micros: int
    max_cpc_bid_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        daily_budget_micros: int = ...,
        max_cpc_bid_micros: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["daily_budget_micros", "max_cpc_bid_micros"]
    ) -> bool: ...

class MaximizeClicksBiddingStrategy(proto.Message):
    daily_target_spend_micros: int
    max_cpc_bid_ceiling_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        daily_target_spend_micros: int = ...,
        max_cpc_bid_ceiling_micros: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["daily_target_spend_micros", "max_cpc_bid_ceiling_micros"]
    ) -> bool: ...

class MaximizeConversionsBiddingStrategy(proto.Message):
    daily_target_spend_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        daily_target_spend_micros: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["daily_target_spend_micros"]
    ) -> bool: ...

class SiteSeed(proto.Message):
    site: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        site: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["site"]
    ) -> bool: ...

class UnusableAdGroup(proto.Message):
    ad_group: str
    campaign: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ad_group: str = ...,
        campaign: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["ad_group", "campaign"]
    ) -> bool: ...

class UrlSeed(proto.Message):
    url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        url: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["url"]
    ) -> bool: ...
