from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.common.types.additional_application_info import (
    AdditionalApplicationInfo,
)
from google.ads.googleads.v23.common.types.criteria import LocationInfo
from google.ads.googleads.v23.common.types.dates import DateRange
from google.ads.googleads.v23.enums.types.benchmarks_marketing_objective import (
    BenchmarksMarketingObjectiveEnum,
)
from google.ads.googleads.v23.enums.types.benchmarks_source_type import (
    BenchmarksSourceTypeEnum,
)

_M = TypeVar("_M")

class BenchmarksLocation(proto.Message):
    location_name: str
    location_type: str
    location_info: LocationInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        location_name: str = ...,
        location_type: str = ...,
        location_info: LocationInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["location_name", "location_type", "location_info"]
    ) -> bool: ...

class BenchmarksProductMetadata(proto.Message):
    product_name: str
    product_code: str
    marketing_objective: BenchmarksMarketingObjectiveEnum.BenchmarksMarketingObjective
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        product_name: str = ...,
        product_code: str = ...,
        marketing_objective: BenchmarksMarketingObjectiveEnum.BenchmarksMarketingObjective = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["product_name", "product_code", "marketing_objective"]
    ) -> bool: ...

class BenchmarksSource(proto.Message):
    industry_vertical_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        industry_vertical_id: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["industry_vertical_id"]
    ) -> bool: ...

class BenchmarksSourceMetadata(proto.Message):
    benchmarks_source_type: BenchmarksSourceTypeEnum.BenchmarksSourceType
    industry_vertical_info: IndustryVerticalInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        benchmarks_source_type: BenchmarksSourceTypeEnum.BenchmarksSourceType = ...,
        industry_vertical_info: IndustryVerticalInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["benchmarks_source_type", "industry_vertical_info"]
    ) -> bool: ...

class GenerateBenchmarksMetricsRequest(proto.Message):
    customer_id: str
    date_range: DateRange
    location: LocationInfo
    benchmarks_source: BenchmarksSource
    product_filter: ProductFilter
    currency_code: str
    customer_benchmarks_group: str
    application_info: AdditionalApplicationInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        date_range: DateRange = ...,
        location: LocationInfo = ...,
        benchmarks_source: BenchmarksSource = ...,
        product_filter: ProductFilter = ...,
        currency_code: str = ...,
        customer_benchmarks_group: str = ...,
        application_info: AdditionalApplicationInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "date_range",
            "location",
            "benchmarks_source",
            "product_filter",
            "currency_code",
            "customer_benchmarks_group",
            "application_info",
        ],
    ) -> bool: ...

class GenerateBenchmarksMetricsResponse(proto.Message):
    customer_metrics: Metrics
    average_benchmarks_metrics: Metrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_metrics: Metrics = ...,
        average_benchmarks_metrics: Metrics = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_metrics", "average_benchmarks_metrics"]
    ) -> bool: ...

class IndustryVerticalInfo(proto.Message):
    industry_vertical_name: str
    industry_vertical_id: int
    parent_industry_vertical_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        industry_vertical_name: str = ...,
        industry_vertical_id: int = ...,
        parent_industry_vertical_id: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "industry_vertical_name",
            "industry_vertical_id",
            "parent_industry_vertical_id",
        ],
    ) -> bool: ...

class ListBenchmarksAvailableDatesRequest(proto.Message):
    application_info: AdditionalApplicationInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        application_info: AdditionalApplicationInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["application_info"]
    ) -> bool: ...

class ListBenchmarksAvailableDatesResponse(proto.Message):
    supported_dates: DateRange
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        supported_dates: DateRange = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["supported_dates"]
    ) -> bool: ...

class ListBenchmarksLocationsRequest(proto.Message):
    application_info: AdditionalApplicationInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        application_info: AdditionalApplicationInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["application_info"]
    ) -> bool: ...

