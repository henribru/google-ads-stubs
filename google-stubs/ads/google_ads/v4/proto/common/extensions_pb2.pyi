# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    overload as typing___overload,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v4.proto.common.custom_parameter_pb2 import (
    CustomParameter as google___ads___googleads___v4___common___custom_parameter_pb2___CustomParameter,
)
from google.ads.google_ads.v4.proto.common.feed_common_pb2 import (
    Money as google___ads___googleads___v4___common___feed_common_pb2___Money,
)
from google.ads.google_ads.v4.proto.enums.app_store_pb2 import (
    AppStoreEnum as google___ads___googleads___v4___enums___app_store_pb2___AppStoreEnum,
)
from google.ads.google_ads.v4.proto.enums.call_conversion_reporting_state_pb2 import (
    CallConversionReportingStateEnum as google___ads___googleads___v4___enums___call_conversion_reporting_state_pb2___CallConversionReportingStateEnum,
)
from google.ads.google_ads.v4.proto.enums.price_extension_price_qualifier_pb2 import (
    PriceExtensionPriceQualifierEnum as google___ads___googleads___v4___enums___price_extension_price_qualifier_pb2___PriceExtensionPriceQualifierEnum,
)
from google.ads.google_ads.v4.proto.enums.price_extension_price_unit_pb2 import (
    PriceExtensionPriceUnitEnum as google___ads___googleads___v4___enums___price_extension_price_unit_pb2___PriceExtensionPriceUnitEnum,
)
from google.ads.google_ads.v4.proto.enums.price_extension_type_pb2 import (
    PriceExtensionTypeEnum as google___ads___googleads___v4___enums___price_extension_type_pb2___PriceExtensionTypeEnum,
)
from google.ads.google_ads.v4.proto.enums.promotion_extension_discount_modifier_pb2 import (
    PromotionExtensionDiscountModifierEnum as google___ads___googleads___v4___enums___promotion_extension_discount_modifier_pb2___PromotionExtensionDiscountModifierEnum,
)
from google.ads.google_ads.v4.proto.enums.promotion_extension_occasion_pb2 import (
    PromotionExtensionOccasionEnum as google___ads___googleads___v4___enums___promotion_extension_occasion_pb2___PromotionExtensionOccasionEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class AppFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    app_store: google___ads___googleads___v4___enums___app_store_pb2___AppStoreEnum.AppStoreValue = ...
    @property
    def link_text(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def app_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def final_urls(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def final_mobile_urls(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def tracking_url_template(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def url_custom_parameters(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v4___common___custom_parameter_pb2___CustomParameter
    ]: ...
    @property
    def final_url_suffix(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        link_text: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        app_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        app_store: typing___Optional[
            google___ads___googleads___v4___enums___app_store_pb2___AppStoreEnum.AppStoreValue
        ] = None,
        final_urls: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        final_mobile_urls: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        tracking_url_template: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        url_custom_parameters: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v4___common___custom_parameter_pb2___CustomParameter
            ]
        ] = None,
        final_url_suffix: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "app_id",
            b"app_id",
            "final_url_suffix",
            b"final_url_suffix",
            "link_text",
            b"link_text",
            "tracking_url_template",
            b"tracking_url_template",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "app_id",
            b"app_id",
            "app_store",
            b"app_store",
            "final_mobile_urls",
            b"final_mobile_urls",
            "final_url_suffix",
            b"final_url_suffix",
            "final_urls",
            b"final_urls",
            "link_text",
            b"link_text",
            "tracking_url_template",
            b"tracking_url_template",
            "url_custom_parameters",
            b"url_custom_parameters",
        ],
    ) -> None: ...

type___AppFeedItem = AppFeedItem

class CallFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    call_conversion_reporting_state: google___ads___googleads___v4___enums___call_conversion_reporting_state_pb2___CallConversionReportingStateEnum.CallConversionReportingStateValue = ...
    @property
    def phone_number(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def country_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def call_tracking_enabled(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def call_conversion_action(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def call_conversion_tracking_disabled(
        self,
    ) -> google___protobuf___wrappers_pb2___BoolValue: ...
    def __init__(
        self,
        *,
        phone_number: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        country_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        call_tracking_enabled: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        call_conversion_action: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        call_conversion_tracking_disabled: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        call_conversion_reporting_state: typing___Optional[
            google___ads___googleads___v4___enums___call_conversion_reporting_state_pb2___CallConversionReportingStateEnum.CallConversionReportingStateValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "call_conversion_action",
            b"call_conversion_action",
            "call_conversion_tracking_disabled",
            b"call_conversion_tracking_disabled",
            "call_tracking_enabled",
            b"call_tracking_enabled",
            "country_code",
            b"country_code",
            "phone_number",
            b"phone_number",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "call_conversion_action",
            b"call_conversion_action",
            "call_conversion_reporting_state",
            b"call_conversion_reporting_state",
            "call_conversion_tracking_disabled",
            b"call_conversion_tracking_disabled",
            "call_tracking_enabled",
            b"call_tracking_enabled",
            "country_code",
            b"country_code",
            "phone_number",
            b"phone_number",
        ],
    ) -> None: ...

type___CallFeedItem = CallFeedItem

class CalloutFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def callout_text(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        callout_text: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["callout_text", b"callout_text"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["callout_text", b"callout_text"]
    ) -> None: ...

type___CalloutFeedItem = CalloutFeedItem

class LocationFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def business_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def address_line_1(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def address_line_2(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def city(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def province(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def postal_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def country_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def phone_number(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        business_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        address_line_1: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        address_line_2: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        city: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        province: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        postal_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        country_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        phone_number: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "address_line_1",
            b"address_line_1",
            "address_line_2",
            b"address_line_2",
            "business_name",
            b"business_name",
            "city",
            b"city",
            "country_code",
            b"country_code",
            "phone_number",
            b"phone_number",
            "postal_code",
            b"postal_code",
            "province",
            b"province",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "address_line_1",
            b"address_line_1",
            "address_line_2",
            b"address_line_2",
            "business_name",
            b"business_name",
            "city",
            b"city",
            "country_code",
            b"country_code",
            "phone_number",
            b"phone_number",
            "postal_code",
            b"postal_code",
            "province",
            b"province",
        ],
    ) -> None: ...

type___LocationFeedItem = LocationFeedItem

class AffiliateLocationFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def business_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def address_line_1(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def address_line_2(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def city(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def province(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def postal_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def country_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def phone_number(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def chain_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def chain_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        business_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        address_line_1: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        address_line_2: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        city: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        province: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        postal_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        country_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        phone_number: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        chain_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        chain_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "address_line_1",
            b"address_line_1",
            "address_line_2",
            b"address_line_2",
            "business_name",
            b"business_name",
            "chain_id",
            b"chain_id",
            "chain_name",
            b"chain_name",
            "city",
            b"city",
            "country_code",
            b"country_code",
            "phone_number",
            b"phone_number",
            "postal_code",
            b"postal_code",
            "province",
            b"province",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "address_line_1",
            b"address_line_1",
            "address_line_2",
            b"address_line_2",
            "business_name",
            b"business_name",
            "chain_id",
            b"chain_id",
            "chain_name",
            b"chain_name",
            "city",
            b"city",
            "country_code",
            b"country_code",
            "phone_number",
            b"phone_number",
            "postal_code",
            b"postal_code",
            "province",
            b"province",
        ],
    ) -> None: ...

type___AffiliateLocationFeedItem = AffiliateLocationFeedItem

class TextMessageFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def business_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def country_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def phone_number(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def text(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def extension_text(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        business_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        country_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        phone_number: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        text: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        extension_text: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "business_name",
            b"business_name",
            "country_code",
            b"country_code",
            "extension_text",
            b"extension_text",
            "phone_number",
            b"phone_number",
            "text",
            b"text",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "business_name",
            b"business_name",
            "country_code",
            b"country_code",
            "extension_text",
            b"extension_text",
            "phone_number",
            b"phone_number",
            "text",
            b"text",
        ],
    ) -> None: ...

type___TextMessageFeedItem = TextMessageFeedItem

class PriceFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type: google___ads___googleads___v4___enums___price_extension_type_pb2___PriceExtensionTypeEnum.PriceExtensionTypeValue = ...
    price_qualifier: google___ads___googleads___v4___enums___price_extension_price_qualifier_pb2___PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifierValue = ...
    @property
    def tracking_url_template(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def language_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def price_offerings(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___PriceOffer
    ]: ...
    @property
    def final_url_suffix(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        type: typing___Optional[
            google___ads___googleads___v4___enums___price_extension_type_pb2___PriceExtensionTypeEnum.PriceExtensionTypeValue
        ] = None,
        price_qualifier: typing___Optional[
            google___ads___googleads___v4___enums___price_extension_price_qualifier_pb2___PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifierValue
        ] = None,
        tracking_url_template: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        language_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        price_offerings: typing___Optional[typing___Iterable[type___PriceOffer]] = None,
        final_url_suffix: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "final_url_suffix",
            b"final_url_suffix",
            "language_code",
            b"language_code",
            "tracking_url_template",
            b"tracking_url_template",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "final_url_suffix",
            b"final_url_suffix",
            "language_code",
            b"language_code",
            "price_offerings",
            b"price_offerings",
            "price_qualifier",
            b"price_qualifier",
            "tracking_url_template",
            b"tracking_url_template",
            "type",
            b"type",
        ],
    ) -> None: ...

type___PriceFeedItem = PriceFeedItem

class PriceOffer(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    unit: google___ads___googleads___v4___enums___price_extension_price_unit_pb2___PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue = ...
    @property
    def header(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def description(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def price(
        self,
    ) -> google___ads___googleads___v4___common___feed_common_pb2___Money: ...
    @property
    def final_urls(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def final_mobile_urls(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    def __init__(
        self,
        *,
        header: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        description: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        price: typing___Optional[
            google___ads___googleads___v4___common___feed_common_pb2___Money
        ] = None,
        unit: typing___Optional[
            google___ads___googleads___v4___enums___price_extension_price_unit_pb2___PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue
        ] = None,
        final_urls: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        final_mobile_urls: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "description", b"description", "header", b"header", "price", b"price"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "description",
            b"description",
            "final_mobile_urls",
            b"final_mobile_urls",
            "final_urls",
            b"final_urls",
            "header",
            b"header",
            "price",
            b"price",
            "unit",
            b"unit",
        ],
    ) -> None: ...

type___PriceOffer = PriceOffer

class PromotionFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    discount_modifier: google___ads___googleads___v4___enums___promotion_extension_discount_modifier_pb2___PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifierValue = ...
    occasion: google___ads___googleads___v4___enums___promotion_extension_occasion_pb2___PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue = ...
    @property
    def promotion_target(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def promotion_start_date(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def promotion_end_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def final_urls(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def final_mobile_urls(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def tracking_url_template(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def url_custom_parameters(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v4___common___custom_parameter_pb2___CustomParameter
    ]: ...
    @property
    def final_url_suffix(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def language_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def percent_off(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def money_amount_off(
        self,
    ) -> google___ads___googleads___v4___common___feed_common_pb2___Money: ...
    @property
    def promotion_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def orders_over_amount(
        self,
    ) -> google___ads___googleads___v4___common___feed_common_pb2___Money: ...
    def __init__(
        self,
        *,
        promotion_target: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        discount_modifier: typing___Optional[
            google___ads___googleads___v4___enums___promotion_extension_discount_modifier_pb2___PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifierValue
        ] = None,
        promotion_start_date: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        promotion_end_date: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        occasion: typing___Optional[
            google___ads___googleads___v4___enums___promotion_extension_occasion_pb2___PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue
        ] = None,
        final_urls: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        final_mobile_urls: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        tracking_url_template: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        url_custom_parameters: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v4___common___custom_parameter_pb2___CustomParameter
            ]
        ] = None,
        final_url_suffix: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        language_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        percent_off: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        money_amount_off: typing___Optional[
            google___ads___googleads___v4___common___feed_common_pb2___Money
        ] = None,
        promotion_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        orders_over_amount: typing___Optional[
            google___ads___googleads___v4___common___feed_common_pb2___Money
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "discount_type",
            b"discount_type",
            "final_url_suffix",
            b"final_url_suffix",
            "language_code",
            b"language_code",
            "money_amount_off",
            b"money_amount_off",
            "orders_over_amount",
            b"orders_over_amount",
            "percent_off",
            b"percent_off",
            "promotion_code",
            b"promotion_code",
            "promotion_end_date",
            b"promotion_end_date",
            "promotion_start_date",
            b"promotion_start_date",
            "promotion_target",
            b"promotion_target",
            "promotion_trigger",
            b"promotion_trigger",
            "tracking_url_template",
            b"tracking_url_template",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "discount_modifier",
            b"discount_modifier",
            "discount_type",
            b"discount_type",
            "final_mobile_urls",
            b"final_mobile_urls",
            "final_url_suffix",
            b"final_url_suffix",
            "final_urls",
            b"final_urls",
            "language_code",
            b"language_code",
            "money_amount_off",
            b"money_amount_off",
            "occasion",
            b"occasion",
            "orders_over_amount",
            b"orders_over_amount",
            "percent_off",
            b"percent_off",
            "promotion_code",
            b"promotion_code",
            "promotion_end_date",
            b"promotion_end_date",
            "promotion_start_date",
            b"promotion_start_date",
            "promotion_target",
            b"promotion_target",
            "promotion_trigger",
            b"promotion_trigger",
            "tracking_url_template",
            b"tracking_url_template",
            "url_custom_parameters",
            b"url_custom_parameters",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["discount_type", b"discount_type"],
    ) -> typing_extensions___Literal["percent_off", "money_amount_off"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "promotion_trigger", b"promotion_trigger"
        ],
    ) -> typing_extensions___Literal["promotion_code", "orders_over_amount"]: ...

type___PromotionFeedItem = PromotionFeedItem

class StructuredSnippetFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def header(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def values(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    def __init__(
        self,
        *,
        header: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        values: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["header", b"header"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "header", b"header", "values", b"values"
        ],
    ) -> None: ...

type___StructuredSnippetFeedItem = StructuredSnippetFeedItem

class SitelinkFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def link_text(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def line1(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def line2(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def final_urls(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def final_mobile_urls(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def tracking_url_template(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def url_custom_parameters(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v4___common___custom_parameter_pb2___CustomParameter
    ]: ...
    @property
    def final_url_suffix(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        link_text: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        line1: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        line2: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        final_urls: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        final_mobile_urls: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        tracking_url_template: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        url_custom_parameters: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v4___common___custom_parameter_pb2___CustomParameter
            ]
        ] = None,
        final_url_suffix: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "final_url_suffix",
            b"final_url_suffix",
            "line1",
            b"line1",
            "line2",
            b"line2",
            "link_text",
            b"link_text",
            "tracking_url_template",
            b"tracking_url_template",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "final_mobile_urls",
            b"final_mobile_urls",
            "final_url_suffix",
            b"final_url_suffix",
            "final_urls",
            b"final_urls",
            "line1",
            b"line1",
            "line2",
            b"line2",
            "link_text",
            b"link_text",
            "tracking_url_template",
            b"tracking_url_template",
            "url_custom_parameters",
            b"url_custom_parameters",
        ],
    ) -> None: ...

type___SitelinkFeedItem = SitelinkFeedItem

class HotelCalloutFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def text(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def language_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        text: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        language_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "language_code", b"language_code", "text", b"text"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "language_code", b"language_code", "text", b"text"
        ],
    ) -> None: ...

type___HotelCalloutFeedItem = HotelCalloutFeedItem
