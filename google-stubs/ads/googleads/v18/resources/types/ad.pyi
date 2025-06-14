from google.ads.googleads.v18.common.types.ad_type_infos import TravelAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import DemandGenProductAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import DemandGenVideoResponsiveAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import DemandGenCarouselAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import DemandGenMultiAssetAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import AppPreRegistrationAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import SmartCampaignAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import ShoppingComparisonListingAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import AppEngagementAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import DisplayUploadAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import LocalAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import ResponsiveDisplayAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import LegacyAppInstallAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import AppAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import LegacyResponsiveDisplayAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import ResponsiveSearchAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import VideoResponsiveAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import VideoAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import ImageAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import ShoppingProductAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import ShoppingSmartAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import HotelAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import ExpandedDynamicSearchAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import CallAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import ExpandedTextAdInfo
from google.ads.googleads.v18.common.types.ad_type_infos import TextAdInfo
from google.ads.googleads.v18.enums.types.system_managed_entity_source import SystemManagedResourceSourceEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.url_collection import UrlCollection
from google.ads.googleads.v18.enums.types.device import DeviceEnum
from google.ads.googleads.v18.enums.types.ad_type import AdTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.custom_parameter import CustomParameter
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.final_app_url import FinalAppUrl
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class Ad(proto.Message):
    resource_name: str
    id: int
    final_urls: MutableSequence[str]
    final_app_urls: MutableSequence[FinalAppUrl]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    final_url_suffix: str
    url_custom_parameters: MutableSequence[CustomParameter]
    display_url: str
    type_: AdTypeEnum.AdType
    added_by_google_ads: bool
    device_preference: DeviceEnum.Device
    url_collections: MutableSequence[UrlCollection]
    name: str
    system_managed_resource_source: SystemManagedResourceSourceEnum.SystemManagedResourceSource
    text_ad: TextAdInfo
    expanded_text_ad: ExpandedTextAdInfo
    call_ad: CallAdInfo
    expanded_dynamic_search_ad: ExpandedDynamicSearchAdInfo
    hotel_ad: HotelAdInfo
    shopping_smart_ad: ShoppingSmartAdInfo
    shopping_product_ad: ShoppingProductAdInfo
    image_ad: ImageAdInfo
    video_ad: VideoAdInfo
    video_responsive_ad: VideoResponsiveAdInfo
    responsive_search_ad: ResponsiveSearchAdInfo
    legacy_responsive_display_ad: LegacyResponsiveDisplayAdInfo
    app_ad: AppAdInfo
    legacy_app_install_ad: LegacyAppInstallAdInfo
    responsive_display_ad: ResponsiveDisplayAdInfo
    local_ad: LocalAdInfo
    display_upload_ad: DisplayUploadAdInfo
    app_engagement_ad: AppEngagementAdInfo
    shopping_comparison_listing_ad: ShoppingComparisonListingAdInfo
    smart_campaign_ad: SmartCampaignAdInfo
    app_pre_registration_ad: AppPreRegistrationAdInfo
    demand_gen_multi_asset_ad: DemandGenMultiAssetAdInfo
    demand_gen_carousel_ad: DemandGenCarouselAdInfo
    demand_gen_video_responsive_ad: DemandGenVideoResponsiveAdInfo
    demand_gen_product_ad: DemandGenProductAdInfo
    travel_ad: TravelAdInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., id: int = ..., final_urls: MutableSequence[str] = ..., final_app_urls: MutableSequence[FinalAppUrl] = ..., final_mobile_urls: MutableSequence[str] = ..., tracking_url_template: str = ..., final_url_suffix: str = ..., url_custom_parameters: MutableSequence[CustomParameter] = ..., display_url: str = ..., type_: AdTypeEnum.AdType = ..., added_by_google_ads: bool = ..., device_preference: DeviceEnum.Device = ..., url_collections: MutableSequence[UrlCollection] = ..., name: str = ..., system_managed_resource_source: SystemManagedResourceSourceEnum.SystemManagedResourceSource = ..., text_ad: TextAdInfo = ..., expanded_text_ad: ExpandedTextAdInfo = ..., call_ad: CallAdInfo = ..., expanded_dynamic_search_ad: ExpandedDynamicSearchAdInfo = ..., hotel_ad: HotelAdInfo = ..., shopping_smart_ad: ShoppingSmartAdInfo = ..., shopping_product_ad: ShoppingProductAdInfo = ..., image_ad: ImageAdInfo = ..., video_ad: VideoAdInfo = ..., video_responsive_ad: VideoResponsiveAdInfo = ..., responsive_search_ad: ResponsiveSearchAdInfo = ..., legacy_responsive_display_ad: LegacyResponsiveDisplayAdInfo = ..., app_ad: AppAdInfo = ..., legacy_app_install_ad: LegacyAppInstallAdInfo = ..., responsive_display_ad: ResponsiveDisplayAdInfo = ..., local_ad: LocalAdInfo = ..., display_upload_ad: DisplayUploadAdInfo = ..., app_engagement_ad: AppEngagementAdInfo = ..., shopping_comparison_listing_ad: ShoppingComparisonListingAdInfo = ..., smart_campaign_ad: SmartCampaignAdInfo = ..., app_pre_registration_ad: AppPreRegistrationAdInfo = ..., demand_gen_multi_asset_ad: DemandGenMultiAssetAdInfo = ..., demand_gen_carousel_ad: DemandGenCarouselAdInfo = ..., demand_gen_video_responsive_ad: DemandGenVideoResponsiveAdInfo = ..., demand_gen_product_ad: DemandGenProductAdInfo = ..., travel_ad: TravelAdInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "final_urls", "final_app_urls", "final_mobile_urls", "tracking_url_template", "final_url_suffix", "url_custom_parameters", "display_url", "type_", "added_by_google_ads", "device_preference", "url_collections", "name", "system_managed_resource_source", "text_ad", "expanded_text_ad", "call_ad", "expanded_dynamic_search_ad", "hotel_ad", "shopping_smart_ad", "shopping_product_ad", "image_ad", "video_ad", "video_responsive_ad", "responsive_search_ad", "legacy_responsive_display_ad", "app_ad", "legacy_app_install_ad", "responsive_display_ad", "local_ad", "display_upload_ad", "app_engagement_ad", "shopping_comparison_listing_ad", "smart_campaign_ad", "app_pre_registration_ad", "demand_gen_multi_asset_ad", "demand_gen_carousel_ad", "demand_gen_video_responsive_ad", "demand_gen_product_ad", "travel_ad"]) -> bool: ...
