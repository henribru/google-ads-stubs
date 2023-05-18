from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v13.common.types.bidding import (
    Commission,
    ManualCpa,
    ManualCpc,
    ManualCpm,
    ManualCpv,
    MaximizeConversions,
    MaximizeConversionValue,
    PercentCpc,
    TargetCpa,
    TargetCpm,
    TargetImpressionShare,
    TargetRoas,
    TargetSpend,
)
from google.ads.googleads.v13.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v13.common.types.frequency_cap import FrequencyCapEntry
from google.ads.googleads.v13.common.types.real_time_bidding_setting import (
    RealTimeBiddingSetting,
)
from google.ads.googleads.v13.common.types.targeting_setting import TargetingSetting
from google.ads.googleads.v13.enums.types.ad_serving_optimization_status import (
    AdServingOptimizationStatusEnum,
)
from google.ads.googleads.v13.enums.types.advertising_channel_sub_type import (
    AdvertisingChannelSubTypeEnum,
)
from google.ads.googleads.v13.enums.types.advertising_channel_type import (
    AdvertisingChannelTypeEnum,
)
from google.ads.googleads.v13.enums.types.app_campaign_app_store import (
    AppCampaignAppStoreEnum,
)
from google.ads.googleads.v13.enums.types.app_campaign_bidding_strategy_goal_type import (
    AppCampaignBiddingStrategyGoalTypeEnum,
)
from google.ads.googleads.v13.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v13.enums.types.asset_set_type import AssetSetTypeEnum
from google.ads.googleads.v13.enums.types.bidding_strategy_system_status import (
    BiddingStrategySystemStatusEnum,
)
from google.ads.googleads.v13.enums.types.bidding_strategy_type import (
    BiddingStrategyTypeEnum,
)
from google.ads.googleads.v13.enums.types.brand_safety_suitability import (
    BrandSafetySuitabilityEnum,
)
from google.ads.googleads.v13.enums.types.campaign_experiment_type import (
    CampaignExperimentTypeEnum,
)
from google.ads.googleads.v13.enums.types.campaign_primary_status import (
    CampaignPrimaryStatusEnum,
)
from google.ads.googleads.v13.enums.types.campaign_primary_status_reason import (
    CampaignPrimaryStatusReasonEnum,
)
from google.ads.googleads.v13.enums.types.campaign_serving_status import (
    CampaignServingStatusEnum,
)
from google.ads.googleads.v13.enums.types.campaign_status import CampaignStatusEnum
from google.ads.googleads.v13.enums.types.listing_type import ListingTypeEnum
from google.ads.googleads.v13.enums.types.location_source_type import (
    LocationSourceTypeEnum,
)
from google.ads.googleads.v13.enums.types.negative_geo_target_type import (
    NegativeGeoTargetTypeEnum,
)
from google.ads.googleads.v13.enums.types.optimization_goal_type import (
    OptimizationGoalTypeEnum,
)
from google.ads.googleads.v13.enums.types.payment_mode import PaymentModeEnum
from google.ads.googleads.v13.enums.types.performance_max_upgrade_status import (
    PerformanceMaxUpgradeStatusEnum,
)
from google.ads.googleads.v13.enums.types.positive_geo_target_type import (
    PositiveGeoTargetTypeEnum,
)
from google.ads.googleads.v13.enums.types.vanity_pharma_display_url_mode import (
    VanityPharmaDisplayUrlModeEnum,
)
from google.ads.googleads.v13.enums.types.vanity_pharma_text import VanityPharmaTextEnum

