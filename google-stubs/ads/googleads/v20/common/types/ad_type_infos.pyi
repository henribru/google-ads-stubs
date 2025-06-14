import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import ad_asset
from google.ads.googleads.v20.enums.types import call_conversion_reporting_state, display_ad_format_setting, display_upload_product_type as gage_display_upload_product_type, legacy_app_install_ad_app_store, mime_type as gage_mime_type, video_thumbnail
from typing import MutableSequence

__protobuf__: Incomplete

class TextAdInfo(proto.Message):
    headline: str
    description1: str
    description2: str

class ExpandedTextAdInfo(proto.Message):
    headline_part1: str
    headline_part2: str
    headline_part3: str
    description: str
    description2: str
    path1: str
    path2: str

class ExpandedDynamicSearchAdInfo(proto.Message):
    description: str
    description2: str

class HotelAdInfo(proto.Message): ...
class TravelAdInfo(proto.Message): ...
class ShoppingSmartAdInfo(proto.Message): ...
class ShoppingProductAdInfo(proto.Message): ...

class ShoppingComparisonListingAdInfo(proto.Message):
    headline: str

class ImageAdInfo(proto.Message):
    pixel_width: int
    pixel_height: int
    image_url: str
    preview_pixel_width: int
    preview_pixel_height: int
    preview_image_url: str
    mime_type: gage_mime_type.MimeTypeEnum.MimeType
    name: str
    image_asset: ad_asset.AdImageAsset
    data: bytes
    ad_id_to_copy_image_from: int

class VideoBumperInStreamAdInfo(proto.Message):
    companion_banner: ad_asset.AdImageAsset
    action_button_label: str
    action_headline: str

class VideoNonSkippableInStreamAdInfo(proto.Message):
    companion_banner: ad_asset.AdImageAsset
    action_button_label: str
    action_headline: str

class VideoTrueViewInStreamAdInfo(proto.Message):
    action_button_label: str
    action_headline: str
    companion_banner: ad_asset.AdImageAsset

class VideoOutstreamAdInfo(proto.Message):
    headline: str
    description: str

class InFeedVideoAdInfo(proto.Message):
    headline: str
    description1: str
    description2: str
    thumbnail: video_thumbnail.VideoThumbnailEnum.VideoThumbnail

class YouTubeAudioAdInfo(proto.Message): ...

class VideoAdInfo(proto.Message):
    video: ad_asset.AdVideoAsset
    in_stream: VideoTrueViewInStreamAdInfo
    bumper: VideoBumperInStreamAdInfo
    out_stream: VideoOutstreamAdInfo
    non_skippable: VideoNonSkippableInStreamAdInfo
    in_feed: InFeedVideoAdInfo
    audio: YouTubeAudioAdInfo

class VideoResponsiveAdInfo(proto.Message):
    headlines: MutableSequence[ad_asset.AdTextAsset]
    long_headlines: MutableSequence[ad_asset.AdTextAsset]
    descriptions: MutableSequence[ad_asset.AdTextAsset]
    call_to_actions: MutableSequence[ad_asset.AdTextAsset]
    videos: MutableSequence[ad_asset.AdVideoAsset]
    companion_banners: MutableSequence[ad_asset.AdImageAsset]
    breadcrumb1: str
    breadcrumb2: str

class ResponsiveSearchAdInfo(proto.Message):
    headlines: MutableSequence[ad_asset.AdTextAsset]
    descriptions: MutableSequence[ad_asset.AdTextAsset]
    path1: str
    path2: str

class LegacyResponsiveDisplayAdInfo(proto.Message):
    short_headline: str
    long_headline: str
    description: str
    business_name: str
    allow_flexible_color: bool
    accent_color: str
    main_color: str
    call_to_action_text: str
    logo_image: str
    square_logo_image: str
    marketing_image: str
    square_marketing_image: str
    format_setting: display_ad_format_setting.DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    price_prefix: str
    promo_text: str

class AppAdInfo(proto.Message):
    mandatory_ad_text: ad_asset.AdTextAsset
    headlines: MutableSequence[ad_asset.AdTextAsset]
    descriptions: MutableSequence[ad_asset.AdTextAsset]
    images: MutableSequence[ad_asset.AdImageAsset]
    youtube_videos: MutableSequence[ad_asset.AdVideoAsset]
    html5_media_bundles: MutableSequence[ad_asset.AdMediaBundleAsset]
    app_deep_link: ad_asset.AdAppDeepLinkAsset

class AppEngagementAdInfo(proto.Message):
    headlines: MutableSequence[ad_asset.AdTextAsset]
    descriptions: MutableSequence[ad_asset.AdTextAsset]
    images: MutableSequence[ad_asset.AdImageAsset]
    videos: MutableSequence[ad_asset.AdVideoAsset]

