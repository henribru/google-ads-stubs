from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.common.types.ad_asset import (
    AdCallToActionAsset,
    AdDiscoveryCarouselCardAsset,
    AdImageAsset,
    AdMediaBundleAsset,
    AdTextAsset,
    AdVideoAsset,
)
from google.ads.googleads.v15.enums.types.call_conversion_reporting_state import (
    CallConversionReportingStateEnum,
)
from google.ads.googleads.v15.enums.types.display_ad_format_setting import (
    DisplayAdFormatSettingEnum,
)
from google.ads.googleads.v15.enums.types.display_upload_product_type import (
    DisplayUploadProductTypeEnum,
)
from google.ads.googleads.v15.enums.types.legacy_app_install_ad_app_store import (
    LegacyAppInstallAdAppStoreEnum,
)
from google.ads.googleads.v15.enums.types.mime_type import MimeTypeEnum
from google.ads.googleads.v15.enums.types.video_thumbnail import VideoThumbnailEnum

_M = TypeVar("_M")

class AppAdInfo(proto.Message):
    mandatory_ad_text: AdTextAsset
    headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    images: MutableSequence[AdImageAsset]
    youtube_videos: MutableSequence[AdVideoAsset]
    html5_media_bundles: MutableSequence[AdMediaBundleAsset]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        mandatory_ad_text: AdTextAsset = ...,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        images: MutableSequence[AdImageAsset] = ...,
        youtube_videos: MutableSequence[AdVideoAsset] = ...,
        html5_media_bundles: MutableSequence[AdMediaBundleAsset] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "mandatory_ad_text",
            "headlines",
            "descriptions",
            "images",
            "youtube_videos",
            "html5_media_bundles",
        ],
    ) -> bool: ...

class AppEngagementAdInfo(proto.Message):
    headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    images: MutableSequence[AdImageAsset]
    videos: MutableSequence[AdVideoAsset]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        images: MutableSequence[AdImageAsset] = ...,
        videos: MutableSequence[AdVideoAsset] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["headlines", "descriptions", "images", "videos"]
    ) -> bool: ...

class AppPreRegistrationAdInfo(proto.Message):
    headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    images: MutableSequence[AdImageAsset]
    youtube_videos: MutableSequence[AdVideoAsset]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        images: MutableSequence[AdImageAsset] = ...,
        youtube_videos: MutableSequence[AdVideoAsset] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["headlines", "descriptions", "images", "youtube_videos"]
    ) -> bool: ...

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
    conversion_reporting_state: (
        CallConversionReportingStateEnum.CallConversionReportingState
    )
    path1: str
    path2: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "country_code",
            "phone_number",
            "business_name",
            "headline1",
            "headline2",
            "description1",
            "description2",
            "call_tracked",
            "disable_call_conversion",
            "phone_number_verification_url",
            "conversion_action",
            "conversion_reporting_state",
            "path1",
            "path2",
        ],
    ) -> bool: ...

class DiscoveryCarouselAdInfo(proto.Message):
    business_name: str
    logo_image: AdImageAsset
    headline: AdTextAsset
    description: AdTextAsset
    call_to_action_text: str
    carousel_cards: MutableSequence[AdDiscoveryCarouselCardAsset]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        business_name: str = ...,
        logo_image: AdImageAsset = ...,
        headline: AdTextAsset = ...,
        description: AdTextAsset = ...,
        call_to_action_text: str = ...,
        carousel_cards: MutableSequence[AdDiscoveryCarouselCardAsset] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "business_name",
            "logo_image",
            "headline",
            "description",
            "call_to_action_text",
            "carousel_cards",
        ],
    ) -> bool: ...

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "marketing_images",
            "square_marketing_images",
            "portrait_marketing_images",
            "logo_images",
            "headlines",
            "descriptions",
            "business_name",
            "call_to_action_text",
            "lead_form_only",
        ],
    ) -> bool: ...

