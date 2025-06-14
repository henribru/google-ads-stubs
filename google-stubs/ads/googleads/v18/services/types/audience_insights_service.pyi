import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import criteria, dates
from google.ads.googleads.v18.enums.types import audience_insights_dimension, audience_insights_marketing_objective
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
    locations: MutableSequence['AudienceInsightsAttributeMetadata']
    age_ranges: MutableSequence[criteria.AgeRangeInfo]
    gender: criteria.GenderInfo
    parental_status: criteria.ParentalStatusInfo
    user_interests: MutableSequence['AudienceInsightsAttributeMetadata']
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
    attributes: MutableSequence['AudienceInsightsAttributeMetadata']

class ListInsightsEligibleDatesRequest(proto.Message): ...

class ListInsightsEligibleDatesResponse(proto.Message):
    data_months: MutableSequence[str]
    last_thirty_days: dates.DateRange

class GenerateAudienceOverlapInsightsRequest(proto.Message):
    customer_id: str
    country_location: criteria.LocationInfo
    primary_attribute: AudienceInsightsAttribute
    dimensions: MutableSequence[audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    customer_insights_group: str

class GenerateAudienceOverlapInsightsResponse(proto.Message):
    primary_attribute_metadata: AudienceInsightsAttributeMetadata
    dimension_results: MutableSequence['DimensionOverlapResult']

class DimensionOverlapResult(proto.Message):
    dimension: audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
    items: MutableSequence['AudienceOverlapItem']

class AudienceOverlapItem(proto.Message):
    attribute_metadata: AudienceInsightsAttributeMetadata
    potential_youtube_reach_intersection: int

class GenerateTargetingSuggestionMetricsRequest(proto.Message):
    customer_id: str
    audiences: MutableSequence['BasicInsightsAudience']
    customer_insights_group: str

class GenerateTargetingSuggestionMetricsResponse(proto.Message):
    suggestions: MutableSequence['TargetingSuggestionMetrics']

class AudienceInsightsAttribute(proto.Message):
    age_range: criteria.AgeRangeInfo
    gender: criteria.GenderInfo
    location: criteria.LocationInfo
    user_interest: criteria.UserInterestInfo
    entity: AudienceInsightsEntity
    category: AudienceInsightsCategory
    dynamic_lineup: AudienceInsightsDynamicLineup
    parental_status: criteria.ParentalStatusInfo
    income_range: criteria.IncomeRangeInfo
    youtube_channel: criteria.YouTubeChannelInfo

class AudienceInsightsTopic(proto.Message):
    entity: AudienceInsightsEntity
    category: AudienceInsightsCategory

class AudienceInsightsEntity(proto.Message):
    knowledge_graph_machine_id: str

class AudienceInsightsCategory(proto.Message):
    category_id: str

class AudienceInsightsDynamicLineup(proto.Message):
    dynamic_lineup_id: str

class BasicInsightsAudience(proto.Message):
    country_location: MutableSequence[criteria.LocationInfo]
    sub_country_locations: MutableSequence[criteria.LocationInfo]
    gender: criteria.GenderInfo
    age_ranges: MutableSequence[criteria.AgeRangeInfo]
    user_interests: MutableSequence[criteria.UserInterestInfo]
    topics: MutableSequence['AudienceInsightsTopic']

class AudienceInsightsAttributeMetadata(proto.Message):
    dimension: audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
    attribute: AudienceInsightsAttribute
    display_name: str
    display_info: str
    potential_youtube_reach: int
    youtube_channel_metadata: YouTubeChannelAttributeMetadata
    dynamic_attribute_metadata: DynamicLineupAttributeMetadata
    location_attribute_metadata: LocationAttributeMetadata
    user_interest_attribute_metadata: UserInterestAttributeMetadata

class YouTubeChannelAttributeMetadata(proto.Message):
    subscriber_count: int

class DynamicLineupAttributeMetadata(proto.Message):
    class SampleChannel(proto.Message):
        youtube_channel: criteria.YouTubeChannelInfo
        display_name: str
        youtube_channel_metadata: YouTubeChannelAttributeMetadata
    inventory_country: criteria.LocationInfo
    median_monthly_inventory: int
    channel_count_lower_bound: int
    channel_count_upper_bound: int
    sample_channels: MutableSequence[SampleChannel]

class LocationAttributeMetadata(proto.Message):
    country_location: criteria.LocationInfo

class UserInterestAttributeMetadata(proto.Message):
    user_interest_description: str

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
    dynamic_lineups: MutableSequence['AudienceInsightsDynamicLineup']
    topic_audience_combinations: MutableSequence['InsightsAudienceAttributeGroup']

class InsightsAudienceAttributeGroup(proto.Message):
    attributes: MutableSequence['AudienceInsightsAttribute']

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
    attribute_metadata: AudienceInsightsAttributeMetadata
    metrics: AudienceCompositionMetrics
