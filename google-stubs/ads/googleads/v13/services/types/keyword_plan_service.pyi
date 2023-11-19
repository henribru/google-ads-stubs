from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v13.common.types.keyword_plan_common import (
    HistoricalMetricsOptions,
    KeywordPlanAggregateMetricResults,
    KeywordPlanAggregateMetrics,
    KeywordPlanHistoricalMetrics,
)
from google.ads.googleads.v13.resources.types.keyword_plan import KeywordPlan

_M = TypeVar("_M")

class ForecastMetrics(proto.Message):
    impressions: float
    ctr: float
    average_cpc: int
    clicks: float
    cost_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        impressions: float = ...,
        ctr: float = ...,
        average_cpc: int = ...,
        clicks: float = ...,
        cost_micros: int = ...
    ) -> None: ...
    def __contains__(self, key: Literal["impressions", "ctr", "average_cpc", "clicks", "cost_micros"]) -> bool: ...  # type: ignore[override]

class GenerateForecastCurveRequest(proto.Message):
    keyword_plan: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_plan: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["keyword_plan"]) -> bool: ...  # type: ignore[override]

class GenerateForecastCurveResponse(proto.Message):
    campaign_forecast_curves: MutableSequence[KeywordPlanCampaignForecastCurve]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        campaign_forecast_curves: MutableSequence[
            KeywordPlanCampaignForecastCurve
        ] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["campaign_forecast_curves"]) -> bool: ...  # type: ignore[override]

class GenerateForecastMetricsRequest(proto.Message):
    keyword_plan: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_plan: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["keyword_plan"]) -> bool: ...  # type: ignore[override]

class GenerateForecastMetricsResponse(proto.Message):
    campaign_forecasts: MutableSequence[KeywordPlanCampaignForecast]
    ad_group_forecasts: MutableSequence[KeywordPlanAdGroupForecast]
    keyword_forecasts: MutableSequence[KeywordPlanKeywordForecast]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        campaign_forecasts: MutableSequence[KeywordPlanCampaignForecast] = ...,
        ad_group_forecasts: MutableSequence[KeywordPlanAdGroupForecast] = ...,
        keyword_forecasts: MutableSequence[KeywordPlanKeywordForecast] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["campaign_forecasts", "ad_group_forecasts", "keyword_forecasts"]) -> bool: ...  # type: ignore[override]

class GenerateForecastTimeSeriesRequest(proto.Message):
    keyword_plan: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_plan: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["keyword_plan"]) -> bool: ...  # type: ignore[override]

class GenerateForecastTimeSeriesResponse(proto.Message):
    weekly_time_series_forecasts: MutableSequence[KeywordPlanWeeklyTimeSeriesForecast]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        weekly_time_series_forecasts: MutableSequence[
            KeywordPlanWeeklyTimeSeriesForecast
        ] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["weekly_time_series_forecasts"]) -> bool: ...  # type: ignore[override]

class GenerateHistoricalMetricsRequest(proto.Message):
    keyword_plan: str
    aggregate_metrics: KeywordPlanAggregateMetrics
    historical_metrics_options: HistoricalMetricsOptions
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_plan: str = ...,
        aggregate_metrics: KeywordPlanAggregateMetrics = ...,
        historical_metrics_options: HistoricalMetricsOptions = ...
    ) -> None: ...
    def __contains__(self, key: Literal["keyword_plan", "aggregate_metrics", "historical_metrics_options"]) -> bool: ...  # type: ignore[override]

class GenerateHistoricalMetricsResponse(proto.Message):
    metrics: MutableSequence[KeywordPlanKeywordHistoricalMetrics]
    aggregate_metric_results: KeywordPlanAggregateMetricResults
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        metrics: MutableSequence[KeywordPlanKeywordHistoricalMetrics] = ...,
        aggregate_metric_results: KeywordPlanAggregateMetricResults = ...
    ) -> None: ...
    def __contains__(self, key: Literal["metrics", "aggregate_metric_results"]) -> bool: ...  # type: ignore[override]

class KeywordPlanAdGroupForecast(proto.Message):
    keyword_plan_ad_group: str
    ad_group_forecast: ForecastMetrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_plan_ad_group: str = ...,
        ad_group_forecast: ForecastMetrics = ...
    ) -> None: ...
    def __contains__(self, key: Literal["keyword_plan_ad_group", "ad_group_forecast"]) -> bool: ...  # type: ignore[override]

