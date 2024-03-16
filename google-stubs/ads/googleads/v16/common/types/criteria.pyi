from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.age_range_type import AgeRangeTypeEnum
from google.ads.googleads.v16.enums.types.app_payment_model_type import (
    AppPaymentModelTypeEnum,
)
from google.ads.googleads.v16.enums.types.content_label_type import ContentLabelTypeEnum
from google.ads.googleads.v16.enums.types.day_of_week import DayOfWeekEnum
from google.ads.googleads.v16.enums.types.device import DeviceEnum
from google.ads.googleads.v16.enums.types.gender_type import GenderTypeEnum
from google.ads.googleads.v16.enums.types.hotel_date_selection_type import (
    HotelDateSelectionTypeEnum,
)
from google.ads.googleads.v16.enums.types.income_range_type import IncomeRangeTypeEnum
from google.ads.googleads.v16.enums.types.interaction_type import InteractionTypeEnum
from google.ads.googleads.v16.enums.types.keyword_match_type import KeywordMatchTypeEnum
from google.ads.googleads.v16.enums.types.listing_group_type import ListingGroupTypeEnum
from google.ads.googleads.v16.enums.types.location_group_radius_units import (
    LocationGroupRadiusUnitsEnum,
)
from google.ads.googleads.v16.enums.types.minute_of_hour import MinuteOfHourEnum
from google.ads.googleads.v16.enums.types.parental_status_type import (
    ParentalStatusTypeEnum,
)
from google.ads.googleads.v16.enums.types.product_category_level import (
    ProductCategoryLevelEnum,
)
from google.ads.googleads.v16.enums.types.product_channel import ProductChannelEnum
from google.ads.googleads.v16.enums.types.product_channel_exclusivity import (
    ProductChannelExclusivityEnum,
)
from google.ads.googleads.v16.enums.types.product_condition import ProductConditionEnum
from google.ads.googleads.v16.enums.types.product_custom_attribute_index import (
    ProductCustomAttributeIndexEnum,
)
from google.ads.googleads.v16.enums.types.product_type_level import ProductTypeLevelEnum
from google.ads.googleads.v16.enums.types.proximity_radius_units import (
    ProximityRadiusUnitsEnum,
)
from google.ads.googleads.v16.enums.types.webpage_condition_operand import (
    WebpageConditionOperandEnum,
)
from google.ads.googleads.v16.enums.types.webpage_condition_operator import (
    WebpageConditionOperatorEnum,
)

_M = TypeVar("_M")

class ActivityCityInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

class ActivityCountryInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

class ActivityIdInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

class ActivityRatingInfo(proto.Message):
    value: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

class ActivityStateInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "start_minute", "end_minute", "start_hour", "end_hour", "day_of_week"
        ],
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "postal_code",
            "province_code",
            "country_code",
            "province_name",
            "street_address",
            "street_address2",
            "city_name",
        ],
    ) -> bool: ...

class AgeRangeInfo(proto.Message):
    type_: AgeRangeTypeEnum.AgeRangeType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: AgeRangeTypeEnum.AgeRangeType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["type_"]
    ) -> bool: ...

class AppPaymentModelInfo(proto.Message):
    type_: AppPaymentModelTypeEnum.AppPaymentModelType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: AppPaymentModelTypeEnum.AppPaymentModelType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["type_"]
    ) -> bool: ...

class AudienceInfo(proto.Message):
    audience: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        audience: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["audience"]
    ) -> bool: ...

class BrandInfo(proto.Message):
    entity_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        entity_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["entity_id"]
    ) -> bool: ...

class BrandListInfo(proto.Message):
    shared_set: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        shared_set: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["shared_set"]
    ) -> bool: ...

class CarrierInfo(proto.Message):
    carrier_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        carrier_constant: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["carrier_constant"]
    ) -> bool: ...

class CombinedAudienceInfo(proto.Message):
    combined_audience: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        combined_audience: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["combined_audience"]
    ) -> bool: ...

class ContentLabelInfo(proto.Message):
    type_: ContentLabelTypeEnum.ContentLabelType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: ContentLabelTypeEnum.ContentLabelType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["type_"]
    ) -> bool: ...

