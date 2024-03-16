from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.criteria import KeywordInfo
from google.ads.googleads.v14.enums.types.ad_destination_type import (
    AdDestinationTypeEnum,
)
from google.ads.googleads.v14.enums.types.ad_network_type import AdNetworkTypeEnum
from google.ads.googleads.v14.enums.types.budget_campaign_association_status import (
    BudgetCampaignAssociationStatusEnum,
)
from google.ads.googleads.v14.enums.types.click_type import ClickTypeEnum
from google.ads.googleads.v14.enums.types.conversion_action_category import (
    ConversionActionCategoryEnum,
)
from google.ads.googleads.v14.enums.types.conversion_attribution_event_type import (
    ConversionAttributionEventTypeEnum,
)
from google.ads.googleads.v14.enums.types.conversion_lag_bucket import (
    ConversionLagBucketEnum,
)
from google.ads.googleads.v14.enums.types.conversion_or_adjustment_lag_bucket import (
    ConversionOrAdjustmentLagBucketEnum,
)
from google.ads.googleads.v14.enums.types.conversion_value_rule_primary_dimension import (
    ConversionValueRulePrimaryDimensionEnum,
)
from google.ads.googleads.v14.enums.types.converting_user_prior_engagement_type_and_ltv_bucket import (
    ConvertingUserPriorEngagementTypeAndLtvBucketEnum,
)
from google.ads.googleads.v14.enums.types.day_of_week import DayOfWeekEnum
from google.ads.googleads.v14.enums.types.device import DeviceEnum
from google.ads.googleads.v14.enums.types.external_conversion_source import (
    ExternalConversionSourceEnum,
)
from google.ads.googleads.v14.enums.types.hotel_date_selection_type import (
    HotelDateSelectionTypeEnum,
)
from google.ads.googleads.v14.enums.types.hotel_price_bucket import HotelPriceBucketEnum
from google.ads.googleads.v14.enums.types.hotel_rate_type import HotelRateTypeEnum
from google.ads.googleads.v14.enums.types.month_of_year import MonthOfYearEnum
from google.ads.googleads.v14.enums.types.placeholder_type import PlaceholderTypeEnum
from google.ads.googleads.v14.enums.types.product_channel import ProductChannelEnum
from google.ads.googleads.v14.enums.types.product_channel_exclusivity import (
    ProductChannelExclusivityEnum,
)
from google.ads.googleads.v14.enums.types.product_condition import ProductConditionEnum
from google.ads.googleads.v14.enums.types.recommendation_type import (
    RecommendationTypeEnum,
)
from google.ads.googleads.v14.enums.types.search_engine_results_page_type import (
    SearchEngineResultsPageTypeEnum,
)
from google.ads.googleads.v14.enums.types.search_term_match_type import (
    SearchTermMatchTypeEnum,
)
from google.ads.googleads.v14.enums.types.sk_ad_network_ad_event_type import (
    SkAdNetworkAdEventTypeEnum,
)
from google.ads.googleads.v14.enums.types.sk_ad_network_attribution_credit import (
    SkAdNetworkAttributionCreditEnum,
)
from google.ads.googleads.v14.enums.types.sk_ad_network_user_type import (
    SkAdNetworkUserTypeEnum,
)
from google.ads.googleads.v14.enums.types.slot import SlotEnum

_M = TypeVar("_M")

class AssetInteractionTarget(proto.Message):
    asset: str
    interaction_on_this_asset: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset: str = ...,
        interaction_on_this_asset: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["asset", "interaction_on_this_asset"]
    ) -> bool: ...

class BudgetCampaignAssociationStatus(proto.Message):
    campaign: str
    status: BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        campaign: str = ...,
        status: BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["campaign", "status"]
    ) -> bool: ...

class Keyword(proto.Message):
    ad_group_criterion: str
    info: KeywordInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ad_group_criterion: str = ...,
        info: KeywordInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["ad_group_criterion", "info"]
    ) -> bool: ...

