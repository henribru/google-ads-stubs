# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v3.proto.common.criteria_pb2 import (
    KeywordInfo as google___ads___googleads___v3___common___criteria_pb2___KeywordInfo,
)

from google.ads.google_ads.v3.proto.enums.ad_network_type_pb2 import (
    AdNetworkTypeEnum as google___ads___googleads___v3___enums___ad_network_type_pb2___AdNetworkTypeEnum,
)

from google.ads.google_ads.v3.proto.enums.click_type_pb2 import (
    ClickTypeEnum as google___ads___googleads___v3___enums___click_type_pb2___ClickTypeEnum,
)

from google.ads.google_ads.v3.proto.enums.conversion_action_category_pb2 import (
    ConversionActionCategoryEnum as google___ads___googleads___v3___enums___conversion_action_category_pb2___ConversionActionCategoryEnum,
)

from google.ads.google_ads.v3.proto.enums.conversion_attribution_event_type_pb2 import (
    ConversionAttributionEventTypeEnum as google___ads___googleads___v3___enums___conversion_attribution_event_type_pb2___ConversionAttributionEventTypeEnum,
)

from google.ads.google_ads.v3.proto.enums.conversion_lag_bucket_pb2 import (
    ConversionLagBucketEnum as google___ads___googleads___v3___enums___conversion_lag_bucket_pb2___ConversionLagBucketEnum,
)

from google.ads.google_ads.v3.proto.enums.conversion_or_adjustment_lag_bucket_pb2 import (
    ConversionOrAdjustmentLagBucketEnum as google___ads___googleads___v3___enums___conversion_or_adjustment_lag_bucket_pb2___ConversionOrAdjustmentLagBucketEnum,
)

from google.ads.google_ads.v3.proto.enums.day_of_week_pb2 import (
    DayOfWeekEnum as google___ads___googleads___v3___enums___day_of_week_pb2___DayOfWeekEnum,
)

from google.ads.google_ads.v3.proto.enums.device_pb2 import (
    DeviceEnum as google___ads___googleads___v3___enums___device_pb2___DeviceEnum,
)

from google.ads.google_ads.v3.proto.enums.external_conversion_source_pb2 import (
    ExternalConversionSourceEnum as google___ads___googleads___v3___enums___external_conversion_source_pb2___ExternalConversionSourceEnum,
)

from google.ads.google_ads.v3.proto.enums.hotel_date_selection_type_pb2 import (
    HotelDateSelectionTypeEnum as google___ads___googleads___v3___enums___hotel_date_selection_type_pb2___HotelDateSelectionTypeEnum,
)

from google.ads.google_ads.v3.proto.enums.hotel_price_bucket_pb2 import (
    HotelPriceBucketEnum as google___ads___googleads___v3___enums___hotel_price_bucket_pb2___HotelPriceBucketEnum,
)

from google.ads.google_ads.v3.proto.enums.hotel_rate_type_pb2 import (
    HotelRateTypeEnum as google___ads___googleads___v3___enums___hotel_rate_type_pb2___HotelRateTypeEnum,
)

from google.ads.google_ads.v3.proto.enums.month_of_year_pb2 import (
    MonthOfYearEnum as google___ads___googleads___v3___enums___month_of_year_pb2___MonthOfYearEnum,
)

from google.ads.google_ads.v3.proto.enums.placeholder_type_pb2 import (
    PlaceholderTypeEnum as google___ads___googleads___v3___enums___placeholder_type_pb2___PlaceholderTypeEnum,
)

from google.ads.google_ads.v3.proto.enums.product_channel_exclusivity_pb2 import (
    ProductChannelExclusivityEnum as google___ads___googleads___v3___enums___product_channel_exclusivity_pb2___ProductChannelExclusivityEnum,
)

from google.ads.google_ads.v3.proto.enums.product_channel_pb2 import (
    ProductChannelEnum as google___ads___googleads___v3___enums___product_channel_pb2___ProductChannelEnum,
)

