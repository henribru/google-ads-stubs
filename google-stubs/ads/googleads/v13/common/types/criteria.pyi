from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.age_range_type import AgeRangeTypeEnum
from google.ads.googleads.v13.enums.types.app_payment_model_type import (
    AppPaymentModelTypeEnum,
)
from google.ads.googleads.v13.enums.types.content_label_type import ContentLabelTypeEnum
from google.ads.googleads.v13.enums.types.day_of_week import DayOfWeekEnum
from google.ads.googleads.v13.enums.types.device import DeviceEnum
from google.ads.googleads.v13.enums.types.gender_type import GenderTypeEnum
from google.ads.googleads.v13.enums.types.hotel_date_selection_type import (
    HotelDateSelectionTypeEnum,
)
from google.ads.googleads.v13.enums.types.income_range_type import IncomeRangeTypeEnum
from google.ads.googleads.v13.enums.types.interaction_type import InteractionTypeEnum
from google.ads.googleads.v13.enums.types.keyword_match_type import KeywordMatchTypeEnum
from google.ads.googleads.v13.enums.types.listing_group_type import ListingGroupTypeEnum
from google.ads.googleads.v13.enums.types.location_group_radius_units import (
    LocationGroupRadiusUnitsEnum,
)
from google.ads.googleads.v13.enums.types.minute_of_hour import MinuteOfHourEnum
from google.ads.googleads.v13.enums.types.parental_status_type import (
    ParentalStatusTypeEnum,
)
from google.ads.googleads.v13.enums.types.product_bidding_category_level import (
    ProductBiddingCategoryLevelEnum,
)
from google.ads.googleads.v13.enums.types.product_channel import ProductChannelEnum
from google.ads.googleads.v13.enums.types.product_channel_exclusivity import (
    ProductChannelExclusivityEnum,
)
from google.ads.googleads.v13.enums.types.product_condition import ProductConditionEnum
from google.ads.googleads.v13.enums.types.product_custom_attribute_index import (
    ProductCustomAttributeIndexEnum,
)
from google.ads.googleads.v13.enums.types.product_type_level import ProductTypeLevelEnum
from google.ads.googleads.v13.enums.types.proximity_radius_units import (
    ProximityRadiusUnitsEnum,
)
from google.ads.googleads.v13.enums.types.webpage_condition_operand import (
    WebpageConditionOperandEnum,
)
from google.ads.googleads.v13.enums.types.webpage_condition_operator import (
    WebpageConditionOperatorEnum,
)

_M = TypeVar("_M")

class ActivityCountryInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...

class ActivityIdInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...

class ActivityRatingInfo(proto.Message):
    value: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: int = ...,
    ) -> None: ...

class AdScheduleInfo(proto.Message):
    start_minute: MinuteOfHourEnum.MinuteOfHour
    end_minute: MinuteOfHourEnum.MinuteOfHour
    start_hour: int
    end_hour: int
    day_of_week: DayOfWeekEnum.DayOfWeek
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        start_minute: MinuteOfHourEnum.MinuteOfHour = ...,
        end_minute: MinuteOfHourEnum.MinuteOfHour = ...,
        start_hour: int = ...,
        end_hour: int = ...,
        day_of_week: DayOfWeekEnum.DayOfWeek = ...,
    ) -> None: ...

class AddressInfo(proto.Message):
    postal_code: str
    province_code: str
    country_code: str
    province_name: str
    street_address: str
    street_address2: str
    city_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        postal_code: str = ...,
        province_code: str = ...,
        country_code: str = ...,
        province_name: str = ...,
        street_address: str = ...,
        street_address2: str = ...,
        city_name: str = ...,
    ) -> None: ...

class AgeRangeInfo(proto.Message):
    type_: AgeRangeTypeEnum.AgeRangeType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: AgeRangeTypeEnum.AgeRangeType = ...,
    ) -> None: ...

class AppPaymentModelInfo(proto.Message):
    type_: AppPaymentModelTypeEnum.AppPaymentModelType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: AppPaymentModelTypeEnum.AppPaymentModelType = ...,
    ) -> None: ...

class AudienceInfo(proto.Message):
    audience: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        audience: str = ...,
    ) -> None: ...

class CarrierInfo(proto.Message):
    carrier_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        carrier_constant: str = ...,
    ) -> None: ...

class CombinedAudienceInfo(proto.Message):
    combined_audience: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        combined_audience: str = ...,
    ) -> None: ...

class ContentLabelInfo(proto.Message):
    type_: ContentLabelTypeEnum.ContentLabelType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: ContentLabelTypeEnum.ContentLabelType = ...,
    ) -> None: ...

class CustomAffinityInfo(proto.Message):
    custom_affinity: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        custom_affinity: str = ...,
    ) -> None: ...

class CustomAudienceInfo(proto.Message):
    custom_audience: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        custom_audience: str = ...,
    ) -> None: ...

class CustomIntentInfo(proto.Message):
    custom_intent: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        custom_intent: str = ...,
    ) -> None: ...

class DeviceInfo(proto.Message):
    type_: DeviceEnum.Device
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: DeviceEnum.Device = ...,
    ) -> None: ...