class DiscoveryVideoResponsiveAdInfo(proto.Message):
    headlines: MutableSequence[AdTextAsset]
    long_headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    videos: MutableSequence[AdVideoAsset]
    logo_images: MutableSequence[AdImageAsset]
    breadcrumb1: str
    breadcrumb2: str
    business_name: AdTextAsset
    call_to_actions: MutableSequence[AdCallToActionAsset]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        headlines: MutableSequence[AdTextAsset] = ...,
        long_headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        videos: MutableSequence[AdVideoAsset] = ...,
        logo_images: MutableSequence[AdImageAsset] = ...,
        breadcrumb1: str = ...,
        breadcrumb2: str = ...,
        business_name: AdTextAsset = ...,
        call_to_actions: MutableSequence[AdCallToActionAsset] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "headlines",
            "long_headlines",
            "descriptions",
            "videos",
            "logo_images",
            "breadcrumb1",
            "breadcrumb2",
            "business_name",
            "call_to_actions",
        ],
    ) -> bool: ...

class DisplayUploadAdInfo(proto.Message):
    display_upload_product_type: DisplayUploadProductTypeEnum.DisplayUploadProductType
    media_bundle: AdMediaBundleAsset
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        display_upload_product_type: DisplayUploadProductTypeEnum.DisplayUploadProductType = ...,
        media_bundle: AdMediaBundleAsset = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["display_upload_product_type", "media_bundle"]
    ) -> bool: ...

class ExpandedDynamicSearchAdInfo(proto.Message):
    description: str
    description2: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        description: str = ...,
        description2: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["description", "description2"]
    ) -> bool: ...

class ExpandedTextAdInfo(proto.Message):
    headline_part1: str
    headline_part2: str
    headline_part3: str
    description: str
    description2: str
    path1: str
    path2: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        headline_part1: str = ...,
        headline_part2: str = ...,
        headline_part3: str = ...,
        description: str = ...,
        description2: str = ...,
        path1: str = ...,
        path2: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "headline_part1",
            "headline_part2",
            "headline_part3",
            "description",
            "description2",
            "path1",
            "path2",
        ],
    ) -> bool: ...

class HotelAdInfo(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

class ImageAdInfo(proto.Message):
    pixel_width: int
    pixel_height: int
    image_url: str
    preview_pixel_width: int
    preview_pixel_height: int
    preview_image_url: str
    mime_type: MimeTypeEnum.MimeType
    name: str
    image_asset: AdImageAsset
    data: bytes
    ad_id_to_copy_image_from: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        pixel_width: int = ...,
        pixel_height: int = ...,
        image_url: str = ...,
        preview_pixel_width: int = ...,
        preview_pixel_height: int = ...,
        preview_image_url: str = ...,
        mime_type: MimeTypeEnum.MimeType = ...,
        name: str = ...,
        image_asset: AdImageAsset = ...,
        data: bytes = ...,
        ad_id_to_copy_image_from: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "pixel_width",
            "pixel_height",
            "image_url",
            "preview_pixel_width",
            "preview_pixel_height",
            "preview_image_url",
            "mime_type",
            "name",
            "image_asset",
            "data",
            "ad_id_to_copy_image_from",
        ],
    ) -> bool: ...

class InFeedVideoAdInfo(proto.Message):
    headline: str
    description1: str
    description2: str
    thumbnail: VideoThumbnailEnum.VideoThumbnail
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        headline: str = ...,
        description1: str = ...,
        description2: str = ...,
        thumbnail: VideoThumbnailEnum.VideoThumbnail = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["headline", "description1", "description2", "thumbnail"]
    ) -> bool: ...

class LegacyAppInstallAdInfo(proto.Message):
    app_id: str
    app_store: LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    headline: str
    description1: str
    description2: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        app_id: str = ...,
        app_store: LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore = ...,
        headline: str = ...,
        description1: str = ...,
        description2: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["app_id", "app_store", "headline", "description1", "description2"],
    ) -> bool: ...

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "short_headline",
            "long_headline",
            "description",
            "business_name",
            "allow_flexible_color",
            "accent_color",
            "main_color",
            "call_to_action_text",
            "logo_image",
            "square_logo_image",
            "marketing_image",
            "square_marketing_image",
            "format_setting",
            "price_prefix",
            "promo_text",
        ],
    ) -> bool: ...

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        call_to_actions: MutableSequence[AdTextAsset] = ...,
        marketing_images: MutableSequence[AdImageAsset] = ...,
        logo_images: MutableSequence[AdImageAsset] = ...,
        videos: MutableSequence[AdVideoAsset] = ...,
        path1: str = ...,
        path2: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "headlines",
            "descriptions",
            "call_to_actions",
            "marketing_images",
            "logo_images",
            "videos",
            "path1",
            "path2",
        ],
    ) -> bool: ...

