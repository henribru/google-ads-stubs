import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import audience_insights_attribute, criteria
from typing import MutableSequence

__protobuf__: Incomplete

class GenerateCreatorInsightsRequest(proto.Message):
    class SearchAttributes(proto.Message):
        audience_attributes: MutableSequence[audience_insights_attribute.AudienceInsightsAttribute]
        creator_attributes: MutableSequence[audience_insights_attribute.AudienceInsightsAttribute]
    class YouTubeChannels(proto.Message):
        youtube_channels: MutableSequence[criteria.YouTubeChannelInfo]
    customer_id: str
    customer_insights_group: str
    search_attributes: SearchAttributes
    search_channels: YouTubeChannels

class GenerateCreatorInsightsResponse(proto.Message):
    creator_insights: MutableSequence['YouTubeCreatorInsights']

class YouTubeCreatorInsights(proto.Message):
    creator_name: str
    creator_channels: MutableSequence['YouTubeChannelInsights']

class YouTubeMetrics(proto.Message):
    subscriber_count: int
    views_count: int

class YouTubeChannelInsights(proto.Message):
    display_name: str
    youtube_channel: criteria.YouTubeChannelInfo
    channel_metrics: YouTubeMetrics
    channel_audience_demographics: MutableSequence[audience_insights_attribute.AudienceInsightsAttributeMetadata]
    channel_attributes: MutableSequence[audience_insights_attribute.AudienceInsightsAttributeMetadata]
    channel_type: str
