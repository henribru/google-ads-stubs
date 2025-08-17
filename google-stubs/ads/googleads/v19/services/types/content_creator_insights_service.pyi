from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v19.common.types.audience_insights_attribute import (
    AudienceInsightsAttribute,
    AudienceInsightsAttributeMetadata,
    AudienceInsightsEntity,
)
from google.ads.googleads.v19.common.types.criteria import (
    LocationInfo,
    YouTubeChannelInfo,
)
from google.ads.googleads.v19.enums.types.insights_trend import InsightsTrendEnum

_M = TypeVar("_M")

class GenerateCreatorInsightsRequest(proto.Message):
    class SearchAttributes(proto.Message):
        audience_attributes: MutableSequence[AudienceInsightsAttribute]
        creator_attributes: MutableSequence[AudienceInsightsAttribute]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            audience_attributes: MutableSequence[AudienceInsightsAttribute] = ...,
            creator_attributes: MutableSequence[AudienceInsightsAttribute] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["audience_attributes", "creator_attributes"]
        ) -> bool: ...

    class SearchBrand(proto.Message):
        brand_entities: MutableSequence[AudienceInsightsAttribute]
        include_related_topics: bool
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            brand_entities: MutableSequence[AudienceInsightsAttribute] = ...,
            include_related_topics: bool = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["brand_entities", "include_related_topics"]
        ) -> bool: ...

    class YouTubeChannels(proto.Message):
        youtube_channels: MutableSequence[YouTubeChannelInfo]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            youtube_channels: MutableSequence[YouTubeChannelInfo] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["youtube_channels"]
        ) -> bool: ...

    customer_id: str
    customer_insights_group: str
    country_locations: MutableSequence[LocationInfo]
    search_attributes: GenerateCreatorInsightsRequest.SearchAttributes
    search_brand: GenerateCreatorInsightsRequest.SearchBrand
    search_channels: GenerateCreatorInsightsRequest.YouTubeChannels
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        customer_insights_group: str = ...,
        country_locations: MutableSequence[LocationInfo] = ...,
        search_attributes: GenerateCreatorInsightsRequest.SearchAttributes = ...,
        search_brand: GenerateCreatorInsightsRequest.SearchBrand = ...,
        search_channels: GenerateCreatorInsightsRequest.YouTubeChannels = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "customer_insights_group",
            "country_locations",
            "search_attributes",
            "search_brand",
            "search_channels",
        ],
    ) -> bool: ...

class GenerateCreatorInsightsResponse(proto.Message):
    creator_insights: MutableSequence[YouTubeCreatorInsights]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        creator_insights: MutableSequence[YouTubeCreatorInsights] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["creator_insights"]
    ) -> bool: ...

class GenerateTrendingInsightsRequest(proto.Message):
    customer_id: str
    customer_insights_group: str
    country_location: LocationInfo
    search_audience: SearchAudience
    search_topics: SearchTopics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        customer_insights_group: str = ...,
        country_location: LocationInfo = ...,
        search_audience: SearchAudience = ...,
        search_topics: SearchTopics = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "customer_insights_group",
            "country_location",
            "search_audience",
            "search_topics",
        ],
    ) -> bool: ...

class GenerateTrendingInsightsResponse(proto.Message):
    trend_insights: MutableSequence[TrendInsight]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        trend_insights: MutableSequence[TrendInsight] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["trend_insights"]
    ) -> bool: ...

class SearchAudience(proto.Message):
    audience_attributes: MutableSequence[AudienceInsightsAttribute]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        audience_attributes: MutableSequence[AudienceInsightsAttribute] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["audience_attributes"]
    ) -> bool: ...

class SearchTopics(proto.Message):
    entities: MutableSequence[AudienceInsightsEntity]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        entities: MutableSequence[AudienceInsightsEntity] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["entities"]
    ) -> bool: ...

class TrendInsight(proto.Message):
    trend_attribute: AudienceInsightsAttributeMetadata
    trend_metrics: TrendInsightMetrics
    trend: InsightsTrendEnum.InsightsTrend
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        trend_attribute: AudienceInsightsAttributeMetadata = ...,
        trend_metrics: TrendInsightMetrics = ...,
        trend: InsightsTrendEnum.InsightsTrend = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["trend_attribute", "trend_metrics", "trend"]
    ) -> bool: ...

class TrendInsightMetrics(proto.Message):
    views_count: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        views_count: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["views_count"]
    ) -> bool: ...

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        display_name: str = ...,
        youtube_channel: YouTubeChannelInfo = ...,
        channel_url: str = ...,
        channel_description: str = ...,
        channel_metrics: YouTubeMetrics = ...,
        channel_audience_attributes: MutableSequence[
            AudienceInsightsAttributeMetadata
        ] = ...,
        channel_attributes: MutableSequence[AudienceInsightsAttributeMetadata] = ...,
        top_videos: MutableSequence[AudienceInsightsAttributeMetadata] = ...,
        channel_type: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "display_name",
            "youtube_channel",
            "channel_url",
            "channel_description",
            "channel_metrics",
            "channel_audience_attributes",
            "channel_attributes",
            "top_videos",
            "channel_type",
        ],
    ) -> bool: ...

class YouTubeCreatorInsights(proto.Message):
    creator_name: str
    creator_channels: MutableSequence[YouTubeChannelInsights]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        creator_name: str = ...,
        creator_channels: MutableSequence[YouTubeChannelInsights] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["creator_name", "creator_channels"]
    ) -> bool: ...

class YouTubeMetrics(proto.Message):
    subscriber_count: int
    views_count: int
    video_count: int
    is_active_shorts_creator: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        subscriber_count: int = ...,
        views_count: int = ...,
        video_count: int = ...,
        is_active_shorts_creator: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "subscriber_count", "views_count", "video_count", "is_active_shorts_creator"
        ],
    ) -> bool: ...
