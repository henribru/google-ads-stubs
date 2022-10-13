from typing import Any

import proto

from google.ads.googleads.v10.common.types.keyword_plan_common import (
    HistoricalMetricsOptions,
    KeywordAnnotations,
    KeywordPlanAggregateMetricResults,
    KeywordPlanAggregateMetrics,
    KeywordPlanHistoricalMetrics,
)
from google.ads.googleads.v10.enums.types.keyword_plan_keyword_annotation import (
    KeywordPlanKeywordAnnotationEnum,
)
from google.ads.googleads.v10.enums.types.keyword_plan_network import (
    KeywordPlanNetworkEnum,
)

class GenerateKeywordHistoricalMetricsRequest(proto.Message):
    customer_id: str
    keywords: list[str]
    historical_metrics_options: HistoricalMetricsOptions
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        keywords: list[str] = ...,
        historical_metrics_options: HistoricalMetricsOptions = ...
    ) -> None: ...

class GenerateKeywordHistoricalMetricsResponse(proto.Message):
    results: list[GenerateKeywordHistoricalMetricsResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[GenerateKeywordHistoricalMetricsResult] = ...
    ) -> None: ...

class GenerateKeywordHistoricalMetricsResult(proto.Message):
    text: str
    close_variants: list[str]
    keyword_metrics: KeywordPlanHistoricalMetrics
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        text: str = ...,
        close_variants: list[str] = ...,
        keyword_metrics: KeywordPlanHistoricalMetrics = ...
    ) -> None: ...

class GenerateKeywordIdeaResponse(proto.Message):
    results: list[GenerateKeywordIdeaResult]
    aggregate_metric_results: KeywordPlanAggregateMetricResults
    next_page_token: str
    total_size: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[GenerateKeywordIdeaResult] = ...,
        aggregate_metric_results: KeywordPlanAggregateMetricResults = ...,
        next_page_token: str = ...,
        total_size: int = ...
    ) -> None: ...

class GenerateKeywordIdeaResult(proto.Message):
    text: str
    keyword_idea_metrics: KeywordPlanHistoricalMetrics
    keyword_annotations: KeywordAnnotations
    close_variants: list[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        text: str = ...,
        keyword_idea_metrics: KeywordPlanHistoricalMetrics = ...,
        keyword_annotations: KeywordAnnotations = ...,
        close_variants: list[str] = ...
    ) -> None: ...

class GenerateKeywordIdeasRequest(proto.Message):
    customer_id: str
    language: str
    geo_target_constants: list[str]
    include_adult_keywords: bool
    page_token: str
    page_size: int
    keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetwork
    keyword_annotation: list[
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
        geo_target_constants: list[str] = ...,
        include_adult_keywords: bool = ...,
        page_token: str = ...,
        page_size: int = ...,
        keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetwork = ...,
        keyword_annotation: list[
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
    keywords: list[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        url: str = ...,
        keywords: list[str] = ...
    ) -> None: ...

class KeywordSeed(proto.Message):
    keywords: list[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keywords: list[str] = ...
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

class UrlSeed(proto.Message):
    url: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        url: str = ...
    ) -> None: ...
