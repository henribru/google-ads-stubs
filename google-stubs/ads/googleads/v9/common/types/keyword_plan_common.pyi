from typing import Any

import proto

from google.ads.googleads.v9.common.types import dates as dates
from google.ads.googleads.v9.enums.types import (
    keyword_plan_aggregate_metric_type as keyword_plan_aggregate_metric_type,
    keyword_plan_competition_level as keyword_plan_competition_level,
    keyword_plan_concept_group_type as keyword_plan_concept_group_type,
    month_of_year as month_of_year,
)

__protobuf__: Any

class KeywordPlanHistoricalMetrics(proto.Message):
    avg_monthly_searches: Any
    monthly_search_volumes: Any
    competition: Any
    competition_index: Any
    low_top_of_page_bid_micros: Any
    high_top_of_page_bid_micros: Any

class HistoricalMetricsOptions(proto.Message):
    year_month_range: Any

class MonthlySearchVolume(proto.Message):
    year: Any
    month: Any
    monthly_searches: Any

class KeywordPlanAggregateMetrics(proto.Message):
    aggregate_metric_types: Any

class KeywordPlanAggregateMetricResults(proto.Message):
    device_searches: Any

class KeywordPlanDeviceSearches(proto.Message):
    device: Any
    search_count: Any

class KeywordAnnotations(proto.Message):
    concepts: Any

class KeywordConcept(proto.Message):
    name: Any
    concept_group: Any

class ConceptGroup(proto.Message):
    name: Any
    type_: Any
