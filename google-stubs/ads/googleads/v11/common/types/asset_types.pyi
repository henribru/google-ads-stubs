import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import (
    criteria as criteria,
    feed_common as feed_common,
)
from google.ads.googleads.v11.enums.types import (
    lead_form_call_to_action_type as lead_form_call_to_action_type,
    lead_form_desired_intent as lead_form_desired_intent,
    lead_form_field_user_input_type as lead_form_field_user_input_type,
    lead_form_post_submit_call_to_action_type as lead_form_post_submit_call_to_action_type,
    mobile_app_vendor as mobile_app_vendor,
    price_extension_price_qualifier as price_extension_price_qualifier,
    price_extension_price_unit as price_extension_price_unit,
    price_extension_type as price_extension_type,
    promotion_extension_discount_modifier as promotion_extension_discount_modifier,
    promotion_extension_occasion as promotion_extension_occasion,
)

__protobuf__: Incomplete

class YoutubeVideoAsset(proto.Message):
    youtube_video_id: Incomplete
    youtube_video_title: Incomplete

class MediaBundleAsset(proto.Message):
    data: Incomplete

class ImageAsset(proto.Message):
    data: Incomplete
    file_size: Incomplete
    mime_type: Incomplete
    full_size: Incomplete

class ImageDimension(proto.Message):
    height_pixels: Incomplete
    width_pixels: Incomplete
    url: Incomplete

class TextAsset(proto.Message):
    text: Incomplete

class LeadFormAsset(proto.Message):
    business_name: Incomplete
    call_to_action_type: Incomplete
    call_to_action_description: Incomplete
    headline: Incomplete
    description: Incomplete
    privacy_policy_url: Incomplete
    post_submit_headline: Incomplete
    post_submit_description: Incomplete
    fields: Incomplete
    custom_question_fields: Incomplete
    delivery_methods: Incomplete
    post_submit_call_to_action_type: Incomplete
    background_image_asset: Incomplete
    desired_intent: Incomplete
    custom_disclosure: Incomplete

class LeadFormField(proto.Message):
    input_type: Incomplete
    single_choice_answers: Incomplete

class LeadFormCustomQuestionField(proto.Message):
    custom_question_text: Incomplete
    single_choice_answers: Incomplete

class LeadFormSingleChoiceAnswers(proto.Message):
    answers: Incomplete

class LeadFormDeliveryMethod(proto.Message):
    webhook: Incomplete

class WebhookDelivery(proto.Message):
    advertiser_webhook_url: Incomplete
    google_secret: Incomplete
    payload_schema_version: Incomplete

class BookOnGoogleAsset(proto.Message): ...

class PromotionAsset(proto.Message):
    promotion_target: Incomplete
    discount_modifier: Incomplete
    redemption_start_date: Incomplete
    redemption_end_date: Incomplete
    occasion: Incomplete
    language_code: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    ad_schedule_targets: Incomplete
    percent_off: Incomplete
    money_amount_off: Incomplete
    promotion_code: Incomplete
    orders_over_amount: Incomplete

class CalloutAsset(proto.Message):
    callout_text: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    ad_schedule_targets: Incomplete

class StructuredSnippetAsset(proto.Message):
    header: Incomplete
    values: Incomplete

class SitelinkAsset(proto.Message):
    link_text: Incomplete
    description1: Incomplete
    description2: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    ad_schedule_targets: Incomplete

class PageFeedAsset(proto.Message):
    page_url: Incomplete
    labels: Incomplete

class DynamicEducationAsset(proto.Message):
    program_id: Incomplete
    location_id: Incomplete
    program_name: Incomplete
    subject: Incomplete
    program_description: Incomplete
    school_name: Incomplete
    address: Incomplete
    contextual_keywords: Incomplete
    android_app_link: Incomplete
    similar_program_ids: Incomplete
    ios_app_link: Incomplete
    ios_app_store_id: Incomplete
    thumbnail_image_url: Incomplete
    image_url: Incomplete

class MobileAppAsset(proto.Message):
    app_id: Incomplete
    app_store: Incomplete
    link_text: Incomplete
    start_date: Incomplete
    end_date: Incomplete

class HotelCalloutAsset(proto.Message):
    text: Incomplete
    language_code: Incomplete

class CallAsset(proto.Message):
    country_code: Incomplete
    phone_number: Incomplete
    call_conversion_reporting_state: Incomplete
    call_conversion_action: Incomplete
    ad_schedule_targets: Incomplete

