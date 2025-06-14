import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import age_range_type, app_payment_model_type, brand_request_rejection_reason, brand_state, content_label_type, day_of_week as gage_day_of_week, device, gender_type, hotel_date_selection_type, income_range_type, interaction_type, keyword_match_type, listing_group_type, location_group_radius_units, minute_of_hour, parental_status_type, product_category_level, product_channel as gage_product_channel, product_channel_exclusivity as gage_product_channel_exclusivity, product_condition as gage_product_condition, product_custom_attribute_index, product_type_level, proximity_radius_units, webpage_condition_operand, webpage_condition_operator
from typing import MutableSequence

__protobuf__: Incomplete

class KeywordInfo(proto.Message):
    text: str
    match_type: keyword_match_type.KeywordMatchTypeEnum.KeywordMatchType

class PlacementInfo(proto.Message):
    url: str

class NegativeKeywordListInfo(proto.Message):
    shared_set: str

class MobileAppCategoryInfo(proto.Message):
    mobile_app_category_constant: str

class MobileApplicationInfo(proto.Message):
    app_id: str
    name: str

class LocationInfo(proto.Message):
    geo_target_constant: str

class DeviceInfo(proto.Message):
    type_: device.DeviceEnum.Device

class ListingGroupInfo(proto.Message):
    type_: listing_group_type.ListingGroupTypeEnum.ListingGroupType
    case_value: ListingDimensionInfo
    parent_ad_group_criterion: str
    path: ListingDimensionPath

class ListingDimensionPath(proto.Message):
    dimensions: MutableSequence['ListingDimensionInfo']

class ListingScopeInfo(proto.Message):
    dimensions: MutableSequence['ListingDimensionInfo']

class ListingDimensionInfo(proto.Message):
    hotel_id: HotelIdInfo
    hotel_class: HotelClassInfo
    hotel_country_region: HotelCountryRegionInfo
    hotel_state: HotelStateInfo
    hotel_city: HotelCityInfo
    product_category: ProductCategoryInfo
    product_brand: ProductBrandInfo
    product_channel: ProductChannelInfo
    product_channel_exclusivity: ProductChannelExclusivityInfo
    product_condition: ProductConditionInfo
    product_custom_attribute: ProductCustomAttributeInfo
    product_item_id: ProductItemIdInfo
    product_type: ProductTypeInfo
    product_grouping: ProductGroupingInfo
    product_labels: ProductLabelsInfo
    product_legacy_condition: ProductLegacyConditionInfo
    product_type_full: ProductTypeFullInfo
    activity_id: ActivityIdInfo
    activity_rating: ActivityRatingInfo
    activity_country: ActivityCountryInfo
    activity_state: ActivityStateInfo
    activity_city: ActivityCityInfo
    unknown_listing_dimension: UnknownListingDimensionInfo

class HotelIdInfo(proto.Message):
    value: str

class HotelClassInfo(proto.Message):
    value: int

class HotelCountryRegionInfo(proto.Message):
    country_region_criterion: str

class HotelStateInfo(proto.Message):
    state_criterion: str

class HotelCityInfo(proto.Message):
    city_criterion: str

class ProductCategoryInfo(proto.Message):
    category_id: int
    level: product_category_level.ProductCategoryLevelEnum.ProductCategoryLevel

class ProductBrandInfo(proto.Message):
    value: str

class ProductChannelInfo(proto.Message):
    channel: gage_product_channel.ProductChannelEnum.ProductChannel

class ProductChannelExclusivityInfo(proto.Message):
    channel_exclusivity: gage_product_channel_exclusivity.ProductChannelExclusivityEnum.ProductChannelExclusivity

class ProductConditionInfo(proto.Message):
    condition: gage_product_condition.ProductConditionEnum.ProductCondition

class ProductCustomAttributeInfo(proto.Message):
    value: str
    index: product_custom_attribute_index.ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex

class ProductItemIdInfo(proto.Message):
    value: str

class ProductTypeInfo(proto.Message):
    value: str
    level: product_type_level.ProductTypeLevelEnum.ProductTypeLevel

class ProductGroupingInfo(proto.Message):
    value: str

class ProductLabelsInfo(proto.Message):
    value: str

class ProductLegacyConditionInfo(proto.Message):
    value: str

class ProductTypeFullInfo(proto.Message):
    value: str

class UnknownListingDimensionInfo(proto.Message): ...

class HotelDateSelectionTypeInfo(proto.Message):
    type_: hotel_date_selection_type.HotelDateSelectionTypeEnum.HotelDateSelectionType

class HotelAdvanceBookingWindowInfo(proto.Message):
    min_days: int
    max_days: int

class HotelLengthOfStayInfo(proto.Message):
    min_nights: int
    max_nights: int

