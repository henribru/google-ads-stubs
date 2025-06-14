import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import criteria, feed_common
from google.ads.googleads.v20.enums.types import business_message_call_to_action_type, business_message_provider, call_conversion_reporting_state as gage_call_conversion_reporting_state, call_to_action_type as gage_call_to_action_type, lead_form_call_to_action_type, lead_form_desired_intent, lead_form_field_user_input_type, lead_form_post_submit_call_to_action_type, location_ownership_type as gage_location_ownership_type, mime_type as gage_mime_type, mobile_app_vendor, price_extension_price_qualifier, price_extension_price_unit, price_extension_type, promotion_extension_discount_modifier, promotion_extension_occasion
from typing import MutableSequence

__protobuf__: Incomplete

class YoutubeVideoAsset(proto.Message):
    youtube_video_id: str
    youtube_video_title: str

class MediaBundleAsset(proto.Message):
    data: bytes

class ImageAsset(proto.Message):
    data: bytes
    file_size: int
    mime_type: gage_mime_type.MimeTypeEnum.MimeType
    full_size: ImageDimension

class ImageDimension(proto.Message):
    height_pixels: int
    width_pixels: int
    url: str

class TextAsset(proto.Message):
    text: str

class LeadFormAsset(proto.Message):
    business_name: str
    call_to_action_type: lead_form_call_to_action_type.LeadFormCallToActionTypeEnum.LeadFormCallToActionType
    call_to_action_description: str
    headline: str
    description: str
    privacy_policy_url: str
    post_submit_headline: str
    post_submit_description: str
    fields: MutableSequence['LeadFormField']
    custom_question_fields: MutableSequence['LeadFormCustomQuestionField']
    delivery_methods: MutableSequence['LeadFormDeliveryMethod']
    post_submit_call_to_action_type: lead_form_post_submit_call_to_action_type.LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType
    background_image_asset: str
    desired_intent: lead_form_desired_intent.LeadFormDesiredIntentEnum.LeadFormDesiredIntent
    custom_disclosure: str

class LeadFormField(proto.Message):
    input_type: lead_form_field_user_input_type.LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType
    single_choice_answers: LeadFormSingleChoiceAnswers
    has_location_answer: bool

class LeadFormCustomQuestionField(proto.Message):
    custom_question_text: str
    single_choice_answers: LeadFormSingleChoiceAnswers
    has_location_answer: bool

class LeadFormSingleChoiceAnswers(proto.Message):
    answers: MutableSequence[str]

class LeadFormDeliveryMethod(proto.Message):
    webhook: WebhookDelivery

class WebhookDelivery(proto.Message):
    advertiser_webhook_url: str
    google_secret: str
    payload_schema_version: int

class BookOnGoogleAsset(proto.Message): ...

class PromotionAsset(proto.Message):
    promotion_target: str
    discount_modifier: promotion_extension_discount_modifier.PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    redemption_start_date: str
    redemption_end_date: str
    occasion: promotion_extension_occasion.PromotionExtensionOccasionEnum.PromotionExtensionOccasion
    language_code: str
    start_date: str
    end_date: str
    ad_schedule_targets: MutableSequence[criteria.AdScheduleInfo]
    percent_off: int
    money_amount_off: feed_common.Money
    promotion_code: str
    orders_over_amount: feed_common.Money

class CalloutAsset(proto.Message):
    callout_text: str
    start_date: str
    end_date: str
    ad_schedule_targets: MutableSequence[criteria.AdScheduleInfo]

class StructuredSnippetAsset(proto.Message):
    header: str
    values: MutableSequence[str]

class SitelinkAsset(proto.Message):
    link_text: str
    description1: str
    description2: str
    start_date: str
    end_date: str
    ad_schedule_targets: MutableSequence[criteria.AdScheduleInfo]

class PageFeedAsset(proto.Message):
    page_url: str
    labels: MutableSequence[str]

class DynamicEducationAsset(proto.Message):
    program_id: str
    location_id: str
    program_name: str
    subject: str
    program_description: str
    school_name: str
    address: str
    contextual_keywords: MutableSequence[str]
    android_app_link: str
    similar_program_ids: MutableSequence[str]
    ios_app_link: str
    ios_app_store_id: int
    thumbnail_image_url: str
    image_url: str

class MobileAppAsset(proto.Message):
    app_id: str
    app_store: mobile_app_vendor.MobileAppVendorEnum.MobileAppVendor
    link_text: str
    start_date: str
    end_date: str

class HotelCalloutAsset(proto.Message):
    text: str
    language_code: str

class CallAsset(proto.Message):
    country_code: str
    phone_number: str
    call_conversion_reporting_state: gage_call_conversion_reporting_state.CallConversionReportingStateEnum.CallConversionReportingState
    call_conversion_action: str
    ad_schedule_targets: MutableSequence[criteria.AdScheduleInfo]

