import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import criteria as criteria
from google.ads.googleads.v11.enums.types import (
    audience_insights_dimension as audience_insights_dimension,
)

__protobuf__: Incomplete

class GenerateInsightsFinderReportRequest(proto.Message):
    customer_id: Incomplete
    baseline_audience: Incomplete
    specific_audience: Incomplete
    customer_insights_group: Incomplete

class GenerateInsightsFinderReportResponse(proto.Message):
    saved_report_url: Incomplete

class GenerateAudienceCompositionInsightsRequest(proto.Message):
    customer_id: Incomplete
    audience: Incomplete
    data_month: Incomplete
    dimensions: Incomplete
    customer_insights_group: Incomplete

class GenerateAudienceCompositionInsightsResponse(proto.Message):
    sections: Incomplete

class ListAudienceInsightsAttributesRequest(proto.Message):
    customer_id: Incomplete
    dimensions: Incomplete
    query_text: Incomplete
    customer_insights_group: Incomplete

class ListAudienceInsightsAttributesResponse(proto.Message):
    attributes: Incomplete

class AudienceInsightsAttribute(proto.Message):
    age_range: Incomplete
    gender: Incomplete
    location: Incomplete
    user_interest: Incomplete
    entity: Incomplete
    category: Incomplete
    dynamic_lineup: Incomplete
    parental_status: Incomplete
    income_range: Incomplete
    youtube_channel: Incomplete

class AudienceInsightsTopic(proto.Message):
    entity: Incomplete
    category: Incomplete

class AudienceInsightsEntity(proto.Message):
    knowledge_graph_machine_id: Incomplete

class AudienceInsightsCategory(proto.Message):
    category_id: Incomplete

class AudienceInsightsDynamicLineup(proto.Message):
    dynamic_lineup_id: Incomplete

class BasicInsightsAudience(proto.Message):
    country_location: Incomplete
    sub_country_locations: Incomplete
    gender: Incomplete
    age_ranges: Incomplete
    user_interests: Incomplete
    topics: Incomplete

class AudienceInsightsAttributeMetadata(proto.Message):
    dimension: Incomplete
    attribute: Incomplete
    display_name: Incomplete
    score: Incomplete
    display_info: Incomplete
    youtube_channel_metadata: Incomplete
    dynamic_attribute_metadata: Incomplete

class YouTubeChannelAttributeMetadata(proto.Message):
    subscriber_count: Incomplete

class DynamicLineupAttributeMetadata(proto.Message):
    inventory_country: Incomplete
    median_monthly_inventory: Incomplete
    channel_count_lower_bound: Incomplete
    channel_count_upper_bound: Incomplete

class InsightsAudience(proto.Message):
    country_locations: Incomplete
    sub_country_locations: Incomplete
    gender: Incomplete
    age_ranges: Incomplete
    parental_status: Incomplete
    income_ranges: Incomplete
    dynamic_lineups: Incomplete
    topic_audience_combinations: Incomplete

class InsightsAudienceAttributeGroup(proto.Message):
    attributes: Incomplete

class AudienceCompositionSection(proto.Message):
    dimension: Incomplete
    top_attributes: Incomplete
    clustered_attributes: Incomplete

class AudienceCompositionAttributeCluster(proto.Message):
    cluster_display_name: Incomplete
    cluster_metrics: Incomplete
    attributes: Incomplete

class AudienceCompositionMetrics(proto.Message):
    baseline_audience_share: Incomplete
    audience_share: Incomplete
    index: Incomplete
    score: Incomplete

class AudienceCompositionAttribute(proto.Message):
    attribute_metadata: Incomplete
    metrics: Incomplete
