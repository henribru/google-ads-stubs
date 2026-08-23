from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v25.common.types.additional_application_info import (
    AdditionalApplicationInfo,
)
from google.ads.googleads.v25.common.types.audience_insights_attribute import (
    AudienceInsightsAttribute,
    AudienceInsightsAttributeMetadata,
    AudienceInsightsEntity,
    InsightsAudienceAttributeGroup,
)
from google.ads.googleads.v25.common.types.criteria import (
    LocationInfo,
    YouTubeChannelInfo,
)
from google.ads.googleads.v25.enums.types.content_creator_insights_supplemental_data import (
    ContentCreatorInsightsSupplementalDataEnum,
)
from google.ads.googleads.v25.enums.types.insights_trend import InsightsTrendEnum
from google.ads.googleads.v25.enums.types.partnership_opportunity import (
    PartnershipOpportunityEnum,
)
from google.ads.googleads.v25.enums.types.sentiment import SentimentEnum

_M = TypeVar("_M")

class BrandSentimentInsight(proto.Message):
    month: str
    has_insufficient_data: bool
    sentiment_distributions: MutableSequence[SentimentInsightDistribution]
    sentiment_summaries: MutableSequence[SentimentInsightSummary]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        month: str = ...,
        has_insufficient_data: bool = ...,
        sentiment_distributions: MutableSequence[SentimentInsightDistribution] = ...,
        sentiment_summaries: MutableSequence[SentimentInsightSummary] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "month",
            "has_insufficient_data",
            "sentiment_distributions",
            "sentiment_summaries",
        ],
    ) -> bool: ...

class GenerateCreatorInsightsRequest(proto.Message):
    class SearchAttributes(proto.Message):
        audience_attributes: MutableSequence[AudienceInsightsAttribute]
        audience_combinations: MutableSequence[InsightsAudienceAttributeGroup]
        creator_attributes: MutableSequence[AudienceInsightsAttribute]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            audience_attributes: MutableSequence[AudienceInsightsAttribute] = ...,
            audience_combinations: MutableSequence[
                InsightsAudienceAttributeGroup
            ] = ...,
            creator_attributes: MutableSequence[AudienceInsightsAttribute] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "audience_attributes", "audience_combinations", "creator_attributes"
            ],
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
    insights_application_info: AdditionalApplicationInfo
    country_locations: MutableSequence[LocationInfo]
    sub_country_locations: MutableSequence[LocationInfo]
    supplemental_data: MutableSequence[
        ContentCreatorInsightsSupplementalDataEnum.ContentCreatorInsightsSupplementalData
    ]
    search_attributes: GenerateCreatorInsightsRequest.SearchAttributes
    search_channels: GenerateCreatorInsightsRequest.YouTubeChannels
    search_topics: SearchTopics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        customer_insights_group: str = ...,
        insights_application_info: AdditionalApplicationInfo = ...,
        country_locations: MutableSequence[LocationInfo] = ...,
        sub_country_locations: MutableSequence[LocationInfo] = ...,
        supplemental_data: MutableSequence[
            ContentCreatorInsightsSupplementalDataEnum.ContentCreatorInsightsSupplementalData
        ] = ...,
        search_attributes: GenerateCreatorInsightsRequest.SearchAttributes = ...,
        search_channels: GenerateCreatorInsightsRequest.YouTubeChannels = ...,
        search_topics: SearchTopics = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "customer_insights_group",
            "insights_application_info",
            "country_locations",
            "sub_country_locations",
            "supplemental_data",
            "search_attributes",
            "search_channels",
            "search_topics",
        ],
    ) -> bool: ...

class GenerateCreatorInsightsResponse(proto.Message):
    creator_insights: MutableSequence[YouTubeCreatorInsights]
    local_creator_insights: MutableSequence[YouTubeCreatorInsights]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        creator_insights: MutableSequence[YouTubeCreatorInsights] = ...,
        local_creator_insights: MutableSequence[YouTubeCreatorInsights] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["creator_insights", "local_creator_insights"]
    ) -> bool: ...

class GenerateTrendingInsightsRequest(proto.Message):
    customer_id: str
    customer_insights_group: str
    insights_application_info: AdditionalApplicationInfo
    country_location: LocationInfo
    sub_country_locations: MutableSequence[LocationInfo]
    supplemental_data: MutableSequence[
        ContentCreatorInsightsSupplementalDataEnum.ContentCreatorInsightsSupplementalData
    ]
    search_audience: SearchAudience
    search_topics: SearchTopics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        customer_insights_group: str = ...,
        insights_application_info: AdditionalApplicationInfo = ...,
        country_location: LocationInfo = ...,
        sub_country_locations: MutableSequence[LocationInfo] = ...,
        supplemental_data: MutableSequence[
            ContentCreatorInsightsSupplementalDataEnum.ContentCreatorInsightsSupplementalData
        ] = ...,
        search_audience: SearchAudience = ...,
        search_topics: SearchTopics = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "customer_insights_group",
            "insights_application_info",
            "country_location",
            "sub_country_locations",
            "supplemental_data",
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

class LanguageDistribution(proto.Message):
    language_code: str
    proportion: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        language_code: str = ...,
        proportion: float = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["language_code", "proportion"]
    ) -> bool: ...

class SearchAudience(proto.Message):
    audience_attributes: MutableSequence[AudienceInsightsAttribute]
    audience_combinations: MutableSequence[InsightsAudienceAttributeGroup]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        audience_attributes: MutableSequence[AudienceInsightsAttribute] = ...,
        audience_combinations: MutableSequence[InsightsAudienceAttributeGroup] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["audience_attributes", "audience_combinations"]
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

