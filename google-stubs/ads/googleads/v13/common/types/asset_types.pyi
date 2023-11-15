from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.common.types.criteria import AdScheduleInfo
from google.ads.googleads.v13.common.types.feed_common import Money
from google.ads.googleads.v13.enums.types.call_conversion_reporting_state import (
    CallConversionReportingStateEnum,
)
from google.ads.googleads.v13.enums.types.call_to_action_type import (
    CallToActionTypeEnum,
)
from google.ads.googleads.v13.enums.types.lead_form_call_to_action_type import (
    LeadFormCallToActionTypeEnum,
)
from google.ads.googleads.v13.enums.types.lead_form_desired_intent import (
    LeadFormDesiredIntentEnum,
)
from google.ads.googleads.v13.enums.types.lead_form_field_user_input_type import (
    LeadFormFieldUserInputTypeEnum,
)
from google.ads.googleads.v13.enums.types.lead_form_post_submit_call_to_action_type import (
    LeadFormPostSubmitCallToActionTypeEnum,
)
from google.ads.googleads.v13.enums.types.location_ownership_type import (
    LocationOwnershipTypeEnum,
)
from google.ads.googleads.v13.enums.types.mime_type import MimeTypeEnum
from google.ads.googleads.v13.enums.types.mobile_app_vendor import MobileAppVendorEnum
from google.ads.googleads.v13.enums.types.price_extension_price_qualifier import (
    PriceExtensionPriceQualifierEnum,
)
from google.ads.googleads.v13.enums.types.price_extension_price_unit import (
    PriceExtensionPriceUnitEnum,
)
from google.ads.googleads.v13.enums.types.price_extension_type import (
    PriceExtensionTypeEnum,
)
from google.ads.googleads.v13.enums.types.promotion_extension_discount_modifier import (
    PromotionExtensionDiscountModifierEnum,
)
from google.ads.googleads.v13.enums.types.promotion_extension_occasion import (
    PromotionExtensionOccasionEnum,
)

_M = TypeVar("_M")

class BookOnGoogleAsset(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    ...

class BusinessProfileLocation(proto.Message):
    labels: MutableSequence[str]
    store_code: str
    listing_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        labels: MutableSequence[str] = ...,
        store_code: str = ...,
        listing_id: int = ...,
    ) -> None: ...

class CallAsset(proto.Message):
    country_code: str
    phone_number: str
    call_conversion_reporting_state: CallConversionReportingStateEnum.CallConversionReportingState
    call_conversion_action: str
    ad_schedule_targets: MutableSequence[AdScheduleInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        country_code: str = ...,
        phone_number: str = ...,
        call_conversion_reporting_state: CallConversionReportingStateEnum.CallConversionReportingState = ...,
        call_conversion_action: str = ...,
        ad_schedule_targets: MutableSequence[AdScheduleInfo] = ...,
    ) -> None: ...

class CallToActionAsset(proto.Message):
    call_to_action: CallToActionTypeEnum.CallToActionType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        call_to_action: CallToActionTypeEnum.CallToActionType = ...,
    ) -> None: ...

class CalloutAsset(proto.Message):
    callout_text: str
    start_date: str
    end_date: str
    ad_schedule_targets: MutableSequence[AdScheduleInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        callout_text: str = ...,
        start_date: str = ...,
        end_date: str = ...,
        ad_schedule_targets: MutableSequence[AdScheduleInfo] = ...,
    ) -> None: ...

