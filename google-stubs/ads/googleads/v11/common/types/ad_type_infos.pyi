from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v11.common.types.ad_asset import (
    AdDiscoveryCarouselCardAsset,
    AdImageAsset,
    AdMediaBundleAsset,
    AdTextAsset,
    AdVideoAsset,
)
from google.ads.googleads.v11.enums.types.call_conversion_reporting_state import (
    CallConversionReportingStateEnum,
)
from google.ads.googleads.v11.enums.types.display_ad_format_setting import (
    DisplayAdFormatSettingEnum,
)
from google.ads.googleads.v11.enums.types.display_upload_product_type import (
    DisplayUploadProductTypeEnum,
)
from google.ads.googleads.v11.enums.types.legacy_app_install_ad_app_store import (
    LegacyAppInstallAdAppStoreEnum,
)
from google.ads.googleads.v11.enums.types.mime_type import MimeTypeEnum
from google.ads.googleads.v11.enums.types.video_thumbnail import VideoThumbnailEnum

class AppAdInfo(proto.Message):
    mandatory_ad_text: AdTextAsset
    headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    images: MutableSequence[AdImageAsset]
    youtube_videos: MutableSequence[AdVideoAsset]
    html5_media_bundles: MutableSequence[AdMediaBundleAsset]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        mandatory_ad_text: AdTextAsset = ...,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        images: MutableSequence[AdImageAsset] = ...,
        youtube_videos: MutableSequence[AdVideoAsset] = ...,
        html5_media_bundles: MutableSequence[AdMediaBundleAsset] = ...,
    ) -> None: ...

class AppEngagementAdInfo(proto.Message):
    headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    images: MutableSequence[AdImageAsset]
    videos: MutableSequence[AdVideoAsset]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        images: MutableSequence[AdImageAsset] = ...,
        videos: MutableSequence[AdVideoAsset] = ...,
    ) -> None: ...

class AppPreRegistrationAdInfo(proto.Message):
    headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    images: MutableSequence[AdImageAsset]
    youtube_videos: MutableSequence[AdVideoAsset]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        images: MutableSequence[AdImageAsset] = ...,
        youtube_videos: MutableSequence[AdVideoAsset] = ...,
    ) -> None: ...

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
    conversion_reporting_state: CallConversionReportingStateEnum.CallConversionReportingState
    path1: str
    path2: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        country_code: str = ...,
        phone_number: str = ...,
        business_name: str = ...,
        headline1: str = ...,
        headline2: str = ...,
        description1: str = ...,
        description2: str = ...,
        call_tracked: bool = ...,
        disable_call_conversion: bool = ...,
        phone_number_verification_url: str = ...,
        conversion_action: str = ...,
        conversion_reporting_state: CallConversionReportingStateEnum.CallConversionReportingState = ...,
        path1: str = ...,
        path2: str = ...,
    ) -> None: ...

class DiscoveryCarouselAdInfo(proto.Message):
    business_name: str
    logo_image: AdImageAsset
    headline: AdTextAsset
    description: AdTextAsset
    call_to_action_text: str
    carousel_cards: MutableSequence[AdDiscoveryCarouselCardAsset]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        business_name: str = ...,
        logo_image: AdImageAsset = ...,
        headline: AdTextAsset = ...,
        description: AdTextAsset = ...,
        call_to_action_text: str = ...,
        carousel_cards: MutableSequence[AdDiscoveryCarouselCardAsset] = ...,
    ) -> None: ...

class DiscoveryMultiAssetAdInfo(proto.Message):
    marketing_images: MutableSequence[AdImageAsset]
    square_marketing_images: MutableSequence[AdImageAsset]
    portrait_marketing_images: MutableSequence[AdImageAsset]
    logo_images: MutableSequence[AdImageAsset]
    headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    business_name: str
    call_to_action_text: str
    lead_form_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        marketing_images: MutableSequence[AdImageAsset] = ...,
        square_marketing_images: MutableSequence[AdImageAsset] = ...,
        portrait_marketing_images: MutableSequence[AdImageAsset] = ...,
        logo_images: MutableSequence[AdImageAsset] = ...,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        business_name: str = ...,
        call_to_action_text: str = ...,
        lead_form_only: bool = ...,
    ) -> None: ...

class DisplayCallToAction(proto.Message):
    text: str
    text_color: str
    url_collection_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        text: str = ...,
        text_color: str = ...,
        url_collection_id: str = ...,
    ) -> None: ...

class DisplayUploadAdInfo(proto.Message):
    display_upload_product_type: DisplayUploadProductTypeEnum.DisplayUploadProductType
    media_bundle: AdMediaBundleAsset
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        display_upload_product_type: DisplayUploadProductTypeEnum.DisplayUploadProductType = ...,
        media_bundle: AdMediaBundleAsset = ...,
    ) -> None: ...