class PriceAsset(proto.Message):
    type_: Incomplete
    price_qualifier: Incomplete
    language_code: Incomplete
    price_offerings: Incomplete

class PriceOffering(proto.Message):
    header: Incomplete
    description: Incomplete
    price: Incomplete
    unit: Incomplete
    final_url: Incomplete
    final_mobile_url: Incomplete

class CallToActionAsset(proto.Message):
    call_to_action: Incomplete

class DynamicRealEstateAsset(proto.Message):
    listing_id: Incomplete
    listing_name: Incomplete
    city_name: Incomplete
    description: Incomplete
    address: Incomplete
    price: Incomplete
    image_url: Incomplete
    property_type: Incomplete
    listing_type: Incomplete
    contextual_keywords: Incomplete
    formatted_price: Incomplete
    android_app_link: Incomplete
    ios_app_link: Incomplete
    ios_app_store_id: Incomplete
    similar_listing_ids: Incomplete

class DynamicCustomAsset(proto.Message):
    id: Incomplete
    id2: Incomplete
    item_title: Incomplete
    item_subtitle: Incomplete
    item_description: Incomplete
    item_address: Incomplete
    item_category: Incomplete
    price: Incomplete
    sale_price: Incomplete
    formatted_price: Incomplete
    formatted_sale_price: Incomplete
    image_url: Incomplete
    contextual_keywords: Incomplete
    android_app_link: Incomplete
    ios_app_link: Incomplete
    ios_app_store_id: Incomplete
    similar_ids: Incomplete

class DynamicHotelsAndRentalsAsset(proto.Message):
    property_id: Incomplete
    property_name: Incomplete
    image_url: Incomplete
    destination_name: Incomplete
    description: Incomplete
    price: Incomplete
    sale_price: Incomplete
    star_rating: Incomplete
    category: Incomplete
    contextual_keywords: Incomplete
    address: Incomplete
    android_app_link: Incomplete
    ios_app_link: Incomplete
    ios_app_store_id: Incomplete
    formatted_price: Incomplete
    formatted_sale_price: Incomplete
    similar_property_ids: Incomplete

class DynamicFlightsAsset(proto.Message):
    destination_id: Incomplete
    origin_id: Incomplete
    flight_description: Incomplete
    image_url: Incomplete
    destination_name: Incomplete
    origin_name: Incomplete
    flight_price: Incomplete
    flight_sale_price: Incomplete
    formatted_price: Incomplete
    formatted_sale_price: Incomplete
    android_app_link: Incomplete
    ios_app_link: Incomplete
    ios_app_store_id: Incomplete
    similar_destination_ids: Incomplete
    custom_mapping: Incomplete

class DiscoveryCarouselCardAsset(proto.Message):
    marketing_image_asset: Incomplete
    square_marketing_image_asset: Incomplete
    portrait_marketing_image_asset: Incomplete
    headline: Incomplete
    call_to_action_text: Incomplete

class DynamicTravelAsset(proto.Message):
    destination_id: Incomplete
    origin_id: Incomplete
    title: Incomplete
    destination_name: Incomplete
    destination_address: Incomplete
    origin_name: Incomplete
    price: Incomplete
    sale_price: Incomplete
    formatted_price: Incomplete
    formatted_sale_price: Incomplete
    category: Incomplete
    contextual_keywords: Incomplete
    similar_destination_ids: Incomplete
    image_url: Incomplete
    android_app_link: Incomplete
    ios_app_link: Incomplete
    ios_app_store_id: Incomplete

class DynamicLocalAsset(proto.Message):
    deal_id: Incomplete
    deal_name: Incomplete
    subtitle: Incomplete
    description: Incomplete
    price: Incomplete
    sale_price: Incomplete
    image_url: Incomplete
    address: Incomplete
    category: Incomplete
    contextual_keywords: Incomplete
    formatted_price: Incomplete
    formatted_sale_price: Incomplete
    android_app_link: Incomplete
    similar_deal_ids: Incomplete
    ios_app_link: Incomplete
    ios_app_store_id: Incomplete

class DynamicJobsAsset(proto.Message):
    job_id: Incomplete
    location_id: Incomplete
    job_title: Incomplete
    job_subtitle: Incomplete
    description: Incomplete
    image_url: Incomplete
    job_category: Incomplete
    contextual_keywords: Incomplete
    address: Incomplete
    salary: Incomplete
    android_app_link: Incomplete
    similar_job_ids: Incomplete
    ios_app_link: Incomplete
    ios_app_store_id: Incomplete
