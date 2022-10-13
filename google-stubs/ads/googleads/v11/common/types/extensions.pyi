from typing import Any

import proto

from google.ads.googleads.v11.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v11.common.types.feed_common import Money
from google.ads.googleads.v11.enums.types.app_store import AppStoreEnum
from google.ads.googleads.v11.enums.types.call_conversion_reporting_state import (
    CallConversionReportingStateEnum,
)
from google.ads.googleads.v11.enums.types.price_extension_price_qualifier import (
    PriceExtensionPriceQualifierEnum,
)
from google.ads.googleads.v11.enums.types.price_extension_price_unit import (
    PriceExtensionPriceUnitEnum,
)
from google.ads.googleads.v11.enums.types.price_extension_type import (
    PriceExtensionTypeEnum,
)
from google.ads.googleads.v11.enums.types.promotion_extension_discount_modifier import (
    PromotionExtensionDiscountModifierEnum,
)
from google.ads.googleads.v11.enums.types.promotion_extension_occasion import (
    PromotionExtensionOccasionEnum,
)

class AffiliateLocationFeedItem(proto.Message):
    business_name: str
    address_line_1: str
    address_line_2: str
    city: str
    province: str
    postal_code: str
    country_code: str
    phone_number: str
    chain_id: int
    chain_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        business_name: str = ...,
        address_line_1: str = ...,
        address_line_2: str = ...,
        city: str = ...,
        province: str = ...,
        postal_code: str = ...,
        country_code: str = ...,
        phone_number: str = ...,
        chain_id: int = ...,
        chain_name: str = ...
    ) -> None: ...

class AppFeedItem(proto.Message):
    link_text: str
    app_id: str
    app_store: AppStoreEnum.AppStore
    final_urls: list[str]
    final_mobile_urls: list[str]
    tracking_url_template: str
    url_custom_parameters: list[CustomParameter]
    final_url_suffix: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        link_text: str = ...,
        app_id: str = ...,
        app_store: AppStoreEnum.AppStore = ...,
        final_urls: list[str] = ...,
        final_mobile_urls: list[str] = ...,
        tracking_url_template: str = ...,
        url_custom_parameters: list[CustomParameter] = ...,
        final_url_suffix: str = ...
    ) -> None: ...

class CallFeedItem(proto.Message):
    phone_number: str
    country_code: str
    call_tracking_enabled: bool
    call_conversion_action: str
    call_conversion_tracking_disabled: bool
    call_conversion_reporting_state: CallConversionReportingStateEnum.CallConversionReportingState
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        phone_number: str = ...,
        country_code: str = ...,
        call_tracking_enabled: bool = ...,
        call_conversion_action: str = ...,
        call_conversion_tracking_disabled: bool = ...,
        call_conversion_reporting_state: CallConversionReportingStateEnum.CallConversionReportingState = ...
    ) -> None: ...

class CalloutFeedItem(proto.Message):
    callout_text: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        callout_text: str = ...
    ) -> None: ...

class HotelCalloutFeedItem(proto.Message):
    text: str
    language_code: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        text: str = ...,
        language_code: str = ...
    ) -> None: ...

class ImageFeedItem(proto.Message):
    image_asset: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        image_asset: str = ...
    ) -> None: ...

class LocationFeedItem(proto.Message):
    business_name: str
    address_line_1: str
    address_line_2: str
    city: str
    province: str
    postal_code: str
    country_code: str
    phone_number: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        business_name: str = ...,
        address_line_1: str = ...,
        address_line_2: str = ...,
        city: str = ...,
        province: str = ...,
        postal_code: str = ...,
        country_code: str = ...,
        phone_number: str = ...
    ) -> None: ...

class PriceFeedItem(proto.Message):
    type_: PriceExtensionTypeEnum.PriceExtensionType
    price_qualifier: PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    tracking_url_template: str
    language_code: str
    price_offerings: list[PriceOffer]
    final_url_suffix: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        type_: PriceExtensionTypeEnum.PriceExtensionType = ...,
        price_qualifier: PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier = ...,
        tracking_url_template: str = ...,
        language_code: str = ...,
        price_offerings: list[PriceOffer] = ...,
        final_url_suffix: str = ...
    ) -> None: ...

class PriceOffer(proto.Message):
    header: str
    description: str
    price: Money
    unit: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    final_urls: list[str]
    final_mobile_urls: list[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        header: str = ...,
        description: str = ...,
        price: Money = ...,
        unit: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit = ...,
        final_urls: list[str] = ...,
        final_mobile_urls: list[str] = ...
    ) -> None: ...

class PromotionFeedItem(proto.Message):
    promotion_target: str
    discount_modifier: PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    promotion_start_date: str
    promotion_end_date: str
    occasion: PromotionExtensionOccasionEnum.PromotionExtensionOccasion
    final_urls: list[str]
    final_mobile_urls: list[str]
    tracking_url_template: str
    url_custom_parameters: list[CustomParameter]
    final_url_suffix: str
    language_code: str
    percent_off: int
    money_amount_off: Money
    promotion_code: str
    orders_over_amount: Money
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        promotion_target: str = ...,
        discount_modifier: PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier = ...,
        promotion_start_date: str = ...,
        promotion_end_date: str = ...,
        occasion: PromotionExtensionOccasionEnum.PromotionExtensionOccasion = ...,
        final_urls: list[str] = ...,
        final_mobile_urls: list[str] = ...,
        tracking_url_template: str = ...,
        url_custom_parameters: list[CustomParameter] = ...,
        final_url_suffix: str = ...,
        language_code: str = ...,
        percent_off: int = ...,
        money_amount_off: Money = ...,
        promotion_code: str = ...,
        orders_over_amount: Money = ...
    ) -> None: ...

class SitelinkFeedItem(proto.Message):
    link_text: str
    line1: str
    line2: str
    final_urls: list[str]
    final_mobile_urls: list[str]
    tracking_url_template: str
    url_custom_parameters: list[CustomParameter]
    final_url_suffix: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        link_text: str = ...,
        line1: str = ...,
        line2: str = ...,
        final_urls: list[str] = ...,
        final_mobile_urls: list[str] = ...,
        tracking_url_template: str = ...,
        url_custom_parameters: list[CustomParameter] = ...,
        final_url_suffix: str = ...
    ) -> None: ...

class StructuredSnippetFeedItem(proto.Message):
    header: str
    values: list[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        header: str = ...,
        values: list[str] = ...
    ) -> None: ...

class TextMessageFeedItem(proto.Message):
    business_name: str
    country_code: str
    phone_number: str
    text: str
    extension_text: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        business_name: str = ...,
        country_code: str = ...,
        phone_number: str = ...,
        text: str = ...,
        extension_text: str = ...
    ) -> None: ...
