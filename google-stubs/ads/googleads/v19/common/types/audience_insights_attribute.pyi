import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import criteria
from google.ads.googleads.v19.enums.types import audience_insights_dimension, insights_knowledge_graph_entity_capabilities
from typing import MutableSequence

__protobuf__: Incomplete

class AudienceInsightsAttributeMetadata(proto.Message):
    dimension: audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
    attribute: AudienceInsightsAttribute
    display_name: str
    display_info: str
    potential_youtube_reach: int
    subscriber_share: float
    viewer_share: float
    youtube_channel_metadata: YouTubeChannelAttributeMetadata
    youtube_video_metadata: YouTubeVideoAttributeMetadata
    dynamic_attribute_metadata: DynamicLineupAttributeMetadata
    location_attribute_metadata: LocationAttributeMetadata
    user_interest_attribute_metadata: UserInterestAttributeMetadata
    knowledge_graph_attribute_metadata: KnowledgeGraphAttributeMetadata

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
    youtube_video: criteria.YouTubeVideoInfo

class AudienceInsightsTopic(proto.Message):
    entity: AudienceInsightsEntity
    category: AudienceInsightsCategory

class AudienceInsightsEntity(proto.Message):
    knowledge_graph_machine_id: str

class AudienceInsightsCategory(proto.Message):
    category_id: str

class AudienceInsightsDynamicLineup(proto.Message):
    dynamic_lineup_id: str

class YouTubeChannelAttributeMetadata(proto.Message):
    subscriber_count: int

class YouTubeVideoAttributeMetadata(proto.Message):
    thumbnail_url: str
    video_url: str

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

class KnowledgeGraphAttributeMetadata(proto.Message):
    entity_capabilities: MutableSequence[insights_knowledge_graph_entity_capabilities.InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities]
