from collections.abc import MutableSequence
from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v12.common.types.keyword_plan_common import (
    HistoricalMetricsOptions,
    KeywordPlanAggregateMetricResults,
    KeywordPlanAggregateMetrics,
    KeywordPlanHistoricalMetrics,
)
from google.ads.googleads.v12.resources.types.keyword_plan import KeywordPlan

class ForecastMetrics(proto.Message):
    impressions: float
    ctr: float
    average_cpc: int
    clicks: float
    cost_micros: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        impressions: float = ...,
        ctr: float = ...,
        average_cpc: int = ...,
        clicks: float = ...,
        cost_micros: int = ...
    ) -> None: ...

class GenerateForecastCurveRequest(proto.Message):
    keyword_plan: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_plan: str = ...
    ) -> None: ...

class GenerateForecastCurveResponse(proto.Message):
    campaign_forecast_curves: MutableSequence[KeywordPlanCampaignForecastCurve]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        campaign_forecast_curves: MutableSequence[
            KeywordPlanCampaignForecastCurve
        ] = ...
    ) -> None: ...

class GenerateForecastMetricsRequest(proto.Message):
    keyword_plan: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_plan: str = ...
    ) -> None: ...

class GenerateForecastMetricsResponse(proto.Message):
    campaign_forecasts: MutableSequence[KeywordPlanCampaignForecast]
    ad_group_forecasts: MutableSequence[KeywordPlanAdGroupForecast]
    keyword_forecasts: MutableSequence[KeywordPlanKeywordForecast]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        campaign_forecasts: MutableSequence[KeywordPlanCampaignForecast] = ...,
        ad_group_forecasts: MutableSequence[KeywordPlanAdGroupForecast] = ...,
        keyword_forecasts: MutableSequence[KeywordPlanKeywordForecast] = ...
    ) -> None: ...

class GenerateForecastTimeSeriesRequest(proto.Message):
    keyword_plan: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_plan: str = ...
    ) -> None: ...

class GenerateForecastTimeSeriesResponse(proto.Message):
    weekly_time_series_forecasts: MutableSequence[KeywordPlanWeeklyTimeSeriesForecast]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        weekly_time_series_forecasts: MutableSequence[
            KeywordPlanWeeklyTimeSeriesForecast
        ] = ...
    ) -> None: ...

class GenerateHistoricalMetricsRequest(proto.Message):
    keyword_plan: str
    aggregate_metrics: KeywordPlanAggregateMetrics
    historical_metrics_options: HistoricalMetricsOptions
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_plan: str = ...,
        aggregate_metrics: KeywordPlanAggregateMetrics = ...,
        historical_metrics_options: HistoricalMetricsOptions = ...
    ) -> None: ...

class GenerateHistoricalMetricsResponse(proto.Message):
    metrics: MutableSequence[KeywordPlanKeywordHistoricalMetrics]
    aggregate_metric_results: KeywordPlanAggregateMetricResults
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        metrics: MutableSequence[KeywordPlanKeywordHistoricalMetrics] = ...,
        aggregate_metric_results: KeywordPlanAggregateMetricResults = ...
    ) -> None: ...

class KeywordPlanAdGroupForecast(proto.Message):
    keyword_plan_ad_group: str
    ad_group_forecast: ForecastMetrics
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_plan_ad_group: str = ...,
        ad_group_forecast: ForecastMetrics = ...
    ) -> None: ...

class KeywordPlanCampaignForecast(proto.Message):
    keyword_plan_campaign: str
    campaign_forecast: ForecastMetrics
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_plan_campaign: str = ...,
        campaign_forecast: ForecastMetrics = ...
    ) -> None: ...

class KeywordPlanCampaignForecastCurve(proto.Message):
    keyword_plan_campaign: str
    max_cpc_bid_forecast_curve: KeywordPlanMaxCpcBidForecastCurve
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_plan_campaign: str = ...,
        max_cpc_bid_forecast_curve: KeywordPlanMaxCpcBidForecastCurve = ...
    ) -> None: ...

class KeywordPlanKeywordForecast(proto.Message):
    keyword_plan_ad_group_keyword: str
    keyword_forecast: ForecastMetrics
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_plan_ad_group_keyword: str = ...,
        keyword_forecast: ForecastMetrics = ...
    ) -> None: ...

class KeywordPlanKeywordHistoricalMetrics(proto.Message):
    search_query: str
    close_variants: MutableSequence[str]
    keyword_metrics: KeywordPlanHistoricalMetrics
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        search_query: str = ...,
        close_variants: MutableSequence[str] = ...,
        keyword_metrics: KeywordPlanHistoricalMetrics = ...
    ) -> None: ...

class KeywordPlanMaxCpcBidForecast(proto.Message):
    max_cpc_bid_micros: int
    max_cpc_bid_forecast: ForecastMetrics
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        max_cpc_bid_micros: int = ...,
        max_cpc_bid_forecast: ForecastMetrics = ...
    ) -> None: ...

class KeywordPlanMaxCpcBidForecastCurve(proto.Message):
    max_cpc_bid_forecasts: MutableSequence[KeywordPlanMaxCpcBidForecast]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        max_cpc_bid_forecasts: MutableSequence[KeywordPlanMaxCpcBidForecast] = ...
    ) -> None: ...

class KeywordPlanOperation(proto.Message):
    update_mask: FieldMask
    create: KeywordPlan
    update: KeywordPlan
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: KeywordPlan = ...,
        update: KeywordPlan = ...,
        remove: str = ...
    ) -> None: ...

class KeywordPlanWeeklyForecast(proto.Message):
    start_date: str
    forecast: ForecastMetrics
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        start_date: str = ...,
        forecast: ForecastMetrics = ...
    ) -> None: ...

class KeywordPlanWeeklyTimeSeriesForecast(proto.Message):
    keyword_plan_campaign: str
    weekly_forecasts: MutableSequence[KeywordPlanWeeklyForecast]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_plan_campaign: str = ...,
        weekly_forecasts: MutableSequence[KeywordPlanWeeklyForecast] = ...
    ) -> None: ...

class MutateKeywordPlansRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[KeywordPlanOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[KeywordPlanOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateKeywordPlansResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateKeywordPlansResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateKeywordPlansResult] = ...
    ) -> None: ...

class MutateKeywordPlansResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