class GenderInfo(proto.Message):
    type_: GenderTypeEnum.GenderType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: GenderTypeEnum.GenderType = ...,
    ) -> None: ...

class GeoPointInfo(proto.Message):
    longitude_in_micro_degrees: int
    latitude_in_micro_degrees: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        longitude_in_micro_degrees: int = ...,
        latitude_in_micro_degrees: int = ...,
    ) -> None: ...

class HotelAdvanceBookingWindowInfo(proto.Message):
    min_days: int
    max_days: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        min_days: int = ...,
        max_days: int = ...,
    ) -> None: ...

class HotelCheckInDateRangeInfo(proto.Message):
    start_date: str
    end_date: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        start_date: str = ...,
        end_date: str = ...,
    ) -> None: ...

class HotelCheckInDayInfo(proto.Message):
    day_of_week: DayOfWeekEnum.DayOfWeek
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        day_of_week: DayOfWeekEnum.DayOfWeek = ...,
    ) -> None: ...

class HotelCityInfo(proto.Message):
    city_criterion: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        city_criterion: str = ...,
    ) -> None: ...

class HotelClassInfo(proto.Message):
    value: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: int = ...,
    ) -> None: ...

class HotelCountryRegionInfo(proto.Message):
    country_region_criterion: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        country_region_criterion: str = ...,
    ) -> None: ...

class HotelDateSelectionTypeInfo(proto.Message):
    type_: HotelDateSelectionTypeEnum.HotelDateSelectionType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: HotelDateSelectionTypeEnum.HotelDateSelectionType = ...,
    ) -> None: ...

class HotelIdInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...

class HotelLengthOfStayInfo(proto.Message):
    min_nights: int
    max_nights: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        min_nights: int = ...,
        max_nights: int = ...,
    ) -> None: ...

class HotelStateInfo(proto.Message):
    state_criterion: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        state_criterion: str = ...,
    ) -> None: ...

class IncomeRangeInfo(proto.Message):
    type_: IncomeRangeTypeEnum.IncomeRangeType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: IncomeRangeTypeEnum.IncomeRangeType = ...,
    ) -> None: ...

class InteractionTypeInfo(proto.Message):
    type_: InteractionTypeEnum.InteractionType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: InteractionTypeEnum.InteractionType = ...,
    ) -> None: ...

class IpBlockInfo(proto.Message):
    ip_address: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ip_address: str = ...,
    ) -> None: ...

class KeywordInfo(proto.Message):
    text: str
    match_type: KeywordMatchTypeEnum.KeywordMatchType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        text: str = ...,
        match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
    ) -> None: ...

class KeywordThemeInfo(proto.Message):
    keyword_theme_constant: str
    free_form_keyword_theme: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_theme_constant: str = ...,
        free_form_keyword_theme: str = ...,
    ) -> None: ...

class LanguageInfo(proto.Message):
    language_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        language_constant: str = ...,
    ) -> None: ...

class ListingDimensionInfo(proto.Message):
    hotel_id: HotelIdInfo
    hotel_class: HotelClassInfo
    hotel_country_region: HotelCountryRegionInfo
    hotel_state: HotelStateInfo
    hotel_city: HotelCityInfo
    product_bidding_category: ProductBiddingCategoryInfo
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
    unknown_listing_dimension: UnknownListingDimensionInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        hotel_id: HotelIdInfo = ...,
        hotel_class: HotelClassInfo = ...,
        hotel_country_region: HotelCountryRegionInfo = ...,
        hotel_state: HotelStateInfo = ...,
        hotel_city: HotelCityInfo = ...,
        product_bidding_category: ProductBiddingCategoryInfo = ...,
        product_brand: ProductBrandInfo = ...,
        product_channel: ProductChannelInfo = ...,
        product_channel_exclusivity: ProductChannelExclusivityInfo = ...,
        product_condition: ProductConditionInfo = ...,
        product_custom_attribute: ProductCustomAttributeInfo = ...,
        product_item_id: ProductItemIdInfo = ...,
        product_type: ProductTypeInfo = ...,
        product_grouping: ProductGroupingInfo = ...,
        product_labels: ProductLabelsInfo = ...,
        product_legacy_condition: ProductLegacyConditionInfo = ...,
        product_type_full: ProductTypeFullInfo = ...,
        activity_id: ActivityIdInfo = ...,
        activity_rating: ActivityRatingInfo = ...,
        activity_country: ActivityCountryInfo = ...,
        unknown_listing_dimension: UnknownListingDimensionInfo = ...,
    ) -> None: ...

class ListingGroupInfo(proto.Message):
    type_: ListingGroupTypeEnum.ListingGroupType
    case_value: ListingDimensionInfo
    parent_ad_group_criterion: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: ListingGroupTypeEnum.ListingGroupType = ...,
        case_value: ListingDimensionInfo = ...,
        parent_ad_group_criterion: str = ...,
    ) -> None: ...

class ListingScopeInfo(proto.Message):
    dimensions: MutableSequence[ListingDimensionInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dimensions: MutableSequence[ListingDimensionInfo] = ...,
    ) -> None: ...

