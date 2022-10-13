from typing import Any

import proto

from google.ads.googleads.v10.common.types.ad_type_infos import (
    AppAdInfo,
    AppEngagementAdInfo,
    AppPreRegistrationAdInfo,
    CallAdInfo,
    DiscoveryCarouselAdInfo,
    DiscoveryMultiAssetAdInfo,
    DisplayUploadAdInfo,
    ExpandedDynamicSearchAdInfo,
    ExpandedTextAdInfo,
    GmailAdInfo,
    HotelAdInfo,
    ImageAdInfo,
    LegacyAppInstallAdInfo,
    LegacyResponsiveDisplayAdInfo,
    LocalAdInfo,
    ResponsiveDisplayAdInfo,
    ResponsiveSearchAdInfo,
    ShoppingComparisonListingAdInfo,
    ShoppingProductAdInfo,
    ShoppingSmartAdInfo,
    SmartCampaignAdInfo,
    TextAdInfo,
    VideoAdInfo,
    VideoResponsiveAdInfo,
)
from google.ads.googleads.v10.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v10.common.types.final_app_url import FinalAppUrl
from google.ads.googleads.v10.common.types.url_collection import UrlCollection
from google.ads.googleads.v10.enums.types.ad_type import AdTypeEnum
from google.ads.googleads.v10.enums.types.device import DeviceEnum
from google.ads.googleads.v10.enums.types.system_managed_entity_source import (
    SystemManagedResourceSourceEnum,
)

class Ad(proto.Message):
    resource_name: str
    id: int
    final_urls: list[str]
    final_app_urls: list[FinalAppUrl]
    final_mobile_urls: list[str]
    tracking_url_template: str
    final_url_suffix: str
    url_custom_parameters: list[CustomParameter]
    display_url: str
    type_: AdTypeEnum.AdType
    added_by_google_ads: bool
    device_preference: DeviceEnum.Device
    url_collections: list[UrlCollection]
    name: str
    system_managed_resource_source: SystemManagedResourceSourceEnum.SystemManagedResourceSource
    text_ad: TextAdInfo
    expanded_text_ad: ExpandedTextAdInfo
    call_ad: CallAdInfo
    expanded_dynamic_search_ad: ExpandedDynamicSearchAdInfo
    hotel_ad: HotelAdInfo
    shopping_smart_ad: ShoppingSmartAdInfo
    shopping_product_ad: ShoppingProductAdInfo
    gmail_ad: GmailAdInfo
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
    discovery_multi_asset_ad: DiscoveryMultiAssetAdInfo
    discovery_carousel_ad: DiscoveryCarouselAdInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        final_urls: list[str] = ...,
        final_app_urls: list[FinalAppUrl] = ...,
        final_mobile_urls: list[str] = ...,
        tracking_url_template: str = ...,
        final_url_suffix: str = ...,
        url_custom_parameters: list[CustomParameter] = ...,
        display_url: str = ...,
        type_: AdTypeEnum.AdType = ...,
        added_by_google_ads: bool = ...,
        device_preference: DeviceEnum.Device = ...,
        url_collections: list[UrlCollection] = ...,
        name: str = ...,
        system_managed_resource_source: SystemManagedResourceSourceEnum.SystemManagedResourceSource = ...,
        text_ad: TextAdInfo = ...,
        expanded_text_ad: ExpandedTextAdInfo = ...,
        call_ad: CallAdInfo = ...,
        expanded_dynamic_search_ad: ExpandedDynamicSearchAdInfo = ...,
        hotel_ad: HotelAdInfo = ...,
        shopping_smart_ad: ShoppingSmartAdInfo = ...,
        shopping_product_ad: ShoppingProductAdInfo = ...,
        gmail_ad: GmailAdInfo = ...,
        image_ad: ImageAdInfo = ...,
        video_ad: VideoAdInfo = ...,
        video_responsive_ad: VideoResponsiveAdInfo = ...,
        responsive_search_ad: ResponsiveSearchAdInfo = ...,
        legacy_responsive_display_ad: LegacyResponsiveDisplayAdInfo = ...,
        app_ad: AppAdInfo = ...,
        legacy_app_install_ad: LegacyAppInstallAdInfo = ...,
        responsive_display_ad: ResponsiveDisplayAdInfo = ...,
        local_ad: LocalAdInfo = ...,
        display_upload_ad: DisplayUploadAdInfo = ...,
        app_engagement_ad: AppEngagementAdInfo = ...,
        shopping_comparison_listing_ad: ShoppingComparisonListingAdInfo = ...,
        smart_campaign_ad: SmartCampaignAdInfo = ...,
        app_pre_registration_ad: AppPreRegistrationAdInfo = ...,
        discovery_multi_asset_ad: DiscoveryMultiAssetAdInfo = ...,
        discovery_carousel_ad: DiscoveryCarouselAdInfo = ...
    ) -> None: ...
