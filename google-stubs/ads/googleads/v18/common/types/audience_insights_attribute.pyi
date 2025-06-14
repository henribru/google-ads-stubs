from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v18.common.types.criteria import (
    AgeRangeInfo,
    GenderInfo,
    IncomeRangeInfo,
    LocationInfo,
    ParentalStatusInfo,
    UserInterestInfo,
    YouTubeChannelInfo,
)
from google.ads.googleads.v18.enums.types.audience_insights_dimension import (
    AudienceInsightsDimensionEnum,
)

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        age_range: AgeRangeInfo = ...,
        gender: GenderInfo = ...,
        location: LocationInfo = ...,
        user_interest: UserInterestInfo = ...,
        entity: AudienceInsightsEntity = ...,
        category: AudienceInsightsCategory = ...,
        dynamic_lineup: AudienceInsightsDynamicLineup = ...,
        parental_status: ParentalStatusInfo = ...,
        income_range: IncomeRangeInfo = ...,
        youtube_channel: YouTubeChannelInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "age_range",
            "gender",
            "location",
            "user_interest",
            "entity",
            "category",
            "dynamic_lineup",
            "parental_status",
            "income_range",
            "youtube_channel",
        ],
    ) -> bool: ...

class AudienceInsightsAttributeMetadata(proto.Message):
    dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    attribute: AudienceInsightsAttribute
    display_name: str
    display_info: str
    potential_youtube_reach: int
    subscriber_share: float
    youtube_channel_metadata: YouTubeChannelAttributeMetadata
    dynamic_attribute_metadata: DynamicLineupAttributeMetadata
    location_attribute_metadata: LocationAttributeMetadata
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension = ...,
        attribute: AudienceInsightsAttribute = ...,
        display_name: str = ...,
        display_info: str = ...,
        potential_youtube_reach: int = ...,
        subscriber_share: float = ...,
        youtube_channel_metadata: YouTubeChannelAttributeMetadata = ...,
        dynamic_attribute_metadata: DynamicLineupAttributeMetadata = ...,
        location_attribute_metadata: LocationAttributeMetadata = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "dimension",
            "attribute",
            "display_name",
            "display_info",
            "potential_youtube_reach",
            "subscriber_share",
            "youtube_channel_metadata",
            "dynamic_attribute_metadata",
            "location_attribute_metadata",
        ],
    ) -> bool: ...

class AudienceInsightsCategory(proto.Message):
    category_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        category_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["category_id"]
    ) -> bool: ...

class AudienceInsightsDynamicLineup(proto.Message):
    dynamic_lineup_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dynamic_lineup_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["dynamic_lineup_id"]
    ) -> bool: ...

class AudienceInsightsEntity(proto.Message):
    knowledge_graph_machine_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        knowledge_graph_machine_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["knowledge_graph_machine_id"]
    ) -> bool: ...

class DynamicLineupAttributeMetadata(proto.Message):
    class SampleChannel(proto.Message):
        youtube_channel: YouTubeChannelInfo
        display_name: str
        youtube_channel_metadata: YouTubeChannelAttributeMetadata
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            youtube_channel: YouTubeChannelInfo = ...,
            display_name: str = ...,
            youtube_channel_metadata: YouTubeChannelAttributeMetadata = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal["youtube_channel", "display_name", "youtube_channel_metadata"],
        ) -> bool: ...

    inventory_country: LocationInfo
    median_monthly_inventory: int
    channel_count_lower_bound: int
    channel_count_upper_bound: int
    sample_channels: MutableSequence[DynamicLineupAttributeMetadata.SampleChannel]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        inventory_country: LocationInfo = ...,
        median_monthly_inventory: int = ...,
        channel_count_lower_bound: int = ...,
        channel_count_upper_bound: int = ...,
        sample_channels: MutableSequence[
            DynamicLineupAttributeMetadata.SampleChannel
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "inventory_country",
            "median_monthly_inventory",
            "channel_count_lower_bound",
            "channel_count_upper_bound",
            "sample_channels",
        ],
    ) -> bool: ...

class LocationAttributeMetadata(proto.Message):
    country_location: LocationInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        country_location: LocationInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["country_location"]
    ) -> bool: ...

class YouTubeChannelAttributeMetadata(proto.Message):
    subscriber_count: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        subscriber_count: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["subscriber_count"]
    ) -> bool: ...
