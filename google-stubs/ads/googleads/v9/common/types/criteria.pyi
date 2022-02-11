from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    age_range_type as age_range_type,
    app_payment_model_type as app_payment_model_type,
    content_label_type as content_label_type,
    device as device,
    gender_type as gender_type,
    hotel_date_selection_type as hotel_date_selection_type,
    income_range_type as income_range_type,
    interaction_type as interaction_type,
    keyword_match_type as keyword_match_type,
    listing_group_type as listing_group_type,
    location_group_radius_units as location_group_radius_units,
    minute_of_hour as minute_of_hour,
    parental_status_type as parental_status_type,
    preferred_content_type as preferred_content_type,
    product_bidding_category_level as product_bidding_category_level,
    product_custom_attribute_index as product_custom_attribute_index,
    product_type_level as product_type_level,
    proximity_radius_units as proximity_radius_units,
    webpage_condition_operand as webpage_condition_operand,
    webpage_condition_operator as webpage_condition_operator,
)

__protobuf__: Any

class KeywordInfo(proto.Message):
    text: Any
    match_type: Any

class PlacementInfo(proto.Message):
    url: Any

class MobileAppCategoryInfo(proto.Message):
    mobile_app_category_constant: Any

class MobileApplicationInfo(proto.Message):
    app_id: Any
    name: Any

class LocationInfo(proto.Message):
    geo_target_constant: Any

class DeviceInfo(proto.Message):
    type_: Any

class PreferredContentInfo(proto.Message):
    type_: Any

class ListingGroupInfo(proto.Message):
    type_: Any
    case_value: Any
    parent_ad_group_criterion: Any

class ListingScopeInfo(proto.Message):
    dimensions: Any

class ListingDimensionInfo(proto.Message):
    hotel_id: Any
    hotel_class: Any
    hotel_country_region: Any
    hotel_state: Any
    hotel_city: Any
    product_bidding_category: Any
    product_brand: Any
    product_channel: Any
    product_channel_exclusivity: Any
    product_condition: Any
    product_custom_attribute: Any
    product_item_id: Any
    product_type: Any
    unknown_listing_dimension: Any

class HotelIdInfo(proto.Message):
    value: Any

class HotelClassInfo(proto.Message):
    value: Any

class HotelCountryRegionInfo(proto.Message):
    country_region_criterion: Any

class HotelStateInfo(proto.Message):
    state_criterion: Any

class HotelCityInfo(proto.Message):
    city_criterion: Any

class ProductBiddingCategoryInfo(proto.Message):
    id: Any
    country_code: Any
    level: Any

class ProductBrandInfo(proto.Message):
    value: Any

class ProductChannelInfo(proto.Message):
    channel: Any

class ProductChannelExclusivityInfo(proto.Message):
    channel_exclusivity: Any

class ProductConditionInfo(proto.Message):
    condition: Any

class ProductCustomAttributeInfo(proto.Message):
    value: Any
    index: Any

class ProductItemIdInfo(proto.Message):
    value: Any

class ProductTypeInfo(proto.Message):
    value: Any
    level: Any

class UnknownListingDimensionInfo(proto.Message): ...

class HotelDateSelectionTypeInfo(proto.Message):
    type_: Any

class HotelAdvanceBookingWindowInfo(proto.Message):
    min_days: Any
    max_days: Any

class HotelLengthOfStayInfo(proto.Message):
    min_nights: Any
    max_nights: Any

class HotelCheckInDateRangeInfo(proto.Message):
    start_date: Any
    end_date: Any

class HotelCheckInDayInfo(proto.Message):
    day_of_week: Any

class InteractionTypeInfo(proto.Message):
    type_: Any

class AdScheduleInfo(proto.Message):
    start_minute: Any
    end_minute: Any
    start_hour: Any
    end_hour: Any
    day_of_week: Any

class AgeRangeInfo(proto.Message):
    type_: Any

class GenderInfo(proto.Message):
    type_: Any

class IncomeRangeInfo(proto.Message):
    type_: Any

class ParentalStatusInfo(proto.Message):
    type_: Any

class YouTubeVideoInfo(proto.Message):
    video_id: Any

class YouTubeChannelInfo(proto.Message):
    channel_id: Any

class UserListInfo(proto.Message):
    user_list: Any

class ProximityInfo(proto.Message):
    geo_point: Any
    radius: Any
    radius_units: Any
    address: Any

class GeoPointInfo(proto.Message):
    longitude_in_micro_degrees: Any
    latitude_in_micro_degrees: Any

class AddressInfo(proto.Message):
    postal_code: Any
    province_code: Any
    country_code: Any
    province_name: Any
    street_address: Any
    street_address2: Any
    city_name: Any

class TopicInfo(proto.Message):
    topic_constant: Any
    path: Any

class LanguageInfo(proto.Message):
    language_constant: Any

class IpBlockInfo(proto.Message):
    ip_address: Any

class ContentLabelInfo(proto.Message):
    type_: Any

class CarrierInfo(proto.Message):
    carrier_constant: Any

class UserInterestInfo(proto.Message):
    user_interest_category: Any

class WebpageInfo(proto.Message):
    criterion_name: Any
    conditions: Any
    coverage_percentage: Any
    sample: Any

class WebpageConditionInfo(proto.Message):
    operand: Any
    operator: Any
    argument: Any

class WebpageSampleInfo(proto.Message):
    sample_urls: Any

class OperatingSystemVersionInfo(proto.Message):
    operating_system_version_constant: Any

class AppPaymentModelInfo(proto.Message):
    type_: Any

class MobileDeviceInfo(proto.Message):
    mobile_device_constant: Any

class CustomAffinityInfo(proto.Message):
    custom_affinity: Any

class CustomIntentInfo(proto.Message):
    custom_intent: Any

class LocationGroupInfo(proto.Message):
    feed: Any
    geo_target_constants: Any
    radius: Any
    radius_units: Any
    feed_item_sets: Any

class CustomAudienceInfo(proto.Message):
    custom_audience: Any

class CombinedAudienceInfo(proto.Message):
    combined_audience: Any

class KeywordThemeInfo(proto.Message):
    keyword_theme_constant: Any
    free_form_keyword_theme: Any