class LocalServiceIdInfo(proto.Message):
    service_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        service_id: str = ...,
    ) -> None: ...

class LocationGroupInfo(proto.Message):
    feed: str
    geo_target_constants: MutableSequence[str]
    radius: int
    radius_units: LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits
    feed_item_sets: MutableSequence[str]
    enable_customer_level_location_asset_set: bool
    location_group_asset_sets: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        feed: str = ...,
        geo_target_constants: MutableSequence[str] = ...,
        radius: int = ...,
        radius_units: LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits = ...,
        feed_item_sets: MutableSequence[str] = ...,
        enable_customer_level_location_asset_set: bool = ...,
        location_group_asset_sets: MutableSequence[str] = ...,
    ) -> None: ...

class LocationInfo(proto.Message):
    geo_target_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        geo_target_constant: str = ...,
    ) -> None: ...

class MobileAppCategoryInfo(proto.Message):
    mobile_app_category_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        mobile_app_category_constant: str = ...,
    ) -> None: ...

class MobileApplicationInfo(proto.Message):
    app_id: str
    name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        app_id: str = ...,
        name: str = ...,
    ) -> None: ...

class MobileDeviceInfo(proto.Message):
    mobile_device_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        mobile_device_constant: str = ...,
    ) -> None: ...

class OperatingSystemVersionInfo(proto.Message):
    operating_system_version_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        operating_system_version_constant: str = ...,
    ) -> None: ...

class ParentalStatusInfo(proto.Message):
    type_: ParentalStatusTypeEnum.ParentalStatusType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: ParentalStatusTypeEnum.ParentalStatusType = ...,
    ) -> None: ...

class PlacementInfo(proto.Message):
    url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        url: str = ...,
    ) -> None: ...

class ProductBiddingCategoryInfo(proto.Message):
    id: int
    level: ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        id: int = ...,
        level: ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel = ...,
    ) -> None: ...

class ProductBrandInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...

class ProductChannelExclusivityInfo(proto.Message):
    channel_exclusivity: ProductChannelExclusivityEnum.ProductChannelExclusivity
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        channel_exclusivity: ProductChannelExclusivityEnum.ProductChannelExclusivity = ...,
    ) -> None: ...

class ProductChannelInfo(proto.Message):
    channel: ProductChannelEnum.ProductChannel
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        channel: ProductChannelEnum.ProductChannel = ...,
    ) -> None: ...

class ProductConditionInfo(proto.Message):
    condition: ProductConditionEnum.ProductCondition
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        condition: ProductConditionEnum.ProductCondition = ...,
    ) -> None: ...

class ProductCustomAttributeInfo(proto.Message):
    value: str
    index: ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
        index: ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex = ...,
    ) -> None: ...

class ProductGroupingInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...

class ProductItemIdInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...

class ProductLabelsInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...

class ProductLegacyConditionInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...

class ProductTypeFullInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...

class ProductTypeInfo(proto.Message):
    value: str
    level: ProductTypeLevelEnum.ProductTypeLevel
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
        level: ProductTypeLevelEnum.ProductTypeLevel = ...,
    ) -> None: ...

class ProximityInfo(proto.Message):
    geo_point: GeoPointInfo
    radius: float
    radius_units: ProximityRadiusUnitsEnum.ProximityRadiusUnits
    address: AddressInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        geo_point: GeoPointInfo = ...,
        radius: float = ...,
        radius_units: ProximityRadiusUnitsEnum.ProximityRadiusUnits = ...,
        address: AddressInfo = ...,
    ) -> None: ...

class TopicInfo(proto.Message):
    topic_constant: str
    path: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        topic_constant: str = ...,
        path: MutableSequence[str] = ...,
    ) -> None: ...

class UnknownListingDimensionInfo(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    ...

class UserInterestInfo(proto.Message):
    user_interest_category: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_interest_category: str = ...,
    ) -> None: ...

class UserListInfo(proto.Message):
    user_list: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_list: str = ...,
    ) -> None: ...

class WebpageConditionInfo(proto.Message):
    operand: WebpageConditionOperandEnum.WebpageConditionOperand
    operator: WebpageConditionOperatorEnum.WebpageConditionOperator
    argument: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        operand: WebpageConditionOperandEnum.WebpageConditionOperand = ...,
        operator: WebpageConditionOperatorEnum.WebpageConditionOperator = ...,
        argument: str = ...,
    ) -> None: ...

class WebpageInfo(proto.Message):
    criterion_name: str
    conditions: MutableSequence[WebpageConditionInfo]
    coverage_percentage: float
    sample: WebpageSampleInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        criterion_name: str = ...,
        conditions: MutableSequence[WebpageConditionInfo] = ...,
        coverage_percentage: float = ...,
        sample: WebpageSampleInfo = ...,
    ) -> None: ...

class WebpageSampleInfo(proto.Message):
    sample_urls: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        sample_urls: MutableSequence[str] = ...,
    ) -> None: ...

class YouTubeChannelInfo(proto.Message):
    channel_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        channel_id: str = ...,
    ) -> None: ...

class YouTubeVideoInfo(proto.Message):
    video_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        video_id: str = ...,
    ) -> None: ...
