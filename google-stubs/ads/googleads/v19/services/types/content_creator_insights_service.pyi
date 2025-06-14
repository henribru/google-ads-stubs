import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import audience_insights_attribute, criteria
from google.ads.googleads.v19.enums.types import insights_trend
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
    country_locations: MutableSequence[criteria.LocationInfo]
    search_attributes: SearchAttributes
    search_brand: SearchBrand
    search_channels: YouTubeChannels

class GenerateCreatorInsightsResponse(proto.Message):
    creator_insights: MutableSequence['YouTubeCreatorInsights']

class GenerateTrendingInsightsRequest(proto.Message):
    customer_id: str
    customer_insights_group: str
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
    is_active_shorts_creator: bool

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
