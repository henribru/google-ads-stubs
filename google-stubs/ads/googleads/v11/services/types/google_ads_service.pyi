import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v11.services.types import (
    ad_group_ad_label_service as ad_group_ad_label_service,
    ad_group_ad_service as ad_group_ad_service,
    ad_group_asset_service as ad_group_asset_service,
    ad_group_bid_modifier_service as ad_group_bid_modifier_service,
    ad_group_criterion_customizer_service as ad_group_criterion_customizer_service,
    ad_group_criterion_label_service as ad_group_criterion_label_service,
    ad_group_criterion_service as ad_group_criterion_service,
    ad_group_customizer_service as ad_group_customizer_service,
    ad_group_extension_setting_service as ad_group_extension_setting_service,
    ad_group_feed_service as ad_group_feed_service,
    ad_group_label_service as ad_group_label_service,
    ad_group_service as ad_group_service,
    ad_parameter_service as ad_parameter_service,
    ad_service as ad_service,
    asset_group_asset_service as asset_group_asset_service,
    asset_group_listing_group_filter_service as asset_group_listing_group_filter_service,
    asset_group_service as asset_group_service,
    asset_group_signal_service as asset_group_signal_service,
    asset_service as asset_service,
    asset_set_asset_service as asset_set_asset_service,
    asset_set_service as asset_set_service,
    audience_service as audience_service,
    bidding_data_exclusion_service as bidding_data_exclusion_service,
    bidding_seasonality_adjustment_service as bidding_seasonality_adjustment_service,
    bidding_strategy_service as bidding_strategy_service,
    campaign_asset_service as campaign_asset_service,
    campaign_asset_set_service as campaign_asset_set_service,
    campaign_bid_modifier_service as campaign_bid_modifier_service,
    campaign_budget_service as campaign_budget_service,
    campaign_conversion_goal_service as campaign_conversion_goal_service,
    campaign_criterion_service as campaign_criterion_service,
    campaign_customizer_service as campaign_customizer_service,
    campaign_draft_service as campaign_draft_service,
    campaign_experiment_service as campaign_experiment_service,
    campaign_extension_setting_service as campaign_extension_setting_service,
    campaign_feed_service as campaign_feed_service,
    campaign_group_service as campaign_group_service,
    campaign_label_service as campaign_label_service,
    campaign_service as campaign_service,
    campaign_shared_set_service as campaign_shared_set_service,
    conversion_action_service as conversion_action_service,
    conversion_custom_variable_service as conversion_custom_variable_service,
    conversion_goal_campaign_config_service as conversion_goal_campaign_config_service,
    conversion_value_rule_service as conversion_value_rule_service,
    conversion_value_rule_set_service as conversion_value_rule_set_service,
    custom_conversion_goal_service as custom_conversion_goal_service,
    customer_asset_service as customer_asset_service,
    customer_conversion_goal_service as customer_conversion_goal_service,
    customer_customizer_service as customer_customizer_service,
    customer_extension_setting_service as customer_extension_setting_service,
    customer_feed_service as customer_feed_service,
    customer_label_service as customer_label_service,
    customer_negative_criterion_service as customer_negative_criterion_service,
    customer_service as customer_service,
    customizer_attribute_service as customizer_attribute_service,
    experiment_arm_service as experiment_arm_service,
    experiment_service as experiment_service,
    extension_feed_item_service as extension_feed_item_service,
    feed_item_service as feed_item_service,
    feed_item_set_link_service as feed_item_set_link_service,
    feed_item_set_service as feed_item_set_service,
    feed_item_target_service as feed_item_target_service,
    feed_mapping_service as feed_mapping_service,
    feed_service as feed_service,
    keyword_plan_ad_group_keyword_service as keyword_plan_ad_group_keyword_service,
    keyword_plan_ad_group_service as keyword_plan_ad_group_service,
    keyword_plan_campaign_keyword_service as keyword_plan_campaign_keyword_service,
    keyword_plan_campaign_service as keyword_plan_campaign_service,
    keyword_plan_service as keyword_plan_service,
    label_service as label_service,
    media_file_service as media_file_service,
    remarketing_action_service as remarketing_action_service,
    shared_criterion_service as shared_criterion_service,
    shared_set_service as shared_set_service,
    smart_campaign_setting_service as smart_campaign_setting_service,
    user_list_service as user_list_service,
)

__protobuf__: Incomplete

