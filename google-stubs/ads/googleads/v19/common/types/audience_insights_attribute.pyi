from google.ads.googleads.v19.common.types.criteria import LocationInfo
from collections.abc import MutableSequence
from google.ads.googleads.v19.enums.types.insights_knowledge_graph_entity_capabilities import InsightsKnowledgeGraphEntityCapabilitiesEnum
from collections.abc import MutableSequence
from google.ads.googleads.v19.common.types.criteria import LocationInfo
from google.ads.googleads.v19.common.types.criteria import YouTubeChannelInfo
from google.ads.googleads.v19.enums.types.audience_insights_dimension import AudienceInsightsDimensionEnum
from google.ads.googleads.v19.common.types.criteria import YouTubeVideoInfo
from google.ads.googleads.v19.common.types.criteria import YouTubeChannelInfo
from google.ads.googleads.v19.common.types.criteria import IncomeRangeInfo
from google.ads.googleads.v19.common.types.criteria import ParentalStatusInfo
from google.ads.googleads.v19.common.types.criteria import UserInterestInfo
from google.ads.googleads.v19.common.types.criteria import LocationInfo
from google.ads.googleads.v19.common.types.criteria import GenderInfo
from google.ads.googleads.v19.common.types.criteria import AgeRangeInfo
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AudienceInsightsAttribute(proto.Message):
    age_range: AgeRangeInfo
    gender: GenderInfo
    location: LocationInfo
    user_interest: UserInterestInfo
    entity: AudienceInsightsEntity
    category: AudienceInsightsCategory
    dynamic_lineup: AudienceInsightsDynamicLineup
    parental_status: ParentalStatusInfo
    income_range: IncomeRangeInfo
    youtube_channel: YouTubeChannelInfo
    youtube_video: YouTubeVideoInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, age_range: AgeRangeInfo = ..., gender: GenderInfo = ..., location: LocationInfo = ..., user_interest: UserInterestInfo = ..., entity: AudienceInsightsEntity = ..., category: AudienceInsightsCategory = ..., dynamic_lineup: AudienceInsightsDynamicLineup = ..., parental_status: ParentalStatusInfo = ..., income_range: IncomeRangeInfo = ..., youtube_channel: YouTubeChannelInfo = ..., youtube_video: YouTubeVideoInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["age_range", "gender", "location", "user_interest", "entity", "category", "dynamic_lineup", "parental_status", "income_range", "youtube_channel", "youtube_video"]) -> bool: ...
class AudienceInsightsAttributeMetadata(proto.Message):
    dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension = ..., attribute: AudienceInsightsAttribute = ..., display_name: str = ..., display_info: str = ..., potential_youtube_reach: int = ..., subscriber_share: float = ..., viewer_share: float = ..., youtube_channel_metadata: YouTubeChannelAttributeMetadata = ..., youtube_video_metadata: YouTubeVideoAttributeMetadata = ..., dynamic_attribute_metadata: DynamicLineupAttributeMetadata = ..., location_attribute_metadata: LocationAttributeMetadata = ..., user_interest_attribute_metadata: UserInterestAttributeMetadata = ..., knowledge_graph_attribute_metadata: KnowledgeGraphAttributeMetadata = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["dimension", "attribute", "display_name", "display_info", "potential_youtube_reach", "subscriber_share", "viewer_share", "youtube_channel_metadata", "youtube_video_metadata", "dynamic_attribute_metadata", "location_attribute_metadata", "user_interest_attribute_metadata", "knowledge_graph_attribute_metadata"]) -> bool: ...
class AudienceInsightsCategory(proto.Message):
    category_id: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, category_id: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["category_id"]) -> bool: ...
class AudienceInsightsDynamicLineup(proto.Message):
    dynamic_lineup_id: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, dynamic_lineup_id: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["dynamic_lineup_id"]) -> bool: ...
class AudienceInsightsEntity(proto.Message):
    knowledge_graph_machine_id: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, knowledge_graph_machine_id: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["knowledge_graph_machine_id"]) -> bool: ...
class AudienceInsightsTopic(proto.Message):
    entity: AudienceInsightsEntity
    category: AudienceInsightsCategory
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, entity: AudienceInsightsEntity = ..., category: AudienceInsightsCategory = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["entity", "category"]) -> bool: ...
class DynamicLineupAttributeMetadata(proto.Message):
    class SampleChannel(proto.Message):
        youtube_channel: YouTubeChannelInfo
        display_name: str
        youtube_channel_metadata: YouTubeChannelAttributeMetadata
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, youtube_channel: YouTubeChannelInfo = ..., display_name: str = ..., youtube_channel_metadata: YouTubeChannelAttributeMetadata = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["youtube_channel", "display_name", "youtube_channel_metadata"]) -> bool: ...
    inventory_country: LocationInfo
    median_monthly_inventory: int
    channel_count_lower_bound: int
    channel_count_upper_bound: int
    sample_channels: MutableSequence[DynamicLineupAttributeMetadata.SampleChannel]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, inventory_country: LocationInfo = ..., median_monthly_inventory: int = ..., channel_count_lower_bound: int = ..., channel_count_upper_bound: int = ..., sample_channels: MutableSequence[DynamicLineupAttributeMetadata.SampleChannel] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["inventory_country", "median_monthly_inventory", "channel_count_lower_bound", "channel_count_upper_bound", "sample_channels"]) -> bool: ...
class KnowledgeGraphAttributeMetadata(proto.Message):
    entity_capabilities: MutableSequence[InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, entity_capabilities: MutableSequence[InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["entity_capabilities"]) -> bool: ...
class LocationAttributeMetadata(proto.Message):
    country_location: LocationInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, country_location: LocationInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["country_location"]) -> bool: ...
class UserInterestAttributeMetadata(proto.Message):
    user_interest_description: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, user_interest_description: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["user_interest_description"]) -> bool: ...
class YouTubeChannelAttributeMetadata(proto.Message):
    subscriber_count: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, subscriber_count: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["subscriber_count"]) -> bool: ...
class YouTubeVideoAttributeMetadata(proto.Message):
    thumbnail_url: str
    video_url: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, thumbnail_url: str = ..., video_url: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["thumbnail_url", "video_url"]) -> bool: ...
