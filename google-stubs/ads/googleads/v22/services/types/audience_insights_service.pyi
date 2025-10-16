from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.audience_insights_attribute import AudienceInsightsAttributeMetadataGroup
from google.ads.googleads.v22.common.types.criteria import ParentalStatusInfo
from google.ads.googleads.v22.common.types.criteria import GenderInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.criteria import AgeRangeInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.audience_insights_attribute import AudienceInsightsAttributeMetadata
from google.ads.googleads.v22.common.types.dates import DateRange
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.additional_application_info import AdditionalApplicationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.audience_insights_attribute import AudienceInsightsAttributeMetadata
from google.ads.googleads.v22.common.types.criteria import LocationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.criteria import LocationInfo
from google.ads.googleads.v22.common.types.additional_application_info import AdditionalApplicationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.audience_insights_dimension import AudienceInsightsDimensionEnum
from google.ads.googleads.v22.enums.types.audience_insights_marketing_objective import AudienceInsightsMarketingObjectiveEnum
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.criteria import LocationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.audience_insights_attribute import AudienceInsightsAttribute
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.criteria import UserListInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.audience_insights_attribute import AudienceInsightsLineup
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.criteria import IncomeRangeInfo
from google.ads.googleads.v22.common.types.criteria import ParentalStatusInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.criteria import AgeRangeInfo
from google.ads.googleads.v22.common.types.criteria import GenderInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.criteria import LocationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.criteria import LocationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.additional_application_info import AdditionalApplicationInfo
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.additional_application_info import AdditionalApplicationInfo
from google.ads.googleads.v22.common.types.additional_application_info import AdditionalApplicationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.audience_insights_attribute import AudienceInsightsAttributeMetadata
from google.ads.googleads.v22.common.types.additional_application_info import AdditionalApplicationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.audience_insights_dimension import AudienceInsightsDimensionEnum
from google.ads.googleads.v22.common.types.audience_insights_attribute import AudienceInsightsAttribute
from google.ads.googleads.v22.common.types.criteria import LocationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.additional_application_info import AdditionalApplicationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.audience_insights_dimension import AudienceInsightsDimensionEnum
from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.audience_insights_dimension import AudienceInsightsDimensionEnum
from google.ads.googleads.v22.common.types.audience_insights_attribute import AudienceInsightsAttributeMetadata
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.audience_insights_dimension import AudienceInsightsDimensionEnum
from collections.abc import MutableSequence
from google.ads.googleads.v22.common.types.audience_insights_attribute import AudienceInsightsAttributeMetadata
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AudienceCompositionAttribute(proto.Message):
    attribute_metadata: AudienceInsightsAttributeMetadata
    metrics: AudienceCompositionMetrics
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, attribute_metadata: AudienceInsightsAttributeMetadata = ..., metrics: AudienceCompositionMetrics = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["attribute_metadata", "metrics"]) -> bool: ...
class AudienceCompositionAttributeCluster(proto.Message):
    cluster_display_name: str
    cluster_metrics: AudienceCompositionMetrics
    attributes: MutableSequence[AudienceCompositionAttribute]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, cluster_display_name: str = ..., cluster_metrics: AudienceCompositionMetrics = ..., attributes: MutableSequence[AudienceCompositionAttribute] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["cluster_display_name", "cluster_metrics", "attributes"]) -> bool: ...
class AudienceCompositionMetrics(proto.Message):
    baseline_audience_share: float
    audience_share: float
    index: float
    score: float
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, baseline_audience_share: float = ..., audience_share: float = ..., index: float = ..., score: float = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["baseline_audience_share", "audience_share", "index", "score"]) -> bool: ...
class AudienceCompositionSection(proto.Message):
    dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    top_attributes: MutableSequence[AudienceCompositionAttribute]
    clustered_attributes: MutableSequence[AudienceCompositionAttributeCluster]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension = ..., top_attributes: MutableSequence[AudienceCompositionAttribute] = ..., clustered_attributes: MutableSequence[AudienceCompositionAttributeCluster] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["dimension", "top_attributes", "clustered_attributes"]) -> bool: ...
class AudienceOverlapItem(proto.Message):
    attribute_metadata: AudienceInsightsAttributeMetadata
    potential_youtube_reach_intersection: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, attribute_metadata: AudienceInsightsAttributeMetadata = ..., potential_youtube_reach_intersection: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["attribute_metadata", "potential_youtube_reach_intersection"]) -> bool: ...
