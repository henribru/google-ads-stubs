from typing import Any

import proto

from google.ads.googleads.v10.common.types.criteria import KeywordInfo
from google.ads.googleads.v10.enums.types.ad_destination_type import (
    AdDestinationTypeEnum,
)
from google.ads.googleads.v10.enums.types.ad_network_type import AdNetworkTypeEnum
from google.ads.googleads.v10.enums.types.budget_campaign_association_status import (
    BudgetCampaignAssociationStatusEnum,
)
from google.ads.googleads.v10.enums.types.click_type import ClickTypeEnum
from google.ads.googleads.v10.enums.types.conversion_action_category import (
    ConversionActionCategoryEnum,
)
from google.ads.googleads.v10.enums.types.conversion_attribution_event_type import (
    ConversionAttributionEventTypeEnum,
)
from google.ads.googleads.v10.enums.types.conversion_lag_bucket import (
    ConversionLagBucketEnum,
)
from google.ads.googleads.v10.enums.types.conversion_or_adjustment_lag_bucket import (
    ConversionOrAdjustmentLagBucketEnum,
)
from google.ads.googleads.v10.enums.types.conversion_value_rule_primary_dimension import (
    ConversionValueRulePrimaryDimensionEnum,
)
from google.ads.googleads.v10.enums.types.day_of_week import DayOfWeekEnum
from google.ads.googleads.v10.enums.types.device import DeviceEnum
from google.ads.googleads.v10.enums.types.external_conversion_source import (
    ExternalConversionSourceEnum,
)
from google.ads.googleads.v10.enums.types.hotel_date_selection_type import (
    HotelDateSelectionTypeEnum,
)
from google.ads.googleads.v10.enums.types.hotel_price_bucket import HotelPriceBucketEnum
from google.ads.googleads.v10.enums.types.hotel_rate_type import HotelRateTypeEnum
from google.ads.googleads.v10.enums.types.month_of_year import MonthOfYearEnum
from google.ads.googleads.v10.enums.types.placeholder_type import PlaceholderTypeEnum
from google.ads.googleads.v10.enums.types.product_channel import ProductChannelEnum
from google.ads.googleads.v10.enums.types.product_channel_exclusivity import (
    ProductChannelExclusivityEnum,
)
from google.ads.googleads.v10.enums.types.product_condition import ProductConditionEnum
from google.ads.googleads.v10.enums.types.recommendation_type import (
    RecommendationTypeEnum,
)
from google.ads.googleads.v10.enums.types.search_engine_results_page_type import (
    SearchEngineResultsPageTypeEnum,
)
from google.ads.googleads.v10.enums.types.search_term_match_type import (
    SearchTermMatchTypeEnum,
)
from google.ads.googleads.v10.enums.types.sk_ad_network_ad_event_type import (
    SkAdNetworkAdEventTypeEnum,
)
from google.ads.googleads.v10.enums.types.sk_ad_network_attribution_credit import (
    SkAdNetworkAttributionCreditEnum,
)
from google.ads.googleads.v10.enums.types.sk_ad_network_user_type import (
    SkAdNetworkUserTypeEnum,
)
from google.ads.googleads.v10.enums.types.slot import SlotEnum

class AssetInteractionTarget(proto.Message):
    asset: str
    interaction_on_this_asset: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        asset: str = ...,
        interaction_on_this_asset: bool = ...
    ) -> None: ...

class BudgetCampaignAssociationStatus(proto.Message):
    campaign: str
    status: BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        campaign: str = ...,
        status: BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus = ...
    ) -> None: ...

class Keyword(proto.Message):
    ad_group_criterion: str
    info: KeywordInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        ad_group_criterion: str = ...,
        info: KeywordInfo = ...
    ) -> None: ...

