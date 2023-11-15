from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v15.common.types.feed_common import Money
from google.ads.googleads.v15.enums.types.app_store import AppStoreEnum
from google.ads.googleads.v15.enums.types.call_conversion_reporting_state import (
    CallConversionReportingStateEnum,
)
from google.ads.googleads.v15.enums.types.price_extension_price_qualifier import (
    PriceExtensionPriceQualifierEnum,
)
from google.ads.googleads.v15.enums.types.price_extension_price_unit import (
    PriceExtensionPriceUnitEnum,
)
from google.ads.googleads.v15.enums.types.price_extension_type import (
    PriceExtensionTypeEnum,
)
from google.ads.googleads.v15.enums.types.promotion_extension_discount_modifier import (
    PromotionExtensionDiscountModifierEnum,
)
from google.ads.googleads.v15.enums.types.promotion_extension_occasion import (
    PromotionExtensionOccasionEnum,
)

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    url_custom_parameters: MutableSequence[CustomParameter]
    final_url_suffix: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        link_text: str = ...,
        app_id: str = ...,
        app_store: AppStoreEnum.AppStore = ...,
        final_urls: MutableSequence[str] = ...,
        final_mobile_urls: MutableSequence[str] = ...,
        tracking_url_template: str = ...,
        url_custom_parameters: MutableSequence[CustomParameter] = ...,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        callout_text: str = ...
    ) -> None: ...

class HotelCalloutFeedItem(proto.Message):
    text: str
    language_code: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        text: str = ...,
        language_code: str = ...
    ) -> None: ...

class ImageFeedItem(proto.Message):
    image_asset: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
    price_offerings: MutableSequence[PriceOffer]
    final_url_suffix: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: PriceExtensionTypeEnum.PriceExtensionType = ...,
        price_qualifier: PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier = ...,
        tracking_url_template: str = ...,
        language_code: str = ...,
        price_offerings: MutableSequence[PriceOffer] = ...,
        final_url_suffix: str = ...
    ) -> None: ...

class PriceOffer(proto.Message):
    header: str
    description: str
    price: Money
    unit: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        header: str = ...,
        description: str = ...,
        price: Money = ...,
        unit: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit = ...,
        final_urls: MutableSequence[str] = ...,
        final_mobile_urls: MutableSequence[str] = ...
    ) -> None: ...

class PromotionFeedItem(proto.Message):
    promotion_target: str
    discount_modifier: PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    promotion_start_date: str
    promotion_end_date: str
    occasion: PromotionExtensionOccasionEnum.PromotionExtensionOccasion
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    url_custom_parameters: MutableSequence[CustomParameter]
    final_url_suffix: str
    language_code: str
    percent_off: int
    money_amount_off: Money
    promotion_code: str
    orders_over_amount: Money
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        promotion_target: str = ...,
        discount_modifier: PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier = ...,
        promotion_start_date: str = ...,
        promotion_end_date: str = ...,
        occasion: PromotionExtensionOccasionEnum.PromotionExtensionOccasion = ...,
        final_urls: MutableSequence[str] = ...,
        final_mobile_urls: MutableSequence[str] = ...,
        tracking_url_template: str = ...,
        url_custom_parameters: MutableSequence[CustomParameter] = ...,
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
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    url_custom_parameters: MutableSequence[CustomParameter]
    final_url_suffix: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        link_text: str = ...,
        line1: str = ...,
        line2: str = ...,
        final_urls: MutableSequence[str] = ...,
        final_mobile_urls: MutableSequence[str] = ...,
        tracking_url_template: str = ...,
        url_custom_parameters: MutableSequence[CustomParameter] = ...,
        final_url_suffix: str = ...
    ) -> None: ...

class StructuredSnippetFeedItem(proto.Message):
    header: str
    values: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        header: str = ...,
        values: MutableSequence[str] = ...
    ) -> None: ...

class TextMessageFeedItem(proto.Message):
    business_name: str
    country_code: str
    phone_number: str
    text: str
    extension_text: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        business_name: str = ...,
        country_code: str = ...,
        phone_number: str = ...,
        text: str = ...,
        extension_text: str = ...
    ) -> None: ...