class KeywordPlanCampaignForecast(proto.Message):
    keyword_plan_campaign: str
    campaign_forecast: ForecastMetrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_plan_campaign: str = ...,
        campaign_forecast: ForecastMetrics = ...
    ) -> None: ...
    def __contains__(self, key: Literal["keyword_plan_campaign", "campaign_forecast"]) -> bool: ...  # type: ignore[override]

class KeywordPlanCampaignForecastCurve(proto.Message):
    keyword_plan_campaign: str
    max_cpc_bid_forecast_curve: KeywordPlanMaxCpcBidForecastCurve
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_plan_campaign: str = ...,
        max_cpc_bid_forecast_curve: KeywordPlanMaxCpcBidForecastCurve = ...
    ) -> None: ...
    def __contains__(self, key: Literal["keyword_plan_campaign", "max_cpc_bid_forecast_curve"]) -> bool: ...  # type: ignore[override]

class KeywordPlanKeywordForecast(proto.Message):
    keyword_plan_ad_group_keyword: str
    keyword_forecast: ForecastMetrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_plan_ad_group_keyword: str = ...,
        keyword_forecast: ForecastMetrics = ...
    ) -> None: ...
    def __contains__(self, key: Literal["keyword_plan_ad_group_keyword", "keyword_forecast"]) -> bool: ...  # type: ignore[override]

class KeywordPlanKeywordHistoricalMetrics(proto.Message):
    search_query: str
    close_variants: MutableSequence[str]
    keyword_metrics: KeywordPlanHistoricalMetrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        search_query: str = ...,
        close_variants: MutableSequence[str] = ...,
        keyword_metrics: KeywordPlanHistoricalMetrics = ...
    ) -> None: ...
    def __contains__(self, key: Literal["search_query", "close_variants", "keyword_metrics"]) -> bool: ...  # type: ignore[override]

class KeywordPlanMaxCpcBidForecast(proto.Message):
    max_cpc_bid_micros: int
    max_cpc_bid_forecast: ForecastMetrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        max_cpc_bid_micros: int = ...,
        max_cpc_bid_forecast: ForecastMetrics = ...
    ) -> None: ...
    def __contains__(self, key: Literal["max_cpc_bid_micros", "max_cpc_bid_forecast"]) -> bool: ...  # type: ignore[override]

class KeywordPlanMaxCpcBidForecastCurve(proto.Message):
    max_cpc_bid_forecasts: MutableSequence[KeywordPlanMaxCpcBidForecast]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        max_cpc_bid_forecasts: MutableSequence[KeywordPlanMaxCpcBidForecast] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["max_cpc_bid_forecasts"]) -> bool: ...  # type: ignore[override]

class KeywordPlanOperation(proto.Message):
    update_mask: FieldMask
    create: KeywordPlan
    update: KeywordPlan
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: KeywordPlan = ...,
        update: KeywordPlan = ...,
        remove: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...  # type: ignore[override]

class KeywordPlanWeeklyForecast(proto.Message):
    start_date: str
    forecast: ForecastMetrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        start_date: str = ...,
        forecast: ForecastMetrics = ...
    ) -> None: ...
    def __contains__(self, key: Literal["start_date", "forecast"]) -> bool: ...  # type: ignore[override]

class KeywordPlanWeeklyTimeSeriesForecast(proto.Message):
    keyword_plan_campaign: str
    weekly_forecasts: MutableSequence[KeywordPlanWeeklyForecast]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_plan_campaign: str = ...,
        weekly_forecasts: MutableSequence[KeywordPlanWeeklyForecast] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["keyword_plan_campaign", "weekly_forecasts"]) -> bool: ...  # type: ignore[override]

class MutateKeywordPlansRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[KeywordPlanOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[KeywordPlanOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operations", "partial_failure", "validate_only"]) -> bool: ...  # type: ignore[override]

class MutateKeywordPlansResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateKeywordPlansResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateKeywordPlansResult] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["partial_failure_error", "results"]) -> bool: ...  # type: ignore[override]

class MutateKeywordPlansResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]
