from typing import Any

import proto

from google.ads.googleads.v11.common.types.criteria import (
    AgeRangeInfo,
    GenderInfo,
    IncomeRangeInfo,
    LocationInfo,
    ParentalStatusInfo,
    UserInterestInfo,
    YouTubeChannelInfo,
)
from google.ads.googleads.v11.enums.types.audience_insights_dimension import (
    AudienceInsightsDimensionEnum,
)

class AudienceCompositionAttribute(proto.Message):
    attribute_metadata: AudienceInsightsAttributeMetadata
    metrics: AudienceCompositionMetrics
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        attribute_metadata: AudienceInsightsAttributeMetadata = ...,
        metrics: AudienceCompositionMetrics = ...
    ) -> None: ...

class AudienceCompositionAttributeCluster(proto.Message):
    cluster_display_name: str
    cluster_metrics: AudienceCompositionMetrics
    attributes: list[AudienceCompositionAttribute]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        cluster_display_name: str = ...,
        cluster_metrics: AudienceCompositionMetrics = ...,
        attributes: list[AudienceCompositionAttribute] = ...
    ) -> None: ...

class AudienceCompositionMetrics(proto.Message):
    baseline_audience_share: float
    audience_share: float
    index: float
    score: float
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        baseline_audience_share: float = ...,
        audience_share: float = ...,
        index: float = ...,
        score: float = ...
    ) -> None: ...

class AudienceCompositionSection(proto.Message):
    dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    top_attributes: list[AudienceCompositionAttribute]
    clustered_attributes: list[AudienceCompositionAttributeCluster]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension = ...,
        top_attributes: list[AudienceCompositionAttribute] = ...,
        clustered_attributes: list[AudienceCompositionAttributeCluster] = ...
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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        age_range: AgeRangeInfo = ...,
        gender: GenderInfo = ...,
        location: LocationInfo = ...,
        user_interest: UserInterestInfo = ...,
        entity: AudienceInsightsEntity = ...,
        category: AudienceInsightsCategory = ...,
        dynamic_lineup: AudienceInsightsDynamicLineup = ...,
        parental_status: ParentalStatusInfo = ...,
        income_range: IncomeRangeInfo = ...,
        youtube_channel: YouTubeChannelInfo = ...
    ) -> None: ...

class AudienceInsightsAttributeMetadata(proto.Message):
    dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    attribute: AudienceInsightsAttribute
    display_name: str
    score: float
    display_info: str
    youtube_channel_metadata: YouTubeChannelAttributeMetadata
    dynamic_attribute_metadata: DynamicLineupAttributeMetadata
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        dimension: AudienceInsightsDimensionEnum.AudienceInsightsDimension = ...,
        attribute: AudienceInsightsAttribute = ...,
        display_name: str = ...,
        score: float = ...,
        display_info: str = ...,
        youtube_channel_metadata: YouTubeChannelAttributeMetadata = ...,
        dynamic_attribute_metadata: DynamicLineupAttributeMetadata = ...
    ) -> None: ...

class AudienceInsightsCategory(proto.Message):
    category_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        category_id: str = ...
    ) -> None: ...

class AudienceInsightsDynamicLineup(proto.Message):
    dynamic_lineup_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        dynamic_lineup_id: str = ...
    ) -> None: ...

class AudienceInsightsEntity(proto.Message):
    knowledge_graph_machine_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        knowledge_graph_machine_id: str = ...
    ) -> None: ...

class AudienceInsightsTopic(proto.Message):
    entity: AudienceInsightsEntity
    category: AudienceInsightsCategory
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        entity: AudienceInsightsEntity = ...,
        category: AudienceInsightsCategory = ...
    ) -> None: ...

class BasicInsightsAudience(proto.Message):
    country_location: list[LocationInfo]
    sub_country_locations: list[LocationInfo]
    gender: GenderInfo
    age_ranges: list[AgeRangeInfo]
    user_interests: list[UserInterestInfo]
    topics: list[AudienceInsightsTopic]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        country_location: list[LocationInfo] = ...,
        sub_country_locations: list[LocationInfo] = ...,
        gender: GenderInfo = ...,
        age_ranges: list[AgeRangeInfo] = ...,
        user_interests: list[UserInterestInfo] = ...,
        topics: list[AudienceInsightsTopic] = ...
    ) -> None: ...

class DynamicLineupAttributeMetadata(proto.Message):
    inventory_country: LocationInfo
    median_monthly_inventory: int
    channel_count_lower_bound: int
    channel_count_upper_bound: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        inventory_country: LocationInfo = ...,
        median_monthly_inventory: int = ...,
        channel_count_lower_bound: int = ...,
        channel_count_upper_bound: int = ...
    ) -> None: ...

class GenerateAudienceCompositionInsightsRequest(proto.Message):
    customer_id: str
    audience: InsightsAudience
    data_month: str
    dimensions: list[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    customer_insights_group: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        audience: InsightsAudience = ...,
        data_month: str = ...,
        dimensions: list[AudienceInsightsDimensionEnum.AudienceInsightsDimension] = ...,
        customer_insights_group: str = ...
    ) -> None: ...

class GenerateAudienceCompositionInsightsResponse(proto.Message):
    sections: list[AudienceCompositionSection]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        sections: list[AudienceCompositionSection] = ...
    ) -> None: ...

class GenerateInsightsFinderReportRequest(proto.Message):
    customer_id: str
    baseline_audience: BasicInsightsAudience
    specific_audience: BasicInsightsAudience
    customer_insights_group: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        baseline_audience: BasicInsightsAudience = ...,
        specific_audience: BasicInsightsAudience = ...,
        customer_insights_group: str = ...
    ) -> None: ...

class GenerateInsightsFinderReportResponse(proto.Message):
    saved_report_url: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        saved_report_url: str = ...
    ) -> None: ...

class InsightsAudience(proto.Message):
    country_locations: list[LocationInfo]
    sub_country_locations: list[LocationInfo]
    gender: GenderInfo
    age_ranges: list[AgeRangeInfo]
    parental_status: ParentalStatusInfo
    income_ranges: list[IncomeRangeInfo]
    dynamic_lineups: list[AudienceInsightsDynamicLineup]
    topic_audience_combinations: list[InsightsAudienceAttributeGroup]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        country_locations: list[LocationInfo] = ...,
        sub_country_locations: list[LocationInfo] = ...,
        gender: GenderInfo = ...,
        age_ranges: list[AgeRangeInfo] = ...,
        parental_status: ParentalStatusInfo = ...,
        income_ranges: list[IncomeRangeInfo] = ...,
        dynamic_lineups: list[AudienceInsightsDynamicLineup] = ...,
        topic_audience_combinations: list[InsightsAudienceAttributeGroup] = ...
    ) -> None: ...

class InsightsAudienceAttributeGroup(proto.Message):
    attributes: list[AudienceInsightsAttribute]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        attributes: list[AudienceInsightsAttribute] = ...
    ) -> None: ...

class ListAudienceInsightsAttributesRequest(proto.Message):
    customer_id: str
    dimensions: list[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    query_text: str
    customer_insights_group: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        dimensions: list[AudienceInsightsDimensionEnum.AudienceInsightsDimension] = ...,
        query_text: str = ...,
        customer_insights_group: str = ...
    ) -> None: ...

class ListAudienceInsightsAttributesResponse(proto.Message):
    attributes: list[AudienceInsightsAttributeMetadata]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        attributes: list[AudienceInsightsAttributeMetadata] = ...
    ) -> None: ...

class YouTubeChannelAttributeMetadata(proto.Message):
    subscriber_count: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        subscriber_count: int = ...
    ) -> None: ...
