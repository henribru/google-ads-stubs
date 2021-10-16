from typing import Any

import proto

from google.ads.googleads.v8.common.types import (
    custom_parameter as custom_parameter,
    feed_common as feed_common,
)
from google.ads.googleads.v8.enums.types import (
    price_extension_price_qualifier as price_extension_price_qualifier,
    price_extension_price_unit as price_extension_price_unit,
    price_extension_type as price_extension_type,
    promotion_extension_discount_modifier as promotion_extension_discount_modifier,
    promotion_extension_occasion as promotion_extension_occasion,
)

__protobuf__: Any

class AppFeedItem(proto.Message):
    link_text: Any
    app_id: Any
    app_store: Any
    final_urls: Any
    final_mobile_urls: Any
    tracking_url_template: Any
    url_custom_parameters: Any
    final_url_suffix: Any

class CallFeedItem(proto.Message):
    phone_number: Any
    country_code: Any
    call_tracking_enabled: Any
    call_conversion_action: Any
    call_conversion_tracking_disabled: Any
    call_conversion_reporting_state: Any

class CalloutFeedItem(proto.Message):
    callout_text: Any

class LocationFeedItem(proto.Message):
    business_name: Any
    address_line_1: Any
    address_line_2: Any
    city: Any
    province: Any
    postal_code: Any
    country_code: Any
    phone_number: Any

class AffiliateLocationFeedItem(proto.Message):
    business_name: Any
    address_line_1: Any
    address_line_2: Any
    city: Any
    province: Any
    postal_code: Any
    country_code: Any
    phone_number: Any
    chain_id: Any
    chain_name: Any

class TextMessageFeedItem(proto.Message):
    business_name: Any
    country_code: Any
    phone_number: Any
    text: Any
    extension_text: Any

class PriceFeedItem(proto.Message):
    type_: Any
    price_qualifier: Any
    tracking_url_template: Any
    language_code: Any
    price_offerings: Any
    final_url_suffix: Any

class PriceOffer(proto.Message):
    header: Any
    description: Any
    price: Any
    unit: Any
    final_urls: Any
    final_mobile_urls: Any

class PromotionFeedItem(proto.Message):
    promotion_target: Any
    discount_modifier: Any
    promotion_start_date: Any
    promotion_end_date: Any
    occasion: Any
    final_urls: Any
    final_mobile_urls: Any
    tracking_url_template: Any
    url_custom_parameters: Any
    final_url_suffix: Any
    language_code: Any
    percent_off: Any
    money_amount_off: Any
    promotion_code: Any
    orders_over_amount: Any

class StructuredSnippetFeedItem(proto.Message):
    header: Any
    values: Any

class SitelinkFeedItem(proto.Message):
    link_text: Any
    line1: Any
    line2: Any
    final_urls: Any
    final_mobile_urls: Any
    tracking_url_template: Any
    url_custom_parameters: Any
    final_url_suffix: Any

class HotelCalloutFeedItem(proto.Message):
    text: Any
    language_code: Any

class ImageFeedItem(proto.Message):
    image_asset: Any
