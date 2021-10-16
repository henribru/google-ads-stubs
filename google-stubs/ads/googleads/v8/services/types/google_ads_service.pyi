from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v8.services.types import (
    ad_group_ad_label_service as ad_group_ad_label_service,
    ad_group_ad_service as ad_group_ad_service,
    ad_group_asset_service as ad_group_asset_service,
    ad_group_bid_modifier_service as ad_group_bid_modifier_service,
    ad_group_criterion_label_service as ad_group_criterion_label_service,
    ad_group_criterion_service as ad_group_criterion_service,
    ad_group_extension_setting_service as ad_group_extension_setting_service,
    ad_group_feed_service as ad_group_feed_service,
    ad_group_label_service as ad_group_label_service,
    ad_group_service as ad_group_service,
    ad_parameter_service as ad_parameter_service,
    ad_service as ad_service,
    asset_service as asset_service,
    bidding_data_exclusion_service as bidding_data_exclusion_service,
    bidding_seasonality_adjustment_service as bidding_seasonality_adjustment_service,
    bidding_strategy_service as bidding_strategy_service,
    campaign_asset_service as campaign_asset_service,
    campaign_bid_modifier_service as campaign_bid_modifier_service,
    campaign_budget_service as campaign_budget_service,
    campaign_criterion_service as campaign_criterion_service,
    campaign_draft_service as campaign_draft_service,
    campaign_experiment_service as campaign_experiment_service,
    campaign_extension_setting_service as campaign_extension_setting_service,
    campaign_feed_service as campaign_feed_service,
    campaign_label_service as campaign_label_service,
    campaign_service as campaign_service,
    campaign_shared_set_service as campaign_shared_set_service,
    conversion_action_service as conversion_action_service,
    conversion_custom_variable_service as conversion_custom_variable_service,
    conversion_value_rule_service as conversion_value_rule_service,
    conversion_value_rule_set_service as conversion_value_rule_set_service,
    customer_asset_service as customer_asset_service,
    customer_extension_setting_service as customer_extension_setting_service,
    customer_feed_service as customer_feed_service,
    customer_label_service as customer_label_service,
    customer_negative_criterion_service as customer_negative_criterion_service,
    customer_service as customer_service,
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

__protobuf__: Any

class SearchGoogleAdsRequest(proto.Message):
    customer_id: Any
    query: Any
    page_token: Any
    page_size: Any
    validate_only: Any
    return_total_results_count: Any
    summary_row_setting: Any

class SearchGoogleAdsResponse(proto.Message):
    @property
    def raw_page(self): ...
    results: Any
    next_page_token: Any
    total_results_count: Any
    field_mask: Any
    summary_row: Any

class SearchGoogleAdsStreamRequest(proto.Message):
    customer_id: Any
    query: Any
    summary_row_setting: Any

class SearchGoogleAdsStreamResponse(proto.Message):
    results: Any
    field_mask: Any
    summary_row: Any
    request_id: Any

class GoogleAdsRow(proto.Message):
    account_budget: Any
    account_budget_proposal: Any
    account_link: Any
    ad_group: Any
    ad_group_ad: Any
    ad_group_ad_asset_view: Any
    ad_group_ad_label: Any
    ad_group_asset: Any
    ad_group_audience_view: Any
    ad_group_bid_modifier: Any
    ad_group_criterion: Any
    ad_group_criterion_label: Any
    ad_group_criterion_simulation: Any
    ad_group_extension_setting: Any
    ad_group_feed: Any
    ad_group_label: Any
    ad_group_simulation: Any
    ad_parameter: Any
    age_range_view: Any
    ad_schedule_view: Any
    domain_category: Any
    asset: Any
    asset_field_type_view: Any
    batch_job: Any
    bidding_data_exclusion: Any
    bidding_seasonality_adjustment: Any
    bidding_strategy: Any
    bidding_strategy_simulation: Any
    billing_setup: Any
    call_view: Any
    campaign_budget: Any
    campaign: Any
    campaign_asset: Any
    campaign_audience_view: Any
    campaign_bid_modifier: Any
    campaign_criterion: Any
    campaign_criterion_simulation: Any
    campaign_draft: Any
    campaign_experiment: Any
    campaign_extension_setting: Any
    campaign_feed: Any
    campaign_label: Any
    campaign_shared_set: Any
    campaign_simulation: Any
    carrier_constant: Any
    change_event: Any
    change_status: Any
    combined_audience: Any
    conversion_action: Any
    conversion_custom_variable: Any
    conversion_value_rule: Any
    conversion_value_rule_set: Any
    click_view: Any
    currency_constant: Any
    custom_audience: Any
    custom_interest: Any
    customer: Any
    customer_asset: Any
    accessible_bidding_strategy: Any
    customer_manager_link: Any
    customer_client_link: Any
    customer_client: Any
    customer_extension_setting: Any
    customer_feed: Any
    customer_label: Any
    customer_negative_criterion: Any
    customer_user_access: Any
    customer_user_access_invitation: Any
    detail_placement_view: Any
    detailed_demographic: Any
    display_keyword_view: Any
    distance_view: Any
    dynamic_search_ads_search_term_view: Any
    expanded_landing_page_view: Any
    extension_feed_item: Any
    feed: Any
    feed_item: Any
    feed_item_set: Any
    feed_item_set_link: Any
    feed_item_target: Any
    feed_mapping: Any
    feed_placeholder_view: Any
    gender_view: Any
    geo_target_constant: Any
    geographic_view: Any
    group_placement_view: Any
    hotel_group_view: Any
    hotel_performance_view: Any
    income_range_view: Any
    keyword_view: Any
    keyword_plan: Any
    keyword_plan_campaign: Any
    keyword_plan_campaign_keyword: Any
    keyword_plan_ad_group: Any
    keyword_plan_ad_group_keyword: Any
    keyword_theme_constant: Any
    label: Any
    landing_page_view: Any
    language_constant: Any
    location_view: Any
    managed_placement_view: Any
    media_file: Any
    mobile_app_category_constant: Any
    mobile_device_constant: Any
    offline_user_data_job: Any
    operating_system_version_constant: Any
    paid_organic_search_term_view: Any
    parental_status_view: Any
    product_bidding_category_constant: Any
    product_group_view: Any
    recommendation: Any
    search_term_view: Any
    shared_criterion: Any
    shared_set: Any
    smart_campaign_setting: Any
    shopping_performance_view: Any
    smart_campaign_search_term_view: Any
    third_party_app_analytics_link: Any
    topic_view: Any
    user_interest: Any
    life_event: Any
    user_list: Any
    user_location_view: Any
    remarketing_action: Any
    topic_constant: Any
    video: Any
    webpage_view: Any
    metrics: Any
    segments: Any

class MutateGoogleAdsRequest(proto.Message):
    customer_id: Any
    mutate_operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class MutateGoogleAdsResponse(proto.Message):
    partial_failure_error: Any
    mutate_operation_responses: Any

class MutateOperation(proto.Message):
    ad_group_ad_label_operation: Any
    ad_group_ad_operation: Any
    ad_group_asset_operation: Any
    ad_group_bid_modifier_operation: Any
    ad_group_criterion_label_operation: Any
    ad_group_criterion_operation: Any
    ad_group_extension_setting_operation: Any
    ad_group_feed_operation: Any
    ad_group_label_operation: Any
    ad_group_operation: Any
    ad_operation: Any
    ad_parameter_operation: Any
    asset_operation: Any
    bidding_data_exclusion_operation: Any
    bidding_seasonality_adjustment_operation: Any
    bidding_strategy_operation: Any
    campaign_asset_operation: Any
    campaign_bid_modifier_operation: Any
    campaign_budget_operation: Any
    campaign_criterion_operation: Any
    campaign_draft_operation: Any
    campaign_experiment_operation: Any
    campaign_extension_setting_operation: Any
    campaign_feed_operation: Any
    campaign_label_operation: Any
    campaign_operation: Any
    campaign_shared_set_operation: Any
    conversion_action_operation: Any
    conversion_custom_variable_operation: Any
    conversion_value_rule_operation: Any
    conversion_value_rule_set_operation: Any
    customer_asset_operation: Any
    customer_extension_setting_operation: Any
    customer_feed_operation: Any
    customer_label_operation: Any
    customer_negative_criterion_operation: Any
    customer_operation: Any
    extension_feed_item_operation: Any
    feed_item_operation: Any
    feed_item_set_operation: Any
    feed_item_set_link_operation: Any
    feed_item_target_operation: Any
    feed_mapping_operation: Any
    feed_operation: Any
    keyword_plan_ad_group_operation: Any
    keyword_plan_ad_group_keyword_operation: Any
    keyword_plan_campaign_keyword_operation: Any
    keyword_plan_campaign_operation: Any
    keyword_plan_operation: Any
    label_operation: Any
    media_file_operation: Any
    remarketing_action_operation: Any
    shared_criterion_operation: Any
    shared_set_operation: Any
    smart_campaign_setting_operation: Any
    user_list_operation: Any

class MutateOperationResponse(proto.Message):
    ad_group_ad_label_result: Any
    ad_group_ad_result: Any
    ad_group_asset_result: Any
    ad_group_bid_modifier_result: Any
    ad_group_criterion_label_result: Any
    ad_group_criterion_result: Any
    ad_group_extension_setting_result: Any
    ad_group_feed_result: Any
    ad_group_label_result: Any
    ad_group_result: Any
    ad_parameter_result: Any
    ad_result: Any
    asset_result: Any
    bidding_data_exclusion_result: Any
    bidding_seasonality_adjustment_result: Any
    bidding_strategy_result: Any
    campaign_asset_result: Any
    campaign_bid_modifier_result: Any
    campaign_budget_result: Any
    campaign_criterion_result: Any
    campaign_draft_result: Any
    campaign_experiment_result: Any
    campaign_extension_setting_result: Any
    campaign_feed_result: Any
    campaign_label_result: Any
    campaign_result: Any
    campaign_shared_set_result: Any
    conversion_action_result: Any
    conversion_custom_variable_result: Any
    conversion_value_rule_result: Any
    conversion_value_rule_set_result: Any
    customer_asset_result: Any
    customer_extension_setting_result: Any
    customer_feed_result: Any
    customer_label_result: Any
    customer_negative_criterion_result: Any
    customer_result: Any
    extension_feed_item_result: Any
    feed_item_result: Any
    feed_item_set_result: Any
    feed_item_set_link_result: Any
    feed_item_target_result: Any
    feed_mapping_result: Any
    feed_result: Any
    keyword_plan_ad_group_result: Any
    keyword_plan_campaign_result: Any
    keyword_plan_ad_group_keyword_result: Any
    keyword_plan_campaign_keyword_result: Any
    keyword_plan_result: Any
    label_result: Any
    media_file_result: Any
    remarketing_action_result: Any
    shared_criterion_result: Any
    shared_set_result: Any
    smart_campaign_setting_result: Any
    user_list_result: Any