class SentimentInsightDistribution(proto.Message):
    sentiment: SentimentEnum.Sentiment
    sentiment_share: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        sentiment: SentimentEnum.Sentiment = ...,
        sentiment_share: float = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["sentiment", "sentiment_share"]
    ) -> bool: ...

class SentimentInsightSummary(proto.Message):
    sentiment: SentimentEnum.Sentiment
    summary: str
    sample_videos: MutableSequence[AudienceInsightsAttributeMetadata]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        sentiment: SentimentEnum.Sentiment = ...,
        summary: str = ...,
        sample_videos: MutableSequence[AudienceInsightsAttributeMetadata] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["sentiment", "summary", "sample_videos"]
    ) -> bool: ...

class TrendInsight(proto.Message):
    trend_attribute: AudienceInsightsAttributeMetadata
    trend_metrics: TrendInsightMetrics
    trend: InsightsTrendEnum.InsightsTrend
    trend_data_points: MutableSequence[TrendInsightDataPoint]
    brand_sentiment_insights: MutableSequence[BrandSentimentInsight]
    related_videos: MutableSequence[AudienceInsightsAttributeMetadata]
    related_creators: MutableSequence[YouTubeCreatorInsights]
    related_local_creators: MutableSequence[YouTubeCreatorInsights]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        trend_attribute: AudienceInsightsAttributeMetadata = ...,
        trend_metrics: TrendInsightMetrics = ...,
        trend: InsightsTrendEnum.InsightsTrend = ...,
        trend_data_points: MutableSequence[TrendInsightDataPoint] = ...,
        brand_sentiment_insights: MutableSequence[BrandSentimentInsight] = ...,
        related_videos: MutableSequence[AudienceInsightsAttributeMetadata] = ...,
        related_creators: MutableSequence[YouTubeCreatorInsights] = ...,
        related_local_creators: MutableSequence[YouTubeCreatorInsights] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "trend_attribute",
            "trend_metrics",
            "trend",
            "trend_data_points",
            "brand_sentiment_insights",
            "related_videos",
            "related_creators",
            "related_local_creators",
        ],
    ) -> bool: ...

class TrendInsightDataPoint(proto.Message):
    month: str
    trend_metrics: TrendInsightMetrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        month: str = ...,
        trend_metrics: TrendInsightMetrics = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["month", "trend_metrics"]
    ) -> bool: ...

class TrendInsightMetrics(proto.Message):
    views_count: int
    views_indexed_value: int
    audience_share: float
    trend_change_percent: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        views_count: int = ...,
        views_indexed_value: int = ...,
        audience_share: float = ...,
        trend_change_percent: float = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "views_count",
            "views_indexed_value",
            "audience_share",
            "trend_change_percent",
        ],
    ) -> bool: ...

class YouTubeChannelInsights(proto.Message):
    display_name: str
    youtube_channel: YouTubeChannelInfo
    channel_url: str
    channel_description: str
    handle: str
    thumbnail_url: str
    publish_date: str
    country_location: LocationInfo
    channel_metrics: YouTubeMetrics
    data_sharing_consent_given: bool
    channel_audience_attributes: MutableSequence[AudienceInsightsAttributeMetadata]
    channel_attributes: MutableSequence[AudienceInsightsAttributeMetadata]
    top_videos: MutableSequence[AudienceInsightsAttributeMetadata]
    language_distributions: MutableSequence[LanguageDistribution]
    channel_type: str
    relevance_score: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        display_name: str = ...,
        youtube_channel: YouTubeChannelInfo = ...,
        channel_url: str = ...,
        channel_description: str = ...,
        handle: str = ...,
        thumbnail_url: str = ...,
        publish_date: str = ...,
        country_location: LocationInfo = ...,
        channel_metrics: YouTubeMetrics = ...,
        data_sharing_consent_given: bool = ...,
        channel_audience_attributes: MutableSequence[
            AudienceInsightsAttributeMetadata
        ] = ...,
        channel_attributes: MutableSequence[AudienceInsightsAttributeMetadata] = ...,
        top_videos: MutableSequence[AudienceInsightsAttributeMetadata] = ...,
        language_distributions: MutableSequence[LanguageDistribution] = ...,
        channel_type: str = ...,
        relevance_score: float = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "display_name",
            "youtube_channel",
            "channel_url",
            "channel_description",
            "handle",
            "thumbnail_url",
            "publish_date",
            "country_location",
            "channel_metrics",
            "data_sharing_consent_given",
            "channel_audience_attributes",
            "channel_attributes",
            "top_videos",
            "language_distributions",
            "channel_type",
            "relevance_score",
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
    is_active_live_stream_creator: bool
    partnership_opportunities: MutableSequence[
        PartnershipOpportunityEnum.PartnershipOpportunity
    ]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        subscriber_count: int = ...,
        views_count: int = ...,
        video_count: int = ...,
        likes_count: int = ...,
        shares_count: int = ...,
        comments_count: int = ...,
        engagement_rate: float = ...,
        average_views_per_video: float = ...,
        average_likes_per_video: float = ...,
        average_shares_per_video: float = ...,
        average_comments_per_video: float = ...,
        shorts_views_count: int = ...,
        shorts_video_count: int = ...,
        is_active_shorts_creator: bool = ...,
        is_active_live_stream_creator: bool = ...,
        partnership_opportunities: MutableSequence[
            PartnershipOpportunityEnum.PartnershipOpportunity
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "subscriber_count",
            "views_count",
            "video_count",
            "likes_count",
            "shares_count",
            "comments_count",
            "engagement_rate",
            "average_views_per_video",
            "average_likes_per_video",
            "average_shares_per_video",
            "average_comments_per_video",
            "shorts_views_count",
            "shorts_video_count",
            "is_active_shorts_creator",
            "is_active_live_stream_creator",
            "partnership_opportunities",
        ],
    ) -> bool: ...