class SearchGoogleAdsRequest(proto.Message):
    customer_id: Incomplete
    query: Incomplete
    page_token: Incomplete
    page_size: Incomplete
    validate_only: Incomplete
    return_total_results_count: Incomplete
    summary_row_setting: Incomplete

class SearchGoogleAdsResponse(proto.Message):
    @property
    def raw_page(self): ...
    results: Incomplete
    next_page_token: Incomplete
    total_results_count: Incomplete
    field_mask: Incomplete
    summary_row: Incomplete

class SearchGoogleAdsStreamRequest(proto.Message):
    customer_id: Incomplete
    query: Incomplete
    summary_row_setting: Incomplete

class SearchGoogleAdsStreamResponse(proto.Message):
    results: Incomplete
    field_mask: Incomplete
    summary_row: Incomplete
    request_id: Incomplete

class GoogleAdsRow(proto.Message):
    account_budget: Incomplete
    account_budget_proposal: Incomplete
    account_link: Incomplete
    ad_group: Incomplete
    ad_group_ad: Incomplete
    ad_group_ad_asset_combination_view: Incomplete
    ad_group_ad_asset_view: Incomplete
    ad_group_ad_label: Incomplete
    ad_group_asset: Incomplete
    ad_group_audience_view: Incomplete
    ad_group_bid_modifier: Incomplete
    ad_group_criterion: Incomplete
    ad_group_criterion_customizer: Incomplete
    ad_group_criterion_label: Incomplete
    ad_group_criterion_simulation: Incomplete
    ad_group_customizer: Incomplete
    ad_group_extension_setting: Incomplete
    ad_group_feed: Incomplete
    ad_group_label: Incomplete
    ad_group_simulation: Incomplete
    ad_parameter: Incomplete
    age_range_view: Incomplete
    ad_schedule_view: Incomplete
    domain_category: Incomplete
    asset: Incomplete
    asset_field_type_view: Incomplete
    asset_group_asset: Incomplete
    asset_group_signal: Incomplete
    asset_group_listing_group_filter: Incomplete
    asset_group_product_group_view: Incomplete
    asset_group: Incomplete
    asset_set_asset: Incomplete
    asset_set: Incomplete
    batch_job: Incomplete
    bidding_data_exclusion: Incomplete
    bidding_seasonality_adjustment: Incomplete
    bidding_strategy: Incomplete
    bidding_strategy_simulation: Incomplete
    billing_setup: Incomplete
    call_view: Incomplete
    campaign_budget: Incomplete
    campaign: Incomplete
    campaign_asset: Incomplete
    campaign_asset_set: Incomplete
    campaign_audience_view: Incomplete
    campaign_bid_modifier: Incomplete
    campaign_conversion_goal: Incomplete
    campaign_criterion: Incomplete
    campaign_criterion_simulation: Incomplete
    campaign_customizer: Incomplete
    campaign_draft: Incomplete
    campaign_experiment: Incomplete
    campaign_extension_setting: Incomplete
    campaign_feed: Incomplete
    campaign_group: Incomplete
    campaign_label: Incomplete
    campaign_shared_set: Incomplete
    campaign_simulation: Incomplete
    carrier_constant: Incomplete
    change_event: Incomplete
    change_status: Incomplete
    combined_audience: Incomplete
    audience: Incomplete
    conversion_action: Incomplete
    conversion_custom_variable: Incomplete
    conversion_goal_campaign_config: Incomplete
    conversion_value_rule: Incomplete
    conversion_value_rule_set: Incomplete
    click_view: Incomplete
    currency_constant: Incomplete
    custom_audience: Incomplete
    custom_conversion_goal: Incomplete
    custom_interest: Incomplete
    customer: Incomplete
    customer_asset: Incomplete
    accessible_bidding_strategy: Incomplete
    customer_customizer: Incomplete
    customer_manager_link: Incomplete
    customer_client_link: Incomplete
    customer_client: Incomplete
    customer_conversion_goal: Incomplete
    customer_extension_setting: Incomplete
    customer_feed: Incomplete
    customer_label: Incomplete
    customer_negative_criterion: Incomplete
    customer_user_access: Incomplete
    customer_user_access_invitation: Incomplete
    customizer_attribute: Incomplete
    detail_placement_view: Incomplete
    detailed_demographic: Incomplete
    display_keyword_view: Incomplete
    distance_view: Incomplete
    dynamic_search_ads_search_term_view: Incomplete
    expanded_landing_page_view: Incomplete
    extension_feed_item: Incomplete
    feed: Incomplete
    feed_item: Incomplete
    feed_item_set: Incomplete
    feed_item_set_link: Incomplete
    feed_item_target: Incomplete
    feed_mapping: Incomplete
    feed_placeholder_view: Incomplete
    gender_view: Incomplete
    geo_target_constant: Incomplete
    geographic_view: Incomplete
    group_placement_view: Incomplete
    hotel_group_view: Incomplete
    hotel_performance_view: Incomplete
    hotel_reconciliation: Incomplete
    income_range_view: Incomplete
    keyword_view: Incomplete
    keyword_plan: Incomplete
    keyword_plan_campaign: Incomplete
    keyword_plan_campaign_keyword: Incomplete
    keyword_plan_ad_group: Incomplete
    keyword_plan_ad_group_keyword: Incomplete
    keyword_theme_constant: Incomplete
    label: Incomplete
    landing_page_view: Incomplete
    language_constant: Incomplete
    location_view: Incomplete
    managed_placement_view: Incomplete
    media_file: Incomplete
    mobile_app_category_constant: Incomplete
    mobile_device_constant: Incomplete
    offline_user_data_job: Incomplete
    operating_system_version_constant: Incomplete
    paid_organic_search_term_view: Incomplete
    parental_status_view: Incomplete
    product_bidding_category_constant: Incomplete
    product_group_view: Incomplete
    recommendation: Incomplete
    search_term_view: Incomplete
    shared_criterion: Incomplete
    shared_set: Incomplete
    smart_campaign_setting: Incomplete
    shopping_performance_view: Incomplete
    smart_campaign_search_term_view: Incomplete
    third_party_app_analytics_link: Incomplete
    topic_view: Incomplete
    experiment: Incomplete
    experiment_arm: Incomplete
    user_interest: Incomplete
    life_event: Incomplete
    user_list: Incomplete
    user_location_view: Incomplete
    remarketing_action: Incomplete
    topic_constant: Incomplete
    video: Incomplete
    webpage_view: Incomplete
    lead_form_submission_data: Incomplete
    metrics: Incomplete
    segments: Incomplete

