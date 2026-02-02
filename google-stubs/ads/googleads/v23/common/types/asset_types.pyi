from collections.abc import MutableSequence
from google.ads.googleads.v23.common.types.ad_asset import AdVideoAsset
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v23.common.types.criteria import AdScheduleInfo
from google.ads.googleads.v23.enums.types.promotion_barcode_type import PromotionBarcodeTypeEnum
from google.ads.googleads.v23.common.types.feed_common import Money
from google.ads.googleads.v23.common.types.feed_common import Money
from collections.abc import MutableSequence
from google.ads.googleads.v23.common.types.criteria import AdScheduleInfo
from google.ads.googleads.v23.enums.types.promotion_extension_occasion import PromotionExtensionOccasionEnum
from google.ads.googleads.v23.enums.types.promotion_extension_discount_modifier import PromotionExtensionDiscountModifierEnum
from google.ads.googleads.v23.enums.types.price_extension_price_unit import PriceExtensionPriceUnitEnum
from google.ads.googleads.v23.common.types.feed_common import Money
from collections.abc import MutableSequence
from google.ads.googleads.v23.enums.types.price_extension_price_qualifier import PriceExtensionPriceQualifierEnum
from google.ads.googleads.v23.enums.types.price_extension_type import PriceExtensionTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v23.enums.types.mobile_app_vendor import MobileAppVendorEnum
from google.ads.googleads.v23.enums.types.location_ownership_type import LocationOwnershipTypeEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v23.enums.types.lead_form_field_user_input_type import LeadFormFieldUserInputTypeEnum
from google.ads.googleads.v23.enums.types.lead_form_desired_intent import LeadFormDesiredIntentEnum
from google.ads.googleads.v23.enums.types.lead_form_post_submit_call_to_action_type import LeadFormPostSubmitCallToActionTypeEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v23.enums.types.lead_form_call_to_action_type import LeadFormCallToActionTypeEnum
from google.ads.googleads.v23.enums.types.mime_type import MimeTypeEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v23.common.types.criteria import AdScheduleInfo
from google.ads.googleads.v23.enums.types.call_to_action_type import CallToActionTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v23.common.types.criteria import AdScheduleInfo
from google.ads.googleads.v23.enums.types.call_conversion_reporting_state import CallConversionReportingStateEnum
from collections.abc import MutableSequence
from google.ads.googleads.v23.enums.types.business_message_call_to_action_type import BusinessMessageCallToActionTypeEnum
from google.ads.googleads.v23.enums.types.business_message_provider import BusinessMessageProviderEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AppDeepLinkAsset(proto.Message):
    app_deep_link_uri: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, app_deep_link_uri: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["app_deep_link_uri"]) -> bool: ...
class BookOnGoogleAsset(proto.Message):
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
class BusinessMessageAsset(proto.Message):
    message_provider: BusinessMessageProviderEnum.BusinessMessageProvider
    starter_message: str
    call_to_action: BusinessMessageCallToActionInfo
    whatsapp_info: WhatsappBusinessMessageInfo
    facebook_messenger_info: FacebookMessengerBusinessMessageInfo
    zalo_info: ZaloBusinessMessageInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, message_provider: BusinessMessageProviderEnum.BusinessMessageProvider = ..., starter_message: str = ..., call_to_action: BusinessMessageCallToActionInfo = ..., whatsapp_info: WhatsappBusinessMessageInfo = ..., facebook_messenger_info: FacebookMessengerBusinessMessageInfo = ..., zalo_info: ZaloBusinessMessageInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["message_provider", "starter_message", "call_to_action", "whatsapp_info", "facebook_messenger_info", "zalo_info"]) -> bool: ...
class BusinessMessageCallToActionInfo(proto.Message):
    call_to_action_selection: BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType
    call_to_action_description: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, call_to_action_selection: BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType = ..., call_to_action_description: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["call_to_action_selection", "call_to_action_description"]) -> bool: ...
class BusinessProfileLocation(proto.Message):
    labels: MutableSequence[str]
    store_code: str
    listing_id: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, labels: MutableSequence[str] = ..., store_code: str = ..., listing_id: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["labels", "store_code", "listing_id"]) -> bool: ...