class HotelCheckInDateRangeInfo(proto.Message):
    start_date: str
    end_date: str

class HotelCheckInDayInfo(proto.Message):
    day_of_week: gage_day_of_week.DayOfWeekEnum.DayOfWeek

class ActivityIdInfo(proto.Message):
    value: str

class ActivityRatingInfo(proto.Message):
    value: int

class ActivityCountryInfo(proto.Message):
    value: str

class ActivityStateInfo(proto.Message):
    value: str

class ActivityCityInfo(proto.Message):
    value: str

class InteractionTypeInfo(proto.Message):
    type_: interaction_type.InteractionTypeEnum.InteractionType

class AdScheduleInfo(proto.Message):
    start_minute: minute_of_hour.MinuteOfHourEnum.MinuteOfHour
    end_minute: minute_of_hour.MinuteOfHourEnum.MinuteOfHour
    start_hour: int
    end_hour: int
    day_of_week: gage_day_of_week.DayOfWeekEnum.DayOfWeek

class AgeRangeInfo(proto.Message):
    type_: age_range_type.AgeRangeTypeEnum.AgeRangeType

class GenderInfo(proto.Message):
    type_: gender_type.GenderTypeEnum.GenderType

class IncomeRangeInfo(proto.Message):
    type_: income_range_type.IncomeRangeTypeEnum.IncomeRangeType

class ParentalStatusInfo(proto.Message):
    type_: parental_status_type.ParentalStatusTypeEnum.ParentalStatusType

class YouTubeVideoInfo(proto.Message):
    video_id: str

class YouTubeChannelInfo(proto.Message):
    channel_id: str

class UserListInfo(proto.Message):
    user_list: str

class ProximityInfo(proto.Message):
    geo_point: GeoPointInfo
    radius: float
    radius_units: proximity_radius_units.ProximityRadiusUnitsEnum.ProximityRadiusUnits
    address: AddressInfo

class GeoPointInfo(proto.Message):
    longitude_in_micro_degrees: int
    latitude_in_micro_degrees: int

class AddressInfo(proto.Message):
    postal_code: str
    province_code: str
    country_code: str
    province_name: str
    street_address: str
    street_address2: str
    city_name: str

class TopicInfo(proto.Message):
    topic_constant: str
    path: MutableSequence[str]

class LanguageInfo(proto.Message):
    language_constant: str

class IpBlockInfo(proto.Message):
    ip_address: str

class ContentLabelInfo(proto.Message):
    type_: content_label_type.ContentLabelTypeEnum.ContentLabelType

class CarrierInfo(proto.Message):
    carrier_constant: str

class UserInterestInfo(proto.Message):
    user_interest_category: str

class WebpageInfo(proto.Message):
    criterion_name: str
    conditions: MutableSequence['WebpageConditionInfo']
    coverage_percentage: float
    sample: WebpageSampleInfo

class WebpageConditionInfo(proto.Message):
    operand: webpage_condition_operand.WebpageConditionOperandEnum.WebpageConditionOperand
    operator: webpage_condition_operator.WebpageConditionOperatorEnum.WebpageConditionOperator
    argument: str

class WebpageListInfo(proto.Message):
    shared_set: str

class WebpageSampleInfo(proto.Message):
    sample_urls: MutableSequence[str]

class OperatingSystemVersionInfo(proto.Message):
    operating_system_version_constant: str

class AppPaymentModelInfo(proto.Message):
    type_: app_payment_model_type.AppPaymentModelTypeEnum.AppPaymentModelType

class MobileDeviceInfo(proto.Message):
    mobile_device_constant: str

class CustomAffinityInfo(proto.Message):
    custom_affinity: str

class CustomIntentInfo(proto.Message):
    custom_intent: str

class LocationGroupInfo(proto.Message):
    geo_target_constants: MutableSequence[str]
    radius: int
    radius_units: location_group_radius_units.LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits
    feed_item_sets: MutableSequence[str]
    enable_customer_level_location_asset_set: bool
    location_group_asset_sets: MutableSequence[str]

class CustomAudienceInfo(proto.Message):
    custom_audience: str

class CombinedAudienceInfo(proto.Message):
    combined_audience: str

class AudienceInfo(proto.Message):
    audience: str

class KeywordThemeInfo(proto.Message):
    keyword_theme_constant: str
    free_form_keyword_theme: str

class LocalServiceIdInfo(proto.Message):
    service_id: str

class SearchThemeInfo(proto.Message):
    text: str

class BrandInfo(proto.Message):
    display_name: str
    entity_id: str
    primary_url: str
    rejection_reason: brand_request_rejection_reason.BrandRequestRejectionReasonEnum.BrandRequestRejectionReason
    status: brand_state.BrandStateEnum.BrandState

class BrandListInfo(proto.Message):
    shared_set: str
