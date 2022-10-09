import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import (
    bidding as bidding,
    custom_parameter as custom_parameter,
    frequency_cap as frequency_cap,
)
from google.ads.googleads.v11.enums.types import (
    app_campaign_app_store as app_campaign_app_store,
    app_campaign_bidding_strategy_goal_type as app_campaign_bidding_strategy_goal_type,
    asset_field_type as asset_field_type,
    brand_safety_suitability as brand_safety_suitability,
    campaign_experiment_type as campaign_experiment_type,
    campaign_serving_status as campaign_serving_status,
    campaign_status as campaign_status,
    optimization_goal_type as optimization_goal_type,
    performance_max_upgrade_status as performance_max_upgrade_status,
)

__protobuf__: Incomplete

class Campaign(proto.Message):
    class PerformanceMaxUpgrade(proto.Message):
        performance_max_campaign: Incomplete
        pre_upgrade_campaign: Incomplete
        status: Incomplete

    class NetworkSettings(proto.Message):
        target_google_search: Incomplete
        target_search_network: Incomplete
        target_content_network: Incomplete
        target_partner_search_network: Incomplete

    class HotelSettingInfo(proto.Message):
        hotel_center_id: Incomplete

    class DynamicSearchAdsSetting(proto.Message):
        domain_name: Incomplete
        language_code: Incomplete
        use_supplied_urls_only: Incomplete
        feeds: Incomplete

    class ShoppingSetting(proto.Message):
        merchant_id: Incomplete
        sales_country: Incomplete
        feed_label: Incomplete
        campaign_priority: Incomplete
        enable_local: Incomplete
        use_vehicle_inventory: Incomplete

    class TrackingSetting(proto.Message):
        tracking_url: Incomplete

    class GeoTargetTypeSetting(proto.Message):
        positive_geo_target_type: Incomplete
        negative_geo_target_type: Incomplete

    class LocalCampaignSetting(proto.Message):
        location_source_type: Incomplete

    class AppCampaignSetting(proto.Message):
        bidding_strategy_goal_type: Incomplete
        app_id: Incomplete
        app_store: Incomplete

    class VanityPharma(proto.Message):
        vanity_pharma_display_url_mode: Incomplete
        vanity_pharma_text: Incomplete

    class SelectiveOptimization(proto.Message):
        conversion_actions: Incomplete

    class OptimizationGoalSetting(proto.Message):
        optimization_goal_types: Incomplete

    class AudienceSetting(proto.Message):
        use_audience_grouped: Incomplete

    class LocalServicesCampaignSettings(proto.Message):
        category_bids: Incomplete

    class CategoryBid(proto.Message):
        category_id: Incomplete
        manual_cpa_bid_micros: Incomplete
    resource_name: Incomplete
    id: Incomplete
    name: Incomplete
    status: Incomplete
    serving_status: Incomplete
    bidding_strategy_system_status: Incomplete
    ad_serving_optimization_status: Incomplete
    advertising_channel_type: Incomplete
    advertising_channel_sub_type: Incomplete
    tracking_url_template: Incomplete
    url_custom_parameters: Incomplete
    local_services_campaign_settings: Incomplete
    real_time_bidding_setting: Incomplete
    network_settings: Incomplete
    hotel_setting: Incomplete
    dynamic_search_ads_setting: Incomplete
    shopping_setting: Incomplete
    targeting_setting: Incomplete
    audience_setting: Incomplete
    geo_target_type_setting: Incomplete
    local_campaign_setting: Incomplete
    app_campaign_setting: Incomplete
    labels: Incomplete
    experiment_type: Incomplete
    base_campaign: Incomplete
    campaign_budget: Incomplete
    bidding_strategy_type: Incomplete
    accessible_bidding_strategy: Incomplete
    start_date: Incomplete
    campaign_group: Incomplete
    end_date: Incomplete
    final_url_suffix: Incomplete
    frequency_caps: Incomplete
    video_brand_safety_suitability: Incomplete
    vanity_pharma: Incomplete
    selective_optimization: Incomplete
    optimization_goal_setting: Incomplete
    tracking_setting: Incomplete
    payment_mode: Incomplete
    optimization_score: Incomplete
    excluded_parent_asset_field_types: Incomplete
    url_expansion_opt_out: Incomplete
    performance_max_upgrade: Incomplete
    bidding_strategy: Incomplete
    commission: Incomplete
    manual_cpa: Incomplete
    manual_cpc: Incomplete
    manual_cpm: Incomplete
    manual_cpv: Incomplete
    maximize_conversions: Incomplete
    maximize_conversion_value: Incomplete
    target_cpa: Incomplete
    target_impression_share: Incomplete
    target_roas: Incomplete
    target_spend: Incomplete
    percent_cpc: Incomplete
    target_cpm: Incomplete