class PriceAsset(proto.Message):
    type_: price_extension_type.PriceExtensionTypeEnum.PriceExtensionType
    price_qualifier: price_extension_price_qualifier.PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    language_code: str
    price_offerings: MutableSequence['PriceOffering']

class PriceOffering(proto.Message):
    header: str
    description: str
    price: feed_common.Money
    unit: price_extension_price_unit.PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    final_url: str
    final_mobile_url: str

class CallToActionAsset(proto.Message):
    call_to_action: gage_call_to_action_type.CallToActionTypeEnum.CallToActionType

class DynamicRealEstateAsset(proto.Message):
    listing_id: str
    listing_name: str
    city_name: str
    description: str
    address: str
    price: str
    image_url: str
    property_type: str
    listing_type: str
    contextual_keywords: MutableSequence[str]
    formatted_price: str
    android_app_link: str
    ios_app_link: str
    ios_app_store_id: int
    similar_listing_ids: MutableSequence[str]

class DynamicCustomAsset(proto.Message):
    id: str
    id2: str
    item_title: str
    item_subtitle: str
    item_description: str
    item_address: str
    item_category: str
    price: str
    sale_price: str
    formatted_price: str
    formatted_sale_price: str
    image_url: str
    contextual_keywords: MutableSequence[str]
    android_app_link: str
    ios_app_link: str
    ios_app_store_id: int
    similar_ids: MutableSequence[str]

class DynamicHotelsAndRentalsAsset(proto.Message):
    property_id: str
    property_name: str
    image_url: str
    destination_name: str
    description: str
    price: str
    sale_price: str
    star_rating: int
    category: str
    contextual_keywords: MutableSequence[str]
    address: str
    android_app_link: str
    ios_app_link: str
    ios_app_store_id: int
    formatted_price: str
    formatted_sale_price: str
    similar_property_ids: MutableSequence[str]

class DynamicFlightsAsset(proto.Message):
    destination_id: str
    origin_id: str
    flight_description: str
    image_url: str
    destination_name: str
    origin_name: str
    flight_price: str
    flight_sale_price: str
    formatted_price: str
    formatted_sale_price: str
    android_app_link: str
    ios_app_link: str
    ios_app_store_id: int
    similar_destination_ids: MutableSequence[str]
    custom_mapping: str

class DemandGenCarouselCardAsset(proto.Message):
    marketing_image_asset: str
    square_marketing_image_asset: str
    portrait_marketing_image_asset: str
    headline: str
    call_to_action_text: str

class DynamicTravelAsset(proto.Message):
    destination_id: str
    origin_id: str
    title: str
    destination_name: str
    destination_address: str
    origin_name: str
    price: str
    sale_price: str
    formatted_price: str
    formatted_sale_price: str
    category: str
    contextual_keywords: MutableSequence[str]
    similar_destination_ids: MutableSequence[str]
    image_url: str
    android_app_link: str
    ios_app_link: str
    ios_app_store_id: int

class DynamicLocalAsset(proto.Message):
    deal_id: str
    deal_name: str
    subtitle: str
    description: str
    price: str
    sale_price: str
    image_url: str
    address: str
    category: str
    contextual_keywords: MutableSequence[str]
    formatted_price: str
    formatted_sale_price: str
    android_app_link: str
    similar_deal_ids: MutableSequence[str]
    ios_app_link: str
    ios_app_store_id: int

class DynamicJobsAsset(proto.Message):
    job_id: str
    location_id: str
    job_title: str
    job_subtitle: str
    description: str
    image_url: str
    job_category: str
    contextual_keywords: MutableSequence[str]
    address: str
    salary: str
    android_app_link: str
    similar_job_ids: MutableSequence[str]
    ios_app_link: str
    ios_app_store_id: int

class LocationAsset(proto.Message):
    place_id: str
    business_profile_locations: MutableSequence['BusinessProfileLocation']
    location_ownership_type: gage_location_ownership_type.LocationOwnershipTypeEnum.LocationOwnershipType

class BusinessProfileLocation(proto.Message):
    labels: MutableSequence[str]
    store_code: str
    listing_id: int

class HotelPropertyAsset(proto.Message):
    place_id: str
    hotel_address: str
    hotel_name: str

class BusinessMessageAsset(proto.Message):
    message_provider: business_message_provider.BusinessMessageProviderEnum.BusinessMessageProvider
    starter_message: str
    call_to_action: BusinessMessageCallToActionInfo
    whatsapp_info: WhatsappBusinessMessageInfo

class WhatsappBusinessMessageInfo(proto.Message):
    country_code: str
    phone_number: str

class BusinessMessageCallToActionInfo(proto.Message):
    call_to_action_selection: business_message_call_to_action_type.BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType
    call_to_action_description: str

class AppDeepLinkAsset(proto.Message):
    app_deep_link_uri: str