from google.ads.google_ads.v3.proto.enums.product_condition_pb2 import (
    ProductConditionEnum as google___ads___googleads___v3___enums___product_condition_pb2___ProductConditionEnum,
)

from google.ads.google_ads.v3.proto.enums.search_engine_results_page_type_pb2 import (
    SearchEngineResultsPageTypeEnum as google___ads___googleads___v3___enums___search_engine_results_page_type_pb2___SearchEngineResultsPageTypeEnum,
)

from google.ads.google_ads.v3.proto.enums.search_term_match_type_pb2 import (
    SearchTermMatchTypeEnum as google___ads___googleads___v3___enums___search_term_match_type_pb2___SearchTermMatchTypeEnum,
)

from google.ads.google_ads.v3.proto.enums.slot_pb2 import (
    SlotEnum as google___ads___googleads___v3___enums___slot_pb2___SlotEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    Int32Value as google___protobuf___wrappers_pb2___Int32Value,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
    UInt64Value as google___protobuf___wrappers_pb2___UInt64Value,
)

from typing import (
    Optional as typing___Optional,
    Union as typing___Union,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class Segments(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ad_network_type = (
        ...
    )  # type: google___ads___googleads___v3___enums___ad_network_type_pb2___AdNetworkTypeEnum.AdNetworkType
    click_type = (
        ...
    )  # type: google___ads___googleads___v3___enums___click_type_pb2___ClickTypeEnum.ClickType
    conversion_action_category = (
        ...
    )  # type: google___ads___googleads___v3___enums___conversion_action_category_pb2___ConversionActionCategoryEnum.ConversionActionCategory
    conversion_attribution_event_type = (
        ...
    )  # type: google___ads___googleads___v3___enums___conversion_attribution_event_type_pb2___ConversionAttributionEventTypeEnum.ConversionAttributionEventType
    conversion_lag_bucket = (
        ...
    )  # type: google___ads___googleads___v3___enums___conversion_lag_bucket_pb2___ConversionLagBucketEnum.ConversionLagBucket
    conversion_or_adjustment_lag_bucket = (
        ...
    )  # type: google___ads___googleads___v3___enums___conversion_or_adjustment_lag_bucket_pb2___ConversionOrAdjustmentLagBucketEnum.ConversionOrAdjustmentLagBucket
    day_of_week = (
        ...
    )  # type: google___ads___googleads___v3___enums___day_of_week_pb2___DayOfWeekEnum.DayOfWeek
    device = (
        ...
    )  # type: google___ads___googleads___v3___enums___device_pb2___DeviceEnum.Device
    external_conversion_source = (
        ...
    )  # type: google___ads___googleads___v3___enums___external_conversion_source_pb2___ExternalConversionSourceEnum.ExternalConversionSource
    hotel_check_in_day_of_week = (
        ...
    )  # type: google___ads___googleads___v3___enums___day_of_week_pb2___DayOfWeekEnum.DayOfWeek
    hotel_date_selection_type = (
        ...
    )  # type: google___ads___googleads___v3___enums___hotel_date_selection_type_pb2___HotelDateSelectionTypeEnum.HotelDateSelectionType
    hotel_rate_type = (
        ...
    )  # type: google___ads___googleads___v3___enums___hotel_rate_type_pb2___HotelRateTypeEnum.HotelRateType
    hotel_price_bucket = (
        ...
    )  # type: google___ads___googleads___v3___enums___hotel_price_bucket_pb2___HotelPriceBucketEnum.HotelPriceBucket
    month_of_year = (
        ...
    )  # type: google___ads___googleads___v3___enums___month_of_year_pb2___MonthOfYearEnum.MonthOfYear
    placeholder_type = (
        ...
    )  # type: google___ads___googleads___v3___enums___placeholder_type_pb2___PlaceholderTypeEnum.PlaceholderType
    product_channel = (
        ...
    )  # type: google___ads___googleads___v3___enums___product_channel_pb2___ProductChannelEnum.ProductChannel
    product_channel_exclusivity = (
        ...
    )  # type: google___ads___googleads___v3___enums___product_channel_exclusivity_pb2___ProductChannelExclusivityEnum.ProductChannelExclusivity
    product_condition = (
        ...
    )  # type: google___ads___googleads___v3___enums___product_condition_pb2___ProductConditionEnum.ProductCondition
    search_engine_results_page_type = (
        ...
    )  # type: google___ads___googleads___v3___enums___search_engine_results_page_type_pb2___SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType
    search_term_match_type = (
        ...
    )  # type: google___ads___googleads___v3___enums___search_term_match_type_pb2___SearchTermMatchTypeEnum.SearchTermMatchType
    slot = ...  # type: google___ads___googleads___v3___enums___slot_pb2___SlotEnum.Slot
    @property
    def conversion_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_action_name(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_adjustment(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def date(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_airport(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_canton(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_city(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_country(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_county(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_district(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_metro(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_most_specific_location(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_postal_code(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_province(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_region(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_state(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def hotel_booking_window_days(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def hotel_center_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def hotel_check_in_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def hotel_city(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def hotel_class(self) -> google___protobuf___wrappers_pb2___Int32Value: ...
    @property
    def hotel_country(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def hotel_length_of_stay(self) -> google___protobuf___wrappers_pb2___Int32Value: ...
    @property
    def hotel_rate_rule_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def hotel_state(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def hour(self) -> google___protobuf___wrappers_pb2___Int32Value: ...
    @property
    def interaction_on_this_extension(
        self,
    ) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def keyword(self) -> global___Keyword: ...
    @property
    def month(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def partner_hotel_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_aggregator_id(
        self,
    ) -> google___protobuf___wrappers_pb2___UInt64Value: ...
    @property
    def product_bidding_category_level1(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_bidding_category_level2(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_bidding_category_level3(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_bidding_category_level4(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_bidding_category_level5(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_brand(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_country(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_custom_attribute0(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_custom_attribute1(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_custom_attribute2(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_custom_attribute3(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_custom_attribute4(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_item_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_language(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_merchant_id(self) -> google___protobuf___wrappers_pb2___UInt64Value: ...
    @property
    def product_store_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_title(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_type_l1(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_type_l2(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_type_l3(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_type_l4(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_type_l5(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def quarter(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def webpage(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def week(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def year(self) -> google___protobuf___wrappers_pb2___Int32Value: ...
    def __init__(
        self,
        *,
        ad_network_type: typing___Optional[
            google___ads___googleads___v3___enums___ad_network_type_pb2___AdNetworkTypeEnum.AdNetworkType
        ] = None,
        click_type: typing___Optional[
            google___ads___googleads___v3___enums___click_type_pb2___ClickTypeEnum.ClickType
        ] = None,
        conversion_action: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        conversion_action_category: typing___Optional[
            google___ads___googleads___v3___enums___conversion_action_category_pb2___ConversionActionCategoryEnum.ConversionActionCategory
        ] = None,
        conversion_action_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        conversion_adjustment: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        conversion_attribution_event_type: typing___Optional[
            google___ads___googleads___v3___enums___conversion_attribution_event_type_pb2___ConversionAttributionEventTypeEnum.ConversionAttributionEventType
        ] = None,
        conversion_lag_bucket: typing___Optional[
            google___ads___googleads___v3___enums___conversion_lag_bucket_pb2___ConversionLagBucketEnum.ConversionLagBucket
        ] = None,
        conversion_or_adjustment_lag_bucket: typing___Optional[
            google___ads___googleads___v3___enums___conversion_or_adjustment_lag_bucket_pb2___ConversionOrAdjustmentLagBucketEnum.ConversionOrAdjustmentLagBucket
        ] = None,
        date: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        day_of_week: typing___Optional[
            google___ads___googleads___v3___enums___day_of_week_pb2___DayOfWeekEnum.DayOfWeek
        ] = None,
        device: typing___Optional[
            google___ads___googleads___v3___enums___device_pb2___DeviceEnum.Device
        ] = None,
        external_conversion_source: typing___Optional[
            google___ads___googleads___v3___enums___external_conversion_source_pb2___ExternalConversionSourceEnum.ExternalConversionSource
        ] = None,
        geo_target_airport: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        geo_target_canton: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        geo_target_city: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        geo_target_country: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        geo_target_county: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        geo_target_district: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        geo_target_metro: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        geo_target_most_specific_location: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        geo_target_postal_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        geo_target_province: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        geo_target_region: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        geo_target_state: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        hotel_booking_window_days: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        hotel_center_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        hotel_check_in_date: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        hotel_check_in_day_of_week: typing___Optional[
            google___ads___googleads___v3___enums___day_of_week_pb2___DayOfWeekEnum.DayOfWeek
        ] = None,
        hotel_city: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        hotel_class: typing___Optional[
            google___protobuf___wrappers_pb2___Int32Value
        ] = None,
        hotel_country: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        hotel_date_selection_type: typing___Optional[
            google___ads___googleads___v3___enums___hotel_date_selection_type_pb2___HotelDateSelectionTypeEnum.HotelDateSelectionType
        ] = None,
        hotel_length_of_stay: typing___Optional[
            google___protobuf___wrappers_pb2___Int32Value
        ] = None,
        hotel_rate_rule_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        hotel_rate_type: typing___Optional[
            google___ads___googleads___v3___enums___hotel_rate_type_pb2___HotelRateTypeEnum.HotelRateType
        ] = None,
        hotel_price_bucket: typing___Optional[
            google___ads___googleads___v3___enums___hotel_price_bucket_pb2___HotelPriceBucketEnum.HotelPriceBucket
        ] = None,
        hotel_state: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        hour: typing___Optional[google___protobuf___wrappers_pb2___Int32Value] = None,
        interaction_on_this_extension: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        keyword: typing___Optional[global___Keyword] = None,
        month: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        month_of_year: typing___Optional[
            google___ads___googleads___v3___enums___month_of_year_pb2___MonthOfYearEnum.MonthOfYear
        ] = None,
        partner_hotel_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        placeholder_type: typing___Optional[
            google___ads___googleads___v3___enums___placeholder_type_pb2___PlaceholderTypeEnum.PlaceholderType
        ] = None,
        product_aggregator_id: typing___Optional[
            google___protobuf___wrappers_pb2___UInt64Value
        ] = None,
        product_bidding_category_level1: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_bidding_category_level2: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_bidding_category_level3: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_bidding_category_level4: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_bidding_category_level5: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_brand: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_channel: typing___Optional[
            google___ads___googleads___v3___enums___product_channel_pb2___ProductChannelEnum.ProductChannel
        ] = None,
        product_channel_exclusivity: typing___Optional[
            google___ads___googleads___v3___enums___product_channel_exclusivity_pb2___ProductChannelExclusivityEnum.ProductChannelExclusivity
        ] = None,
        product_condition: typing___Optional[
            google___ads___googleads___v3___enums___product_condition_pb2___ProductConditionEnum.ProductCondition
        ] = None,
        product_country: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_custom_attribute0: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_custom_attribute1: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_custom_attribute2: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_custom_attribute3: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_custom_attribute4: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_item_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_language: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_merchant_id: typing___Optional[
            google___protobuf___wrappers_pb2___UInt64Value
        ] = None,
        product_store_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_title: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_type_l1: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_type_l2: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_type_l3: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_type_l4: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_type_l5: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        quarter: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        search_engine_results_page_type: typing___Optional[
            google___ads___googleads___v3___enums___search_engine_results_page_type_pb2___SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType
        ] = None,
        search_term_match_type: typing___Optional[
            google___ads___googleads___v3___enums___search_term_match_type_pb2___SearchTermMatchTypeEnum.SearchTermMatchType
        ] = None,
        slot: typing___Optional[
            google___ads___googleads___v3___enums___slot_pb2___SlotEnum.Slot
        ] = None,
        webpage: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        week: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        year: typing___Optional[google___protobuf___wrappers_pb2___Int32Value] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Segments: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> Segments: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "conversion_action",
            b"conversion_action",
            "conversion_action_name",
            b"conversion_action_name",
            "conversion_adjustment",
            b"conversion_adjustment",
            "date",
            b"date",
            "geo_target_airport",
            b"geo_target_airport",
            "geo_target_canton",
            b"geo_target_canton",
            "geo_target_city",
            b"geo_target_city",
            "geo_target_country",
            b"geo_target_country",
            "geo_target_county",
            b"geo_target_county",
            "geo_target_district",
            b"geo_target_district",
            "geo_target_metro",
            b"geo_target_metro",
            "geo_target_most_specific_location",
            b"geo_target_most_specific_location",
            "geo_target_postal_code",
            b"geo_target_postal_code",
            "geo_target_province",
            b"geo_target_province",
            "geo_target_region",
            b"geo_target_region",
            "geo_target_state",
            b"geo_target_state",
            "hotel_booking_window_days",
            b"hotel_booking_window_days",
            "hotel_center_id",
            b"hotel_center_id",
            "hotel_check_in_date",
            b"hotel_check_in_date",
            "hotel_city",
            b"hotel_city",
            "hotel_class",
            b"hotel_class",
            "hotel_country",
            b"hotel_country",
            "hotel_length_of_stay",
            b"hotel_length_of_stay",
            "hotel_rate_rule_id",
            b"hotel_rate_rule_id",
            "hotel_state",
            b"hotel_state",
            "hour",
            b"hour",
            "interaction_on_this_extension",
            b"interaction_on_this_extension",
            "keyword",
            b"keyword",
            "month",
            b"month",
            "partner_hotel_id",
            b"partner_hotel_id",
            "product_aggregator_id",
            b"product_aggregator_id",
            "product_bidding_category_level1",
            b"product_bidding_category_level1",
            "product_bidding_category_level2",
            b"product_bidding_category_level2",
            "product_bidding_category_level3",
            b"product_bidding_category_level3",
            "product_bidding_category_level4",
            b"product_bidding_category_level4",
            "product_bidding_category_level5",
            b"product_bidding_category_level5",
            "product_brand",
            b"product_brand",
            "product_country",
            b"product_country",
            "product_custom_attribute0",
            b"product_custom_attribute0",
            "product_custom_attribute1",
            b"product_custom_attribute1",
            "product_custom_attribute2",
            b"product_custom_attribute2",
            "product_custom_attribute3",
            b"product_custom_attribute3",
            "product_custom_attribute4",
            b"product_custom_attribute4",
            "product_item_id",
            b"product_item_id",
            "product_language",
            b"product_language",
            "product_merchant_id",
            b"product_merchant_id",
            "product_store_id",
            b"product_store_id",
            "product_title",
            b"product_title",
            "product_type_l1",
            b"product_type_l1",
            "product_type_l2",
            b"product_type_l2",
            "product_type_l3",
            b"product_type_l3",
            "product_type_l4",
            b"product_type_l4",
            "product_type_l5",
            b"product_type_l5",
            "quarter",
            b"quarter",
            "webpage",
            b"webpage",
            "week",
            b"week",
            "year",
            b"year",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ad_network_type",
            b"ad_network_type",
            "click_type",
            b"click_type",
            "conversion_action",
            b"conversion_action",
            "conversion_action_category",
            b"conversion_action_category",
            "conversion_action_name",
            b"conversion_action_name",
            "conversion_adjustment",
            b"conversion_adjustment",
            "conversion_attribution_event_type",
            b"conversion_attribution_event_type",
            "conversion_lag_bucket",
            b"conversion_lag_bucket",
            "conversion_or_adjustment_lag_bucket",
            b"conversion_or_adjustment_lag_bucket",
            "date",
            b"date",
            "day_of_week",
            b"day_of_week",
            "device",
            b"device",
            "external_conversion_source",
            b"external_conversion_source",
            "geo_target_airport",
            b"geo_target_airport",
            "geo_target_canton",
            b"geo_target_canton",
            "geo_target_city",
            b"geo_target_city",
            "geo_target_country",
            b"geo_target_country",
            "geo_target_county",
            b"geo_target_county",
            "geo_target_district",
            b"geo_target_district",
            "geo_target_metro",
            b"geo_target_metro",
            "geo_target_most_specific_location",
            b"geo_target_most_specific_location",
            "geo_target_postal_code",
            b"geo_target_postal_code",
            "geo_target_province",
            b"geo_target_province",
            "geo_target_region",
            b"geo_target_region",
            "geo_target_state",
            b"geo_target_state",
            "hotel_booking_window_days",
            b"hotel_booking_window_days",
            "hotel_center_id",
            b"hotel_center_id",
            "hotel_check_in_date",
            b"hotel_check_in_date",
            "hotel_check_in_day_of_week",
            b"hotel_check_in_day_of_week",
            "hotel_city",
            b"hotel_city",
            "hotel_class",
            b"hotel_class",
            "hotel_country",
            b"hotel_country",
            "hotel_date_selection_type",
            b"hotel_date_selection_type",
            "hotel_length_of_stay",
            b"hotel_length_of_stay",
            "hotel_price_bucket",
            b"hotel_price_bucket",
            "hotel_rate_rule_id",
            b"hotel_rate_rule_id",
            "hotel_rate_type",
            b"hotel_rate_type",
            "hotel_state",
            b"hotel_state",
            "hour",
            b"hour",
            "interaction_on_this_extension",
            b"interaction_on_this_extension",
            "keyword",
            b"keyword",
            "month",
            b"month",
            "month_of_year",
            b"month_of_year",
            "partner_hotel_id",
            b"partner_hotel_id",
            "placeholder_type",
            b"placeholder_type",
            "product_aggregator_id",
            b"product_aggregator_id",
            "product_bidding_category_level1",
            b"product_bidding_category_level1",
            "product_bidding_category_level2",
            b"product_bidding_category_level2",
            "product_bidding_category_level3",
            b"product_bidding_category_level3",
            "product_bidding_category_level4",
            b"product_bidding_category_level4",
            "product_bidding_category_level5",
            b"product_bidding_category_level5",
            "product_brand",
            b"product_brand",
            "product_channel",
            b"product_channel",
            "product_channel_exclusivity",
            b"product_channel_exclusivity",
            "product_condition",
            b"product_condition",
            "product_country",
            b"product_country",
            "product_custom_attribute0",
            b"product_custom_attribute0",
            "product_custom_attribute1",
            b"product_custom_attribute1",
            "product_custom_attribute2",
            b"product_custom_attribute2",
            "product_custom_attribute3",
            b"product_custom_attribute3",
            "product_custom_attribute4",
            b"product_custom_attribute4",
            "product_item_id",
            b"product_item_id",
            "product_language",
            b"product_language",
            "product_merchant_id",
            b"product_merchant_id",
            "product_store_id",
            b"product_store_id",
            "product_title",
            b"product_title",
            "product_type_l1",
            b"product_type_l1",
            "product_type_l2",
            b"product_type_l2",
            "product_type_l3",
            b"product_type_l3",
            "product_type_l4",
            b"product_type_l4",
            "product_type_l5",
            b"product_type_l5",
            "quarter",
            b"quarter",
            "search_engine_results_page_type",
            b"search_engine_results_page_type",
            "search_term_match_type",
            b"search_term_match_type",
            "slot",
            b"slot",
            "webpage",
            b"webpage",
            "week",
            b"week",
            "year",
            b"year",
        ],
    ) -> None: ...

global___Segments = Segments

class Keyword(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def ad_group_criterion(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def info(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___KeywordInfo: ...
    def __init__(
        self,
        *,
        ad_group_criterion: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        info: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___KeywordInfo
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Keyword: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> Keyword: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group_criterion", b"ad_group_criterion", "info", b"info"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group_criterion", b"ad_group_criterion", "info", b"info"
        ],
    ) -> None: ...

global___Keyword = Keyword