class ExpandedDynamicSearchAdInfo(proto.Message):
    description: str
    description2: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        description: str = ...,
        description2: str = ...,
    ) -> None: ...

class ExpandedTextAdInfo(proto.Message):
    headline_part1: str
    headline_part2: str
    headline_part3: str
    description: str
    description2: str
    path1: str
    path2: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        headline_part1: str = ...,
        headline_part2: str = ...,
        headline_part3: str = ...,
        description: str = ...,
        description2: str = ...,
        path1: str = ...,
        path2: str = ...,
    ) -> None: ...

class GmailAdInfo(proto.Message):
    teaser: GmailTeaser
    header_image: str
    marketing_image: str
    marketing_image_headline: str
    marketing_image_description: str
    marketing_image_display_call_to_action: DisplayCallToAction
    product_images: MutableSequence[ProductImage]
    product_videos: MutableSequence[ProductVideo]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        teaser: GmailTeaser = ...,
        header_image: str = ...,
        marketing_image: str = ...,
        marketing_image_headline: str = ...,
        marketing_image_description: str = ...,
        marketing_image_display_call_to_action: DisplayCallToAction = ...,
        product_images: MutableSequence[ProductImage] = ...,
        product_videos: MutableSequence[ProductVideo] = ...,
    ) -> None: ...

class GmailTeaser(proto.Message):
    headline: str
    description: str
    business_name: str
    logo_image: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        headline: str = ...,
        description: str = ...,
        business_name: str = ...,
        logo_image: str = ...,
    ) -> None: ...

class HotelAdInfo(proto.Message):
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
    ...

class ImageAdInfo(proto.Message):
    pixel_width: int
    pixel_height: int
    image_url: str
    preview_pixel_width: int
    preview_pixel_height: int
    preview_image_url: str
    mime_type: MimeTypeEnum.MimeType
    name: str
    media_file: str
    data: bytes
    ad_id_to_copy_image_from: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        pixel_width: int = ...,
        pixel_height: int = ...,
        image_url: str = ...,
        preview_pixel_width: int = ...,
        preview_pixel_height: int = ...,
        preview_image_url: str = ...,
        mime_type: MimeTypeEnum.MimeType = ...,
        name: str = ...,
        media_file: str = ...,
        data: bytes = ...,
        ad_id_to_copy_image_from: int = ...,
    ) -> None: ...

class InFeedVideoAdInfo(proto.Message):
    headline: str
    description1: str
    description2: str
    thumbnail: VideoThumbnailEnum.VideoThumbnail
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        headline: str = ...,
        description1: str = ...,
        description2: str = ...,
        thumbnail: VideoThumbnailEnum.VideoThumbnail = ...,
    ) -> None: ...

class LegacyAppInstallAdInfo(proto.Message):
    app_id: str
    app_store: LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    headline: str
    description1: str
    description2: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        app_id: str = ...,
        app_store: LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore = ...,
        headline: str = ...,
        description1: str = ...,
        description2: str = ...,
    ) -> None: ...

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
    format_setting: DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    price_prefix: str
    promo_text: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        short_headline: str = ...,
        long_headline: str = ...,
        description: str = ...,
        business_name: str = ...,
        allow_flexible_color: bool = ...,
        accent_color: str = ...,
        main_color: str = ...,
        call_to_action_text: str = ...,
        logo_image: str = ...,
        square_logo_image: str = ...,
        marketing_image: str = ...,
        square_marketing_image: str = ...,
        format_setting: DisplayAdFormatSettingEnum.DisplayAdFormatSetting = ...,
        price_prefix: str = ...,
        promo_text: str = ...,
    ) -> None: ...

class LocalAdInfo(proto.Message):
    headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    call_to_actions: MutableSequence[AdTextAsset]
    marketing_images: MutableSequence[AdImageAsset]
    logo_images: MutableSequence[AdImageAsset]
    videos: MutableSequence[AdVideoAsset]
    path1: str
    path2: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        call_to_actions: MutableSequence[AdTextAsset] = ...,
        marketing_images: MutableSequence[AdImageAsset] = ...,
        logo_images: MutableSequence[AdImageAsset] = ...,
        videos: MutableSequence[AdVideoAsset] = ...,
        path1: str = ...,
        path2: str = ...,
    ) -> None: ...

class ProductImage(proto.Message):
    product_image: str
    description: str
    display_call_to_action: DisplayCallToAction
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        product_image: str = ...,
        description: str = ...,
        display_call_to_action: DisplayCallToAction = ...,
    ) -> None: ...

class ProductVideo(proto.Message):
    product_video: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        product_video: str = ...,
    ) -> None: ...

class ResponsiveDisplayAdControlSpec(proto.Message):
    enable_asset_enhancements: bool
    enable_autogen_video: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        enable_asset_enhancements: bool = ...,
        enable_autogen_video: bool = ...,
    ) -> None: ...

