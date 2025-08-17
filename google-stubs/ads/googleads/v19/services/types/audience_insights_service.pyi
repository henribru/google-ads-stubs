from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v19.common.types.audience_insights_attribute import (
    AudienceInsightsAttribute,
    AudienceInsightsAttributeMetadata,
    AudienceInsightsDynamicLineup,
    AudienceInsightsTopic,
)
from google.ads.googleads.v19.common.types.criteria import (
    AgeRangeInfo,
    GenderInfo,
    IncomeRangeInfo,
    LocationInfo,
    ParentalStatusInfo,
    UserInterestInfo,
)
from google.ads.googleads.v19.common.types.dates import DateRange
from google.ads.googleads.v19.enums.types.audience_insights_dimension import (
    AudienceInsightsDimensionEnum,
)
from google.ads.googleads.v19.enums.types.audience_insights_marketing_objective import (
    AudienceInsightsMarketingObjectiveEnum,
)

_M = TypeVar("_M")

class AudienceCompositionAttribute(proto.Message):
    attribute_metadata: AudienceInsightsAttributeMetadata
    metrics: AudienceCompositionMetrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        attribute_metadata: AudienceInsightsAttributeMetadata = ...,
        metrics: AudienceCompositionMetrics = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["attribute_metadata", "metrics"]
    ) -> bool: ...

class AudienceCompositionAttributeCluster(proto.Message):
    cluster_display_name: str
    cluster_metrics: AudienceCompositionMetrics
    attributes: MutableSequence[AudienceCompositionAttribute]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        cluster_display_name: str = ...,
        cluster_metrics: AudienceCompositionMetrics = ...,
        attributes: MutableSequence[AudienceCompositionAttribute] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["cluster_display_name", "cluster_metrics", "attributes"]
    ) -> bool: ...

class AudienceCompositionMetrics(proto.Message):
    baseline_audience_share: float
    audience_share: float
    index: float
    score: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        baseline_audience_share: float = ...,
        audience_share: float = ...,
        index: float = ...,
        score: float = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["baseline_audience_share", "audience_share", "index", "score"],
    ) -> bool: ...

class AudienceCompositionSection(proto.Message):
    dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    top_attributes: MutableSequence[AudienceCompositionAttribute]
    clustered_attributes: MutableSequence[AudienceCompositionAttributeCluster]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension = ...,
        top_attributes: MutableSequence[AudienceCompositionAttribute] = ...,
        clustered_attributes: MutableSequence[
            AudienceCompositionAttributeCluster
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["dimension", "top_attributes", "clustered_attributes"]
    ) -> bool: ...

class AudienceOverlapItem(proto.Message):
    attribute_metadata: AudienceInsightsAttributeMetadata
    potential_youtube_reach_intersection: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        attribute_metadata: AudienceInsightsAttributeMetadata = ...,
        potential_youtube_reach_intersection: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["attribute_metadata", "potential_youtube_reach_intersection"]
    ) -> bool: ...

class BasicInsightsAudience(proto.Message):
    country_location: MutableSequence[LocationInfo]
    sub_country_locations: MutableSequence[LocationInfo]
    gender: GenderInfo
    age_ranges: MutableSequence[AgeRangeInfo]
    user_interests: MutableSequence[UserInterestInfo]
    topics: MutableSequence[AudienceInsightsTopic]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        country_location: MutableSequence[LocationInfo] = ...,
        sub_country_locations: MutableSequence[LocationInfo] = ...,
        gender: GenderInfo = ...,
        age_ranges: MutableSequence[AgeRangeInfo] = ...,
        user_interests: MutableSequence[UserInterestInfo] = ...,
        topics: MutableSequence[AudienceInsightsTopic] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "country_location",
            "sub_country_locations",
            "gender",
            "age_ranges",
            "user_interests",
            "topics",
        ],
    ) -> bool: ...

class DimensionOverlapResult(proto.Message):
    dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    items: MutableSequence[AudienceOverlapItem]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension = ...,
        items: MutableSequence[AudienceOverlapItem] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["dimension", "items"]
    ) -> bool: ...