class Segments(proto.Message):
    ad_destination_type: AdDestinationTypeEnum.AdDestinationType
    ad_network_type: AdNetworkTypeEnum.AdNetworkType
    budget_campaign_association_status: BudgetCampaignAssociationStatus
    click_type: ClickTypeEnum.ClickType
    conversion_action: str
    conversion_action_category: ConversionActionCategoryEnum.ConversionActionCategory
    conversion_action_name: str
    conversion_adjustment: bool
    conversion_attribution_event_type: ConversionAttributionEventTypeEnum.ConversionAttributionEventType
    conversion_lag_bucket: ConversionLagBucketEnum.ConversionLagBucket
    conversion_or_adjustment_lag_bucket: ConversionOrAdjustmentLagBucketEnum.ConversionOrAdjustmentLagBucket
    date: str
    day_of_week: DayOfWeekEnum.DayOfWeek
    device: DeviceEnum.Device
    external_conversion_source: ExternalConversionSourceEnum.ExternalConversionSource
    geo_target_airport: str
    geo_target_canton: str
    geo_target_city: str
    geo_target_country: str
    geo_target_county: str
    geo_target_district: str
    geo_target_metro: str
    geo_target_most_specific_location: str
    geo_target_postal_code: str
    geo_target_province: str
    geo_target_region: str
    geo_target_state: str
    hotel_booking_window_days: int
    hotel_center_id: int
    hotel_check_in_date: str
    hotel_check_in_day_of_week: DayOfWeekEnum.DayOfWeek
    hotel_city: str
    hotel_class: int
    hotel_country: str
    hotel_date_selection_type: HotelDateSelectionTypeEnum.HotelDateSelectionType
    hotel_length_of_stay: int
    hotel_rate_rule_id: str
    hotel_rate_type: HotelRateTypeEnum.HotelRateType
    hotel_price_bucket: HotelPriceBucketEnum.HotelPriceBucket
    hotel_state: str
    hour: int
    interaction_on_this_extension: bool
    keyword: Keyword
    month: str
    month_of_year: MonthOfYearEnum.MonthOfYear
    partner_hotel_id: str
    placeholder_type: PlaceholderTypeEnum.PlaceholderType
    product_aggregator_id: int
    product_bidding_category_level1: str
    product_bidding_category_level2: str
    product_bidding_category_level3: str
    product_bidding_category_level4: str
    product_bidding_category_level5: str
    product_brand: str
    product_channel: ProductChannelEnum.ProductChannel
    product_channel_exclusivity: ProductChannelExclusivityEnum.ProductChannelExclusivity
    product_condition: ProductConditionEnum.ProductCondition
    product_country: str
    product_custom_attribute0: str
    product_custom_attribute1: str
    product_custom_attribute2: str
    product_custom_attribute3: str
    product_custom_attribute4: str
    product_item_id: str
    product_language: str
    product_merchant_id: int
    product_store_id: str
    product_title: str
    product_type_l1: str
    product_type_l2: str
    product_type_l3: str
    product_type_l4: str
    product_type_l5: str
    quarter: str
    recommendation_type: RecommendationTypeEnum.RecommendationType
    search_engine_results_page_type: SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType
    search_term_match_type: SearchTermMatchTypeEnum.SearchTermMatchType
    slot: SlotEnum.Slot
    conversion_value_rule_primary_dimension: ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    webpage: str
    week: str
    year: int
    sk_ad_network_conversion_value: int
    sk_ad_network_user_type: SkAdNetworkUserTypeEnum.SkAdNetworkUserType
    sk_ad_network_ad_event_type: SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType
    sk_ad_network_source_app: SkAdNetworkSourceApp
    sk_ad_network_attribution_credit: SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit
    asset_interaction_target: AssetInteractionTarget
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        ad_destination_type: AdDestinationTypeEnum.AdDestinationType = ...,
        ad_network_type: AdNetworkTypeEnum.AdNetworkType = ...,
        budget_campaign_association_status: BudgetCampaignAssociationStatus = ...,
        click_type: ClickTypeEnum.ClickType = ...,
        conversion_action: str = ...,
        conversion_action_category: ConversionActionCategoryEnum.ConversionActionCategory = ...,
        conversion_action_name: str = ...,
        conversion_adjustment: bool = ...,
        conversion_attribution_event_type: ConversionAttributionEventTypeEnum.ConversionAttributionEventType = ...,
        conversion_lag_bucket: ConversionLagBucketEnum.ConversionLagBucket = ...,
        conversion_or_adjustment_lag_bucket: ConversionOrAdjustmentLagBucketEnum.ConversionOrAdjustmentLagBucket = ...,
        date: str = ...,
        day_of_week: DayOfWeekEnum.DayOfWeek = ...,
        device: DeviceEnum.Device = ...,
        external_conversion_source: ExternalConversionSourceEnum.ExternalConversionSource = ...,
        geo_target_airport: str = ...,
        geo_target_canton: str = ...,
        geo_target_city: str = ...,
        geo_target_country: str = ...,
        geo_target_county: str = ...,
        geo_target_district: str = ...,
        geo_target_metro: str = ...,
        geo_target_most_specific_location: str = ...,
        geo_target_postal_code: str = ...,
        geo_target_province: str = ...,
        geo_target_region: str = ...,
        geo_target_state: str = ...,
        hotel_booking_window_days: int = ...,
        hotel_center_id: int = ...,
        hotel_check_in_date: str = ...,
        hotel_check_in_day_of_week: DayOfWeekEnum.DayOfWeek = ...,
        hotel_city: str = ...,
        hotel_class: int = ...,
        hotel_country: str = ...,
        hotel_date_selection_type: HotelDateSelectionTypeEnum.HotelDateSelectionType = ...,
        hotel_length_of_stay: int = ...,
        hotel_rate_rule_id: str = ...,
        hotel_rate_type: HotelRateTypeEnum.HotelRateType = ...,
        hotel_price_bucket: HotelPriceBucketEnum.HotelPriceBucket = ...,
        hotel_state: str = ...,
        hour: int = ...,
        interaction_on_this_extension: bool = ...,
        keyword: Keyword = ...,
        month: str = ...,
        month_of_year: MonthOfYearEnum.MonthOfYear = ...,
        partner_hotel_id: str = ...,
        placeholder_type: PlaceholderTypeEnum.PlaceholderType = ...,
        product_aggregator_id: int = ...,
        product_bidding_category_level1: str = ...,
        product_bidding_category_level2: str = ...,
        product_bidding_category_level3: str = ...,
        product_bidding_category_level4: str = ...,
        product_bidding_category_level5: str = ...,
        product_brand: str = ...,
        product_channel: ProductChannelEnum.ProductChannel = ...,
        product_channel_exclusivity: ProductChannelExclusivityEnum.ProductChannelExclusivity = ...,
        product_condition: ProductConditionEnum.ProductCondition = ...,
        product_country: str = ...,
        product_custom_attribute0: str = ...,
        product_custom_attribute1: str = ...,
        product_custom_attribute2: str = ...,
        product_custom_attribute3: str = ...,
        product_custom_attribute4: str = ...,
        product_item_id: str = ...,
        product_language: str = ...,
        product_merchant_id: int = ...,
        product_store_id: str = ...,
        product_title: str = ...,
        product_type_l1: str = ...,
        product_type_l2: str = ...,
        product_type_l3: str = ...,
        product_type_l4: str = ...,
        product_type_l5: str = ...,
        quarter: str = ...,
        recommendation_type: RecommendationTypeEnum.RecommendationType = ...,
        search_engine_results_page_type: SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType = ...,
        search_term_match_type: SearchTermMatchTypeEnum.SearchTermMatchType = ...,
        slot: SlotEnum.Slot = ...,
        conversion_value_rule_primary_dimension: ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension = ...,
        webpage: str = ...,
        week: str = ...,
        year: int = ...,
        sk_ad_network_conversion_value: int = ...,
        sk_ad_network_user_type: SkAdNetworkUserTypeEnum.SkAdNetworkUserType = ...,
        sk_ad_network_ad_event_type: SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType = ...,
        sk_ad_network_source_app: SkAdNetworkSourceApp = ...,
        sk_ad_network_attribution_credit: SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit = ...,
        asset_interaction_target: AssetInteractionTarget = ...
    ) -> None: ...

class SkAdNetworkSourceApp(proto.Message):
    sk_ad_network_source_app_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        sk_ad_network_source_app_id: str = ...
    ) -> None: ...