class DimensionOverlapResult(proto.Message):
    dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    items: MutableSequence[AudienceOverlapItem]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension = ..., items: MutableSequence[AudienceOverlapItem] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["dimension", "items"]) -> bool: ...
class GenerateAudienceCompositionInsightsRequest(proto.Message):
    customer_id: str
    audience: InsightsAudience
    baseline_audience: InsightsAudience
    data_month: str
    dimensions: MutableSequence[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    customer_insights_group: str
    insights_application_info: AdditionalApplicationInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., audience: InsightsAudience = ..., baseline_audience: InsightsAudience = ..., data_month: str = ..., dimensions: MutableSequence[AudienceInsightsDimensionEnum.AudienceInsightsDimension] = ..., customer_insights_group: str = ..., insights_application_info: AdditionalApplicationInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "audience", "baseline_audience", "data_month", "dimensions", "customer_insights_group", "insights_application_info"]) -> bool: ...
class GenerateAudienceCompositionInsightsResponse(proto.Message):
    sections: MutableSequence[AudienceCompositionSection]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, sections: MutableSequence[AudienceCompositionSection] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["sections"]) -> bool: ...
class GenerateAudienceOverlapInsightsRequest(proto.Message):
    customer_id: str
    country_location: LocationInfo
    primary_attribute: AudienceInsightsAttribute
    dimensions: MutableSequence[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    customer_insights_group: str
    insights_application_info: AdditionalApplicationInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., country_location: LocationInfo = ..., primary_attribute: AudienceInsightsAttribute = ..., dimensions: MutableSequence[AudienceInsightsDimensionEnum.AudienceInsightsDimension] = ..., customer_insights_group: str = ..., insights_application_info: AdditionalApplicationInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "country_location", "primary_attribute", "dimensions", "customer_insights_group", "insights_application_info"]) -> bool: ...
class GenerateAudienceOverlapInsightsResponse(proto.Message):
    primary_attribute_metadata: AudienceInsightsAttributeMetadata
    dimension_results: MutableSequence[DimensionOverlapResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, primary_attribute_metadata: AudienceInsightsAttributeMetadata = ..., dimension_results: MutableSequence[DimensionOverlapResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["primary_attribute_metadata", "dimension_results"]) -> bool: ...
class GenerateInsightsFinderReportRequest(proto.Message):
    customer_id: str
    baseline_audience: InsightsAudience
    specific_audience: InsightsAudience
    customer_insights_group: str
    insights_application_info: AdditionalApplicationInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., baseline_audience: InsightsAudience = ..., specific_audience: InsightsAudience = ..., customer_insights_group: str = ..., insights_application_info: AdditionalApplicationInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "baseline_audience", "specific_audience", "customer_insights_group", "insights_application_info"]) -> bool: ...
class GenerateInsightsFinderReportResponse(proto.Message):
    saved_report_url: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, saved_report_url: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["saved_report_url"]) -> bool: ...
class GenerateSuggestedTargetingInsightsRequest(proto.Message):
    customer_id: str
    customer_insights_group: str
    insights_application_info: AdditionalApplicationInfo
    audience_definition: InsightsAudienceDefinition
    audience_description: InsightsAudienceDescription
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., customer_insights_group: str = ..., insights_application_info: AdditionalApplicationInfo = ..., audience_definition: InsightsAudienceDefinition = ..., audience_description: InsightsAudienceDescription = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "customer_insights_group", "insights_application_info", "audience_definition", "audience_description"]) -> bool: ...
class GenerateSuggestedTargetingInsightsResponse(proto.Message):
    suggestions: MutableSequence[TargetingSuggestionMetrics]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, suggestions: MutableSequence[TargetingSuggestionMetrics] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["suggestions"]) -> bool: ...
class GenerateTargetingSuggestionMetricsRequest(proto.Message):
    customer_id: str
    audiences: MutableSequence[InsightsAudience]
    customer_insights_group: str
    insights_application_info: AdditionalApplicationInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., audiences: MutableSequence[InsightsAudience] = ..., customer_insights_group: str = ..., insights_application_info: AdditionalApplicationInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "audiences", "customer_insights_group", "insights_application_info"]) -> bool: ...
class GenerateTargetingSuggestionMetricsResponse(proto.Message):
    suggestions: MutableSequence[TargetingSuggestionMetrics]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, suggestions: MutableSequence[TargetingSuggestionMetrics] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["suggestions"]) -> bool: ...
