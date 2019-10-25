# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.common.custom_parameter_pb2 import (
    CustomParameter as google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter,
)

from google.ads.google_ads.v1.proto.common.feed_common_pb2 import (
    Money as google___ads___googleads___v1___common___feed_common_pb2___Money,
)

from google.ads.google_ads.v1.proto.enums.app_store_pb2 import (
    AppStoreEnum as google___ads___googleads___v1___enums___app_store_pb2___AppStoreEnum,
)

from google.ads.google_ads.v1.proto.enums.call_conversion_reporting_state_pb2 import (
    CallConversionReportingStateEnum as google___ads___googleads___v1___enums___call_conversion_reporting_state_pb2___CallConversionReportingStateEnum,
)

from google.ads.google_ads.v1.proto.enums.price_extension_price_qualifier_pb2 import (
    PriceExtensionPriceQualifierEnum as google___ads___googleads___v1___enums___price_extension_price_qualifier_pb2___PriceExtensionPriceQualifierEnum,
)

from google.ads.google_ads.v1.proto.enums.price_extension_price_unit_pb2 import (
    PriceExtensionPriceUnitEnum as google___ads___googleads___v1___enums___price_extension_price_unit_pb2___PriceExtensionPriceUnitEnum,
)

from google.ads.google_ads.v1.proto.enums.price_extension_type_pb2 import (
    PriceExtensionTypeEnum as google___ads___googleads___v1___enums___price_extension_type_pb2___PriceExtensionTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.promotion_extension_discount_modifier_pb2 import (
    PromotionExtensionDiscountModifierEnum as google___ads___googleads___v1___enums___promotion_extension_discount_modifier_pb2___PromotionExtensionDiscountModifierEnum,
)

from google.ads.google_ads.v1.proto.enums.promotion_extension_occasion_pb2 import (
    PromotionExtensionOccasionEnum as google___ads___googleads___v1___enums___promotion_extension_occasion_pb2___PromotionExtensionOccasionEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    overload as typing___overload,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class AppFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    app_store = ... # type: google___ads___googleads___v1___enums___app_store_pb2___AppStoreEnum.AppStore

    @property
    def link_text(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def app_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def final_urls(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    @property
    def final_mobile_urls(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    @property
    def tracking_url_template(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def url_custom_parameters(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter]: ...

    @property
    def final_url_suffix(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        link_text : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        app_id : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        app_store : typing___Optional[google___ads___googleads___v1___enums___app_store_pb2___AppStoreEnum.AppStore] = None,
        final_urls : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        final_mobile_urls : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        tracking_url_template : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        url_custom_parameters : typing___Optional[typing___Iterable[google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter]] = None,
        final_url_suffix : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AppFeedItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"app_id",u"final_url_suffix",u"link_text",u"tracking_url_template"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"app_id",u"app_store",u"final_mobile_urls",u"final_url_suffix",u"final_urls",u"link_text",u"tracking_url_template",u"url_custom_parameters"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"app_id",b"app_id",u"final_url_suffix",b"final_url_suffix",u"link_text",b"link_text",u"tracking_url_template",b"tracking_url_template"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"app_id",b"app_id",u"app_store",b"app_store",u"final_mobile_urls",b"final_mobile_urls",u"final_url_suffix",b"final_url_suffix",u"final_urls",b"final_urls",u"link_text",b"link_text",u"tracking_url_template",b"tracking_url_template",u"url_custom_parameters",b"url_custom_parameters"]) -> None: ...

class CallFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    call_conversion_reporting_state = ... # type: google___ads___googleads___v1___enums___call_conversion_reporting_state_pb2___CallConversionReportingStateEnum.CallConversionReportingState

    @property
    def phone_number(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def country_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def call_tracking_enabled(self) -> google___protobuf___wrappers_pb2___BoolValue: ...

    @property
    def call_conversion_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def call_conversion_tracking_disabled(self) -> google___protobuf___wrappers_pb2___BoolValue: ...

    def __init__(self,
        *,
        phone_number : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        country_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        call_tracking_enabled : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        call_conversion_action : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        call_conversion_tracking_disabled : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        call_conversion_reporting_state : typing___Optional[google___ads___googleads___v1___enums___call_conversion_reporting_state_pb2___CallConversionReportingStateEnum.CallConversionReportingState] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CallFeedItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"call_conversion_action",u"call_conversion_tracking_disabled",u"call_tracking_enabled",u"country_code",u"phone_number"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"call_conversion_action",u"call_conversion_reporting_state",u"call_conversion_tracking_disabled",u"call_tracking_enabled",u"country_code",u"phone_number"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"call_conversion_action",b"call_conversion_action",u"call_conversion_tracking_disabled",b"call_conversion_tracking_disabled",u"call_tracking_enabled",b"call_tracking_enabled",u"country_code",b"country_code",u"phone_number",b"phone_number"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"call_conversion_action",b"call_conversion_action",u"call_conversion_reporting_state",b"call_conversion_reporting_state",u"call_conversion_tracking_disabled",b"call_conversion_tracking_disabled",u"call_tracking_enabled",b"call_tracking_enabled",u"country_code",b"country_code",u"phone_number",b"phone_number"]) -> None: ...

class CalloutFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def callout_text(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        callout_text : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CalloutFeedItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"callout_text"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"callout_text"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"callout_text",b"callout_text"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"callout_text",b"callout_text"]) -> None: ...

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

    def __init__(self,
        *,
        business_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        address_line_1 : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        address_line_2 : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        city : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        province : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        postal_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        country_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        phone_number : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LocationFeedItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"address_line_1",u"address_line_2",u"business_name",u"city",u"country_code",u"phone_number",u"postal_code",u"province"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"address_line_1",u"address_line_2",u"business_name",u"city",u"country_code",u"phone_number",u"postal_code",u"province"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"address_line_1",b"address_line_1",u"address_line_2",b"address_line_2",u"business_name",b"business_name",u"city",b"city",u"country_code",b"country_code",u"phone_number",b"phone_number",u"postal_code",b"postal_code",u"province",b"province"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"address_line_1",b"address_line_1",u"address_line_2",b"address_line_2",u"business_name",b"business_name",u"city",b"city",u"country_code",b"country_code",u"phone_number",b"phone_number",u"postal_code",b"postal_code",u"province",b"province"]) -> None: ...

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

    def __init__(self,
        *,
        business_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        address_line_1 : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        address_line_2 : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        city : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        province : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        postal_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        country_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        phone_number : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        chain_id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        chain_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AffiliateLocationFeedItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"address_line_1",u"address_line_2",u"business_name",u"chain_id",u"chain_name",u"city",u"country_code",u"phone_number",u"postal_code",u"province"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"address_line_1",u"address_line_2",u"business_name",u"chain_id",u"chain_name",u"city",u"country_code",u"phone_number",u"postal_code",u"province"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"address_line_1",b"address_line_1",u"address_line_2",b"address_line_2",u"business_name",b"business_name",u"chain_id",b"chain_id",u"chain_name",b"chain_name",u"city",b"city",u"country_code",b"country_code",u"phone_number",b"phone_number",u"postal_code",b"postal_code",u"province",b"province"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"address_line_1",b"address_line_1",u"address_line_2",b"address_line_2",u"business_name",b"business_name",u"chain_id",b"chain_id",u"chain_name",b"chain_name",u"city",b"city",u"country_code",b"country_code",u"phone_number",b"phone_number",u"postal_code",b"postal_code",u"province",b"province"]) -> None: ...

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

    def __init__(self,
        *,
        business_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        country_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        phone_number : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        text : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        extension_text : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> TextMessageFeedItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"business_name",u"country_code",u"extension_text",u"phone_number",u"text"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"business_name",u"country_code",u"extension_text",u"phone_number",u"text"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"business_name",b"business_name",u"country_code",b"country_code",u"extension_text",b"extension_text",u"phone_number",b"phone_number",u"text",b"text"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"business_name",b"business_name",u"country_code",b"country_code",u"extension_text",b"extension_text",u"phone_number",b"phone_number",u"text",b"text"]) -> None: ...

class PriceFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type = ... # type: google___ads___googleads___v1___enums___price_extension_type_pb2___PriceExtensionTypeEnum.PriceExtensionType
    price_qualifier = ... # type: google___ads___googleads___v1___enums___price_extension_price_qualifier_pb2___PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier

    @property
    def tracking_url_template(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def language_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def price_offerings(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PriceOffer]: ...

    @property
    def final_url_suffix(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        type : typing___Optional[google___ads___googleads___v1___enums___price_extension_type_pb2___PriceExtensionTypeEnum.PriceExtensionType] = None,
        price_qualifier : typing___Optional[google___ads___googleads___v1___enums___price_extension_price_qualifier_pb2___PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier] = None,
        tracking_url_template : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        language_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        price_offerings : typing___Optional[typing___Iterable[PriceOffer]] = None,
        final_url_suffix : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PriceFeedItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"final_url_suffix",u"language_code",u"tracking_url_template"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"final_url_suffix",u"language_code",u"price_offerings",u"price_qualifier",u"tracking_url_template",u"type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"final_url_suffix",b"final_url_suffix",u"language_code",b"language_code",u"tracking_url_template",b"tracking_url_template"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"final_url_suffix",b"final_url_suffix",u"language_code",b"language_code",u"price_offerings",b"price_offerings",u"price_qualifier",b"price_qualifier",u"tracking_url_template",b"tracking_url_template",u"type",b"type"]) -> None: ...

class PriceOffer(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    unit = ... # type: google___ads___googleads___v1___enums___price_extension_price_unit_pb2___PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit

    @property
    def header(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def description(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def price(self) -> google___ads___googleads___v1___common___feed_common_pb2___Money: ...

    @property
    def final_urls(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    @property
    def final_mobile_urls(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    def __init__(self,
        *,
        header : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        description : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        price : typing___Optional[google___ads___googleads___v1___common___feed_common_pb2___Money] = None,
        unit : typing___Optional[google___ads___googleads___v1___enums___price_extension_price_unit_pb2___PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit] = None,
        final_urls : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        final_mobile_urls : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PriceOffer: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"description",u"header",u"price"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"description",u"final_mobile_urls",u"final_urls",u"header",u"price",u"unit"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"description",b"description",u"header",b"header",u"price",b"price"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"description",b"description",u"final_mobile_urls",b"final_mobile_urls",u"final_urls",b"final_urls",u"header",b"header",u"price",b"price",u"unit",b"unit"]) -> None: ...

class PromotionFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    discount_modifier = ... # type: google___ads___googleads___v1___enums___promotion_extension_discount_modifier_pb2___PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    occasion = ... # type: google___ads___googleads___v1___enums___promotion_extension_occasion_pb2___PromotionExtensionOccasionEnum.PromotionExtensionOccasion

    @property
    def promotion_target(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def promotion_start_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def promotion_end_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def final_urls(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    @property
    def final_mobile_urls(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    @property
    def tracking_url_template(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def url_custom_parameters(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter]: ...

    @property
    def final_url_suffix(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def language_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def percent_off(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def money_amount_off(self) -> google___ads___googleads___v1___common___feed_common_pb2___Money: ...

    @property
    def promotion_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def orders_over_amount(self) -> google___ads___googleads___v1___common___feed_common_pb2___Money: ...

    def __init__(self,
        *,
        promotion_target : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        discount_modifier : typing___Optional[google___ads___googleads___v1___enums___promotion_extension_discount_modifier_pb2___PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier] = None,
        promotion_start_date : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        promotion_end_date : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        occasion : typing___Optional[google___ads___googleads___v1___enums___promotion_extension_occasion_pb2___PromotionExtensionOccasionEnum.PromotionExtensionOccasion] = None,
        final_urls : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        final_mobile_urls : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        tracking_url_template : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        url_custom_parameters : typing___Optional[typing___Iterable[google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter]] = None,
        final_url_suffix : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        language_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        percent_off : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        money_amount_off : typing___Optional[google___ads___googleads___v1___common___feed_common_pb2___Money] = None,
        promotion_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        orders_over_amount : typing___Optional[google___ads___googleads___v1___common___feed_common_pb2___Money] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PromotionFeedItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"discount_type",u"final_url_suffix",u"language_code",u"money_amount_off",u"orders_over_amount",u"percent_off",u"promotion_code",u"promotion_end_date",u"promotion_start_date",u"promotion_target",u"promotion_trigger",u"tracking_url_template"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"discount_modifier",u"discount_type",u"final_mobile_urls",u"final_url_suffix",u"final_urls",u"language_code",u"money_amount_off",u"occasion",u"orders_over_amount",u"percent_off",u"promotion_code",u"promotion_end_date",u"promotion_start_date",u"promotion_target",u"promotion_trigger",u"tracking_url_template",u"url_custom_parameters"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"discount_type",b"discount_type",u"final_url_suffix",b"final_url_suffix",u"language_code",b"language_code",u"money_amount_off",b"money_amount_off",u"orders_over_amount",b"orders_over_amount",u"percent_off",b"percent_off",u"promotion_code",b"promotion_code",u"promotion_end_date",b"promotion_end_date",u"promotion_start_date",b"promotion_start_date",u"promotion_target",b"promotion_target",u"promotion_trigger",b"promotion_trigger",u"tracking_url_template",b"tracking_url_template"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"discount_modifier",b"discount_modifier",u"discount_type",b"discount_type",u"final_mobile_urls",b"final_mobile_urls",u"final_url_suffix",b"final_url_suffix",u"final_urls",b"final_urls",u"language_code",b"language_code",u"money_amount_off",b"money_amount_off",u"occasion",b"occasion",u"orders_over_amount",b"orders_over_amount",u"percent_off",b"percent_off",u"promotion_code",b"promotion_code",u"promotion_end_date",b"promotion_end_date",u"promotion_start_date",b"promotion_start_date",u"promotion_target",b"promotion_target",u"promotion_trigger",b"promotion_trigger",u"tracking_url_template",b"tracking_url_template",u"url_custom_parameters",b"url_custom_parameters"]) -> None: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"discount_type",b"discount_type"]) -> typing_extensions___Literal["percent_off","money_amount_off"]: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"promotion_trigger",b"promotion_trigger"]) -> typing_extensions___Literal["promotion_code","orders_over_amount"]: ...

class StructuredSnippetFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def header(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def values(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    def __init__(self,
        *,
        header : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        values : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> StructuredSnippetFeedItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"header"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"header",u"values"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"header",b"header"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"header",b"header",u"values",b"values"]) -> None: ...

class SitelinkFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def link_text(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def line1(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def line2(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def final_urls(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    @property
    def final_mobile_urls(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    @property
    def tracking_url_template(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def url_custom_parameters(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter]: ...

    @property
    def final_url_suffix(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        link_text : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        line1 : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        line2 : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        final_urls : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        final_mobile_urls : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        tracking_url_template : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        url_custom_parameters : typing___Optional[typing___Iterable[google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter]] = None,
        final_url_suffix : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SitelinkFeedItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"final_url_suffix",u"line1",u"line2",u"link_text",u"tracking_url_template"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"final_mobile_urls",u"final_url_suffix",u"final_urls",u"line1",u"line2",u"link_text",u"tracking_url_template",u"url_custom_parameters"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"final_url_suffix",b"final_url_suffix",u"line1",b"line1",u"line2",b"line2",u"link_text",b"link_text",u"tracking_url_template",b"tracking_url_template"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"final_mobile_urls",b"final_mobile_urls",u"final_url_suffix",b"final_url_suffix",u"final_urls",b"final_urls",u"line1",b"line1",u"line2",b"line2",u"link_text",b"link_text",u"tracking_url_template",b"tracking_url_template",u"url_custom_parameters",b"url_custom_parameters"]) -> None: ...
