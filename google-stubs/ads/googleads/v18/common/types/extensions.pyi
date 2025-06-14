import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import custom_parameter, feed_common
from google.ads.googleads.v18.enums.types import app_store as gage_app_store, call_conversion_reporting_state as gage_call_conversion_reporting_state, price_extension_price_qualifier, price_extension_price_unit, price_extension_type, promotion_extension_discount_modifier, promotion_extension_occasion
from typing import MutableSequence

__protobuf__: Incomplete

class AppFeedItem(proto.Message):
    link_text: str
    app_id: str
    app_store: gage_app_store.AppStoreEnum.AppStore
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    url_custom_parameters: MutableSequence[custom_parameter.CustomParameter]
    final_url_suffix: str

class CallFeedItem(proto.Message):
    phone_number: str
    country_code: str
    call_tracking_enabled: bool
    call_conversion_action: str
    call_conversion_tracking_disabled: bool
    call_conversion_reporting_state: gage_call_conversion_reporting_state.CallConversionReportingStateEnum.CallConversionReportingState

class CalloutFeedItem(proto.Message):
    callout_text: str

class LocationFeedItem(proto.Message):
    business_name: str
    address_line_1: str
    address_line_2: str
    city: str
    province: str
    postal_code: str
    country_code: str
    phone_number: str

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

class TextMessageFeedItem(proto.Message):
    business_name: str
    country_code: str
    phone_number: str
    text: str
    extension_text: str

class PriceFeedItem(proto.Message):
    type_: price_extension_type.PriceExtensionTypeEnum.PriceExtensionType
    price_qualifier: price_extension_price_qualifier.PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    tracking_url_template: str
    language_code: str
    price_offerings: MutableSequence['PriceOffer']
    final_url_suffix: str

class PriceOffer(proto.Message):
    header: str
    description: str
    price: feed_common.Money
    unit: price_extension_price_unit.PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]

class PromotionFeedItem(proto.Message):
    promotion_target: str
    discount_modifier: promotion_extension_discount_modifier.PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    promotion_start_date: str
    promotion_end_date: str
    occasion: promotion_extension_occasion.PromotionExtensionOccasionEnum.PromotionExtensionOccasion
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    url_custom_parameters: MutableSequence[custom_parameter.CustomParameter]
    final_url_suffix: str
    language_code: str
    percent_off: int
    money_amount_off: feed_common.Money
    promotion_code: str
    orders_over_amount: feed_common.Money

class StructuredSnippetFeedItem(proto.Message):
    header: str
    values: MutableSequence[str]

class SitelinkFeedItem(proto.Message):
    link_text: str
    line1: str
    line2: str
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    url_custom_parameters: MutableSequence[custom_parameter.CustomParameter]
    final_url_suffix: str

class HotelCalloutFeedItem(proto.Message):
    text: str
    language_code: str

class ImageFeedItem(proto.Message):
    image_asset: str