class GenerateAudienceCompositionInsightsRequest(proto.Message):
    customer_id: str
    audience: InsightsAudience
    baseline_audience: InsightsAudience
    data_month: str
    dimensions: MutableSequence[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    customer_insights_group: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        audience: InsightsAudience = ...,
        baseline_audience: InsightsAudience = ...,
        data_month: str = ...,
        dimensions: MutableSequence[
            AudienceInsightsDimensionEnum.AudienceInsightsDimension
        ] = ...,
        customer_insights_group: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "audience",
            "baseline_audience",
            "data_month",
            "dimensions",
            "customer_insights_group",
        ],
    ) -> bool: ...

class GenerateAudienceCompositionInsightsResponse(proto.Message):
    sections: MutableSequence[AudienceCompositionSection]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        sections: MutableSequence[AudienceCompositionSection] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["sections"]
    ) -> bool: ...

class GenerateAudienceOverlapInsightsRequest(proto.Message):
    customer_id: str
    country_location: LocationInfo
    primary_attribute: AudienceInsightsAttribute
    dimensions: MutableSequence[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    customer_insights_group: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        country_location: LocationInfo = ...,
        primary_attribute: AudienceInsightsAttribute = ...,
        dimensions: MutableSequence[
            AudienceInsightsDimensionEnum.AudienceInsightsDimension
        ] = ...,
        customer_insights_group: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "country_location",
            "primary_attribute",
            "dimensions",
            "customer_insights_group",
        ],
    ) -> bool: ...

class GenerateAudienceOverlapInsightsResponse(proto.Message):
    primary_attribute_metadata: AudienceInsightsAttributeMetadata
    dimension_results: MutableSequence[DimensionOverlapResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        primary_attribute_metadata: AudienceInsightsAttributeMetadata = ...,
        dimension_results: MutableSequence[DimensionOverlapResult] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["primary_attribute_metadata", "dimension_results"]
    ) -> bool: ...

class GenerateInsightsFinderReportRequest(proto.Message):
    customer_id: str
    baseline_audience: BasicInsightsAudience
    specific_audience: BasicInsightsAudience
    customer_insights_group: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        baseline_audience: BasicInsightsAudience = ...,
        specific_audience: BasicInsightsAudience = ...,
        customer_insights_group: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "baseline_audience",
            "specific_audience",
            "customer_insights_group",
        ],
    ) -> bool: ...

class GenerateInsightsFinderReportResponse(proto.Message):
    saved_report_url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        saved_report_url: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["saved_report_url"]
    ) -> bool: ...

class GenerateSuggestedTargetingInsightsRequest(proto.Message):
    customer_id: str
    customer_insights_group: str
    audience_definition: InsightsAudienceDefinition
    audience_description: InsightsAudienceDescription
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        customer_insights_group: str = ...,
        audience_definition: InsightsAudienceDefinition = ...,
        audience_description: InsightsAudienceDescription = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "customer_insights_group",
            "audience_definition",
            "audience_description",
        ],
    ) -> bool: ...

class GenerateSuggestedTargetingInsightsResponse(proto.Message):
    suggestions: MutableSequence[TargetingSuggestionMetrics]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        suggestions: MutableSequence[TargetingSuggestionMetrics] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["suggestions"]
    ) -> bool: ...

class GenerateTargetingSuggestionMetricsRequest(proto.Message):
    customer_id: str
    audiences: MutableSequence[BasicInsightsAudience]
    customer_insights_group: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        audiences: MutableSequence[BasicInsightsAudience] = ...,
        customer_insights_group: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "audiences", "customer_insights_group"]
    ) -> bool: ...

class GenerateTargetingSuggestionMetricsResponse(proto.Message):
    suggestions: MutableSequence[TargetingSuggestionMetrics]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        suggestions: MutableSequence[TargetingSuggestionMetrics] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["suggestions"]
    ) -> bool: ...