class CustomAffinityInfo(proto.Message):
    custom_affinity: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        custom_affinity: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["custom_affinity"]
    ) -> bool: ...

class CustomAudienceInfo(proto.Message):
    custom_audience: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        custom_audience: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["custom_audience"]
    ) -> bool: ...

class CustomIntentInfo(proto.Message):
    custom_intent: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        custom_intent: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["custom_intent"]
    ) -> bool: ...

class DeviceInfo(proto.Message):
    type_: DeviceEnum.Device
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: DeviceEnum.Device = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["type_"]
    ) -> bool: ...

class GenderInfo(proto.Message):
    type_: GenderTypeEnum.GenderType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: GenderTypeEnum.GenderType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["type_"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["longitude_in_micro_degrees", "latitude_in_micro_degrees"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["min_days", "max_days"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["start_date", "end_date"]
    ) -> bool: ...

class HotelCheckInDayInfo(proto.Message):
    day_of_week: DayOfWeekEnum.DayOfWeek
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        day_of_week: DayOfWeekEnum.DayOfWeek = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["day_of_week"]
    ) -> bool: ...

class HotelCityInfo(proto.Message):
    city_criterion: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        city_criterion: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["city_criterion"]
    ) -> bool: ...

class HotelClassInfo(proto.Message):
    value: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

class HotelCountryRegionInfo(proto.Message):
    country_region_criterion: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        country_region_criterion: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["country_region_criterion"]
    ) -> bool: ...

class HotelDateSelectionTypeInfo(proto.Message):
    type_: HotelDateSelectionTypeEnum.HotelDateSelectionType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: HotelDateSelectionTypeEnum.HotelDateSelectionType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["type_"]
    ) -> bool: ...

class HotelIdInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["min_nights", "max_nights"]
    ) -> bool: ...

class HotelStateInfo(proto.Message):
    state_criterion: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        state_criterion: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["state_criterion"]
    ) -> bool: ...

class IncomeRangeInfo(proto.Message):
    type_: IncomeRangeTypeEnum.IncomeRangeType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: IncomeRangeTypeEnum.IncomeRangeType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["type_"]
    ) -> bool: ...

class InteractionTypeInfo(proto.Message):
    type_: InteractionTypeEnum.InteractionType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: InteractionTypeEnum.InteractionType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["type_"]
    ) -> bool: ...

class IpBlockInfo(proto.Message):
    ip_address: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ip_address: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["ip_address"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["text", "match_type"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["keyword_theme_constant", "free_form_keyword_theme"]
    ) -> bool: ...

class LanguageInfo(proto.Message):
    language_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        language_constant: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["language_constant"]
    ) -> bool: ...

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
        product_category: ProductCategoryInfo = ...,
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
        activity_state: ActivityStateInfo = ...,
        activity_city: ActivityCityInfo = ...,
        unknown_listing_dimension: UnknownListingDimensionInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "hotel_id",
            "hotel_class",
            "hotel_country_region",
            "hotel_state",
            "hotel_city",
            "product_category",
            "product_brand",
            "product_channel",
            "product_channel_exclusivity",
            "product_condition",
            "product_custom_attribute",
            "product_item_id",
            "product_type",
            "product_grouping",
            "product_labels",
            "product_legacy_condition",
            "product_type_full",
            "activity_id",
            "activity_rating",
            "activity_country",
            "activity_state",
            "activity_city",
            "unknown_listing_dimension",
        ],
    ) -> bool: ...

class ListingDimensionPath(proto.Message):
    dimensions: MutableSequence[ListingDimensionInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dimensions: MutableSequence[ListingDimensionInfo] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["dimensions"]
    ) -> bool: ...

class ListingGroupInfo(proto.Message):
    type_: ListingGroupTypeEnum.ListingGroupType
    case_value: ListingDimensionInfo
    parent_ad_group_criterion: str
    path: ListingDimensionPath
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: ListingGroupTypeEnum.ListingGroupType = ...,
        case_value: ListingDimensionInfo = ...,
        parent_ad_group_criterion: str = ...,
        path: ListingDimensionPath = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["type_", "case_value", "parent_ad_group_criterion", "path"]
    ) -> bool: ...