class CallAsset(proto.Message):
    country_code: str
    phone_number: str
    call_conversion_reporting_state: CallConversionReportingStateEnum.CallConversionReportingState
    call_conversion_action: str
    ad_schedule_targets: MutableSequence[AdScheduleInfo]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, country_code: str = ..., phone_number: str = ..., call_conversion_reporting_state: CallConversionReportingStateEnum.CallConversionReportingState = ..., call_conversion_action: str = ..., ad_schedule_targets: MutableSequence[AdScheduleInfo] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["country_code", "phone_number", "call_conversion_reporting_state", "call_conversion_action", "ad_schedule_targets"]) -> bool: ...
class CallToActionAsset(proto.Message):
    call_to_action: CallToActionTypeEnum.CallToActionType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, call_to_action: CallToActionTypeEnum.CallToActionType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["call_to_action"]) -> bool: ...
class CalloutAsset(proto.Message):
    callout_text: str
    start_date: str
    end_date: str
    ad_schedule_targets: MutableSequence[AdScheduleInfo]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, callout_text: str = ..., start_date: str = ..., end_date: str = ..., ad_schedule_targets: MutableSequence[AdScheduleInfo] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["callout_text", "start_date", "end_date", "ad_schedule_targets"]) -> bool: ...
class DemandGenCarouselCardAsset(proto.Message):
    marketing_image_asset: str
    square_marketing_image_asset: str
    portrait_marketing_image_asset: str
    headline: str
    call_to_action_text: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, marketing_image_asset: str = ..., square_marketing_image_asset: str = ..., portrait_marketing_image_asset: str = ..., headline: str = ..., call_to_action_text: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["marketing_image_asset", "square_marketing_image_asset", "portrait_marketing_image_asset", "headline", "call_to_action_text"]) -> bool: ...
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, id: str = ..., id2: str = ..., item_title: str = ..., item_subtitle: str = ..., item_description: str = ..., item_address: str = ..., item_category: str = ..., price: str = ..., sale_price: str = ..., formatted_price: str = ..., formatted_sale_price: str = ..., image_url: str = ..., contextual_keywords: MutableSequence[str] = ..., android_app_link: str = ..., ios_app_link: str = ..., ios_app_store_id: int = ..., similar_ids: MutableSequence[str] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["id", "id2", "item_title", "item_subtitle", "item_description", "item_address", "item_category", "price", "sale_price", "formatted_price", "formatted_sale_price", "image_url", "contextual_keywords", "android_app_link", "ios_app_link", "ios_app_store_id", "similar_ids"]) -> bool: ...
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, program_id: str = ..., location_id: str = ..., program_name: str = ..., subject: str = ..., program_description: str = ..., school_name: str = ..., address: str = ..., contextual_keywords: MutableSequence[str] = ..., android_app_link: str = ..., similar_program_ids: MutableSequence[str] = ..., ios_app_link: str = ..., ios_app_store_id: int = ..., thumbnail_image_url: str = ..., image_url: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["program_id", "location_id", "program_name", "subject", "program_description", "school_name", "address", "contextual_keywords", "android_app_link", "similar_program_ids", "ios_app_link", "ios_app_store_id", "thumbnail_image_url", "image_url"]) -> bool: ...
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, destination_id: str = ..., origin_id: str = ..., flight_description: str = ..., image_url: str = ..., destination_name: str = ..., origin_name: str = ..., flight_price: str = ..., flight_sale_price: str = ..., formatted_price: str = ..., formatted_sale_price: str = ..., android_app_link: str = ..., ios_app_link: str = ..., ios_app_store_id: int = ..., similar_destination_ids: MutableSequence[str] = ..., custom_mapping: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["destination_id", "origin_id", "flight_description", "image_url", "destination_name", "origin_name", "flight_price", "flight_sale_price", "formatted_price", "formatted_sale_price", "android_app_link", "ios_app_link", "ios_app_store_id", "similar_destination_ids", "custom_mapping"]) -> bool: ...
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, property_id: str = ..., property_name: str = ..., image_url: str = ..., destination_name: str = ..., description: str = ..., price: str = ..., sale_price: str = ..., star_rating: int = ..., category: str = ..., contextual_keywords: MutableSequence[str] = ..., address: str = ..., android_app_link: str = ..., ios_app_link: str = ..., ios_app_store_id: int = ..., formatted_price: str = ..., formatted_sale_price: str = ..., similar_property_ids: MutableSequence[str] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["property_id", "property_name", "image_url", "destination_name", "description", "price", "sale_price", "star_rating", "category", "contextual_keywords", "address", "android_app_link", "ios_app_link", "ios_app_store_id", "formatted_price", "formatted_sale_price", "similar_property_ids"]) -> bool: ...
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, job_id: str = ..., location_id: str = ..., job_title: str = ..., job_subtitle: str = ..., description: str = ..., image_url: str = ..., job_category: str = ..., contextual_keywords: MutableSequence[str] = ..., address: str = ..., salary: str = ..., android_app_link: str = ..., similar_job_ids: MutableSequence[str] = ..., ios_app_link: str = ..., ios_app_store_id: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["job_id", "location_id", "job_title", "job_subtitle", "description", "image_url", "job_category", "contextual_keywords", "address", "salary", "android_app_link", "similar_job_ids", "ios_app_link", "ios_app_store_id"]) -> bool: ...
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, deal_id: str = ..., deal_name: str = ..., subtitle: str = ..., description: str = ..., price: str = ..., sale_price: str = ..., image_url: str = ..., address: str = ..., category: str = ..., contextual_keywords: MutableSequence[str] = ..., formatted_price: str = ..., formatted_sale_price: str = ..., android_app_link: str = ..., similar_deal_ids: MutableSequence[str] = ..., ios_app_link: str = ..., ios_app_store_id: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["deal_id", "deal_name", "subtitle", "description", "price", "sale_price", "image_url", "address", "category", "contextual_keywords", "formatted_price", "formatted_sale_price", "android_app_link", "similar_deal_ids", "ios_app_link", "ios_app_store_id"]) -> bool: ...
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, listing_id: str = ..., listing_name: str = ..., city_name: str = ..., description: str = ..., address: str = ..., price: str = ..., image_url: str = ..., property_type: str = ..., listing_type: str = ..., contextual_keywords: MutableSequence[str] = ..., formatted_price: str = ..., android_app_link: str = ..., ios_app_link: str = ..., ios_app_store_id: int = ..., similar_listing_ids: MutableSequence[str] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["listing_id", "listing_name", "city_name", "description", "address", "price", "image_url", "property_type", "listing_type", "contextual_keywords", "formatted_price", "android_app_link", "ios_app_link", "ios_app_store_id", "similar_listing_ids"]) -> bool: ...
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, destination_id: str = ..., origin_id: str = ..., title: str = ..., destination_name: str = ..., destination_address: str = ..., origin_name: str = ..., price: str = ..., sale_price: str = ..., formatted_price: str = ..., formatted_sale_price: str = ..., category: str = ..., contextual_keywords: MutableSequence[str] = ..., similar_destination_ids: MutableSequence[str] = ..., image_url: str = ..., android_app_link: str = ..., ios_app_link: str = ..., ios_app_store_id: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["destination_id", "origin_id", "title", "destination_name", "destination_address", "origin_name", "price", "sale_price", "formatted_price", "formatted_sale_price", "category", "contextual_keywords", "similar_destination_ids", "image_url", "android_app_link", "ios_app_link", "ios_app_store_id"]) -> bool: ...
class FacebookMessengerBusinessMessageInfo(proto.Message):
    page_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, page_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["page_name"]) -> bool: ...
