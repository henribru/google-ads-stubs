import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import additional_application_info, audience_insights_attribute, criteria
from google.ads.googleads.v20.enums.types import insights_trend
from typing import MutableSequence

__protobuf__: Incomplete

class GenerateCreatorInsightsRequest(proto.Message):
    class SearchAttributes(proto.Message):
        audience_attributes: MutableSequence[audience_insights_attribute.AudienceInsightsAttribute]
        creator_attributes: MutableSequence[audience_insights_attribute.AudienceInsightsAttribute]
    class SearchBrand(proto.Message):
        brand_entities: MutableSequence[audience_insights_attribute.AudienceInsightsAttribute]
        include_related_topics: bool
    class YouTubeChannels(proto.Message):
        youtube_channels: MutableSequence[criteria.YouTubeChannelInfo]
    customer_id: str
    customer_insights_group: str
    insights_application_info: additional_application_info.AdditionalApplicationInfo
    country_locations: MutableSequence[criteria.LocationInfo]
    sub_country_locations: MutableSequence[criteria.LocationInfo]
    search_attributes: SearchAttributes
    search_brand: SearchBrand
    search_channels: YouTubeChannels

class GenerateCreatorInsightsResponse(proto.Message):
    creator_insights: MutableSequence['YouTubeCreatorInsights']

class GenerateTrendingInsightsRequest(proto.Message):
    customer_id: str
    customer_insights_group: str
    insights_application_info: additional_application_info.AdditionalApplicationInfo
    country_location: criteria.LocationInfo
    search_audience: SearchAudience
    search_topics: SearchTopics

class GenerateTrendingInsightsResponse(proto.Message):
    trend_insights: MutableSequence['TrendInsight']

class YouTubeCreatorInsights(proto.Message):
    creator_name: str
    creator_channels: MutableSequence['YouTubeChannelInsights']

class YouTubeMetrics(proto.Message):
    subscriber_count: int
    views_count: int
    video_count: int
    likes_count: int
    shares_count: int
    comments_count: int
    engagement_rate: float
    average_views_per_video: float
    average_likes_per_video: float
    average_shares_per_video: float
    average_comments_per_video: float
    shorts_views_count: int
    shorts_video_count: int
    is_active_shorts_creator: bool
    is_brand_connect_creator: bool

class YouTubeChannelInsights(proto.Message):
    display_name: str
    youtube_channel: criteria.YouTubeChannelInfo
    channel_url: str
    channel_description: str
    channel_metrics: YouTubeMetrics
    channel_audience_attributes: MutableSequence[audience_insights_attribute.AudienceInsightsAttributeMetadata]
    channel_attributes: MutableSequence[audience_insights_attribute.AudienceInsightsAttributeMetadata]
    top_videos: MutableSequence[audience_insights_attribute.AudienceInsightsAttributeMetadata]
    channel_type: str

class SearchAudience(proto.Message):
    audience_attributes: MutableSequence[audience_insights_attribute.AudienceInsightsAttribute]

class SearchTopics(proto.Message):
    entities: MutableSequence[audience_insights_attribute.AudienceInsightsEntity]

class TrendInsight(proto.Message):
    trend_attribute: audience_insights_attribute.AudienceInsightsAttributeMetadata
    trend_metrics: TrendInsightMetrics
    trend: insights_trend.InsightsTrendEnum.InsightsTrend

class TrendInsightMetrics(proto.Message):
    views_count: int