class ResponsiveDisplayAdInfo(proto.Message):
    marketing_images: MutableSequence[AdImageAsset]
    square_marketing_images: MutableSequence[AdImageAsset]
    logo_images: MutableSequence[AdImageAsset]
    square_logo_images: MutableSequence[AdImageAsset]
    headlines: MutableSequence[AdTextAsset]
    long_headline: AdTextAsset
    descriptions: MutableSequence[AdTextAsset]
    youtube_videos: MutableSequence[AdVideoAsset]
    business_name: str
    main_color: str
    accent_color: str
    allow_flexible_color: bool
    call_to_action_text: str
    price_prefix: str
    promo_text: str
    format_setting: DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    control_spec: ResponsiveDisplayAdControlSpec
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        marketing_images: MutableSequence[AdImageAsset] = ...,
        square_marketing_images: MutableSequence[AdImageAsset] = ...,
        logo_images: MutableSequence[AdImageAsset] = ...,
        square_logo_images: MutableSequence[AdImageAsset] = ...,
        headlines: MutableSequence[AdTextAsset] = ...,
        long_headline: AdTextAsset = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        youtube_videos: MutableSequence[AdVideoAsset] = ...,
        business_name: str = ...,
        main_color: str = ...,
        accent_color: str = ...,
        allow_flexible_color: bool = ...,
        call_to_action_text: str = ...,
        price_prefix: str = ...,
        promo_text: str = ...,
        format_setting: DisplayAdFormatSettingEnum.DisplayAdFormatSetting = ...,
        control_spec: ResponsiveDisplayAdControlSpec = ...,
    ) -> None: ...

class ResponsiveSearchAdInfo(proto.Message):
    headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    path1: str
    path2: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        path1: str = ...,
        path2: str = ...,
    ) -> None: ...

class ShoppingComparisonListingAdInfo(proto.Message):
    headline: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        headline: str = ...,
    ) -> None: ...

class ShoppingProductAdInfo(proto.Message):
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
    ...

class ShoppingSmartAdInfo(proto.Message):
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
    ...

class SmartCampaignAdInfo(proto.Message):
    headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
    ) -> None: ...

class TextAdInfo(proto.Message):
    headline: str
    description1: str
    description2: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        headline: str = ...,
        description1: str = ...,
        description2: str = ...,
    ) -> None: ...

class VideoAdInfo(proto.Message):
    video: AdVideoAsset
    in_stream: VideoTrueViewInStreamAdInfo
    bumper: VideoBumperInStreamAdInfo
    out_stream: VideoOutstreamAdInfo
    non_skippable: VideoNonSkippableInStreamAdInfo
    in_feed: InFeedVideoAdInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        video: AdVideoAsset = ...,
        in_stream: VideoTrueViewInStreamAdInfo = ...,
        bumper: VideoBumperInStreamAdInfo = ...,
        out_stream: VideoOutstreamAdInfo = ...,
        non_skippable: VideoNonSkippableInStreamAdInfo = ...,
        in_feed: InFeedVideoAdInfo = ...,
    ) -> None: ...

class VideoBumperInStreamAdInfo(proto.Message):
    companion_banner: AdImageAsset
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        companion_banner: AdImageAsset = ...,
    ) -> None: ...

class VideoNonSkippableInStreamAdInfo(proto.Message):
    companion_banner: AdImageAsset
    action_button_label: str
    action_headline: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        companion_banner: AdImageAsset = ...,
        action_button_label: str = ...,
        action_headline: str = ...,
    ) -> None: ...

class VideoOutstreamAdInfo(proto.Message):
    headline: str
    description: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        headline: str = ...,
        description: str = ...,
    ) -> None: ...

class VideoResponsiveAdInfo(proto.Message):
    headlines: MutableSequence[AdTextAsset]
    long_headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    call_to_actions: MutableSequence[AdTextAsset]
    videos: MutableSequence[AdVideoAsset]
    companion_banners: MutableSequence[AdImageAsset]
    breadcrumb1: str
    breadcrumb2: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        headlines: MutableSequence[AdTextAsset] = ...,
        long_headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        call_to_actions: MutableSequence[AdTextAsset] = ...,
        videos: MutableSequence[AdVideoAsset] = ...,
        companion_banners: MutableSequence[AdImageAsset] = ...,
        breadcrumb1: str = ...,
        breadcrumb2: str = ...,
    ) -> None: ...

class VideoTrueViewInStreamAdInfo(proto.Message):
    action_button_label: str
    action_headline: str
    companion_banner: AdImageAsset
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        action_button_label: str = ...,
        action_headline: str = ...,
        companion_banner: AdImageAsset = ...,
    ) -> None: ...