class HotelCalloutAsset(proto.Message):
    text: str
    language_code: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, text: str = ..., language_code: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["text", "language_code"]) -> bool: ...
class HotelPropertyAsset(proto.Message):
    place_id: str
    hotel_address: str
    hotel_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, place_id: str = ..., hotel_address: str = ..., hotel_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["place_id", "hotel_address", "hotel_name"]) -> bool: ...
class ImageAsset(proto.Message):
    data: bytes
    file_size: int
    mime_type: MimeTypeEnum.MimeType
    full_size: ImageDimension
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, data: bytes = ..., file_size: int = ..., mime_type: MimeTypeEnum.MimeType = ..., full_size: ImageDimension = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["data", "file_size", "mime_type", "full_size"]) -> bool: ...
class ImageDimension(proto.Message):
    height_pixels: int
    width_pixels: int
    url: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, height_pixels: int = ..., width_pixels: int = ..., url: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["height_pixels", "width_pixels", "url"]) -> bool: ...
class LeadFormAsset(proto.Message):
    business_name: str
    call_to_action_type: LeadFormCallToActionTypeEnum.LeadFormCallToActionType
    call_to_action_description: str
    headline: str
    description: str
    privacy_policy_url: str
    post_submit_headline: str
    post_submit_description: str
    fields: MutableSequence[LeadFormField]
    custom_question_fields: MutableSequence[LeadFormCustomQuestionField]
    delivery_methods: MutableSequence[LeadFormDeliveryMethod]
    post_submit_call_to_action_type: LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType
    background_image_asset: str
    desired_intent: LeadFormDesiredIntentEnum.LeadFormDesiredIntent
    custom_disclosure: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, business_name: str = ..., call_to_action_type: LeadFormCallToActionTypeEnum.LeadFormCallToActionType = ..., call_to_action_description: str = ..., headline: str = ..., description: str = ..., privacy_policy_url: str = ..., post_submit_headline: str = ..., post_submit_description: str = ..., fields: MutableSequence[LeadFormField] = ..., custom_question_fields: MutableSequence[LeadFormCustomQuestionField] = ..., delivery_methods: MutableSequence[LeadFormDeliveryMethod] = ..., post_submit_call_to_action_type: LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType = ..., background_image_asset: str = ..., desired_intent: LeadFormDesiredIntentEnum.LeadFormDesiredIntent = ..., custom_disclosure: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["business_name", "call_to_action_type", "call_to_action_description", "headline", "description", "privacy_policy_url", "post_submit_headline", "post_submit_description", "fields", "custom_question_fields", "delivery_methods", "post_submit_call_to_action_type", "background_image_asset", "desired_intent", "custom_disclosure"]) -> bool: ...
