from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.common.types.dates import YearMonthRange
from google.ads.googleads.v15.enums.types.device import DeviceEnum
from google.ads.googleads.v15.enums.types.keyword_plan_aggregate_metric_type import (
    KeywordPlanAggregateMetricTypeEnum,
)
from google.ads.googleads.v15.enums.types.keyword_plan_competition_level import (
    KeywordPlanCompetitionLevelEnum,
)
from google.ads.googleads.v15.enums.types.keyword_plan_concept_group_type import (
    KeywordPlanConceptGroupTypeEnum,
)
from google.ads.googleads.v15.enums.types.month_of_year import MonthOfYearEnum

_M = TypeVar("_M")

class ConceptGroup(proto.Message):
    name: str
    type_: KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        name: str = ...,
        type_: KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["name", "type_"]
    ) -> bool: ...

class HistoricalMetricsOptions(proto.Message):
    year_month_range: YearMonthRange
    include_average_cpc: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        year_month_range: YearMonthRange = ...,
        include_average_cpc: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["year_month_range", "include_average_cpc"]
    ) -> bool: ...

class KeywordAnnotations(proto.Message):
    concepts: MutableSequence[KeywordConcept]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        concepts: MutableSequence[KeywordConcept] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["concepts"]
    ) -> bool: ...

class KeywordConcept(proto.Message):
    name: str
    concept_group: ConceptGroup
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        name: str = ...,
        concept_group: ConceptGroup = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["name", "concept_group"]
    ) -> bool: ...

class KeywordPlanAggregateMetricResults(proto.Message):
    device_searches: MutableSequence[KeywordPlanDeviceSearches]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        device_searches: MutableSequence[KeywordPlanDeviceSearches] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["device_searches"]
    ) -> bool: ...

class KeywordPlanAggregateMetrics(proto.Message):
    aggregate_metric_types: MutableSequence[
        KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType
    ]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        aggregate_metric_types: MutableSequence[
            KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["aggregate_metric_types"]
    ) -> bool: ...

class KeywordPlanDeviceSearches(proto.Message):
    device: DeviceEnum.Device
    search_count: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        device: DeviceEnum.Device = ...,
        search_count: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["device", "search_count"]
    ) -> bool: ...

class KeywordPlanHistoricalMetrics(proto.Message):
    avg_monthly_searches: int
    monthly_search_volumes: MutableSequence[MonthlySearchVolume]
    competition: KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
    competition_index: int
    low_top_of_page_bid_micros: int
    high_top_of_page_bid_micros: int
    average_cpc_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        avg_monthly_searches: int = ...,
        monthly_search_volumes: MutableSequence[MonthlySearchVolume] = ...,
        competition: KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel = ...,
        competition_index: int = ...,
        low_top_of_page_bid_micros: int = ...,
        high_top_of_page_bid_micros: int = ...,
        average_cpc_micros: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "avg_monthly_searches",
            "monthly_search_volumes",
            "competition",
            "competition_index",
            "low_top_of_page_bid_micros",
            "high_top_of_page_bid_micros",
            "average_cpc_micros",
        ],
    ) -> bool: ...

class MonthlySearchVolume(proto.Message):
    year: int
    month: MonthOfYearEnum.MonthOfYear
    monthly_searches: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        year: int = ...,
        month: MonthOfYearEnum.MonthOfYear = ...,
        monthly_searches: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["year", "month", "monthly_searches"]
    ) -> bool: ...
