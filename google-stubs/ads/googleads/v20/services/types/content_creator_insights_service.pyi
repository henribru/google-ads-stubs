from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.audience_insights_attribute import AudienceInsightsAttributeMetadata
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.audience_insights_attribute import AudienceInsightsAttributeMetadata
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.audience_insights_attribute import AudienceInsightsAttributeMetadata
from google.ads.googleads.v20.common.types.criteria import YouTubeChannelInfo
from google.ads.googleads.v20.enums.types.insights_trend import InsightsTrendEnum
from google.ads.googleads.v20.common.types.audience_insights_attribute import AudienceInsightsAttributeMetadata
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.audience_insights_attribute import AudienceInsightsEntity
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.audience_insights_attribute import AudienceInsightsAttribute
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.criteria import LocationInfo
from google.ads.googleads.v20.common.types.additional_application_info import AdditionalApplicationInfo
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.criteria import LocationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.criteria import LocationInfo
from google.ads.googleads.v20.common.types.additional_application_info import AdditionalApplicationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.criteria import YouTubeChannelInfo
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.audience_insights_attribute import AudienceInsightsAttribute
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.audience_insights_attribute import AudienceInsightsAttribute
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.audience_insights_attribute import AudienceInsightsAttribute
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class GenerateCreatorInsightsRequest(proto.Message):
    class SearchAttributes(proto.Message):
        audience_attributes: MutableSequence[AudienceInsightsAttribute]
        creator_attributes: MutableSequence[AudienceInsightsAttribute]
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., audience_attributes: MutableSequence[AudienceInsightsAttribute] = ..., creator_attributes: MutableSequence[AudienceInsightsAttribute] = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["audience_attributes", "creator_attributes"]) -> bool: ...
    class SearchBrand(proto.Message):
        brand_entities: MutableSequence[AudienceInsightsAttribute]
        include_related_topics: bool
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., brand_entities: MutableSequence[AudienceInsightsAttribute] = ..., include_related_topics: bool = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["brand_entities", "include_related_topics"]) -> bool: ...
    class YouTubeChannels(proto.Message):
        youtube_channels: MutableSequence[YouTubeChannelInfo]
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., youtube_channels: MutableSequence[YouTubeChannelInfo] = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["youtube_channels"]) -> bool: ...
    customer_id: str
    customer_insights_group: str
    insights_application_info: AdditionalApplicationInfo
    country_locations: MutableSequence[LocationInfo]
    sub_country_locations: MutableSequence[LocationInfo]
    search_attributes: GenerateCreatorInsightsRequest.SearchAttributes
    search_brand: GenerateCreatorInsightsRequest.SearchBrand
    search_channels: GenerateCreatorInsightsRequest.YouTubeChannels
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., customer_insights_group: str = ..., insights_application_info: AdditionalApplicationInfo = ..., country_locations: MutableSequence[LocationInfo] = ..., sub_country_locations: MutableSequence[LocationInfo] = ..., search_attributes: GenerateCreatorInsightsRequest.SearchAttributes = ..., search_brand: GenerateCreatorInsightsRequest.SearchBrand = ..., search_channels: GenerateCreatorInsightsRequest.YouTubeChannels = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "customer_insights_group", "insights_application_info", "country_locations", "sub_country_locations", "search_attributes", "search_brand", "search_channels"]) -> bool: ...
class GenerateCreatorInsightsResponse(proto.Message):
    creator_insights: MutableSequence[YouTubeCreatorInsights]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., creator_insights: MutableSequence[YouTubeCreatorInsights] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["creator_insights"]) -> bool: ...
class GenerateTrendingInsightsRequest(proto.Message):
    customer_id: str
    customer_insights_group: str
    insights_application_info: AdditionalApplicationInfo
    country_location: LocationInfo
    search_audience: SearchAudience
    search_topics: SearchTopics
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., customer_insights_group: str = ..., insights_application_info: AdditionalApplicationInfo = ..., country_location: LocationInfo = ..., search_audience: SearchAudience = ..., search_topics: SearchTopics = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "customer_insights_group", "insights_application_info", "country_location", "search_audience", "search_topics"]) -> bool: ...
class GenerateTrendingInsightsResponse(proto.Message):
    trend_insights: MutableSequence[TrendInsight]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., trend_insights: MutableSequence[TrendInsight] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["trend_insights"]) -> bool: ...
class SearchAudience(proto.Message):
    audience_attributes: MutableSequence[AudienceInsightsAttribute]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., audience_attributes: MutableSequence[AudienceInsightsAttribute] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["audience_attributes"]) -> bool: ...
class SearchTopics(proto.Message):
    entities: MutableSequence[AudienceInsightsEntity]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., entities: MutableSequence[AudienceInsightsEntity] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["entities"]) -> bool: ...
class TrendInsight(proto.Message):
    trend_attribute: AudienceInsightsAttributeMetadata
    trend_metrics: TrendInsightMetrics
    trend: InsightsTrendEnum.InsightsTrend
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., trend_attribute: AudienceInsightsAttributeMetadata = ..., trend_metrics: TrendInsightMetrics = ..., trend: InsightsTrendEnum.InsightsTrend = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["trend_attribute", "trend_metrics", "trend"]) -> bool: ...
class TrendInsightMetrics(proto.Message):
    views_count: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., views_count: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["views_count"]) -> bool: ...
class YouTubeChannelInsights(proto.Message):
    display_name: str
    youtube_channel: YouTubeChannelInfo
    channel_url: str
    channel_description: str
    channel_metrics: YouTubeMetrics
    channel_audience_attributes: MutableSequence[AudienceInsightsAttributeMetadata]
    channel_attributes: MutableSequence[AudienceInsightsAttributeMetadata]
    top_videos: MutableSequence[AudienceInsightsAttributeMetadata]
    channel_type: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., display_name: str = ..., youtube_channel: YouTubeChannelInfo = ..., channel_url: str = ..., channel_description: str = ..., channel_metrics: YouTubeMetrics = ..., channel_audience_attributes: MutableSequence[AudienceInsightsAttributeMetadata] = ..., channel_attributes: MutableSequence[AudienceInsightsAttributeMetadata] = ..., top_videos: MutableSequence[AudienceInsightsAttributeMetadata] = ..., channel_type: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["display_name", "youtube_channel", "channel_url", "channel_description", "channel_metrics", "channel_audience_attributes", "channel_attributes", "top_videos", "channel_type"]) -> bool: ...
class YouTubeCreatorInsights(proto.Message):
    creator_name: str
    creator_channels: MutableSequence[YouTubeChannelInsights]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., creator_name: str = ..., creator_channels: MutableSequence[YouTubeChannelInsights] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["creator_name", "creator_channels"]) -> bool: ...
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., subscriber_count: int = ..., views_count: int = ..., video_count: int = ..., likes_count: int = ..., shares_count: int = ..., comments_count: int = ..., engagement_rate: float = ..., average_views_per_video: float = ..., average_likes_per_video: float = ..., average_shares_per_video: float = ..., average_comments_per_video: float = ..., shorts_views_count: int = ..., shorts_video_count: int = ..., is_active_shorts_creator: bool = ..., is_brand_connect_creator: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["subscriber_count", "views_count", "video_count", "likes_count", "shares_count", "comments_count", "engagement_rate", "average_views_per_video", "average_likes_per_video", "average_shares_per_video", "average_comments_per_video", "shorts_views_count", "shorts_video_count", "is_active_shorts_creator", "is_brand_connect_creator"]) -> bool: ...