class LeadFormCustomQuestionField(proto.Message):
    custom_question_text: str
    single_choice_answers: LeadFormSingleChoiceAnswers
    has_location_answer: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, custom_question_text: str = ..., single_choice_answers: LeadFormSingleChoiceAnswers = ..., has_location_answer: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["custom_question_text", "single_choice_answers", "has_location_answer"]) -> bool: ...
class LeadFormDeliveryMethod(proto.Message):
    webhook: WebhookDelivery
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, webhook: WebhookDelivery = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["webhook"]) -> bool: ...
class LeadFormField(proto.Message):
    input_type: LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType
    single_choice_answers: LeadFormSingleChoiceAnswers
    has_location_answer: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, input_type: LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType = ..., single_choice_answers: LeadFormSingleChoiceAnswers = ..., has_location_answer: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["input_type", "single_choice_answers", "has_location_answer"]) -> bool: ...
class LeadFormSingleChoiceAnswers(proto.Message):
    answers: MutableSequence[str]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, answers: MutableSequence[str] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["answers"]) -> bool: ...
class LocationAsset(proto.Message):
    place_id: str
    business_profile_locations: MutableSequence[BusinessProfileLocation]
    location_ownership_type: LocationOwnershipTypeEnum.LocationOwnershipType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, place_id: str = ..., business_profile_locations: MutableSequence[BusinessProfileLocation] = ..., location_ownership_type: LocationOwnershipTypeEnum.LocationOwnershipType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["place_id", "business_profile_locations", "location_ownership_type"]) -> bool: ...
class MediaBundleAsset(proto.Message):
    data: bytes
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, data: bytes = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["data"]) -> bool: ...
class MobileAppAsset(proto.Message):
    app_id: str
    app_store: MobileAppVendorEnum.MobileAppVendor
    link_text: str
    start_date: str
    end_date: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, app_id: str = ..., app_store: MobileAppVendorEnum.MobileAppVendor = ..., link_text: str = ..., start_date: str = ..., end_date: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["app_id", "app_store", "link_text", "start_date", "end_date"]) -> bool: ...
class PageFeedAsset(proto.Message):
    page_url: str
    labels: MutableSequence[str]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, page_url: str = ..., labels: MutableSequence[str] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["page_url", "labels"]) -> bool: ...
class PriceAsset(proto.Message):
    type_: PriceExtensionTypeEnum.PriceExtensionType
    price_qualifier: PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    language_code: str
    price_offerings: MutableSequence[PriceOffering]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, type_: PriceExtensionTypeEnum.PriceExtensionType = ..., price_qualifier: PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier = ..., language_code: str = ..., price_offerings: MutableSequence[PriceOffering] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["type_", "price_qualifier", "language_code", "price_offerings"]) -> bool: ...
