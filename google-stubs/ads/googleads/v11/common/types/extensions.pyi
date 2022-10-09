import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import (
    custom_parameter as custom_parameter,
    feed_common as feed_common,
)
from google.ads.googleads.v11.enums.types import (
    price_extension_price_qualifier as price_extension_price_qualifier,
    price_extension_price_unit as price_extension_price_unit,
    price_extension_type as price_extension_type,
    promotion_extension_discount_modifier as promotion_extension_discount_modifier,
    promotion_extension_occasion as promotion_extension_occasion,
)

__protobuf__: Incomplete

class AppFeedItem(proto.Message):
    link_text: Incomplete
    app_id: Incomplete
    app_store: Incomplete
    final_urls: Incomplete
    final_mobile_urls: Incomplete
    tracking_url_template: Incomplete
    url_custom_parameters: Incomplete
    final_url_suffix: Incomplete

class CallFeedItem(proto.Message):
    phone_number: Incomplete
    country_code: Incomplete
    call_tracking_enabled: Incomplete
    call_conversion_action: Incomplete
    call_conversion_tracking_disabled: Incomplete
    call_conversion_reporting_state: Incomplete

class CalloutFeedItem(proto.Message):
    callout_text: Incomplete

class LocationFeedItem(proto.Message):
    business_name: Incomplete
    address_line_1: Incomplete
    address_line_2: Incomplete
    city: Incomplete
    province: Incomplete
    postal_code: Incomplete
    country_code: Incomplete
    phone_number: Incomplete

class AffiliateLocationFeedItem(proto.Message):
    business_name: Incomplete
    address_line_1: Incomplete
    address_line_2: Incomplete
    city: Incomplete
    province: Incomplete
    postal_code: Incomplete
    country_code: Incomplete
    phone_number: Incomplete
    chain_id: Incomplete
    chain_name: Incomplete

class TextMessageFeedItem(proto.Message):
    business_name: Incomplete
    country_code: Incomplete
    phone_number: Incomplete
    text: Incomplete
    extension_text: Incomplete

class PriceFeedItem(proto.Message):
    type_: Incomplete
    price_qualifier: Incomplete
    tracking_url_template: Incomplete
    language_code: Incomplete
    price_offerings: Incomplete
    final_url_suffix: Incomplete

class PriceOffer(proto.Message):
    header: Incomplete
    description: Incomplete
    price: Incomplete
    unit: Incomplete
    final_urls: Incomplete
    final_mobile_urls: Incomplete

class PromotionFeedItem(proto.Message):
    promotion_target: Incomplete
    discount_modifier: Incomplete
    promotion_start_date: Incomplete
    promotion_end_date: Incomplete
    occasion: Incomplete
    final_urls: Incomplete
    final_mobile_urls: Incomplete
    tracking_url_template: Incomplete
    url_custom_parameters: Incomplete
    final_url_suffix: Incomplete
    language_code: Incomplete
    percent_off: Incomplete
    money_amount_off: Incomplete
    promotion_code: Incomplete
    orders_over_amount: Incomplete

class StructuredSnippetFeedItem(proto.Message):
    header: Incomplete
    values: Incomplete

class SitelinkFeedItem(proto.Message):
    link_text: Incomplete
    line1: Incomplete
    line2: Incomplete
    final_urls: Incomplete
    final_mobile_urls: Incomplete
    tracking_url_template: Incomplete
    url_custom_parameters: Incomplete
    final_url_suffix: Incomplete

class HotelCalloutFeedItem(proto.Message):
    text: Incomplete
    language_code: Incomplete

class ImageFeedItem(proto.Message):
    image_asset: Incomplete
