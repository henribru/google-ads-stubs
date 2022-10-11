import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v11.common.types import (
    keyword_plan_common as keyword_plan_common,
)

__protobuf__: Incomplete

class MutateKeywordPlansRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class KeywordPlanOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateKeywordPlansResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateKeywordPlansResult(proto.Message):
    resource_name: Incomplete

class GenerateForecastCurveRequest(proto.Message):
    keyword_plan: Incomplete

class GenerateForecastCurveResponse(proto.Message):
    campaign_forecast_curves: Incomplete

class GenerateForecastTimeSeriesRequest(proto.Message):
    keyword_plan: Incomplete

class GenerateForecastTimeSeriesResponse(proto.Message):
    weekly_time_series_forecasts: Incomplete

class GenerateForecastMetricsRequest(proto.Message):
    keyword_plan: Incomplete

class GenerateForecastMetricsResponse(proto.Message):
    campaign_forecasts: Incomplete
    ad_group_forecasts: Incomplete
    keyword_forecasts: Incomplete

class KeywordPlanCampaignForecast(proto.Message):
    keyword_plan_campaign: Incomplete
    campaign_forecast: Incomplete

class KeywordPlanAdGroupForecast(proto.Message):
    keyword_plan_ad_group: Incomplete
    ad_group_forecast: Incomplete

class KeywordPlanKeywordForecast(proto.Message):
    keyword_plan_ad_group_keyword: Incomplete
    keyword_forecast: Incomplete

class KeywordPlanCampaignForecastCurve(proto.Message):
    keyword_plan_campaign: Incomplete
    max_cpc_bid_forecast_curve: Incomplete

class KeywordPlanMaxCpcBidForecastCurve(proto.Message):
    max_cpc_bid_forecasts: Incomplete

class KeywordPlanMaxCpcBidForecast(proto.Message):
    max_cpc_bid_micros: Incomplete
    max_cpc_bid_forecast: Incomplete

class KeywordPlanWeeklyTimeSeriesForecast(proto.Message):
    keyword_plan_campaign: Incomplete
    weekly_forecasts: Incomplete

class KeywordPlanWeeklyForecast(proto.Message):
    start_date: Incomplete
    forecast: Incomplete

class ForecastMetrics(proto.Message):
    impressions: Incomplete
    ctr: Incomplete
    average_cpc: Incomplete
    clicks: Incomplete
    cost_micros: Incomplete

class GenerateHistoricalMetricsRequest(proto.Message):
    keyword_plan: Incomplete
    aggregate_metrics: Incomplete
    historical_metrics_options: Incomplete

class GenerateHistoricalMetricsResponse(proto.Message):
    metrics: Incomplete
    aggregate_metric_results: Incomplete

class KeywordPlanKeywordHistoricalMetrics(proto.Message):
    search_query: Incomplete
    close_variants: Incomplete
    keyword_metrics: Incomplete