class DiscoveryCarouselCardAsset(proto.Message):
    marketing_image_asset: str
    square_marketing_image_asset: str
    portrait_marketing_image_asset: str
    headline: str
    call_to_action_text: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        marketing_image_asset: str = ...,
        square_marketing_image_asset: str = ...,
        portrait_marketing_image_asset: str = ...,
        headline: str = ...,
        call_to_action_text: str = ...,
    ) -> None: ...

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        id: str = ...,
        id2: str = ...,
        item_title: str = ...,
        item_subtitle: str = ...,
        item_description: str = ...,
        item_address: str = ...,
        item_category: str = ...,
        price: str = ...,
        sale_price: str = ...,
        formatted_price: str = ...,
        formatted_sale_price: str = ...,
        image_url: str = ...,
        contextual_keywords: MutableSequence[str] = ...,
        android_app_link: str = ...,
        ios_app_link: str = ...,
        ios_app_store_id: int = ...,
        similar_ids: MutableSequence[str] = ...,
    ) -> None: ...

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        program_id: str = ...,
        location_id: str = ...,
        program_name: str = ...,
        subject: str = ...,
        program_description: str = ...,
        school_name: str = ...,
        address: str = ...,
        contextual_keywords: MutableSequence[str] = ...,
        android_app_link: str = ...,
        similar_program_ids: MutableSequence[str] = ...,
        ios_app_link: str = ...,
        ios_app_store_id: int = ...,
        thumbnail_image_url: str = ...,
        image_url: str = ...,
    ) -> None: ...

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        destination_id: str = ...,
        origin_id: str = ...,
        flight_description: str = ...,
        image_url: str = ...,
        destination_name: str = ...,
        origin_name: str = ...,
        flight_price: str = ...,
        flight_sale_price: str = ...,
        formatted_price: str = ...,
        formatted_sale_price: str = ...,
        android_app_link: str = ...,
        ios_app_link: str = ...,
        ios_app_store_id: int = ...,
        similar_destination_ids: MutableSequence[str] = ...,
        custom_mapping: str = ...,
    ) -> None: ...

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        property_id: str = ...,
        property_name: str = ...,
        image_url: str = ...,
        destination_name: str = ...,
        description: str = ...,
        price: str = ...,
        sale_price: str = ...,
        star_rating: int = ...,
        category: str = ...,
        contextual_keywords: MutableSequence[str] = ...,
        address: str = ...,
        android_app_link: str = ...,
        ios_app_link: str = ...,
        ios_app_store_id: int = ...,
        formatted_price: str = ...,
        formatted_sale_price: str = ...,
        similar_property_ids: MutableSequence[str] = ...,
    ) -> None: ...

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        job_id: str = ...,
        location_id: str = ...,
        job_title: str = ...,
        job_subtitle: str = ...,
        description: str = ...,
        image_url: str = ...,
        job_category: str = ...,
        contextual_keywords: MutableSequence[str] = ...,
        address: str = ...,
        salary: str = ...,
        android_app_link: str = ...,
        similar_job_ids: MutableSequence[str] = ...,
        ios_app_link: str = ...,
        ios_app_store_id: int = ...,
    ) -> None: ...

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        deal_id: str = ...,
        deal_name: str = ...,
        subtitle: str = ...,
        description: str = ...,
        price: str = ...,
        sale_price: str = ...,
        image_url: str = ...,
        address: str = ...,
        category: str = ...,
        contextual_keywords: MutableSequence[str] = ...,
        formatted_price: str = ...,
        formatted_sale_price: str = ...,
        android_app_link: str = ...,
        similar_deal_ids: MutableSequence[str] = ...,
        ios_app_link: str = ...,
        ios_app_store_id: int = ...,
    ) -> None: ...

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        listing_id: str = ...,
        listing_name: str = ...,
        city_name: str = ...,
        description: str = ...,
        address: str = ...,
        price: str = ...,
        image_url: str = ...,
        property_type: str = ...,
        listing_type: str = ...,
        contextual_keywords: MutableSequence[str] = ...,
        formatted_price: str = ...,
        android_app_link: str = ...,
        ios_app_link: str = ...,
        ios_app_store_id: int = ...,
        similar_listing_ids: MutableSequence[str] = ...,
    ) -> None: ...

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        destination_id: str = ...,
        origin_id: str = ...,
        title: str = ...,
        destination_name: str = ...,
        destination_address: str = ...,
        origin_name: str = ...,
        price: str = ...,
        sale_price: str = ...,
        formatted_price: str = ...,
        formatted_sale_price: str = ...,
        category: str = ...,
        contextual_keywords: MutableSequence[str] = ...,
        similar_destination_ids: MutableSequence[str] = ...,
        image_url: str = ...,
        android_app_link: str = ...,
        ios_app_link: str = ...,
        ios_app_store_id: int = ...,
    ) -> None: ...

class HotelCalloutAsset(proto.Message):
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

class HotelPropertyAsset(proto.Message):
    place_id: str
    hotel_address: str
    hotel_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        place_id: str = ...,
        hotel_address: str = ...,
        hotel_name: str = ...,
    ) -> None: ...

class ImageAsset(proto.Message):
    data: bytes
    file_size: int
    mime_type: MimeTypeEnum.MimeType
    full_size: ImageDimension
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        data: bytes = ...,
        file_size: int = ...,
        mime_type: MimeTypeEnum.MimeType = ...,
        full_size: ImageDimension = ...,
    ) -> None: ...

class ImageDimension(proto.Message):
    height_pixels: int
    width_pixels: int
    url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        height_pixels: int = ...,
        width_pixels: int = ...,
        url: str = ...,
    ) -> None: ...

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        business_name: str = ...,
        call_to_action_type: LeadFormCallToActionTypeEnum.LeadFormCallToActionType = ...,
        call_to_action_description: str = ...,
        headline: str = ...,
        description: str = ...,
        privacy_policy_url: str = ...,
        post_submit_headline: str = ...,
        post_submit_description: str = ...,
        fields: MutableSequence[LeadFormField] = ...,
        custom_question_fields: MutableSequence[LeadFormCustomQuestionField] = ...,
        delivery_methods: MutableSequence[LeadFormDeliveryMethod] = ...,
        post_submit_call_to_action_type: LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType = ...,
        background_image_asset: str = ...,
        desired_intent: LeadFormDesiredIntentEnum.LeadFormDesiredIntent = ...,
        custom_disclosure: str = ...,
    ) -> None: ...

