import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import audience_insights_attribute, criteria, dates
from google.ads.googleads.v19.enums.types import audience_insights_dimension, audience_insights_marketing_objective
from typing import MutableSequence

__protobuf__: Incomplete

class GenerateInsightsFinderReportRequest(proto.Message):
    customer_id: str
    baseline_audience: BasicInsightsAudience
    specific_audience: BasicInsightsAudience
    customer_insights_group: str

class GenerateInsightsFinderReportResponse(proto.Message):
    saved_report_url: str

class GenerateAudienceCompositionInsightsRequest(proto.Message):
    customer_id: str
    audience: InsightsAudience
    baseline_audience: InsightsAudience
    data_month: str
    dimensions: MutableSequence[audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    customer_insights_group: str

class GenerateAudienceCompositionInsightsResponse(proto.Message):
    sections: MutableSequence['AudienceCompositionSection']

class GenerateSuggestedTargetingInsightsRequest(proto.Message):
    customer_id: str
    customer_insights_group: str
    audience_definition: InsightsAudienceDefinition
    audience_description: InsightsAudienceDescription

class GenerateSuggestedTargetingInsightsResponse(proto.Message):
    suggestions: MutableSequence['TargetingSuggestionMetrics']

class TargetingSuggestionMetrics(proto.Message):
    locations: MutableSequence[audience_insights_attribute.AudienceInsightsAttributeMetadata]
    age_ranges: MutableSequence[criteria.AgeRangeInfo]
    gender: criteria.GenderInfo
    parental_status: criteria.ParentalStatusInfo
    user_interests: MutableSequence[audience_insights_attribute.AudienceInsightsAttributeMetadata]
    coverage: float
    index: float
    potential_youtube_reach: int

class ListAudienceInsightsAttributesRequest(proto.Message):
    customer_id: str
    dimensions: MutableSequence[audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    query_text: str
    customer_insights_group: str
    location_country_filters: MutableSequence[criteria.LocationInfo]
    youtube_reach_location: criteria.LocationInfo

class ListAudienceInsightsAttributesResponse(proto.Message):
    attributes: MutableSequence[audience_insights_attribute.AudienceInsightsAttributeMetadata]

class ListInsightsEligibleDatesRequest(proto.Message): ...

class ListInsightsEligibleDatesResponse(proto.Message):
    data_months: MutableSequence[str]
    last_thirty_days: dates.DateRange

class GenerateAudienceOverlapInsightsRequest(proto.Message):
    customer_id: str
    country_location: criteria.LocationInfo
    primary_attribute: audience_insights_attribute.AudienceInsightsAttribute
    dimensions: MutableSequence[audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    customer_insights_group: str

class GenerateAudienceOverlapInsightsResponse(proto.Message):
    primary_attribute_metadata: audience_insights_attribute.AudienceInsightsAttributeMetadata
    dimension_results: MutableSequence['DimensionOverlapResult']

class DimensionOverlapResult(proto.Message):
    dimension: audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
    items: MutableSequence['AudienceOverlapItem']

class AudienceOverlapItem(proto.Message):
    attribute_metadata: audience_insights_attribute.AudienceInsightsAttributeMetadata
    potential_youtube_reach_intersection: int

class GenerateTargetingSuggestionMetricsRequest(proto.Message):
    customer_id: str
    audiences: MutableSequence['BasicInsightsAudience']
    customer_insights_group: str

class GenerateTargetingSuggestionMetricsResponse(proto.Message):
    suggestions: MutableSequence['TargetingSuggestionMetrics']

class BasicInsightsAudience(proto.Message):
    country_location: MutableSequence[criteria.LocationInfo]
    sub_country_locations: MutableSequence[criteria.LocationInfo]
    gender: criteria.GenderInfo
    age_ranges: MutableSequence[criteria.AgeRangeInfo]
    user_interests: MutableSequence[criteria.UserInterestInfo]
    topics: MutableSequence[audience_insights_attribute.AudienceInsightsTopic]

class InsightsAudienceDefinition(proto.Message):
    audience: InsightsAudience
    baseline_audience: InsightsAudience
    data_month: str

class InsightsAudienceDescription(proto.Message):
    country_locations: MutableSequence[criteria.LocationInfo]
    audience_description: str
    marketing_objective: audience_insights_marketing_objective.AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective

class InsightsAudience(proto.Message):
    country_locations: MutableSequence[criteria.LocationInfo]
    sub_country_locations: MutableSequence[criteria.LocationInfo]
    gender: criteria.GenderInfo
    age_ranges: MutableSequence[criteria.AgeRangeInfo]
    parental_status: criteria.ParentalStatusInfo
    income_ranges: MutableSequence[criteria.IncomeRangeInfo]
    dynamic_lineups: MutableSequence[audience_insights_attribute.AudienceInsightsDynamicLineup]
    topic_audience_combinations: MutableSequence['InsightsAudienceAttributeGroup']

class InsightsAudienceAttributeGroup(proto.Message):
    attributes: MutableSequence[audience_insights_attribute.AudienceInsightsAttribute]

class AudienceCompositionSection(proto.Message):
    dimension: audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
    top_attributes: MutableSequence['AudienceCompositionAttribute']
    clustered_attributes: MutableSequence['AudienceCompositionAttributeCluster']

class AudienceCompositionAttributeCluster(proto.Message):
    cluster_display_name: str
    cluster_metrics: AudienceCompositionMetrics
    attributes: MutableSequence['AudienceCompositionAttribute']

class AudienceCompositionMetrics(proto.Message):
    baseline_audience_share: float
    audience_share: float
    index: float
    score: float

class AudienceCompositionAttribute(proto.Message):
    attribute_metadata: audience_insights_attribute.AudienceInsightsAttributeMetadata
    metrics: AudienceCompositionMetrics
