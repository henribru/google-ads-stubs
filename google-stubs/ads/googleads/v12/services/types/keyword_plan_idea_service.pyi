from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v12.common.types.keyword_plan_common import (
    HistoricalMetricsOptions,
    KeywordAnnotations,
    KeywordPlanAggregateMetricResults,
    KeywordPlanAggregateMetrics,
    KeywordPlanHistoricalMetrics,
)
from google.ads.googleads.v12.enums.types.keyword_match_type import KeywordMatchTypeEnum
from google.ads.googleads.v12.enums.types.keyword_plan_keyword_annotation import (
    KeywordPlanKeywordAnnotationEnum,
)
from google.ads.googleads.v12.enums.types.keyword_plan_network import (
    KeywordPlanNetworkEnum,
)

class AdGroupKeywordSuggestion(proto.Message):
    keyword_text: str
    suggested_keyword_text: str
    suggested_match_type: KeywordMatchTypeEnum.KeywordMatchType
    suggested_ad_group: str
    suggested_campaign: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_text: str = ...,
        suggested_keyword_text: str = ...,
        suggested_match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
        suggested_ad_group: str = ...,
        suggested_campaign: str = ...
    ) -> None: ...

class GenerateAdGroupThemesRequest(proto.Message):
    customer_id: str
    keywords: MutableSequence[str]
    ad_groups: MutableSequence[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        keywords: MutableSequence[str] = ...,
        ad_groups: MutableSequence[str] = ...
    ) -> None: ...

class GenerateAdGroupThemesResponse(proto.Message):
    ad_group_keyword_suggestions: MutableSequence[AdGroupKeywordSuggestion]
    unusable_ad_groups: MutableSequence[UnusableAdGroup]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        ad_group_keyword_suggestions: MutableSequence[AdGroupKeywordSuggestion] = ...,
        unusable_ad_groups: MutableSequence[UnusableAdGroup] = ...
    ) -> None: ...

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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        keywords: MutableSequence[str] = ...,
        language: str = ...,
        include_adult_keywords: bool = ...,
        geo_target_constants: MutableSequence[str] = ...,
        keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetwork = ...,
        aggregate_metrics: KeywordPlanAggregateMetrics = ...,
        historical_metrics_options: HistoricalMetricsOptions = ...
    ) -> None: ...

class GenerateKeywordHistoricalMetricsResponse(proto.Message):
    results: MutableSequence[GenerateKeywordHistoricalMetricsResult]
    aggregate_metric_results: KeywordPlanAggregateMetricResults
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: MutableSequence[GenerateKeywordHistoricalMetricsResult] = ...,
        aggregate_metric_results: KeywordPlanAggregateMetricResults = ...
    ) -> None: ...

class GenerateKeywordHistoricalMetricsResult(proto.Message):
    text: str
    close_variants: MutableSequence[str]
    keyword_metrics: KeywordPlanHistoricalMetrics
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        text: str = ...,
        close_variants: MutableSequence[str] = ...,
        keyword_metrics: KeywordPlanHistoricalMetrics = ...
    ) -> None: ...

class GenerateKeywordIdeaResponse(proto.Message):
    results: MutableSequence[GenerateKeywordIdeaResult]
    aggregate_metric_results: KeywordPlanAggregateMetricResults
    next_page_token: str
    total_size: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: MutableSequence[GenerateKeywordIdeaResult] = ...,
        aggregate_metric_results: KeywordPlanAggregateMetricResults = ...,
        next_page_token: str = ...,
        total_size: int = ...
    ) -> None: ...

class GenerateKeywordIdeaResult(proto.Message):
    text: str
    keyword_idea_metrics: KeywordPlanHistoricalMetrics
    keyword_annotations: KeywordAnnotations
    close_variants: MutableSequence[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        text: str = ...,
        keyword_idea_metrics: KeywordPlanHistoricalMetrics = ...,
        keyword_annotations: KeywordAnnotations = ...,
        close_variants: MutableSequence[str] = ...
    ) -> None: ...

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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        site_seed: SiteSeed = ...
    ) -> None: ...

class KeywordAndUrlSeed(proto.Message):
    url: str
    keywords: MutableSequence[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        url: str = ...,
        keywords: MutableSequence[str] = ...
    ) -> None: ...

class KeywordSeed(proto.Message):
    keywords: MutableSequence[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keywords: MutableSequence[str] = ...
    ) -> None: ...

class SiteSeed(proto.Message):
    site: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        site: str = ...
    ) -> None: ...

class UnusableAdGroup(proto.Message):
    ad_group: str
    campaign: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        ad_group: str = ...,
        campaign: str = ...
    ) -> None: ...

class UrlSeed(proto.Message):
    url: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        url: str = ...
    ) -> None: ...