class AppPreRegistrationAdInfo(proto.Message):
    headlines: MutableSequence[ad_asset.AdTextAsset]
    descriptions: MutableSequence[ad_asset.AdTextAsset]
    images: MutableSequence[ad_asset.AdImageAsset]
    youtube_videos: MutableSequence[ad_asset.AdVideoAsset]

class LegacyAppInstallAdInfo(proto.Message):
    app_id: str
    app_store: legacy_app_install_ad_app_store.LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    headline: str
    description1: str
    description2: str

class ResponsiveDisplayAdInfo(proto.Message):
    marketing_images: MutableSequence[ad_asset.AdImageAsset]
    square_marketing_images: MutableSequence[ad_asset.AdImageAsset]
    logo_images: MutableSequence[ad_asset.AdImageAsset]
    square_logo_images: MutableSequence[ad_asset.AdImageAsset]
    headlines: MutableSequence[ad_asset.AdTextAsset]
    long_headline: ad_asset.AdTextAsset
    descriptions: MutableSequence[ad_asset.AdTextAsset]
    youtube_videos: MutableSequence[ad_asset.AdVideoAsset]
    business_name: str
    main_color: str
    accent_color: str
    allow_flexible_color: bool
    call_to_action_text: str
    price_prefix: str
    promo_text: str
    format_setting: display_ad_format_setting.DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    control_spec: ResponsiveDisplayAdControlSpec

class LocalAdInfo(proto.Message):
    headlines: MutableSequence[ad_asset.AdTextAsset]
    descriptions: MutableSequence[ad_asset.AdTextAsset]
    call_to_actions: MutableSequence[ad_asset.AdTextAsset]
    marketing_images: MutableSequence[ad_asset.AdImageAsset]
    logo_images: MutableSequence[ad_asset.AdImageAsset]
    videos: MutableSequence[ad_asset.AdVideoAsset]
    path1: str
    path2: str

class DisplayUploadAdInfo(proto.Message):
    display_upload_product_type: gage_display_upload_product_type.DisplayUploadProductTypeEnum.DisplayUploadProductType
    media_bundle: ad_asset.AdMediaBundleAsset

class ResponsiveDisplayAdControlSpec(proto.Message):
    enable_asset_enhancements: bool
    enable_autogen_video: bool

class SmartCampaignAdInfo(proto.Message):
    headlines: MutableSequence[ad_asset.AdTextAsset]
    descriptions: MutableSequence[ad_asset.AdTextAsset]

class CallAdInfo(proto.Message):
    country_code: str
    phone_number: str
    business_name: str
    headline1: str
    headline2: str
    description1: str
    description2: str
    call_tracked: bool
    disable_call_conversion: bool
    phone_number_verification_url: str
    conversion_action: str
    conversion_reporting_state: call_conversion_reporting_state.CallConversionReportingStateEnum.CallConversionReportingState
    path1: str
    path2: str

class DemandGenMultiAssetAdInfo(proto.Message):
    marketing_images: MutableSequence[ad_asset.AdImageAsset]
    square_marketing_images: MutableSequence[ad_asset.AdImageAsset]
    portrait_marketing_images: MutableSequence[ad_asset.AdImageAsset]
    tall_portrait_marketing_images: MutableSequence[ad_asset.AdImageAsset]
    logo_images: MutableSequence[ad_asset.AdImageAsset]
    headlines: MutableSequence[ad_asset.AdTextAsset]
    descriptions: MutableSequence[ad_asset.AdTextAsset]
    business_name: str
    call_to_action_text: str
    lead_form_only: bool

class DemandGenCarouselAdInfo(proto.Message):
    business_name: str
    logo_image: ad_asset.AdImageAsset
    headline: ad_asset.AdTextAsset
    description: ad_asset.AdTextAsset
    call_to_action_text: str
    carousel_cards: MutableSequence[ad_asset.AdDemandGenCarouselCardAsset]

class DemandGenVideoResponsiveAdInfo(proto.Message):
    headlines: MutableSequence[ad_asset.AdTextAsset]
    long_headlines: MutableSequence[ad_asset.AdTextAsset]
    descriptions: MutableSequence[ad_asset.AdTextAsset]
    videos: MutableSequence[ad_asset.AdVideoAsset]
    logo_images: MutableSequence[ad_asset.AdImageAsset]
    breadcrumb1: str
    breadcrumb2: str
    business_name: ad_asset.AdTextAsset
    call_to_actions: MutableSequence[ad_asset.AdCallToActionAsset]

class DemandGenProductAdInfo(proto.Message):
    headline: ad_asset.AdTextAsset
    description: ad_asset.AdTextAsset
    logo_image: ad_asset.AdImageAsset
    breadcrumb1: str
    breadcrumb2: str
    business_name: ad_asset.AdTextAsset
    call_to_action: ad_asset.AdCallToActionAsset
