import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import criteria
from google.ads.googleads.v20.enums.types import campaign_criterion_status, criterion_type

__protobuf__: Incomplete

class CampaignCriterion(proto.Message):
    resource_name: str
    campaign: str
    criterion_id: int
    display_name: str
    bid_modifier: float
    negative: bool
    type_: criterion_type.CriterionTypeEnum.CriterionType
    status: campaign_criterion_status.CampaignCriterionStatusEnum.CampaignCriterionStatus
    keyword: criteria.KeywordInfo
    placement: criteria.PlacementInfo
    mobile_app_category: criteria.MobileAppCategoryInfo
    mobile_application: criteria.MobileApplicationInfo
    location: criteria.LocationInfo
    device: criteria.DeviceInfo
    ad_schedule: criteria.AdScheduleInfo
    age_range: criteria.AgeRangeInfo
    gender: criteria.GenderInfo
    income_range: criteria.IncomeRangeInfo
    parental_status: criteria.ParentalStatusInfo
    user_list: criteria.UserListInfo
    youtube_video: criteria.YouTubeVideoInfo
    youtube_channel: criteria.YouTubeChannelInfo
    proximity: criteria.ProximityInfo
    topic: criteria.TopicInfo
    listing_scope: criteria.ListingScopeInfo
    language: criteria.LanguageInfo
    ip_block: criteria.IpBlockInfo
    content_label: criteria.ContentLabelInfo
    carrier: criteria.CarrierInfo
    user_interest: criteria.UserInterestInfo
    webpage: criteria.WebpageInfo
    operating_system_version: criteria.OperatingSystemVersionInfo
    mobile_device: criteria.MobileDeviceInfo
    location_group: criteria.LocationGroupInfo
    custom_affinity: criteria.CustomAffinityInfo
    custom_audience: criteria.CustomAudienceInfo
    combined_audience: criteria.CombinedAudienceInfo
    keyword_theme: criteria.KeywordThemeInfo
    local_service_id: criteria.LocalServiceIdInfo
    brand_list: criteria.BrandListInfo
    webpage_list: criteria.WebpageListInfo