class PriceOffering(proto.Message):
    header: str
    description: str
    price: Money
    unit: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    final_url: str
    final_mobile_url: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, header: str = ..., description: str = ..., price: Money = ..., unit: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit = ..., final_url: str = ..., final_mobile_url: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["header", "description", "price", "unit", "final_url", "final_mobile_url"]) -> bool: ...
class PromotionAsset(proto.Message):
    promotion_target: str
    discount_modifier: PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    redemption_start_date: str
    redemption_end_date: str
    occasion: PromotionExtensionOccasionEnum.PromotionExtensionOccasion
    language_code: str
    start_date: str
    end_date: str
    ad_schedule_targets: MutableSequence[AdScheduleInfo]
    terms_and_conditions_text: str
    terms_and_conditions_uri: str
    percent_off: int
    money_amount_off: Money
    promotion_code: str
    orders_over_amount: Money
    promotion_barcode_info: PromotionBarcodeInfo
    promotion_qr_code_info: PromotionQrCodeInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, promotion_target: str = ..., discount_modifier: PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier = ..., redemption_start_date: str = ..., redemption_end_date: str = ..., occasion: PromotionExtensionOccasionEnum.PromotionExtensionOccasion = ..., language_code: str = ..., start_date: str = ..., end_date: str = ..., ad_schedule_targets: MutableSequence[AdScheduleInfo] = ..., terms_and_conditions_text: str = ..., terms_and_conditions_uri: str = ..., percent_off: int = ..., money_amount_off: Money = ..., promotion_code: str = ..., orders_over_amount: Money = ..., promotion_barcode_info: PromotionBarcodeInfo = ..., promotion_qr_code_info: PromotionQrCodeInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["promotion_target", "discount_modifier", "redemption_start_date", "redemption_end_date", "occasion", "language_code", "start_date", "end_date", "ad_schedule_targets", "terms_and_conditions_text", "terms_and_conditions_uri", "percent_off", "money_amount_off", "promotion_code", "orders_over_amount", "promotion_barcode_info", "promotion_qr_code_info"]) -> bool: ...
class PromotionBarcodeInfo(proto.Message):
    type_: PromotionBarcodeTypeEnum.PromotionBarcodeType
    barcode_content: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, type_: PromotionBarcodeTypeEnum.PromotionBarcodeType = ..., barcode_content: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["type_", "barcode_content"]) -> bool: ...
class PromotionQrCodeInfo(proto.Message):
    qr_code_content: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, qr_code_content: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["qr_code_content"]) -> bool: ...
class SitelinkAsset(proto.Message):
    link_text: str
    description1: str
    description2: str
    start_date: str
    end_date: str
    ad_schedule_targets: MutableSequence[AdScheduleInfo]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, link_text: str = ..., description1: str = ..., description2: str = ..., start_date: str = ..., end_date: str = ..., ad_schedule_targets: MutableSequence[AdScheduleInfo] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["link_text", "description1", "description2", "start_date", "end_date", "ad_schedule_targets"]) -> bool: ...
class StructuredSnippetAsset(proto.Message):
    header: str
    values: MutableSequence[str]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, header: str = ..., values: MutableSequence[str] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["header", "values"]) -> bool: ...
class TextAsset(proto.Message):
    text: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, text: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["text"]) -> bool: ...
class WebhookDelivery(proto.Message):
    advertiser_webhook_url: str
    google_secret: str
    payload_schema_version: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, advertiser_webhook_url: str = ..., google_secret: str = ..., payload_schema_version: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["advertiser_webhook_url", "google_secret", "payload_schema_version"]) -> bool: ...
class WhatsappBusinessMessageInfo(proto.Message):
    country_code: str
    phone_number: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, country_code: str = ..., phone_number: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["country_code", "phone_number"]) -> bool: ...
class YouTubeVideoListAsset(proto.Message):
    youtube_videos: MutableSequence[AdVideoAsset]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, youtube_videos: MutableSequence[AdVideoAsset] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["youtube_videos"]) -> bool: ...
class YoutubeVideoAsset(proto.Message):
    youtube_video_id: str
    youtube_video_title: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, youtube_video_id: str = ..., youtube_video_title: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["youtube_video_id", "youtube_video_title"]) -> bool: ...
class ZaloBusinessMessageInfo(proto.Message):
    oa_id: int
    custom_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, oa_id: int = ..., custom_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["oa_id", "custom_name"]) -> bool: ...
