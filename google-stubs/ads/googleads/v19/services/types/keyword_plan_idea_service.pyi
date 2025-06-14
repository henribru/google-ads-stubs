import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import criteria, dates, keyword_plan_common
from google.ads.googleads.v19.enums.types import keyword_match_type, keyword_plan_keyword_annotation, keyword_plan_network as gage_keyword_plan_network
from typing import MutableSequence

__protobuf__: Incomplete

class GenerateKeywordIdeasRequest(proto.Message):
    customer_id: str
    language: str
    geo_target_constants: MutableSequence[str]
    include_adult_keywords: bool
    page_token: str
    page_size: int
    keyword_plan_network: gage_keyword_plan_network.KeywordPlanNetworkEnum.KeywordPlanNetwork
    keyword_annotation: MutableSequence[keyword_plan_keyword_annotation.KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation]
    aggregate_metrics: keyword_plan_common.KeywordPlanAggregateMetrics
    historical_metrics_options: keyword_plan_common.HistoricalMetricsOptions
    keyword_and_url_seed: KeywordAndUrlSeed
    keyword_seed: KeywordSeed
    url_seed: UrlSeed
    site_seed: SiteSeed

class KeywordAndUrlSeed(proto.Message):
    url: str
    keywords: MutableSequence[str]

class KeywordSeed(proto.Message):
    keywords: MutableSequence[str]

class SiteSeed(proto.Message):
    site: str

class UrlSeed(proto.Message):
    url: str

class GenerateKeywordIdeaResponse(proto.Message):
    @property
    def raw_page(self): ...
    results: MutableSequence['GenerateKeywordIdeaResult']
    aggregate_metric_results: keyword_plan_common.KeywordPlanAggregateMetricResults
    next_page_token: str
    total_size: int

class GenerateKeywordIdeaResult(proto.Message):
    text: str
    keyword_idea_metrics: keyword_plan_common.KeywordPlanHistoricalMetrics
    keyword_annotations: keyword_plan_common.KeywordAnnotations
    close_variants: MutableSequence[str]

class GenerateKeywordHistoricalMetricsRequest(proto.Message):
    customer_id: str
    keywords: MutableSequence[str]
    language: str
    include_adult_keywords: bool
    geo_target_constants: MutableSequence[str]
    keyword_plan_network: gage_keyword_plan_network.KeywordPlanNetworkEnum.KeywordPlanNetwork
    aggregate_metrics: keyword_plan_common.KeywordPlanAggregateMetrics
    historical_metrics_options: keyword_plan_common.HistoricalMetricsOptions

class GenerateKeywordHistoricalMetricsResponse(proto.Message):
    results: MutableSequence['GenerateKeywordHistoricalMetricsResult']
    aggregate_metric_results: keyword_plan_common.KeywordPlanAggregateMetricResults

class GenerateKeywordHistoricalMetricsResult(proto.Message):
    text: str
    close_variants: MutableSequence[str]
    keyword_metrics: keyword_plan_common.KeywordPlanHistoricalMetrics

class GenerateAdGroupThemesRequest(proto.Message):
    customer_id: str
    keywords: MutableSequence[str]
    ad_groups: MutableSequence[str]

class GenerateAdGroupThemesResponse(proto.Message):
    ad_group_keyword_suggestions: MutableSequence['AdGroupKeywordSuggestion']
    unusable_ad_groups: MutableSequence['UnusableAdGroup']

class AdGroupKeywordSuggestion(proto.Message):
    keyword_text: str
    suggested_keyword_text: str
    suggested_match_type: keyword_match_type.KeywordMatchTypeEnum.KeywordMatchType
    suggested_ad_group: str
    suggested_campaign: str

class UnusableAdGroup(proto.Message):
    ad_group: str
    campaign: str

class GenerateKeywordForecastMetricsRequest(proto.Message):
    customer_id: str
    currency_code: str
    forecast_period: dates.DateRange
    campaign: CampaignToForecast

class CampaignToForecast(proto.Message):
    class CampaignBiddingStrategy(proto.Message):
        manual_cpc_bidding_strategy: ManualCpcBiddingStrategy
        maximize_clicks_bidding_strategy: MaximizeClicksBiddingStrategy
        maximize_conversions_bidding_strategy: MaximizeConversionsBiddingStrategy
    language_constants: MutableSequence[str]
    geo_modifiers: MutableSequence['CriterionBidModifier']
    keyword_plan_network: gage_keyword_plan_network.KeywordPlanNetworkEnum.KeywordPlanNetwork
    negative_keywords: MutableSequence[criteria.KeywordInfo]
    bidding_strategy: CampaignBiddingStrategy
    conversion_rate: float
    ad_groups: MutableSequence['ForecastAdGroup']

class ForecastAdGroup(proto.Message):
    max_cpc_bid_micros: int
    biddable_keywords: MutableSequence['BiddableKeyword']
    negative_keywords: MutableSequence[criteria.KeywordInfo]

class BiddableKeyword(proto.Message):
    keyword: criteria.KeywordInfo
    max_cpc_bid_micros: int

class CriterionBidModifier(proto.Message):
    geo_target_constant: str
    bid_modifier: float

class ManualCpcBiddingStrategy(proto.Message):
    daily_budget_micros: int
    max_cpc_bid_micros: int

class MaximizeClicksBiddingStrategy(proto.Message):
    daily_target_spend_micros: int
    max_cpc_bid_ceiling_micros: int

class MaximizeConversionsBiddingStrategy(proto.Message):
    daily_target_spend_micros: int

class GenerateKeywordForecastMetricsResponse(proto.Message):
    campaign_forecast_metrics: KeywordForecastMetrics

class KeywordForecastMetrics(proto.Message):
    impressions: float
    click_through_rate: float
    average_cpc_micros: int
    clicks: float
    cost_micros: int
    conversions: float
    conversion_rate: float
    average_cpa_micros: int