class MutateGoogleAdsRequest(proto.Message):
    customer_id: Incomplete
    mutate_operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class MutateGoogleAdsResponse(proto.Message):
    partial_failure_error: Incomplete
    mutate_operation_responses: Incomplete

class MutateOperation(proto.Message):
    ad_group_ad_label_operation: Incomplete
    ad_group_ad_operation: Incomplete
    ad_group_asset_operation: Incomplete
    ad_group_bid_modifier_operation: Incomplete
    ad_group_criterion_customizer_operation: Incomplete
    ad_group_criterion_label_operation: Incomplete
    ad_group_criterion_operation: Incomplete
    ad_group_customizer_operation: Incomplete
    ad_group_extension_setting_operation: Incomplete
    ad_group_feed_operation: Incomplete
    ad_group_label_operation: Incomplete
    ad_group_operation: Incomplete
    ad_operation: Incomplete
    ad_parameter_operation: Incomplete
    asset_operation: Incomplete
    asset_group_asset_operation: Incomplete
    asset_group_listing_group_filter_operation: Incomplete
    asset_group_signal_operation: Incomplete
    asset_group_operation: Incomplete
    asset_set_asset_operation: Incomplete
    asset_set_operation: Incomplete
    audience_operation: Incomplete
    bidding_data_exclusion_operation: Incomplete
    bidding_seasonality_adjustment_operation: Incomplete
    bidding_strategy_operation: Incomplete
    campaign_asset_operation: Incomplete
    campaign_asset_set_operation: Incomplete
    campaign_bid_modifier_operation: Incomplete
    campaign_budget_operation: Incomplete
    campaign_conversion_goal_operation: Incomplete
    campaign_criterion_operation: Incomplete
    campaign_customizer_operation: Incomplete
    campaign_draft_operation: Incomplete
    campaign_experiment_operation: Incomplete
    campaign_extension_setting_operation: Incomplete
    campaign_feed_operation: Incomplete
    campaign_group_operation: Incomplete
    campaign_label_operation: Incomplete
    campaign_operation: Incomplete
    campaign_shared_set_operation: Incomplete
    conversion_action_operation: Incomplete
    conversion_custom_variable_operation: Incomplete
    conversion_goal_campaign_config_operation: Incomplete
    conversion_value_rule_operation: Incomplete
    conversion_value_rule_set_operation: Incomplete
    custom_conversion_goal_operation: Incomplete
    customer_asset_operation: Incomplete
    customer_conversion_goal_operation: Incomplete
    customer_customizer_operation: Incomplete
    customer_extension_setting_operation: Incomplete
    customer_feed_operation: Incomplete
    customer_label_operation: Incomplete
    customer_negative_criterion_operation: Incomplete
    customer_operation: Incomplete
    customizer_attribute_operation: Incomplete
    experiment_operation: Incomplete
    experiment_arm_operation: Incomplete
    extension_feed_item_operation: Incomplete
    feed_item_operation: Incomplete
    feed_item_set_operation: Incomplete
    feed_item_set_link_operation: Incomplete
    feed_item_target_operation: Incomplete
    feed_mapping_operation: Incomplete
    feed_operation: Incomplete
    keyword_plan_ad_group_operation: Incomplete
    keyword_plan_ad_group_keyword_operation: Incomplete
    keyword_plan_campaign_keyword_operation: Incomplete
    keyword_plan_campaign_operation: Incomplete
    keyword_plan_operation: Incomplete
    label_operation: Incomplete
    media_file_operation: Incomplete
    remarketing_action_operation: Incomplete
    shared_criterion_operation: Incomplete
    shared_set_operation: Incomplete
    smart_campaign_setting_operation: Incomplete
    user_list_operation: Incomplete

