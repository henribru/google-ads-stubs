from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.criteria import (
    AdScheduleInfo,
    AgeRangeInfo,
    CarrierInfo,
    CombinedAudienceInfo,
    ContentLabelInfo,
    CustomAffinityInfo,
    CustomAudienceInfo,
    DeviceInfo,
    GenderInfo,
    IncomeRangeInfo,
    IpBlockInfo,
    KeywordInfo,
    KeywordThemeInfo,
    LanguageInfo,
    ListingScopeInfo,
    LocalServiceIdInfo,
    LocationGroupInfo,
    LocationInfo,
    MobileAppCategoryInfo,
    MobileApplicationInfo,
    MobileDeviceInfo,
    OperatingSystemVersionInfo,
    ParentalStatusInfo,
    PlacementInfo,
    ProximityInfo,
    TopicInfo,
    UserInterestInfo,
    UserListInfo,
    WebpageInfo,
    YouTubeChannelInfo,
    YouTubeVideoInfo,
)
from google.ads.googleads.v14.enums.types.campaign_criterion_status import (
    CampaignCriterionStatusEnum,
)
from google.ads.googleads.v14.enums.types.criterion_type import CriterionTypeEnum

_M = TypeVar("_M")

class CampaignCriterion(proto.Message):
    resource_name: str
    campaign: str
    criterion_id: int
    display_name: str
    bid_modifier: float
    negative: bool
    type_: CriterionTypeEnum.CriterionType
    status: CampaignCriterionStatusEnum.CampaignCriterionStatus
    keyword: KeywordInfo
    placement: PlacementInfo
    mobile_app_category: MobileAppCategoryInfo
    mobile_application: MobileApplicationInfo
    location: LocationInfo
    device: DeviceInfo
    ad_schedule: AdScheduleInfo
    age_range: AgeRangeInfo
    gender: GenderInfo
    income_range: IncomeRangeInfo
    parental_status: ParentalStatusInfo
    user_list: UserListInfo
    youtube_video: YouTubeVideoInfo
    youtube_channel: YouTubeChannelInfo
    proximity: ProximityInfo
    topic: TopicInfo
    listing_scope: ListingScopeInfo
    language: LanguageInfo
    ip_block: IpBlockInfo
    content_label: ContentLabelInfo
    carrier: CarrierInfo
    user_interest: UserInterestInfo
    webpage: WebpageInfo
    operating_system_version: OperatingSystemVersionInfo
    mobile_device: MobileDeviceInfo
    location_group: LocationGroupInfo
    custom_affinity: CustomAffinityInfo
    custom_audience: CustomAudienceInfo
    combined_audience: CombinedAudienceInfo
    keyword_theme: KeywordThemeInfo
    local_service_id: LocalServiceIdInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: str = ...,
        criterion_id: int = ...,
        display_name: str = ...,
        bid_modifier: float = ...,
        negative: bool = ...,
        type_: CriterionTypeEnum.CriterionType = ...,
        status: CampaignCriterionStatusEnum.CampaignCriterionStatus = ...,
        keyword: KeywordInfo = ...,
        placement: PlacementInfo = ...,
        mobile_app_category: MobileAppCategoryInfo = ...,
        mobile_application: MobileApplicationInfo = ...,
        location: LocationInfo = ...,
        device: DeviceInfo = ...,
        ad_schedule: AdScheduleInfo = ...,
        age_range: AgeRangeInfo = ...,
        gender: GenderInfo = ...,
        income_range: IncomeRangeInfo = ...,
        parental_status: ParentalStatusInfo = ...,
        user_list: UserListInfo = ...,
        youtube_video: YouTubeVideoInfo = ...,
        youtube_channel: YouTubeChannelInfo = ...,
        proximity: ProximityInfo = ...,
        topic: TopicInfo = ...,
        listing_scope: ListingScopeInfo = ...,
        language: LanguageInfo = ...,
        ip_block: IpBlockInfo = ...,
        content_label: ContentLabelInfo = ...,
        carrier: CarrierInfo = ...,
        user_interest: UserInterestInfo = ...,
        webpage: WebpageInfo = ...,
        operating_system_version: OperatingSystemVersionInfo = ...,
        mobile_device: MobileDeviceInfo = ...,
        location_group: LocationGroupInfo = ...,
        custom_affinity: CustomAffinityInfo = ...,
        custom_audience: CustomAudienceInfo = ...,
        combined_audience: CombinedAudienceInfo = ...,
        keyword_theme: KeywordThemeInfo = ...,
        local_service_id: LocalServiceIdInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "campaign",
            "criterion_id",
            "display_name",
            "bid_modifier",
            "negative",
            "type_",
            "status",
            "keyword",
            "placement",
            "mobile_app_category",
            "mobile_application",
            "location",
            "device",
            "ad_schedule",
            "age_range",
            "gender",
            "income_range",
            "parental_status",
            "user_list",
            "youtube_video",
            "youtube_channel",
            "proximity",
            "topic",
            "listing_scope",
            "language",
            "ip_block",
            "content_label",
            "carrier",
            "user_interest",
            "webpage",
            "operating_system_version",
            "mobile_device",
            "location_group",
            "custom_affinity",
            "custom_audience",
            "combined_audience",
            "keyword_theme",
            "local_service_id",
        ],
    ) -> bool: ...