class LeadFormCustomQuestionField(proto.Message):
    custom_question_text: str
    single_choice_answers: LeadFormSingleChoiceAnswers
    has_location_answer: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        custom_question_text: str = ...,
        single_choice_answers: LeadFormSingleChoiceAnswers = ...,
        has_location_answer: bool = ...,
    ) -> None: ...

class LeadFormDeliveryMethod(proto.Message):
    webhook: WebhookDelivery
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        webhook: WebhookDelivery = ...,
    ) -> None: ...

class LeadFormField(proto.Message):
    input_type: LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType
    single_choice_answers: LeadFormSingleChoiceAnswers
    has_location_answer: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        input_type: LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType = ...,
        single_choice_answers: LeadFormSingleChoiceAnswers = ...,
        has_location_answer: bool = ...,
    ) -> None: ...

class LeadFormSingleChoiceAnswers(proto.Message):
    answers: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        answers: MutableSequence[str] = ...,
    ) -> None: ...

class LocationAsset(proto.Message):
    place_id: str
    business_profile_locations: MutableSequence[BusinessProfileLocation]
    location_ownership_type: LocationOwnershipTypeEnum.LocationOwnershipType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        place_id: str = ...,
        business_profile_locations: MutableSequence[BusinessProfileLocation] = ...,
        location_ownership_type: LocationOwnershipTypeEnum.LocationOwnershipType = ...,
    ) -> None: ...

class MediaBundleAsset(proto.Message):
    data: bytes
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        data: bytes = ...,
    ) -> None: ...

class MobileAppAsset(proto.Message):
    app_id: str
    app_store: MobileAppVendorEnum.MobileAppVendor
    link_text: str
    start_date: str
    end_date: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        app_id: str = ...,
        app_store: MobileAppVendorEnum.MobileAppVendor = ...,
        link_text: str = ...,
        start_date: str = ...,
        end_date: str = ...,
    ) -> None: ...

class PageFeedAsset(proto.Message):
    page_url: str
    labels: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        page_url: str = ...,
        labels: MutableSequence[str] = ...,
    ) -> None: ...

class PriceAsset(proto.Message):
    type_: PriceExtensionTypeEnum.PriceExtensionType
    price_qualifier: PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    language_code: str
    price_offerings: MutableSequence[PriceOffering]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: PriceExtensionTypeEnum.PriceExtensionType = ...,
        price_qualifier: PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier = ...,
        language_code: str = ...,
        price_offerings: MutableSequence[PriceOffering] = ...,
    ) -> None: ...

class PriceOffering(proto.Message):
    header: str
    description: str
    price: Money
    unit: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    final_url: str
    final_mobile_url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        header: str = ...,
        description: str = ...,
        price: Money = ...,
        unit: PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit = ...,
        final_url: str = ...,
        final_mobile_url: str = ...,
    ) -> None: ...

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
        redemption_start_date: str = ...,
        redemption_end_date: str = ...,
        occasion: PromotionExtensionOccasionEnum.PromotionExtensionOccasion = ...,
        language_code: str = ...,
        start_date: str = ...,
        end_date: str = ...,
        ad_schedule_targets: MutableSequence[AdScheduleInfo] = ...,
        percent_off: int = ...,
        money_amount_off: Money = ...,
        promotion_code: str = ...,
        orders_over_amount: Money = ...,
    ) -> None: ...

class SitelinkAsset(proto.Message):
    link_text: str
    description1: str
    description2: str
    start_date: str
    end_date: str
    ad_schedule_targets: MutableSequence[AdScheduleInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        link_text: str = ...,
        description1: str = ...,
        description2: str = ...,
        start_date: str = ...,
        end_date: str = ...,
        ad_schedule_targets: MutableSequence[AdScheduleInfo] = ...,
    ) -> None: ...

class StructuredSnippetAsset(proto.Message):
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

class TextAsset(proto.Message):
    text: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        text: str = ...,
    ) -> None: ...

class WebhookDelivery(proto.Message):
    advertiser_webhook_url: str
    google_secret: str
    payload_schema_version: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        advertiser_webhook_url: str = ...,
        google_secret: str = ...,
        payload_schema_version: int = ...,
    ) -> None: ...

class YoutubeVideoAsset(proto.Message):
    youtube_video_id: str
    youtube_video_title: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        youtube_video_id: str = ...,
        youtube_video_title: str = ...,
    ) -> None: ...
