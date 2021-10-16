from typing import Any

import proto

from google.ads.googleads.v7.common.types import (
    bidding as bidding,
    custom_parameter as custom_parameter,
    frequency_cap as frequency_cap,
)
from google.ads.googleads.v7.enums.types import (
    app_campaign_app_store as app_campaign_app_store,
    app_campaign_bidding_strategy_goal_type as app_campaign_bidding_strategy_goal_type,
    asset_field_type as asset_field_type,
    brand_safety_suitability as brand_safety_suitability,
    campaign_experiment_type as campaign_experiment_type,
    campaign_serving_status as campaign_serving_status,
    campaign_status as campaign_status,
    optimization_goal_type as optimization_goal_type,
)

__protobuf__: Any

class Campaign(proto.Message):
    class NetworkSettings(proto.Message):
        target_google_search: Any
        target_search_network: Any
        target_content_network: Any
        target_partner_search_network: Any
    class HotelSettingInfo(proto.Message):
        hotel_center_id: Any
    class LocalCampaignSetting(proto.Message):
        location_source_type: Any
    class DynamicSearchAdsSetting(proto.Message):
        domain_name: Any
        language_code: Any
        use_supplied_urls_only: Any
        feeds: Any
    class TrackingSetting(proto.Message):
        tracking_url: Any
    class VanityPharma(proto.Message):
        vanity_pharma_display_url_mode: Any
        vanity_pharma_text: Any
    class ShoppingSetting(proto.Message):
        merchant_id: Any
        sales_country: Any
        campaign_priority: Any
        enable_local: Any
    class OptimizationGoalSetting(proto.Message):
        optimization_goal_types: Any
    class GeoTargetTypeSetting(proto.Message):
        positive_geo_target_type: Any
        negative_geo_target_type: Any
    class SelectiveOptimization(proto.Message):
        conversion_actions: Any
    class AppCampaignSetting(proto.Message):
        bidding_strategy_goal_type: Any
        app_id: Any
        app_store: Any
    resource_name: Any
    id: Any
    name: Any
    status: Any
    serving_status: Any
    ad_serving_optimization_status: Any
    advertising_channel_type: Any
    advertising_channel_sub_type: Any
    tracking_url_template: Any
    url_custom_parameters: Any
    real_time_bidding_setting: Any
    network_settings: Any
    hotel_setting: Any
    dynamic_search_ads_setting: Any
    shopping_setting: Any
    targeting_setting: Any
    geo_target_type_setting: Any
    local_campaign_setting: Any
    app_campaign_setting: Any
    labels: Any
    experiment_type: Any
    base_campaign: Any
    campaign_budget: Any
    bidding_strategy_type: Any
    start_date: Any
    end_date: Any
    final_url_suffix: Any
    frequency_caps: Any
    video_brand_safety_suitability: Any
    vanity_pharma: Any
    selective_optimization: Any
    optimization_goal_setting: Any
    tracking_setting: Any
    payment_mode: Any
    optimization_score: Any
    excluded_parent_asset_field_types: Any
    bidding_strategy: Any
    commission: Any
    manual_cpc: Any
    manual_cpm: Any
    manual_cpv: Any
    maximize_conversions: Any
    maximize_conversion_value: Any
    target_cpa: Any
    target_impression_share: Any
    target_roas: Any
    target_spend: Any
    percent_cpc: Any
    target_cpm: Any
