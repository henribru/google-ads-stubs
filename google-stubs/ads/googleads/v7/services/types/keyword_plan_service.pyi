from typing import Any

import proto

from google.ads.googleads.v7.common.types import (
    keyword_plan_common as keyword_plan_common,
)

__protobuf__: Any

class GetKeywordPlanRequest(proto.Message):
    resource_name: Any

class MutateKeywordPlansRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class KeywordPlanOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateKeywordPlansResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateKeywordPlansResult(proto.Message):
    resource_name: Any

class GenerateForecastCurveRequest(proto.Message):
    keyword_plan: Any

class GenerateForecastCurveResponse(proto.Message):
    campaign_forecast_curves: Any

class GenerateForecastTimeSeriesRequest(proto.Message):
    keyword_plan: Any

class GenerateForecastTimeSeriesResponse(proto.Message):
    weekly_time_series_forecasts: Any

class GenerateForecastMetricsRequest(proto.Message):
    keyword_plan: Any

class GenerateForecastMetricsResponse(proto.Message):
    campaign_forecasts: Any
    ad_group_forecasts: Any
    keyword_forecasts: Any

class KeywordPlanCampaignForecast(proto.Message):
    keyword_plan_campaign: Any
    campaign_forecast: Any

class KeywordPlanAdGroupForecast(proto.Message):
    keyword_plan_ad_group: Any
    ad_group_forecast: Any

class KeywordPlanKeywordForecast(proto.Message):
    keyword_plan_ad_group_keyword: Any
    keyword_forecast: Any

class KeywordPlanCampaignForecastCurve(proto.Message):
    keyword_plan_campaign: Any
    max_cpc_bid_forecast_curve: Any

class KeywordPlanMaxCpcBidForecastCurve(proto.Message):
    max_cpc_bid_forecasts: Any

class KeywordPlanMaxCpcBidForecast(proto.Message):
    max_cpc_bid_micros: Any
    max_cpc_bid_forecast: Any

class KeywordPlanWeeklyTimeSeriesForecast(proto.Message):
    keyword_plan_campaign: Any
    weekly_forecasts: Any

class KeywordPlanWeeklyForecast(proto.Message):
    start_date: Any
    forecast: Any

class ForecastMetrics(proto.Message):
    impressions: Any
    ctr: Any
    average_cpc: Any
    clicks: Any
    cost_micros: Any

class GenerateHistoricalMetricsRequest(proto.Message):
    keyword_plan: Any
    aggregate_metrics: Any
    historical_metrics_options: Any

class GenerateHistoricalMetricsResponse(proto.Message):
    metrics: Any
    aggregate_metric_results: Any

class KeywordPlanKeywordHistoricalMetrics(proto.Message):
    search_query: Any
    close_variants: Any
    keyword_metrics: Any
