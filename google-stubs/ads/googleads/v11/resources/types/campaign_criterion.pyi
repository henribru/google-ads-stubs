from typing import Any

import proto

from google.ads.googleads.v11.common.types.criteria import (
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
from google.ads.googleads.v11.enums.types.campaign_criterion_status import (
    CampaignCriterionStatusEnum,
)
from google.ads.googleads.v11.enums.types.criterion_type import CriterionTypeEnum

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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        keyword_theme: KeywordThemeInfo = ...
    ) -> None: ...
