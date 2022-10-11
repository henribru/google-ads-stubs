import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import ad_asset as ad_asset
from google.ads.googleads.v11.enums.types import (
    call_conversion_reporting_state as call_conversion_reporting_state,
    display_ad_format_setting as display_ad_format_setting,
    legacy_app_install_ad_app_store as legacy_app_install_ad_app_store,
    video_thumbnail as video_thumbnail,
)

__protobuf__: Incomplete

class TextAdInfo(proto.Message):
    headline: Incomplete
    description1: Incomplete
    description2: Incomplete

class ExpandedTextAdInfo(proto.Message):
    headline_part1: Incomplete
    headline_part2: Incomplete
    headline_part3: Incomplete
    description: Incomplete
    description2: Incomplete
    path1: Incomplete
    path2: Incomplete

class ExpandedDynamicSearchAdInfo(proto.Message):
    description: Incomplete
    description2: Incomplete

class HotelAdInfo(proto.Message): ...
class ShoppingSmartAdInfo(proto.Message): ...
class ShoppingProductAdInfo(proto.Message): ...

class ShoppingComparisonListingAdInfo(proto.Message):
    headline: Incomplete

class GmailAdInfo(proto.Message):
    teaser: Incomplete
    header_image: Incomplete
    marketing_image: Incomplete
    marketing_image_headline: Incomplete
    marketing_image_description: Incomplete
    marketing_image_display_call_to_action: Incomplete
    product_images: Incomplete
    product_videos: Incomplete

class GmailTeaser(proto.Message):
    headline: Incomplete
    description: Incomplete
    business_name: Incomplete
    logo_image: Incomplete

class DisplayCallToAction(proto.Message):
    text: Incomplete
    text_color: Incomplete
    url_collection_id: Incomplete

class ProductImage(proto.Message):
    product_image: Incomplete
    description: Incomplete
    display_call_to_action: Incomplete

class ProductVideo(proto.Message):
    product_video: Incomplete

class ImageAdInfo(proto.Message):
    pixel_width: Incomplete
    pixel_height: Incomplete
    image_url: Incomplete
    preview_pixel_width: Incomplete
    preview_pixel_height: Incomplete
    preview_image_url: Incomplete
    mime_type: Incomplete
    name: Incomplete
    media_file: Incomplete
    data: Incomplete
    ad_id_to_copy_image_from: Incomplete

class VideoBumperInStreamAdInfo(proto.Message):
    companion_banner: Incomplete

class VideoNonSkippableInStreamAdInfo(proto.Message):
    companion_banner: Incomplete
    action_button_label: Incomplete
    action_headline: Incomplete

class VideoTrueViewInStreamAdInfo(proto.Message):
    action_button_label: Incomplete
    action_headline: Incomplete
    companion_banner: Incomplete

class VideoOutstreamAdInfo(proto.Message):
    headline: Incomplete
    description: Incomplete

class InFeedVideoAdInfo(proto.Message):
    headline: Incomplete
    description1: Incomplete
    description2: Incomplete
    thumbnail: Incomplete

class VideoAdInfo(proto.Message):
    video: Incomplete
    in_stream: Incomplete
    bumper: Incomplete
    out_stream: Incomplete
    non_skippable: Incomplete
    in_feed: Incomplete

class VideoResponsiveAdInfo(proto.Message):
    headlines: Incomplete
    long_headlines: Incomplete
    descriptions: Incomplete
    call_to_actions: Incomplete
    videos: Incomplete
    companion_banners: Incomplete
    breadcrumb1: Incomplete
    breadcrumb2: Incomplete

class ResponsiveSearchAdInfo(proto.Message):
    headlines: Incomplete
    descriptions: Incomplete
    path1: Incomplete
    path2: Incomplete

class LegacyResponsiveDisplayAdInfo(proto.Message):
    short_headline: Incomplete
    long_headline: Incomplete
    description: Incomplete
    business_name: Incomplete
    allow_flexible_color: Incomplete
    accent_color: Incomplete
    main_color: Incomplete
    call_to_action_text: Incomplete
    logo_image: Incomplete
    square_logo_image: Incomplete
    marketing_image: Incomplete
    square_marketing_image: Incomplete
    format_setting: Incomplete
    price_prefix: Incomplete
    promo_text: Incomplete

class AppAdInfo(proto.Message):
    mandatory_ad_text: Incomplete
    headlines: Incomplete
    descriptions: Incomplete
    images: Incomplete
    youtube_videos: Incomplete
    html5_media_bundles: Incomplete

class AppEngagementAdInfo(proto.Message):
    headlines: Incomplete
    descriptions: Incomplete
    images: Incomplete
    videos: Incomplete

class AppPreRegistrationAdInfo(proto.Message):
    headlines: Incomplete
    descriptions: Incomplete
    images: Incomplete
    youtube_videos: Incomplete

class LegacyAppInstallAdInfo(proto.Message):
    app_id: Incomplete
    app_store: Incomplete
    headline: Incomplete
    description1: Incomplete
    description2: Incomplete

class ResponsiveDisplayAdInfo(proto.Message):
    marketing_images: Incomplete
    square_marketing_images: Incomplete
    logo_images: Incomplete
    square_logo_images: Incomplete
    headlines: Incomplete
    long_headline: Incomplete
    descriptions: Incomplete
    youtube_videos: Incomplete
    business_name: Incomplete
    main_color: Incomplete
    accent_color: Incomplete
    allow_flexible_color: Incomplete
    call_to_action_text: Incomplete
    price_prefix: Incomplete
    promo_text: Incomplete
    format_setting: Incomplete
    control_spec: Incomplete

class LocalAdInfo(proto.Message):
    headlines: Incomplete
    descriptions: Incomplete
    call_to_actions: Incomplete
    marketing_images: Incomplete
    logo_images: Incomplete
    videos: Incomplete
    path1: Incomplete
    path2: Incomplete

class DisplayUploadAdInfo(proto.Message):
    display_upload_product_type: Incomplete
    media_bundle: Incomplete

class ResponsiveDisplayAdControlSpec(proto.Message):
    enable_asset_enhancements: Incomplete
    enable_autogen_video: Incomplete

class SmartCampaignAdInfo(proto.Message):
    headlines: Incomplete
    descriptions: Incomplete

class CallAdInfo(proto.Message):
    country_code: Incomplete
    phone_number: Incomplete
    business_name: Incomplete
    headline1: Incomplete
    headline2: Incomplete
    description1: Incomplete
    description2: Incomplete
    call_tracked: Incomplete
    disable_call_conversion: Incomplete
    phone_number_verification_url: Incomplete
    conversion_action: Incomplete
    conversion_reporting_state: Incomplete
    path1: Incomplete
    path2: Incomplete

class DiscoveryMultiAssetAdInfo(proto.Message):
    marketing_images: Incomplete
    square_marketing_images: Incomplete
    portrait_marketing_images: Incomplete
    logo_images: Incomplete
    headlines: Incomplete
    descriptions: Incomplete
    business_name: Incomplete
    call_to_action_text: Incomplete
    lead_form_only: Incomplete

class DiscoveryCarouselAdInfo(proto.Message):
    business_name: Incomplete
    logo_image: Incomplete
    headline: Incomplete
    description: Incomplete
    call_to_action_text: Incomplete
    carousel_cards: Incomplete