class ListBenchmarksLocationsResponse(proto.Message):
    benchmarks_locations: MutableSequence[BenchmarksLocation]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        benchmarks_locations: MutableSequence[BenchmarksLocation] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["benchmarks_locations"]
    ) -> bool: ...

class ListBenchmarksProductsRequest(proto.Message):
    application_info: AdditionalApplicationInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        application_info: AdditionalApplicationInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["application_info"]
    ) -> bool: ...

class ListBenchmarksProductsResponse(proto.Message):
    benchmarks_products: MutableSequence[BenchmarksProductMetadata]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        benchmarks_products: MutableSequence[BenchmarksProductMetadata] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["benchmarks_products"]
    ) -> bool: ...

class ListBenchmarksSourcesRequest(proto.Message):
    benchmarks_sources: MutableSequence[BenchmarksSourceTypeEnum.BenchmarksSourceType]
    application_info: AdditionalApplicationInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        benchmarks_sources: MutableSequence[
            BenchmarksSourceTypeEnum.BenchmarksSourceType
        ] = ...,
        application_info: AdditionalApplicationInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["benchmarks_sources", "application_info"]
    ) -> bool: ...

class ListBenchmarksSourcesResponse(proto.Message):
    benchmarks_sources: MutableSequence[BenchmarksSourceMetadata]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        benchmarks_sources: MutableSequence[BenchmarksSourceMetadata] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["benchmarks_sources"]
    ) -> bool: ...

class Metrics(proto.Message):
    average_rate_metrics: RateMetrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        average_rate_metrics: RateMetrics = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["average_rate_metrics"]
    ) -> bool: ...

class ProductFilter(proto.Message):
    class MarketingObjectiveList(proto.Message):
        marketing_objectives: MutableSequence[
            BenchmarksMarketingObjectiveEnum.BenchmarksMarketingObjective
        ]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            marketing_objectives: MutableSequence[
                BenchmarksMarketingObjectiveEnum.BenchmarksMarketingObjective
            ] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["marketing_objectives"]
        ) -> bool: ...

    class ProductList(proto.Message):
        product_codes: MutableSequence[str]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            product_codes: MutableSequence[str] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["product_codes"]
        ) -> bool: ...

    product_list: ProductFilter.ProductList
    marketing_objective_list: ProductFilter.MarketingObjectiveList
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        product_list: ProductFilter.ProductList = ...,
        marketing_objective_list: ProductFilter.MarketingObjectiveList = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["product_list", "marketing_objective_list"]
    ) -> bool: ...

class RateMetrics(proto.Message):
    average_cpm: float
    average_active_view_cpm: float
    trueview_average_cpv: float
    average_cpc: float
    average_cpi: float
    average_cpe: float
    interaction_rate: float
    engagement_rate: float
    active_view_viewability: float
    trueview_view_rate: float
    click_through_rate: float
    video_completion_p25_rate: float
    video_completion_p50_rate: float
    video_completion_p75_rate: float
    video_completion_p100_rate: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        average_cpm: float = ...,
        average_active_view_cpm: float = ...,
        trueview_average_cpv: float = ...,
        average_cpc: float = ...,
        average_cpi: float = ...,
        average_cpe: float = ...,
        interaction_rate: float = ...,
        engagement_rate: float = ...,
        active_view_viewability: float = ...,
        trueview_view_rate: float = ...,
        click_through_rate: float = ...,
        video_completion_p25_rate: float = ...,
        video_completion_p50_rate: float = ...,
        video_completion_p75_rate: float = ...,
        video_completion_p100_rate: float = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "average_cpm",
            "average_active_view_cpm",
            "trueview_average_cpv",
            "average_cpc",
            "average_cpi",
            "average_cpe",
            "interaction_rate",
            "engagement_rate",
            "active_view_viewability",
            "trueview_view_rate",
            "click_through_rate",
            "video_completion_p25_rate",
            "video_completion_p50_rate",
            "video_completion_p75_rate",
            "video_completion_p100_rate",
        ],
    ) -> bool: ...
