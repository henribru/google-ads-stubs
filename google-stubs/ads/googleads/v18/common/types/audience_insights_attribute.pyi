import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import criteria
from google.ads.googleads.v18.enums.types import audience_insights_dimension
from typing import MutableSequence

__protobuf__: Incomplete

class AudienceInsightsAttributeMetadata(proto.Message):
    dimension: audience_insights_dimension.AudienceInsightsDimensionEnum.AudienceInsightsDimension
    attribute: AudienceInsightsAttribute
    display_name: str
    display_info: str
    potential_youtube_reach: int
    subscriber_share: float
    youtube_channel_metadata: YouTubeChannelAttributeMetadata
    dynamic_attribute_metadata: DynamicLineupAttributeMetadata
    location_attribute_metadata: LocationAttributeMetadata

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

class AudienceInsightsEntity(proto.Message):
    knowledge_graph_machine_id: str

class AudienceInsightsCategory(proto.Message):
    category_id: str

class AudienceInsightsDynamicLineup(proto.Message):
    dynamic_lineup_id: str

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
