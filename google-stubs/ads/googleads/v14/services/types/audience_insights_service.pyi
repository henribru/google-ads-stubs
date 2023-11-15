from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.common.types.criteria import (
    AgeRangeInfo,
    GenderInfo,
    IncomeRangeInfo,
    LocationInfo,
    ParentalStatusInfo,
    UserInterestInfo,
    YouTubeChannelInfo,
)
from google.ads.googleads.v14.common.types.dates import DateRange
from google.ads.googleads.v14.enums.types.audience_insights_dimension import (
    AudienceInsightsDimensionEnum,
)

_M = TypeVar("_M")

class AudienceCompositionAttribute(proto.Message):
    attribute_metadata: AudienceInsightsAttributeMetadata
    metrics: AudienceCompositionMetrics
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        attribute_metadata: AudienceInsightsAttributeMetadata = ...,
        metrics: AudienceCompositionMetrics = ...,
    ) -> None: ...

class AudienceCompositionAttributeCluster(proto.Message):
    cluster_display_name: str
    cluster_metrics: AudienceCompositionMetrics
    attributes: MutableSequence[AudienceCompositionAttribute]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        cluster_display_name: str = ...,
        cluster_metrics: AudienceCompositionMetrics = ...,
        attributes: MutableSequence[AudienceCompositionAttribute] = ...,
    ) -> None: ...

class AudienceCompositionMetrics(proto.Message):
    baseline_audience_share: float
    audience_share: float
    index: float
    score: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        baseline_audience_share: float = ...,
        audience_share: float = ...,
        index: float = ...,
        score: float = ...,
    ) -> None: ...

class AudienceCompositionSection(proto.Message):
    dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    top_attributes: MutableSequence[AudienceCompositionAttribute]
    clustered_attributes: MutableSequence[AudienceCompositionAttributeCluster]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension = ...,
        top_attributes: MutableSequence[AudienceCompositionAttribute] = ...,
        clustered_attributes: MutableSequence[
            AudienceCompositionAttributeCluster
        ] = ...,
    ) -> None: ...

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

class AudienceInsightsAttributeMetadata(proto.Message):
    dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    attribute: AudienceInsightsAttribute
    display_name: str
    score: float
    display_info: str
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
        score: float = ...,
        display_info: str = ...,
        youtube_channel_metadata: YouTubeChannelAttributeMetadata = ...,
        dynamic_attribute_metadata: DynamicLineupAttributeMetadata = ...,
        location_attribute_metadata: LocationAttributeMetadata = ...,
    ) -> None: ...

class AudienceInsightsCategory(proto.Message):
    category_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        category_id: str = ...,
    ) -> None: ...

class AudienceInsightsDynamicLineup(proto.Message):
    dynamic_lineup_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dynamic_lineup_id: str = ...,
    ) -> None: ...

class AudienceInsightsEntity(proto.Message):
    knowledge_graph_machine_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        knowledge_graph_machine_id: str = ...,
    ) -> None: ...

class AudienceInsightsTopic(proto.Message):
    entity: AudienceInsightsEntity
    category: AudienceInsightsCategory
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        entity: AudienceInsightsEntity = ...,
        category: AudienceInsightsCategory = ...,
    ) -> None: ...

class BasicInsightsAudience(proto.Message):
    country_location: MutableSequence[LocationInfo]
    sub_country_locations: MutableSequence[LocationInfo]
    gender: GenderInfo
    age_ranges: MutableSequence[AgeRangeInfo]
    user_interests: MutableSequence[UserInterestInfo]
    topics: MutableSequence[AudienceInsightsTopic]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        country_location: MutableSequence[LocationInfo] = ...,
        sub_country_locations: MutableSequence[LocationInfo] = ...,
        gender: GenderInfo = ...,
        age_ranges: MutableSequence[AgeRangeInfo] = ...,
        user_interests: MutableSequence[UserInterestInfo] = ...,
        topics: MutableSequence[AudienceInsightsTopic] = ...,
    ) -> None: ...

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

