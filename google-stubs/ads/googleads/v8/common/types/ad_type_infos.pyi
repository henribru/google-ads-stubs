from typing import Any

import proto

from google.ads.googleads.v8.common.types import ad_asset as ad_asset
from google.ads.googleads.v8.enums.types import (
    call_conversion_reporting_state as call_conversion_reporting_state,
    display_ad_format_setting as display_ad_format_setting,
    legacy_app_install_ad_app_store as legacy_app_install_ad_app_store,
)

__protobuf__: Any

class TextAdInfo(proto.Message):
    headline: Any
    description1: Any
    description2: Any

class ExpandedTextAdInfo(proto.Message):
    headline_part1: Any
    headline_part2: Any
    headline_part3: Any
    description: Any
    description2: Any
    path1: Any
    path2: Any

class ExpandedDynamicSearchAdInfo(proto.Message):
    description: Any
    description2: Any

class HotelAdInfo(proto.Message): ...
class ShoppingSmartAdInfo(proto.Message): ...
class ShoppingProductAdInfo(proto.Message): ...

class ShoppingComparisonListingAdInfo(proto.Message):
    headline: Any

class GmailAdInfo(proto.Message):
    teaser: Any
    header_image: Any
    marketing_image: Any
    marketing_image_headline: Any
    marketing_image_description: Any
    marketing_image_display_call_to_action: Any
    product_images: Any
    product_videos: Any

class GmailTeaser(proto.Message):
    headline: Any
    description: Any
    business_name: Any
    logo_image: Any

class DisplayCallToAction(proto.Message):
    text: Any
    text_color: Any
    url_collection_id: Any

class ProductImage(proto.Message):
    product_image: Any
    description: Any
    display_call_to_action: Any

class ProductVideo(proto.Message):
    product_video: Any

class ImageAdInfo(proto.Message):
    pixel_width: Any
    pixel_height: Any
    image_url: Any
    preview_pixel_width: Any
    preview_pixel_height: Any
    preview_image_url: Any
    mime_type: Any
    name: Any
    media_file: Any
    data: Any
    ad_id_to_copy_image_from: Any

class VideoBumperInStreamAdInfo(proto.Message):
    companion_banner: Any

class VideoNonSkippableInStreamAdInfo(proto.Message):
    companion_banner: Any

class VideoTrueViewInStreamAdInfo(proto.Message):
    action_button_label: Any
    action_headline: Any
    companion_banner: Any

class VideoOutstreamAdInfo(proto.Message):
    headline: Any
    description: Any

class VideoTrueViewDiscoveryAdInfo(proto.Message):
    headline: Any
    description1: Any
    description2: Any

class VideoAdInfo(proto.Message):
    media_file: Any
    in_stream: Any
    bumper: Any
    out_stream: Any
    non_skippable: Any
    discovery: Any

class VideoResponsiveAdInfo(proto.Message):
    headlines: Any
    long_headlines: Any
    descriptions: Any
    call_to_actions: Any
    videos: Any
    companion_banners: Any

class ResponsiveSearchAdInfo(proto.Message):
    headlines: Any
    descriptions: Any
    path1: Any
    path2: Any

class LegacyResponsiveDisplayAdInfo(proto.Message):
    short_headline: Any
    long_headline: Any
    description: Any
    business_name: Any
    allow_flexible_color: Any
    accent_color: Any
    main_color: Any
    call_to_action_text: Any
    logo_image: Any
    square_logo_image: Any
    marketing_image: Any
    square_marketing_image: Any
    format_setting: Any
    price_prefix: Any
    promo_text: Any

class AppAdInfo(proto.Message):
    mandatory_ad_text: Any
    headlines: Any
    descriptions: Any
    images: Any
    youtube_videos: Any
    html5_media_bundles: Any

class AppEngagementAdInfo(proto.Message):
    headlines: Any
    descriptions: Any
    images: Any
    videos: Any

class LegacyAppInstallAdInfo(proto.Message):
    app_id: Any
    app_store: Any
    headline: Any
    description1: Any
    description2: Any

class ResponsiveDisplayAdInfo(proto.Message):
    marketing_images: Any
    square_marketing_images: Any
    logo_images: Any
    square_logo_images: Any
    headlines: Any
    long_headline: Any
    descriptions: Any
    youtube_videos: Any
    business_name: Any
    main_color: Any
    accent_color: Any
    allow_flexible_color: Any
    call_to_action_text: Any
    price_prefix: Any
    promo_text: Any
    format_setting: Any
    control_spec: Any

class LocalAdInfo(proto.Message):
    headlines: Any
    descriptions: Any
    call_to_actions: Any
    marketing_images: Any
    logo_images: Any
    videos: Any
    path1: Any
    path2: Any

class DisplayUploadAdInfo(proto.Message):
    display_upload_product_type: Any
    media_bundle: Any

class ResponsiveDisplayAdControlSpec(proto.Message):
    enable_asset_enhancements: Any
    enable_autogen_video: Any

class SmartCampaignAdInfo(proto.Message):
    headlines: Any
    descriptions: Any

class CallAdInfo(proto.Message):
    country_code: Any
    phone_number: Any
    business_name: Any
    headline1: Any
    headline2: Any
    description1: Any
    description2: Any
    call_tracked: Any
    disable_call_conversion: Any
    phone_number_verification_url: Any
    conversion_action: Any
    conversion_reporting_state: Any
    path1: Any
    path2: Any
