import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
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

__protobuf__: Incomplete

class KeywordInfo(proto.Message):
    text: Incomplete
    match_type: Incomplete

class PlacementInfo(proto.Message):
    url: Incomplete

class MobileAppCategoryInfo(proto.Message):
    mobile_app_category_constant: Incomplete

class MobileApplicationInfo(proto.Message):
    app_id: Incomplete
    name: Incomplete

class LocationInfo(proto.Message):
    geo_target_constant: Incomplete

class DeviceInfo(proto.Message):
    type_: Incomplete

class PreferredContentInfo(proto.Message):
    type_: Incomplete

class ListingGroupInfo(proto.Message):
    type_: Incomplete
    case_value: Incomplete
    parent_ad_group_criterion: Incomplete

class ListingScopeInfo(proto.Message):
    dimensions: Incomplete

class ListingDimensionInfo(proto.Message):
    hotel_id: Incomplete
    hotel_class: Incomplete
    hotel_country_region: Incomplete
    hotel_state: Incomplete
    hotel_city: Incomplete
    product_bidding_category: Incomplete
    product_brand: Incomplete
    product_channel: Incomplete
    product_channel_exclusivity: Incomplete
    product_condition: Incomplete
    product_custom_attribute: Incomplete
    product_item_id: Incomplete
    product_type: Incomplete
    product_grouping: Incomplete
    product_labels: Incomplete
    product_legacy_condition: Incomplete
    product_type_full: Incomplete
    unknown_listing_dimension: Incomplete

class HotelIdInfo(proto.Message):
    value: Incomplete

class HotelClassInfo(proto.Message):
    value: Incomplete

class HotelCountryRegionInfo(proto.Message):
    country_region_criterion: Incomplete

class HotelStateInfo(proto.Message):
    state_criterion: Incomplete

class HotelCityInfo(proto.Message):
    city_criterion: Incomplete

class ProductBiddingCategoryInfo(proto.Message):
    id: Incomplete
    country_code: Incomplete
    level: Incomplete

class ProductBrandInfo(proto.Message):
    value: Incomplete

class ProductChannelInfo(proto.Message):
    channel: Incomplete

class ProductChannelExclusivityInfo(proto.Message):
    channel_exclusivity: Incomplete

class ProductConditionInfo(proto.Message):
    condition: Incomplete

class ProductCustomAttributeInfo(proto.Message):
    value: Incomplete
    index: Incomplete

class ProductItemIdInfo(proto.Message):
    value: Incomplete

class ProductTypeInfo(proto.Message):
    value: Incomplete
    level: Incomplete

class ProductGroupingInfo(proto.Message):
    value: Incomplete

class ProductLabelsInfo(proto.Message):
    value: Incomplete

class ProductLegacyConditionInfo(proto.Message):
    value: Incomplete

class ProductTypeFullInfo(proto.Message):
    value: Incomplete

class UnknownListingDimensionInfo(proto.Message): ...

class HotelDateSelectionTypeInfo(proto.Message):
    type_: Incomplete

class HotelAdvanceBookingWindowInfo(proto.Message):
    min_days: Incomplete
    max_days: Incomplete

class HotelLengthOfStayInfo(proto.Message):
    min_nights: Incomplete
    max_nights: Incomplete

class HotelCheckInDateRangeInfo(proto.Message):
    start_date: Incomplete
    end_date: Incomplete

class HotelCheckInDayInfo(proto.Message):
    day_of_week: Incomplete

class InteractionTypeInfo(proto.Message):
    type_: Incomplete

class AdScheduleInfo(proto.Message):
    start_minute: Incomplete
    end_minute: Incomplete
    start_hour: Incomplete
    end_hour: Incomplete
    day_of_week: Incomplete

class AgeRangeInfo(proto.Message):
    type_: Incomplete

class GenderInfo(proto.Message):
    type_: Incomplete

class IncomeRangeInfo(proto.Message):
    type_: Incomplete

class ParentalStatusInfo(proto.Message):
    type_: Incomplete

class YouTubeVideoInfo(proto.Message):
    video_id: Incomplete

class YouTubeChannelInfo(proto.Message):
    channel_id: Incomplete

class UserListInfo(proto.Message):
    user_list: Incomplete

class ProximityInfo(proto.Message):
    geo_point: Incomplete
    radius: Incomplete
    radius_units: Incomplete
    address: Incomplete

class GeoPointInfo(proto.Message):
    longitude_in_micro_degrees: Incomplete
    latitude_in_micro_degrees: Incomplete

class AddressInfo(proto.Message):
    postal_code: Incomplete
    province_code: Incomplete
    country_code: Incomplete
    province_name: Incomplete
    street_address: Incomplete
    street_address2: Incomplete
    city_name: Incomplete

class TopicInfo(proto.Message):
    topic_constant: Incomplete
    path: Incomplete

class LanguageInfo(proto.Message):
    language_constant: Incomplete

class IpBlockInfo(proto.Message):
    ip_address: Incomplete

class ContentLabelInfo(proto.Message):
    type_: Incomplete

class CarrierInfo(proto.Message):
    carrier_constant: Incomplete

class UserInterestInfo(proto.Message):
    user_interest_category: Incomplete

class WebpageInfo(proto.Message):
    criterion_name: Incomplete
    conditions: Incomplete
    coverage_percentage: Incomplete
    sample: Incomplete

class WebpageConditionInfo(proto.Message):
    operand: Incomplete
    operator: Incomplete
    argument: Incomplete

class WebpageSampleInfo(proto.Message):
    sample_urls: Incomplete

class OperatingSystemVersionInfo(proto.Message):
    operating_system_version_constant: Incomplete

class AppPaymentModelInfo(proto.Message):
    type_: Incomplete

class MobileDeviceInfo(proto.Message):
    mobile_device_constant: Incomplete

class CustomAffinityInfo(proto.Message):
    custom_affinity: Incomplete

class CustomIntentInfo(proto.Message):
    custom_intent: Incomplete

class LocationGroupInfo(proto.Message):
    feed: Incomplete
    geo_target_constants: Incomplete
    radius: Incomplete
    radius_units: Incomplete
    feed_item_sets: Incomplete

class CustomAudienceInfo(proto.Message):
    custom_audience: Incomplete

class CombinedAudienceInfo(proto.Message):
    combined_audience: Incomplete

class AudienceInfo(proto.Message):
    audience: Incomplete

class KeywordThemeInfo(proto.Message):
    keyword_theme_constant: Incomplete
    free_form_keyword_theme: Incomplete