class Campaign(proto.Message):
    class AppCampaignSetting(proto.Message):
        bidding_strategy_goal_type: AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType
        app_id: str
        app_store: AppCampaignAppStoreEnum.AppCampaignAppStore
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            bidding_strategy_goal_type: AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType = ...,
            app_id: str = ...,
            app_store: AppCampaignAppStoreEnum.AppCampaignAppStore = ...
        ) -> None: ...

    class AudienceSetting(proto.Message):
        use_audience_grouped: bool
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            use_audience_grouped: bool = ...
        ) -> None: ...

    class CategoryBid(proto.Message):
        category_id: str
        manual_cpa_bid_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            category_id: str = ...,
            manual_cpa_bid_micros: int = ...
        ) -> None: ...

    class DynamicSearchAdsSetting(proto.Message):
        domain_name: str
        language_code: str
        use_supplied_urls_only: bool
        feeds: MutableSequence[str]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            domain_name: str = ...,
            language_code: str = ...,
            use_supplied_urls_only: bool = ...,
            feeds: MutableSequence[str] = ...
        ) -> None: ...

    class GeoTargetTypeSetting(proto.Message):
        positive_geo_target_type: PositiveGeoTargetTypeEnum.PositiveGeoTargetType
        negative_geo_target_type: NegativeGeoTargetTypeEnum.NegativeGeoTargetType
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            positive_geo_target_type: PositiveGeoTargetTypeEnum.PositiveGeoTargetType = ...,
            negative_geo_target_type: NegativeGeoTargetTypeEnum.NegativeGeoTargetType = ...
        ) -> None: ...

    class HotelSettingInfo(proto.Message):
        hotel_center_id: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            hotel_center_id: int = ...
        ) -> None: ...

    class LocalCampaignSetting(proto.Message):
        location_source_type: LocationSourceTypeEnum.LocationSourceType
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            location_source_type: LocationSourceTypeEnum.LocationSourceType = ...
        ) -> None: ...

    class LocalServicesCampaignSettings(proto.Message):
        category_bids: MutableSequence[Campaign.CategoryBid]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            category_bids: MutableSequence[Campaign.CategoryBid] = ...
        ) -> None: ...

    class NetworkSettings(proto.Message):
        target_google_search: bool
        target_search_network: bool
        target_content_network: bool
        target_partner_search_network: bool
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            target_google_search: bool = ...,
            target_search_network: bool = ...,
            target_content_network: bool = ...,
            target_partner_search_network: bool = ...
        ) -> None: ...

    class OptimizationGoalSetting(proto.Message):
        optimization_goal_types: MutableSequence[
            OptimizationGoalTypeEnum.OptimizationGoalType
        ]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            optimization_goal_types: MutableSequence[
                OptimizationGoalTypeEnum.OptimizationGoalType
            ] = ...
        ) -> None: ...

    class PerformanceMaxUpgrade(proto.Message):
        performance_max_campaign: str
        pre_upgrade_campaign: str
        status: PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            performance_max_campaign: str = ...,
            pre_upgrade_campaign: str = ...,
            status: PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus = ...
        ) -> None: ...

    class SelectiveOptimization(proto.Message):
        conversion_actions: MutableSequence[str]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            conversion_actions: MutableSequence[str] = ...
        ) -> None: ...

    class ShoppingSetting(proto.Message):
        merchant_id: int
        sales_country: str
        feed_label: str
        campaign_priority: int
        enable_local: bool
        use_vehicle_inventory: bool
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            merchant_id: int = ...,
            sales_country: str = ...,
            feed_label: str = ...,
            campaign_priority: int = ...,
            enable_local: bool = ...,
            use_vehicle_inventory: bool = ...
        ) -> None: ...

    class TrackingSetting(proto.Message):
        tracking_url: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            tracking_url: str = ...
        ) -> None: ...

    class TravelCampaignSettings(proto.Message):
        travel_account_id: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            travel_account_id: int = ...
        ) -> None: ...

    class VanityPharma(proto.Message):
        vanity_pharma_display_url_mode: VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode
        vanity_pharma_text: VanityPharmaTextEnum.VanityPharmaText
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            vanity_pharma_display_url_mode: VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode = ...,
            vanity_pharma_text: VanityPharmaTextEnum.VanityPharmaText = ...
        ) -> None: ...
    resource_name: str
    id: int
    name: str
    primary_status: CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    primary_status_reasons: MutableSequence[
        CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    ]
    status: CampaignStatusEnum.CampaignStatus
    serving_status: CampaignServingStatusEnum.CampaignServingStatus
    bidding_strategy_system_status: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    ad_serving_optimization_status: AdServingOptimizationStatusEnum.AdServingOptimizationStatus
    advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType
    advertising_channel_sub_type: AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType
    tracking_url_template: str
    url_custom_parameters: MutableSequence[CustomParameter]
    local_services_campaign_settings: Campaign.LocalServicesCampaignSettings
    travel_campaign_settings: Campaign.TravelCampaignSettings
    real_time_bidding_setting: RealTimeBiddingSetting
    network_settings: Campaign.NetworkSettings
    hotel_setting: Campaign.HotelSettingInfo
    dynamic_search_ads_setting: Campaign.DynamicSearchAdsSetting
    shopping_setting: Campaign.ShoppingSetting
    targeting_setting: TargetingSetting
    audience_setting: Campaign.AudienceSetting
    geo_target_type_setting: Campaign.GeoTargetTypeSetting
    local_campaign_setting: Campaign.LocalCampaignSetting
    app_campaign_setting: Campaign.AppCampaignSetting
    labels: MutableSequence[str]
    experiment_type: CampaignExperimentTypeEnum.CampaignExperimentType
    base_campaign: str
    campaign_budget: str
    bidding_strategy_type: BiddingStrategyTypeEnum.BiddingStrategyType
    accessible_bidding_strategy: str
    start_date: str
    campaign_group: str
    end_date: str
    final_url_suffix: str
    frequency_caps: MutableSequence[FrequencyCapEntry]
    video_brand_safety_suitability: BrandSafetySuitabilityEnum.BrandSafetySuitability
    vanity_pharma: Campaign.VanityPharma
    selective_optimization: Campaign.SelectiveOptimization
    optimization_goal_setting: Campaign.OptimizationGoalSetting
    tracking_setting: Campaign.TrackingSetting
    payment_mode: PaymentModeEnum.PaymentMode
    optimization_score: float
    excluded_parent_asset_field_types: MutableSequence[
        AssetFieldTypeEnum.AssetFieldType
    ]
    excluded_parent_asset_set_types: MutableSequence[AssetSetTypeEnum.AssetSetType]
    url_expansion_opt_out: bool
    performance_max_upgrade: Campaign.PerformanceMaxUpgrade
    hotel_property_asset_set: str
    listing_type: ListingTypeEnum.ListingType
    bidding_strategy: str
    commission: Commission
    manual_cpa: ManualCpa
    manual_cpc: ManualCpc
    manual_cpm: ManualCpm
    manual_cpv: ManualCpv
    maximize_conversions: MaximizeConversions
    maximize_conversion_value: MaximizeConversionValue
    target_cpa: TargetCpa
    target_impression_share: TargetImpressionShare
    target_roas: TargetRoas
    target_spend: TargetSpend
    percent_cpc: PercentCpc
    target_cpm: TargetCpm
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        primary_status: CampaignPrimaryStatusEnum.CampaignPrimaryStatus = ...,
        primary_status_reasons: MutableSequence[
            CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
        ] = ...,
        status: CampaignStatusEnum.CampaignStatus = ...,
        serving_status: CampaignServingStatusEnum.CampaignServingStatus = ...,
        bidding_strategy_system_status: BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus = ...,
        ad_serving_optimization_status: AdServingOptimizationStatusEnum.AdServingOptimizationStatus = ...,
        advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType = ...,
        advertising_channel_sub_type: AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType = ...,
        tracking_url_template: str = ...,
        url_custom_parameters: MutableSequence[CustomParameter] = ...,
        local_services_campaign_settings: Campaign.LocalServicesCampaignSettings = ...,
        travel_campaign_settings: Campaign.TravelCampaignSettings = ...,
        real_time_bidding_setting: RealTimeBiddingSetting = ...,
        network_settings: Campaign.NetworkSettings = ...,
        hotel_setting: Campaign.HotelSettingInfo = ...,
        dynamic_search_ads_setting: Campaign.DynamicSearchAdsSetting = ...,
        shopping_setting: Campaign.ShoppingSetting = ...,
        targeting_setting: TargetingSetting = ...,
        audience_setting: Campaign.AudienceSetting = ...,
        geo_target_type_setting: Campaign.GeoTargetTypeSetting = ...,
        local_campaign_setting: Campaign.LocalCampaignSetting = ...,
        app_campaign_setting: Campaign.AppCampaignSetting = ...,
        labels: MutableSequence[str] = ...,
        experiment_type: CampaignExperimentTypeEnum.CampaignExperimentType = ...,
        base_campaign: str = ...,
        campaign_budget: str = ...,
        bidding_strategy_type: BiddingStrategyTypeEnum.BiddingStrategyType = ...,
        accessible_bidding_strategy: str = ...,
        start_date: str = ...,
        campaign_group: str = ...,
        end_date: str = ...,
        final_url_suffix: str = ...,
        frequency_caps: MutableSequence[FrequencyCapEntry] = ...,
        video_brand_safety_suitability: BrandSafetySuitabilityEnum.BrandSafetySuitability = ...,
        vanity_pharma: Campaign.VanityPharma = ...,
        selective_optimization: Campaign.SelectiveOptimization = ...,
        optimization_goal_setting: Campaign.OptimizationGoalSetting = ...,
        tracking_setting: Campaign.TrackingSetting = ...,
        payment_mode: PaymentModeEnum.PaymentMode = ...,
        optimization_score: float = ...,
        excluded_parent_asset_field_types: MutableSequence[
            AssetFieldTypeEnum.AssetFieldType
        ] = ...,
        excluded_parent_asset_set_types: MutableSequence[
            AssetSetTypeEnum.AssetSetType
        ] = ...,
        url_expansion_opt_out: bool = ...,
        performance_max_upgrade: Campaign.PerformanceMaxUpgrade = ...,
        hotel_property_asset_set: str = ...,
        listing_type: ListingTypeEnum.ListingType = ...,
        bidding_strategy: str = ...,
        commission: Commission = ...,
        manual_cpa: ManualCpa = ...,
        manual_cpc: ManualCpc = ...,
        manual_cpm: ManualCpm = ...,
        manual_cpv: ManualCpv = ...,
        maximize_conversions: MaximizeConversions = ...,
        maximize_conversion_value: MaximizeConversionValue = ...,
        target_cpa: TargetCpa = ...,
        target_impression_share: TargetImpressionShare = ...,
        target_roas: TargetRoas = ...,
        target_spend: TargetSpend = ...,
        percent_cpc: PercentCpc = ...,
        target_cpm: TargetCpm = ...
    ) -> None: ...