class GenerateAudienceCompositionInsightsRequest(proto.Message):
    customer_id: str
    audience: InsightsAudience
    baseline_audience: InsightsAudience
    data_month: str
    dimensions: MutableSequence[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    customer_insights_group: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        audience: InsightsAudience = ...,
        baseline_audience: InsightsAudience = ...,
        data_month: str = ...,
        dimensions: MutableSequence[
            AudienceInsightsDimensionEnum.AudienceInsightsDimension
        ] = ...,
        customer_insights_group: str = ...,
    ) -> None: ...

class GenerateAudienceCompositionInsightsResponse(proto.Message):
    sections: MutableSequence[AudienceCompositionSection]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        sections: MutableSequence[AudienceCompositionSection] = ...,
    ) -> None: ...

class GenerateInsightsFinderReportRequest(proto.Message):
    customer_id: str
    baseline_audience: BasicInsightsAudience
    specific_audience: BasicInsightsAudience
    customer_insights_group: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        baseline_audience: BasicInsightsAudience = ...,
        specific_audience: BasicInsightsAudience = ...,
        customer_insights_group: str = ...,
    ) -> None: ...

class GenerateInsightsFinderReportResponse(proto.Message):
    saved_report_url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        saved_report_url: str = ...,
    ) -> None: ...

class InsightsAudience(proto.Message):
    country_locations: MutableSequence[LocationInfo]
    sub_country_locations: MutableSequence[LocationInfo]
    gender: GenderInfo
    age_ranges: MutableSequence[AgeRangeInfo]
    parental_status: ParentalStatusInfo
    income_ranges: MutableSequence[IncomeRangeInfo]
    dynamic_lineups: MutableSequence[AudienceInsightsDynamicLineup]
    topic_audience_combinations: MutableSequence[InsightsAudienceAttributeGroup]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        country_locations: MutableSequence[LocationInfo] = ...,
        sub_country_locations: MutableSequence[LocationInfo] = ...,
        gender: GenderInfo = ...,
        age_ranges: MutableSequence[AgeRangeInfo] = ...,
        parental_status: ParentalStatusInfo = ...,
        income_ranges: MutableSequence[IncomeRangeInfo] = ...,
        dynamic_lineups: MutableSequence[AudienceInsightsDynamicLineup] = ...,
        topic_audience_combinations: MutableSequence[
            InsightsAudienceAttributeGroup
        ] = ...,
    ) -> None: ...

class InsightsAudienceAttributeGroup(proto.Message):
    attributes: MutableSequence[AudienceInsightsAttribute]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        attributes: MutableSequence[AudienceInsightsAttribute] = ...,
    ) -> None: ...

class ListAudienceInsightsAttributesRequest(proto.Message):
    customer_id: str
    dimensions: MutableSequence[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    query_text: str
    customer_insights_group: str
    location_country_filters: MutableSequence[LocationInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        dimensions: MutableSequence[
            AudienceInsightsDimensionEnum.AudienceInsightsDimension
        ] = ...,
        query_text: str = ...,
        customer_insights_group: str = ...,
        location_country_filters: MutableSequence[LocationInfo] = ...,
    ) -> None: ...

class ListAudienceInsightsAttributesResponse(proto.Message):
    attributes: MutableSequence[AudienceInsightsAttributeMetadata]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        attributes: MutableSequence[AudienceInsightsAttributeMetadata] = ...,
    ) -> None: ...

class ListInsightsEligibleDatesRequest(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    ...

class ListInsightsEligibleDatesResponse(proto.Message):
    data_months: MutableSequence[str]
    last_thirty_days: DateRange
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        data_months: MutableSequence[str] = ...,
        last_thirty_days: DateRange = ...,
    ) -> None: ...

class LocationAttributeMetadata(proto.Message):
    country_location: LocationInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        country_location: LocationInfo = ...,
    ) -> None: ...

class YouTubeChannelAttributeMetadata(proto.Message):
    subscriber_count: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        subscriber_count: int = ...,
    ) -> None: ...