class Segments(proto.Message):
    activity_account_id: int
    activity_rating: int
    external_activity_id: str
    ad_destination_type: AdDestinationTypeEnum.AdDestinationType
    ad_network_type: AdNetworkTypeEnum.AdNetworkType
    ad_group: str
    asset_group: str
    auction_insight_domain: str
    budget_campaign_association_status: BudgetCampaignAssociationStatus
    campaign: str
    click_type: ClickTypeEnum.ClickType
    conversion_action: str
    conversion_action_category: ConversionActionCategoryEnum.ConversionActionCategory
    conversion_action_name: str
    conversion_adjustment: bool
    conversion_attribution_event_type: (
        ConversionAttributionEventTypeEnum.ConversionAttributionEventType
    )
    conversion_lag_bucket: ConversionLagBucketEnum.ConversionLagBucket
    conversion_or_adjustment_lag_bucket: (
        ConversionOrAdjustmentLagBucketEnum.ConversionOrAdjustmentLagBucket
    )
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
    product_feed_label: str
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
    search_engine_results_page_type: (
        SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType
    )
    search_subcategory: str
    search_term: str
    search_term_match_type: SearchTermMatchTypeEnum.SearchTermMatchType
    slot: SlotEnum.Slot
    conversion_value_rule_primary_dimension: (
        ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    )
    webpage: str
    week: str
    year: int
    sk_ad_network_conversion_value: int
    sk_ad_network_user_type: SkAdNetworkUserTypeEnum.SkAdNetworkUserType
    sk_ad_network_ad_event_type: SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType
    sk_ad_network_source_app: SkAdNetworkSourceApp
    sk_ad_network_attribution_credit: (
        SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit
    )
    asset_interaction_target: AssetInteractionTarget
    new_versus_returning_customers: ConvertingUserPriorEngagementTypeAndLtvBucketEnum.ConvertingUserPriorEngagementTypeAndLtvBucket
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        activity_account_id: int = ...,
        activity_rating: int = ...,
        external_activity_id: str = ...,
        ad_destination_type: AdDestinationTypeEnum.AdDestinationType = ...,
        ad_network_type: AdNetworkTypeEnum.AdNetworkType = ...,
        ad_group: str = ...,
        asset_group: str = ...,
        auction_insight_domain: str = ...,
        budget_campaign_association_status: BudgetCampaignAssociationStatus = ...,
        campaign: str = ...,
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
        product_feed_label: str = ...,
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
        search_subcategory: str = ...,
        search_term: str = ...,
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
        asset_interaction_target: AssetInteractionTarget = ...,
        new_versus_returning_customers: ConvertingUserPriorEngagementTypeAndLtvBucketEnum.ConvertingUserPriorEngagementTypeAndLtvBucket = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "activity_account_id",
            "activity_rating",
            "external_activity_id",
            "ad_destination_type",
            "ad_network_type",
            "ad_group",
            "asset_group",
            "auction_insight_domain",
            "budget_campaign_association_status",
            "campaign",
            "click_type",
            "conversion_action",
            "conversion_action_category",
            "conversion_action_name",
            "conversion_adjustment",
            "conversion_attribution_event_type",
            "conversion_lag_bucket",
            "conversion_or_adjustment_lag_bucket",
            "date",
            "day_of_week",
            "device",
            "external_conversion_source",
            "geo_target_airport",
            "geo_target_canton",
            "geo_target_city",
            "geo_target_country",
            "geo_target_county",
            "geo_target_district",
            "geo_target_metro",
            "geo_target_most_specific_location",
            "geo_target_postal_code",
            "geo_target_province",
            "geo_target_region",
            "geo_target_state",
            "hotel_booking_window_days",
            "hotel_center_id",
            "hotel_check_in_date",
            "hotel_check_in_day_of_week",
            "hotel_city",
            "hotel_class",
            "hotel_country",
            "hotel_date_selection_type",
            "hotel_length_of_stay",
            "hotel_rate_rule_id",
            "hotel_rate_type",
            "hotel_price_bucket",
            "hotel_state",
            "hour",
            "interaction_on_this_extension",
            "keyword",
            "month",
            "month_of_year",
            "partner_hotel_id",
            "placeholder_type",
            "product_aggregator_id",
            "product_bidding_category_level1",
            "product_bidding_category_level2",
            "product_bidding_category_level3",
            "product_bidding_category_level4",
            "product_bidding_category_level5",
            "product_brand",
            "product_channel",
            "product_channel_exclusivity",
            "product_condition",
            "product_country",
            "product_custom_attribute0",
            "product_custom_attribute1",
            "product_custom_attribute2",
            "product_custom_attribute3",
            "product_custom_attribute4",
            "product_feed_label",
            "product_item_id",
            "product_language",
            "product_merchant_id",
            "product_store_id",
            "product_title",
            "product_type_l1",
            "product_type_l2",
            "product_type_l3",
            "product_type_l4",
            "product_type_l5",
            "quarter",
            "recommendation_type",
            "search_engine_results_page_type",
            "search_subcategory",
            "search_term",
            "search_term_match_type",
            "slot",
            "conversion_value_rule_primary_dimension",
            "webpage",
            "week",
            "year",
            "sk_ad_network_conversion_value",
            "sk_ad_network_user_type",
            "sk_ad_network_ad_event_type",
            "sk_ad_network_source_app",
            "sk_ad_network_attribution_credit",
            "asset_interaction_target",
            "new_versus_returning_customers",
        ],
    ) -> bool: ...

class SkAdNetworkSourceApp(proto.Message):
    sk_ad_network_source_app_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        sk_ad_network_source_app_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["sk_ad_network_source_app_id"]
    ) -> bool: ...
