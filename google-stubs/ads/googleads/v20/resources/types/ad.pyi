import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import ad_type_infos, custom_parameter, final_app_url, url_collection
from google.ads.googleads.v20.enums.types import ad_type, device, system_managed_entity_source
from typing import MutableSequence

__protobuf__: Incomplete

class Ad(proto.Message):
    resource_name: str
    id: int
    final_urls: MutableSequence[str]
    final_app_urls: MutableSequence[final_app_url.FinalAppUrl]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    final_url_suffix: str
    url_custom_parameters: MutableSequence[custom_parameter.CustomParameter]
    display_url: str
    type_: ad_type.AdTypeEnum.AdType
    added_by_google_ads: bool
    device_preference: device.DeviceEnum.Device
    url_collections: MutableSequence[url_collection.UrlCollection]
    name: str
    system_managed_resource_source: system_managed_entity_source.SystemManagedResourceSourceEnum.SystemManagedResourceSource
    text_ad: ad_type_infos.TextAdInfo
    expanded_text_ad: ad_type_infos.ExpandedTextAdInfo
    call_ad: ad_type_infos.CallAdInfo
    expanded_dynamic_search_ad: ad_type_infos.ExpandedDynamicSearchAdInfo
    hotel_ad: ad_type_infos.HotelAdInfo
    shopping_smart_ad: ad_type_infos.ShoppingSmartAdInfo
    shopping_product_ad: ad_type_infos.ShoppingProductAdInfo
    image_ad: ad_type_infos.ImageAdInfo
    video_ad: ad_type_infos.VideoAdInfo
    video_responsive_ad: ad_type_infos.VideoResponsiveAdInfo
    responsive_search_ad: ad_type_infos.ResponsiveSearchAdInfo
    legacy_responsive_display_ad: ad_type_infos.LegacyResponsiveDisplayAdInfo
    app_ad: ad_type_infos.AppAdInfo
    legacy_app_install_ad: ad_type_infos.LegacyAppInstallAdInfo
    responsive_display_ad: ad_type_infos.ResponsiveDisplayAdInfo
    local_ad: ad_type_infos.LocalAdInfo
    display_upload_ad: ad_type_infos.DisplayUploadAdInfo
    app_engagement_ad: ad_type_infos.AppEngagementAdInfo
    shopping_comparison_listing_ad: ad_type_infos.ShoppingComparisonListingAdInfo
    smart_campaign_ad: ad_type_infos.SmartCampaignAdInfo
    app_pre_registration_ad: ad_type_infos.AppPreRegistrationAdInfo
    demand_gen_multi_asset_ad: ad_type_infos.DemandGenMultiAssetAdInfo
    demand_gen_carousel_ad: ad_type_infos.DemandGenCarouselAdInfo
    demand_gen_video_responsive_ad: ad_type_infos.DemandGenVideoResponsiveAdInfo
    demand_gen_product_ad: ad_type_infos.DemandGenProductAdInfo
    travel_ad: ad_type_infos.TravelAdInfo
