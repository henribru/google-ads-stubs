import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.common.types import dates as dates
from google.ads.googleads.v10.enums.types import (
    keyword_plan_aggregate_metric_type as keyword_plan_aggregate_metric_type,
    keyword_plan_competition_level as keyword_plan_competition_level,
    keyword_plan_concept_group_type as keyword_plan_concept_group_type,
    month_of_year as month_of_year,
)

__protobuf__: Incomplete

class KeywordPlanHistoricalMetrics(proto.Message):
    avg_monthly_searches: Incomplete
    monthly_search_volumes: Incomplete
    competition: Incomplete
    competition_index: Incomplete
    low_top_of_page_bid_micros: Incomplete
    high_top_of_page_bid_micros: Incomplete
    average_cpc_micros: Incomplete

class HistoricalMetricsOptions(proto.Message):
    year_month_range: Incomplete
    include_average_cpc: Incomplete

class MonthlySearchVolume(proto.Message):
    year: Incomplete
    month: Incomplete
    monthly_searches: Incomplete

class KeywordPlanAggregateMetrics(proto.Message):
    aggregate_metric_types: Incomplete

class KeywordPlanAggregateMetricResults(proto.Message):
    device_searches: Incomplete

class KeywordPlanDeviceSearches(proto.Message):
    device: Incomplete
    search_count: Incomplete

class KeywordAnnotations(proto.Message):
    concepts: Incomplete

class KeywordConcept(proto.Message):
    name: Incomplete
    concept_group: Incomplete

class ConceptGroup(proto.Message):
    name: Incomplete
    type_: Incomplete