class ResponsiveDisplayAdControlSpec(proto.Message):
    enable_asset_enhancements: bool
    enable_autogen_video: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        enable_asset_enhancements: bool = ...,
        enable_autogen_video: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["enable_asset_enhancements", "enable_autogen_video"]
    ) -> bool: ...

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "marketing_images",
            "square_marketing_images",
            "logo_images",
            "square_logo_images",
            "headlines",
            "long_headline",
            "descriptions",
            "youtube_videos",
            "business_name",
            "main_color",
            "accent_color",
            "allow_flexible_color",
            "call_to_action_text",
            "price_prefix",
            "promo_text",
            "format_setting",
            "control_spec",
        ],
    ) -> bool: ...

class ResponsiveSearchAdInfo(proto.Message):
    headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    path1: str
    path2: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        path1: str = ...,
        path2: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["headlines", "descriptions", "path1", "path2"]
    ) -> bool: ...

class ShoppingComparisonListingAdInfo(proto.Message):
    headline: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        headline: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["headline"]
    ) -> bool: ...

class ShoppingProductAdInfo(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

class ShoppingSmartAdInfo(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

class SmartCampaignAdInfo(proto.Message):
    headlines: MutableSequence[AdTextAsset]
    descriptions: MutableSequence[AdTextAsset]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["headlines", "descriptions"]
    ) -> bool: ...

class TextAdInfo(proto.Message):
    headline: str
    description1: str
    description2: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        headline: str = ...,
        description1: str = ...,
        description2: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["headline", "description1", "description2"]
    ) -> bool: ...

class TravelAdInfo(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

class VideoAdInfo(proto.Message):
    video: AdVideoAsset
    in_stream: VideoTrueViewInStreamAdInfo
    bumper: VideoBumperInStreamAdInfo
    out_stream: VideoOutstreamAdInfo
    non_skippable: VideoNonSkippableInStreamAdInfo
    in_feed: InFeedVideoAdInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        video: AdVideoAsset = ...,
        in_stream: VideoTrueViewInStreamAdInfo = ...,
        bumper: VideoBumperInStreamAdInfo = ...,
        out_stream: VideoOutstreamAdInfo = ...,
        non_skippable: VideoNonSkippableInStreamAdInfo = ...,
        in_feed: InFeedVideoAdInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "video", "in_stream", "bumper", "out_stream", "non_skippable", "in_feed"
        ],
    ) -> bool: ...

class VideoBumperInStreamAdInfo(proto.Message):
    companion_banner: AdImageAsset
    action_button_label: str
    action_headline: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        companion_banner: AdImageAsset = ...,
        action_button_label: str = ...,
        action_headline: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["companion_banner", "action_button_label", "action_headline"]
    ) -> bool: ...

class VideoNonSkippableInStreamAdInfo(proto.Message):
    companion_banner: AdImageAsset
    action_button_label: str
    action_headline: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        companion_banner: AdImageAsset = ...,
        action_button_label: str = ...,
        action_headline: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["companion_banner", "action_button_label", "action_headline"]
    ) -> bool: ...

class VideoOutstreamAdInfo(proto.Message):
    headline: str
    description: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        headline: str = ...,
        description: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["headline", "description"]
    ) -> bool: ...

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        headlines: MutableSequence[AdTextAsset] = ...,
        long_headlines: MutableSequence[AdTextAsset] = ...,
        descriptions: MutableSequence[AdTextAsset] = ...,
        call_to_actions: MutableSequence[AdTextAsset] = ...,
        videos: MutableSequence[AdVideoAsset] = ...,
        companion_banners: MutableSequence[AdImageAsset] = ...,
        breadcrumb1: str = ...,
        breadcrumb2: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "headlines",
            "long_headlines",
            "descriptions",
            "call_to_actions",
            "videos",
            "companion_banners",
            "breadcrumb1",
            "breadcrumb2",
        ],
    ) -> bool: ...

class VideoTrueViewInStreamAdInfo(proto.Message):
    action_button_label: str
    action_headline: str
    companion_banner: AdImageAsset
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        action_button_label: str = ...,
        action_headline: str = ...,
        companion_banner: AdImageAsset = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["action_button_label", "action_headline", "companion_banner"]
    ) -> bool: ...