class MutateOperationResponse(proto.Message):
    ad_group_ad_label_result: Incomplete
    ad_group_ad_result: Incomplete
    ad_group_asset_result: Incomplete
    ad_group_bid_modifier_result: Incomplete
    ad_group_criterion_customizer_result: Incomplete
    ad_group_criterion_label_result: Incomplete
    ad_group_criterion_result: Incomplete
    ad_group_customizer_result: Incomplete
    ad_group_extension_setting_result: Incomplete
    ad_group_feed_result: Incomplete
    ad_group_label_result: Incomplete
    ad_group_result: Incomplete
    ad_parameter_result: Incomplete
    ad_result: Incomplete
    asset_result: Incomplete
    asset_group_asset_result: Incomplete
    asset_group_listing_group_filter_result: Incomplete
    asset_group_signal_result: Incomplete
    asset_group_result: Incomplete
    asset_set_asset_result: Incomplete
    asset_set_result: Incomplete
    audience_result: Incomplete
    bidding_data_exclusion_result: Incomplete
    bidding_seasonality_adjustment_result: Incomplete
    bidding_strategy_result: Incomplete
    campaign_asset_result: Incomplete
    campaign_asset_set_result: Incomplete
    campaign_bid_modifier_result: Incomplete
    campaign_budget_result: Incomplete
    campaign_conversion_goal_result: Incomplete
    campaign_criterion_result: Incomplete
    campaign_customizer_result: Incomplete
    campaign_draft_result: Incomplete
    campaign_experiment_result: Incomplete
    campaign_extension_setting_result: Incomplete
    campaign_feed_result: Incomplete
    campaign_group_result: Incomplete
    campaign_label_result: Incomplete
    campaign_result: Incomplete
    campaign_shared_set_result: Incomplete
    conversion_action_result: Incomplete
    conversion_custom_variable_result: Incomplete
    conversion_goal_campaign_config_result: Incomplete
    conversion_value_rule_result: Incomplete
    conversion_value_rule_set_result: Incomplete
    custom_conversion_goal_result: Incomplete
    customer_asset_result: Incomplete
    customer_conversion_goal_result: Incomplete
    customer_customizer_result: Incomplete
    customer_extension_setting_result: Incomplete
    customer_feed_result: Incomplete
    customer_label_result: Incomplete
    customer_negative_criterion_result: Incomplete
    customer_result: Incomplete
    customizer_attribute_result: Incomplete
    experiment_result: Incomplete
    experiment_arm_result: Incomplete
    extension_feed_item_result: Incomplete
    feed_item_result: Incomplete
    feed_item_set_result: Incomplete
    feed_item_set_link_result: Incomplete
    feed_item_target_result: Incomplete
    feed_mapping_result: Incomplete
    feed_result: Incomplete
    keyword_plan_ad_group_result: Incomplete
    keyword_plan_campaign_result: Incomplete
    keyword_plan_ad_group_keyword_result: Incomplete
    keyword_plan_campaign_keyword_result: Incomplete
    keyword_plan_result: Incomplete
    label_result: Incomplete
    media_file_result: Incomplete
    remarketing_action_result: Incomplete
    shared_criterion_result: Incomplete
    shared_set_result: Incomplete
    smart_campaign_setting_result: Incomplete
    user_list_result: Incomplete
