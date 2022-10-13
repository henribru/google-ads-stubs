from typing import Any

import proto

from google.ads.googleads.v11.common.types.dates import YearMonthRange
from google.ads.googleads.v11.enums.types.device import DeviceEnum
from google.ads.googleads.v11.enums.types.keyword_plan_aggregate_metric_type import (
    KeywordPlanAggregateMetricTypeEnum,
)
from google.ads.googleads.v11.enums.types.keyword_plan_competition_level import (
    KeywordPlanCompetitionLevelEnum,
)
from google.ads.googleads.v11.enums.types.keyword_plan_concept_group_type import (
    KeywordPlanConceptGroupTypeEnum,
)
from google.ads.googleads.v11.enums.types.month_of_year import MonthOfYearEnum

class ConceptGroup(proto.Message):
    name: str
    type_: KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        name: str = ...,
        type_: KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType = ...
    ) -> None: ...

class HistoricalMetricsOptions(proto.Message):
    year_month_range: YearMonthRange
    include_average_cpc: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        year_month_range: YearMonthRange = ...,
        include_average_cpc: bool = ...
    ) -> None: ...

class KeywordAnnotations(proto.Message):
    concepts: list[KeywordConcept]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        concepts: list[KeywordConcept] = ...
    ) -> None: ...

class KeywordConcept(proto.Message):
    name: str
    concept_group: ConceptGroup
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        name: str = ...,
        concept_group: ConceptGroup = ...
    ) -> None: ...

class KeywordPlanAggregateMetricResults(proto.Message):
    device_searches: list[KeywordPlanDeviceSearches]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        device_searches: list[KeywordPlanDeviceSearches] = ...
    ) -> None: ...

class KeywordPlanAggregateMetrics(proto.Message):
    aggregate_metric_types: list[
        KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType
    ]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        aggregate_metric_types: list[
            KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType
        ] = ...
    ) -> None: ...

class KeywordPlanDeviceSearches(proto.Message):
    device: DeviceEnum.Device
    search_count: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        device: DeviceEnum.Device = ...,
        search_count: int = ...
    ) -> None: ...

class KeywordPlanHistoricalMetrics(proto.Message):
    avg_monthly_searches: int
    monthly_search_volumes: list[MonthlySearchVolume]
    competition: KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
    competition_index: int
    low_top_of_page_bid_micros: int
    high_top_of_page_bid_micros: int
    average_cpc_micros: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        avg_monthly_searches: int = ...,
        monthly_search_volumes: list[MonthlySearchVolume] = ...,
        competition: KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel = ...,
        competition_index: int = ...,
        low_top_of_page_bid_micros: int = ...,
        high_top_of_page_bid_micros: int = ...,
        average_cpc_micros: int = ...
    ) -> None: ...

class MonthlySearchVolume(proto.Message):
    year: int
    month: MonthOfYearEnum.MonthOfYear
    monthly_searches: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        year: int = ...,
        month: MonthOfYearEnum.MonthOfYear = ...,
        monthly_searches: int = ...
    ) -> None: ...
