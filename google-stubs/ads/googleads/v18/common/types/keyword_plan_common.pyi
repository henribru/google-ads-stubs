import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import dates
from google.ads.googleads.v18.enums.types import device as gage_device, keyword_plan_aggregate_metric_type, keyword_plan_competition_level, keyword_plan_concept_group_type, month_of_year
from typing import MutableSequence

__protobuf__: Incomplete

class KeywordPlanHistoricalMetrics(proto.Message):
    avg_monthly_searches: int
    monthly_search_volumes: MutableSequence['MonthlySearchVolume']
    competition: keyword_plan_competition_level.KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
    competition_index: int
    low_top_of_page_bid_micros: int
    high_top_of_page_bid_micros: int
    average_cpc_micros: int

class HistoricalMetricsOptions(proto.Message):
    year_month_range: dates.YearMonthRange
    include_average_cpc: bool

class MonthlySearchVolume(proto.Message):
    year: int
    month: month_of_year.MonthOfYearEnum.MonthOfYear
    monthly_searches: int

class KeywordPlanAggregateMetrics(proto.Message):
    aggregate_metric_types: MutableSequence[keyword_plan_aggregate_metric_type.KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType]

class KeywordPlanAggregateMetricResults(proto.Message):
    device_searches: MutableSequence['KeywordPlanDeviceSearches']

class KeywordPlanDeviceSearches(proto.Message):
    device: gage_device.DeviceEnum.Device
    search_count: int

class KeywordAnnotations(proto.Message):
    concepts: MutableSequence['KeywordConcept']

class KeywordConcept(proto.Message):
    name: str
    concept_group: ConceptGroup

class ConceptGroup(proto.Message):
    name: str
    type_: keyword_plan_concept_group_type.KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType
