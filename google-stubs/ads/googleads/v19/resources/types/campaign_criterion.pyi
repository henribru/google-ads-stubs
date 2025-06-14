from google.ads.googleads.v19.common.types.criteria import BrandListInfo
from google.ads.googleads.v19.common.types.criteria import LocalServiceIdInfo
from google.ads.googleads.v19.common.types.criteria import KeywordThemeInfo
from google.ads.googleads.v19.common.types.criteria import CombinedAudienceInfo
from google.ads.googleads.v19.common.types.criteria import CustomAudienceInfo
from google.ads.googleads.v19.common.types.criteria import CustomAffinityInfo
from google.ads.googleads.v19.common.types.criteria import LocationGroupInfo
from google.ads.googleads.v19.common.types.criteria import MobileDeviceInfo
from google.ads.googleads.v19.common.types.criteria import OperatingSystemVersionInfo
from google.ads.googleads.v19.common.types.criteria import WebpageInfo
from google.ads.googleads.v19.common.types.criteria import UserInterestInfo
from google.ads.googleads.v19.common.types.criteria import CarrierInfo
from google.ads.googleads.v19.common.types.criteria import ContentLabelInfo
from google.ads.googleads.v19.common.types.criteria import IpBlockInfo
from google.ads.googleads.v19.common.types.criteria import LanguageInfo
from google.ads.googleads.v19.common.types.criteria import ListingScopeInfo
from google.ads.googleads.v19.common.types.criteria import TopicInfo
from google.ads.googleads.v19.common.types.criteria import ProximityInfo
from google.ads.googleads.v19.common.types.criteria import YouTubeChannelInfo
from google.ads.googleads.v19.common.types.criteria import YouTubeVideoInfo
from google.ads.googleads.v19.common.types.criteria import UserListInfo
from google.ads.googleads.v19.common.types.criteria import ParentalStatusInfo
from google.ads.googleads.v19.common.types.criteria import IncomeRangeInfo
from google.ads.googleads.v19.common.types.criteria import GenderInfo
from google.ads.googleads.v19.common.types.criteria import AgeRangeInfo
from google.ads.googleads.v19.common.types.criteria import AdScheduleInfo
from google.ads.googleads.v19.common.types.criteria import DeviceInfo
from google.ads.googleads.v19.common.types.criteria import LocationInfo
from google.ads.googleads.v19.common.types.criteria import MobileApplicationInfo
from google.ads.googleads.v19.common.types.criteria import MobileAppCategoryInfo
from google.ads.googleads.v19.common.types.criteria import PlacementInfo
from google.ads.googleads.v19.common.types.criteria import KeywordInfo
from google.ads.googleads.v19.enums.types.campaign_criterion_status import CampaignCriterionStatusEnum
from google.ads.googleads.v19.enums.types.criterion_type import CriterionTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    brand_list: BrandListInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., campaign: str = ..., criterion_id: int = ..., display_name: str = ..., bid_modifier: float = ..., negative: bool = ..., type_: CriterionTypeEnum.CriterionType = ..., status: CampaignCriterionStatusEnum.CampaignCriterionStatus = ..., keyword: KeywordInfo = ..., placement: PlacementInfo = ..., mobile_app_category: MobileAppCategoryInfo = ..., mobile_application: MobileApplicationInfo = ..., location: LocationInfo = ..., device: DeviceInfo = ..., ad_schedule: AdScheduleInfo = ..., age_range: AgeRangeInfo = ..., gender: GenderInfo = ..., income_range: IncomeRangeInfo = ..., parental_status: ParentalStatusInfo = ..., user_list: UserListInfo = ..., youtube_video: YouTubeVideoInfo = ..., youtube_channel: YouTubeChannelInfo = ..., proximity: ProximityInfo = ..., topic: TopicInfo = ..., listing_scope: ListingScopeInfo = ..., language: LanguageInfo = ..., ip_block: IpBlockInfo = ..., content_label: ContentLabelInfo = ..., carrier: CarrierInfo = ..., user_interest: UserInterestInfo = ..., webpage: WebpageInfo = ..., operating_system_version: OperatingSystemVersionInfo = ..., mobile_device: MobileDeviceInfo = ..., location_group: LocationGroupInfo = ..., custom_affinity: CustomAffinityInfo = ..., custom_audience: CustomAudienceInfo = ..., combined_audience: CombinedAudienceInfo = ..., keyword_theme: KeywordThemeInfo = ..., local_service_id: LocalServiceIdInfo = ..., brand_list: BrandListInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "campaign", "criterion_id", "display_name", "bid_modifier", "negative", "type_", "status", "keyword", "placement", "mobile_app_category", "mobile_application", "location", "device", "ad_schedule", "age_range", "gender", "income_range", "parental_status", "user_list", "youtube_video", "youtube_channel", "proximity", "topic", "listing_scope", "language", "ip_block", "content_label", "carrier", "user_interest", "webpage", "operating_system_version", "mobile_device", "location_group", "custom_affinity", "custom_audience", "combined_audience", "keyword_theme", "local_service_id", "brand_list"]) -> bool: ...