class InsightsAudience(proto.Message):
    country_locations: MutableSequence[LocationInfo]
    sub_country_locations: MutableSequence[LocationInfo]
    gender: GenderInfo
    age_ranges: MutableSequence[AgeRangeInfo]
    parental_status: ParentalStatusInfo
    income_ranges: MutableSequence[IncomeRangeInfo]
    dynamic_lineups: MutableSequence[AudienceInsightsDynamicLineup]
    topic_audience_combinations: MutableSequence[InsightsAudienceAttributeGroup]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        country_locations: MutableSequence[LocationInfo] = ...,
        sub_country_locations: MutableSequence[LocationInfo] = ...,
        gender: GenderInfo = ...,
        age_ranges: MutableSequence[AgeRangeInfo] = ...,
        parental_status: ParentalStatusInfo = ...,
        income_ranges: MutableSequence[IncomeRangeInfo] = ...,
        dynamic_lineups: MutableSequence[AudienceInsightsDynamicLineup] = ...,
        topic_audience_combinations: MutableSequence[
            InsightsAudienceAttributeGroup
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "country_locations",
            "sub_country_locations",
            "gender",
            "age_ranges",
            "parental_status",
            "income_ranges",
            "dynamic_lineups",
            "topic_audience_combinations",
        ],
    ) -> bool: ...

class InsightsAudienceAttributeGroup(proto.Message):
    attributes: MutableSequence[AudienceInsightsAttribute]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        attributes: MutableSequence[AudienceInsightsAttribute] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["attributes"]
    ) -> bool: ...

class InsightsAudienceDefinition(proto.Message):
    audience: InsightsAudience
    baseline_audience: InsightsAudience
    data_month: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        audience: InsightsAudience = ...,
        baseline_audience: InsightsAudience = ...,
        data_month: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["audience", "baseline_audience", "data_month"]
    ) -> bool: ...

class InsightsAudienceDescription(proto.Message):
    country_locations: MutableSequence[LocationInfo]
    audience_description: str
    marketing_objective: (
        AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective
    )
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        country_locations: MutableSequence[LocationInfo] = ...,
        audience_description: str = ...,
        marketing_objective: AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "country_locations", "audience_description", "marketing_objective"
        ],
    ) -> bool: ...

class ListAudienceInsightsAttributesRequest(proto.Message):
    customer_id: str
    dimensions: MutableSequence[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    query_text: str
    customer_insights_group: str
    location_country_filters: MutableSequence[LocationInfo]
    youtube_reach_location: LocationInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        dimensions: MutableSequence[
            AudienceInsightsDimensionEnum.AudienceInsightsDimension
        ] = ...,
        query_text: str = ...,
        customer_insights_group: str = ...,
        location_country_filters: MutableSequence[LocationInfo] = ...,
        youtube_reach_location: LocationInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "dimensions",
            "query_text",
            "customer_insights_group",
            "location_country_filters",
            "youtube_reach_location",
        ],
    ) -> bool: ...

class ListAudienceInsightsAttributesResponse(proto.Message):
    attributes: MutableSequence[AudienceInsightsAttributeMetadata]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        attributes: MutableSequence[AudienceInsightsAttributeMetadata] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["attributes"]
    ) -> bool: ...

class ListInsightsEligibleDatesRequest(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

class ListInsightsEligibleDatesResponse(proto.Message):
    data_months: MutableSequence[str]
    last_thirty_days: DateRange
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        data_months: MutableSequence[str] = ...,
        last_thirty_days: DateRange = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["data_months", "last_thirty_days"]
    ) -> bool: ...

class TargetingSuggestionMetrics(proto.Message):
    locations: MutableSequence[AudienceInsightsAttributeMetadata]
    age_ranges: MutableSequence[AgeRangeInfo]
    gender: GenderInfo
    parental_status: ParentalStatusInfo
    user_interests: MutableSequence[AudienceInsightsAttributeMetadata]
    coverage: float
    index: float
    potential_youtube_reach: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        locations: MutableSequence[AudienceInsightsAttributeMetadata] = ...,
        age_ranges: MutableSequence[AgeRangeInfo] = ...,
        gender: GenderInfo = ...,
        parental_status: ParentalStatusInfo = ...,
        user_interests: MutableSequence[AudienceInsightsAttributeMetadata] = ...,
        coverage: float = ...,
        index: float = ...,
        potential_youtube_reach: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "locations",
            "age_ranges",
            "gender",
            "parental_status",
            "user_interests",
            "coverage",
            "index",
            "potential_youtube_reach",
        ],
    ) -> bool: ...
