from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v14.common.types.feed_common import Money
from google.ads.googleads.v14.enums.types.app_store import AppStoreEnum
from google.ads.googleads.v14.enums.types.call_conversion_reporting_state import (
    CallConversionReportingStateEnum,
)
from google.ads.googleads.v14.enums.types.price_extension_price_qualifier import (
    PriceExtensionPriceQualifierEnum,
)
from google.ads.googleads.v14.enums.types.price_extension_price_unit import (
    PriceExtensionPriceUnitEnum,
)
from google.ads.googleads.v14.enums.types.price_extension_type import (
    PriceExtensionTypeEnum,
)
from google.ads.googleads.v14.enums.types.promotion_extension_discount_modifier import (
    PromotionExtensionDiscountModifierEnum,
)
from google.ads.googleads.v14.enums.types.promotion_extension_occasion import (
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
        chain_name: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "business_name",
            "address_line_1",
            "address_line_2",
            "city",
            "province",
            "postal_code",
            "country_code",
            "phone_number",
            "chain_id",
            "chain_name",
        ],
    ) -> bool: ...

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
        final_url_suffix: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "link_text",
            "app_id",
            "app_store",
            "final_urls",
            "final_mobile_urls",
            "tracking_url_template",
            "url_custom_parameters",
            "final_url_suffix",
        ],
    ) -> bool: ...

class CallFeedItem(proto.Message):
    phone_number: str
    country_code: str
    call_tracking_enabled: bool
    call_conversion_action: str
    call_conversion_tracking_disabled: bool
    call_conversion_reporting_state: (
        CallConversionReportingStateEnum.CallConversionReportingState
    )
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
        call_conversion_reporting_state: CallConversionReportingStateEnum.CallConversionReportingState = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "phone_number",
            "country_code",
            "call_tracking_enabled",
            "call_conversion_action",
            "call_conversion_tracking_disabled",
            "call_conversion_reporting_state",
        ],
    ) -> bool: ...

class CalloutFeedItem(proto.Message):
    callout_text: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        callout_text: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["callout_text"]
    ) -> bool: ...

class HotelCalloutFeedItem(proto.Message):
    text: str
    language_code: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        text: str = ...,
        language_code: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["text", "language_code"]
    ) -> bool: ...

class ImageFeedItem(proto.Message):
    image_asset: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        image_asset: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["image_asset"]
    ) -> bool: ...

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
        phone_number: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "business_name",
            "address_line_1",
            "address_line_2",
            "city",
            "province",
            "postal_code",
            "country_code",
            "phone_number",
        ],
    ) -> bool: ...

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
        final_url_suffix: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "type_",
            "price_qualifier",
            "tracking_url_template",
            "language_code",
            "price_offerings",
            "final_url_suffix",
        ],
    ) -> bool: ...

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
        final_mobile_urls: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "header", "description", "price", "unit", "final_urls", "final_mobile_urls"
        ],
    ) -> bool: ...

class PromotionFeedItem(proto.Message):
    promotion_target: str
    discount_modifier: (
        PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    )
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
        orders_over_amount: Money = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "promotion_target",
            "discount_modifier",
            "promotion_start_date",
            "promotion_end_date",
            "occasion",
            "final_urls",
            "final_mobile_urls",
            "tracking_url_template",
            "url_custom_parameters",
            "final_url_suffix",
            "language_code",
            "percent_off",
            "money_amount_off",
            "promotion_code",
            "orders_over_amount",
        ],
    ) -> bool: ...

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
        final_url_suffix: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "link_text",
            "line1",
            "line2",
            "final_urls",
            "final_mobile_urls",
            "tracking_url_template",
            "url_custom_parameters",
            "final_url_suffix",
        ],
    ) -> bool: ...

class StructuredSnippetFeedItem(proto.Message):
    header: str
    values: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        header: str = ...,
        values: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["header", "values"]
    ) -> bool: ...

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
        extension_text: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "business_name", "country_code", "phone_number", "text", "extension_text"
        ],
    ) -> bool: ...