class InsightsAudience(proto.Message):
    country_locations: MutableSequence[LocationInfo]
    sub_country_locations: MutableSequence[LocationInfo]
    gender: GenderInfo
    age_ranges: MutableSequence[AgeRangeInfo]
    parental_status: ParentalStatusInfo
    income_ranges: MutableSequence[IncomeRangeInfo]
    lineups: MutableSequence[AudienceInsightsLineup]
    user_list: UserListInfo
    topic_audience_combinations: MutableSequence[InsightsAudienceAttributeGroup]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, country_locations: MutableSequence[LocationInfo] = ..., sub_country_locations: MutableSequence[LocationInfo] = ..., gender: GenderInfo = ..., age_ranges: MutableSequence[AgeRangeInfo] = ..., parental_status: ParentalStatusInfo = ..., income_ranges: MutableSequence[IncomeRangeInfo] = ..., lineups: MutableSequence[AudienceInsightsLineup] = ..., user_list: UserListInfo = ..., topic_audience_combinations: MutableSequence[InsightsAudienceAttributeGroup] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["country_locations", "sub_country_locations", "gender", "age_ranges", "parental_status", "income_ranges", "lineups", "user_list", "topic_audience_combinations"]) -> bool: ...
class InsightsAudienceAttributeGroup(proto.Message):
    attributes: MutableSequence[AudienceInsightsAttribute]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, attributes: MutableSequence[AudienceInsightsAttribute] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["attributes"]) -> bool: ...
class InsightsAudienceDefinition(proto.Message):
    audience: InsightsAudience
    baseline_audience: InsightsAudience
    data_month: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, audience: InsightsAudience = ..., baseline_audience: InsightsAudience = ..., data_month: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["audience", "baseline_audience", "data_month"]) -> bool: ...
class InsightsAudienceDescription(proto.Message):
    country_locations: MutableSequence[LocationInfo]
    audience_description: str
    marketing_objective: AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, country_locations: MutableSequence[LocationInfo] = ..., audience_description: str = ..., marketing_objective: AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["country_locations", "audience_description", "marketing_objective"]) -> bool: ...
class ListAudienceInsightsAttributesRequest(proto.Message):
    customer_id: str
    dimensions: MutableSequence[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    query_text: str
    customer_insights_group: str
    insights_application_info: AdditionalApplicationInfo
    location_country_filters: MutableSequence[LocationInfo]
    youtube_reach_location: LocationInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., dimensions: MutableSequence[AudienceInsightsDimensionEnum.AudienceInsightsDimension] = ..., query_text: str = ..., customer_insights_group: str = ..., insights_application_info: AdditionalApplicationInfo = ..., location_country_filters: MutableSequence[LocationInfo] = ..., youtube_reach_location: LocationInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "dimensions", "query_text", "customer_insights_group", "insights_application_info", "location_country_filters", "youtube_reach_location"]) -> bool: ...
class ListAudienceInsightsAttributesResponse(proto.Message):
    attributes: MutableSequence[AudienceInsightsAttributeMetadata]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, attributes: MutableSequence[AudienceInsightsAttributeMetadata] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["attributes"]) -> bool: ...
class ListInsightsEligibleDatesRequest(proto.Message):
    insights_application_info: AdditionalApplicationInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, insights_application_info: AdditionalApplicationInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["insights_application_info"]) -> bool: ...
class ListInsightsEligibleDatesResponse(proto.Message):
    data_months: MutableSequence[str]
    last_thirty_days: DateRange
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, data_months: MutableSequence[str] = ..., last_thirty_days: DateRange = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["data_months", "last_thirty_days"]) -> bool: ...
class TargetingSuggestionMetrics(proto.Message):
    locations: MutableSequence[AudienceInsightsAttributeMetadata]
    age_ranges: MutableSequence[AgeRangeInfo]
    gender: GenderInfo
    parental_status: ParentalStatusInfo
    user_interests: MutableSequence[AudienceInsightsAttributeMetadataGroup]
    coverage: float
    index: float
    potential_youtube_reach: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, locations: MutableSequence[AudienceInsightsAttributeMetadata] = ..., age_ranges: MutableSequence[AgeRangeInfo] = ..., gender: GenderInfo = ..., parental_status: ParentalStatusInfo = ..., user_interests: MutableSequence[AudienceInsightsAttributeMetadataGroup] = ..., coverage: float = ..., index: float = ..., potential_youtube_reach: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["locations", "age_ranges", "gender", "parental_status", "user_interests", "coverage", "index", "potential_youtube_reach"]) -> bool: ...
