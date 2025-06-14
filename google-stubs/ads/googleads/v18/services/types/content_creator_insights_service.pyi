from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.audience_insights_attribute import AudienceInsightsAttributeMetadata
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.audience_insights_attribute import AudienceInsightsAttributeMetadata
from google.ads.googleads.v18.common.types.criteria import YouTubeChannelInfo
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.criteria import YouTubeChannelInfo
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.audience_insights_attribute import AudienceInsightsAttribute
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.audience_insights_attribute import AudienceInsightsAttribute
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
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, audience_attributes: MutableSequence[AudienceInsightsAttribute] = ..., creator_attributes: MutableSequence[AudienceInsightsAttribute] = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["audience_attributes", "creator_attributes"]) -> bool: ...
    class YouTubeChannels(proto.Message):
        youtube_channels: MutableSequence[YouTubeChannelInfo]
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, youtube_channels: MutableSequence[YouTubeChannelInfo] = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["youtube_channels"]) -> bool: ...
    customer_id: str
    customer_insights_group: str
    search_attributes: GenerateCreatorInsightsRequest.SearchAttributes
    search_channels: GenerateCreatorInsightsRequest.YouTubeChannels
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., customer_insights_group: str = ..., search_attributes: GenerateCreatorInsightsRequest.SearchAttributes = ..., search_channels: GenerateCreatorInsightsRequest.YouTubeChannels = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "customer_insights_group", "search_attributes", "search_channels"]) -> bool: ...
class GenerateCreatorInsightsResponse(proto.Message):
    creator_insights: MutableSequence[YouTubeCreatorInsights]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, creator_insights: MutableSequence[YouTubeCreatorInsights] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["creator_insights"]) -> bool: ...
class YouTubeChannelInsights(proto.Message):
    display_name: str
    youtube_channel: YouTubeChannelInfo
    channel_metrics: YouTubeMetrics
    channel_audience_demographics: MutableSequence[AudienceInsightsAttributeMetadata]
    channel_attributes: MutableSequence[AudienceInsightsAttributeMetadata]
    channel_type: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, display_name: str = ..., youtube_channel: YouTubeChannelInfo = ..., channel_metrics: YouTubeMetrics = ..., channel_audience_demographics: MutableSequence[AudienceInsightsAttributeMetadata] = ..., channel_attributes: MutableSequence[AudienceInsightsAttributeMetadata] = ..., channel_type: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["display_name", "youtube_channel", "channel_metrics", "channel_audience_demographics", "channel_attributes", "channel_type"]) -> bool: ...
class YouTubeCreatorInsights(proto.Message):
    creator_name: str
    creator_channels: MutableSequence[YouTubeChannelInsights]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, creator_name: str = ..., creator_channels: MutableSequence[YouTubeChannelInsights] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["creator_name", "creator_channels"]) -> bool: ...
class YouTubeMetrics(proto.Message):
    subscriber_count: int
    views_count: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, subscriber_count: int = ..., views_count: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["subscriber_count", "views_count"]) -> bool: ...