class ListingScopeInfo(proto.Message):
    dimensions: MutableSequence[ListingDimensionInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dimensions: MutableSequence[ListingDimensionInfo] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["dimensions"]
    ) -> bool: ...

class LocalServiceIdInfo(proto.Message):
    service_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        service_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["service_id"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "feed",
            "geo_target_constants",
            "radius",
            "radius_units",
            "feed_item_sets",
            "enable_customer_level_location_asset_set",
            "location_group_asset_sets",
        ],
    ) -> bool: ...

class LocationInfo(proto.Message):
    geo_target_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        geo_target_constant: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["geo_target_constant"]
    ) -> bool: ...

class MobileAppCategoryInfo(proto.Message):
    mobile_app_category_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        mobile_app_category_constant: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["mobile_app_category_constant"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["app_id", "name"]
    ) -> bool: ...

class MobileDeviceInfo(proto.Message):
    mobile_device_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        mobile_device_constant: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["mobile_device_constant"]
    ) -> bool: ...

class NegativeKeywordListInfo(proto.Message):
    shared_set: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        shared_set: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["shared_set"]
    ) -> bool: ...

class OperatingSystemVersionInfo(proto.Message):
    operating_system_version_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        operating_system_version_constant: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["operating_system_version_constant"]
    ) -> bool: ...

class ParentalStatusInfo(proto.Message):
    type_: ParentalStatusTypeEnum.ParentalStatusType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: ParentalStatusTypeEnum.ParentalStatusType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["type_"]
    ) -> bool: ...

class PlacementInfo(proto.Message):
    url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        url: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["url"]
    ) -> bool: ...

class ProductBrandInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

class ProductCategoryInfo(proto.Message):
    category_id: int
    level: ProductCategoryLevelEnum.ProductCategoryLevel
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        category_id: int = ...,
        level: ProductCategoryLevelEnum.ProductCategoryLevel = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["category_id", "level"]
    ) -> bool: ...

class ProductChannelExclusivityInfo(proto.Message):
    channel_exclusivity: ProductChannelExclusivityEnum.ProductChannelExclusivity
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        channel_exclusivity: ProductChannelExclusivityEnum.ProductChannelExclusivity = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["channel_exclusivity"]
    ) -> bool: ...

class ProductChannelInfo(proto.Message):
    channel: ProductChannelEnum.ProductChannel
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        channel: ProductChannelEnum.ProductChannel = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["channel"]
    ) -> bool: ...

class ProductConditionInfo(proto.Message):
    condition: ProductConditionEnum.ProductCondition
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        condition: ProductConditionEnum.ProductCondition = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["condition"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["value", "index"]
    ) -> bool: ...

class ProductGroupingInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

class ProductItemIdInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

class ProductLabelsInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

class ProductLegacyConditionInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

class ProductTypeFullInfo(proto.Message):
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["value"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["value", "level"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["geo_point", "radius", "radius_units", "address"]
    ) -> bool: ...

class SearchThemeInfo(proto.Message):
    text: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        text: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["text"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["topic_constant", "path"]
    ) -> bool: ...

class UnknownListingDimensionInfo(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

class UserInterestInfo(proto.Message):
    user_interest_category: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_interest_category: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["user_interest_category"]
    ) -> bool: ...

class UserListInfo(proto.Message):
    user_list: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_list: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["user_list"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["operand", "operator", "argument"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["criterion_name", "conditions", "coverage_percentage", "sample"],
    ) -> bool: ...

class WebpageSampleInfo(proto.Message):
    sample_urls: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        sample_urls: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["sample_urls"]
    ) -> bool: ...

class YouTubeChannelInfo(proto.Message):
    channel_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        channel_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["channel_id"]
    ) -> bool: ...

class YouTubeVideoInfo(proto.Message):
    video_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        video_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["video_id"]
    ) -> bool: ...
