import proto
from _typeshed import Incomplete
from google.protobuf import duration_pb2 as duration_pb2

from google.ads.googleads.v11.common.types import policy as policy, value as value
from google.ads.googleads.v11.enums.types import (
    resource_limit_type as resource_limit_type,
)

__protobuf__: Incomplete

class GoogleAdsFailure(proto.Message):
    errors: Incomplete
    request_id: Incomplete

class GoogleAdsError(proto.Message):
    error_code: Incomplete
    message: Incomplete
    trigger: Incomplete
    location: Incomplete
    details: Incomplete

class ErrorCode(proto.Message):
    request_error: Incomplete
    bidding_strategy_error: Incomplete
    url_field_error: Incomplete
    list_operation_error: Incomplete
    query_error: Incomplete
    mutate_error: Incomplete
    field_mask_error: Incomplete
    authorization_error: Incomplete
    internal_error: Incomplete
    quota_error: Incomplete
    ad_error: Incomplete
    ad_group_error: Incomplete
    campaign_budget_error: Incomplete
    campaign_error: Incomplete
    authentication_error: Incomplete
    ad_group_criterion_customizer_error: Incomplete
    ad_group_criterion_error: Incomplete
    ad_group_customizer_error: Incomplete
    ad_customizer_error: Incomplete
    ad_group_ad_error: Incomplete
    ad_sharing_error: Incomplete
    adx_error: Incomplete
    asset_error: Incomplete
    asset_group_asset_error: Incomplete
    asset_group_listing_group_filter_error: Incomplete
    asset_group_error: Incomplete
    asset_set_asset_error: Incomplete
    asset_set_link_error: Incomplete
    asset_set_error: Incomplete
    bidding_error: Incomplete
    campaign_criterion_error: Incomplete
    campaign_conversion_goal_error: Incomplete
    campaign_customizer_error: Incomplete
    collection_size_error: Incomplete
    conversion_goal_campaign_config_error: Incomplete
    country_code_error: Incomplete
    criterion_error: Incomplete
    custom_conversion_goal_error: Incomplete
    customer_customizer_error: Incomplete
    customer_error: Incomplete
    customizer_attribute_error: Incomplete
    date_error: Incomplete
    date_range_error: Incomplete
    distinct_error: Incomplete
    feed_attribute_reference_error: Incomplete
    function_error: Incomplete
    function_parsing_error: Incomplete
    id_error: Incomplete
    image_error: Incomplete
    language_code_error: Incomplete
    media_bundle_error: Incomplete
    media_upload_error: Incomplete
    media_file_error: Incomplete
    merchant_center_error: Incomplete
    multiplier_error: Incomplete
    new_resource_creation_error: Incomplete
    not_empty_error: Incomplete
    null_error: Incomplete
    operator_error: Incomplete
    range_error: Incomplete
    recommendation_error: Incomplete
    region_code_error: Incomplete
    setting_error: Incomplete
    string_format_error: Incomplete
    string_length_error: Incomplete
    operation_access_denied_error: Incomplete
    resource_access_denied_error: Incomplete
    resource_count_limit_exceeded_error: Incomplete
    youtube_video_registration_error: Incomplete
    ad_group_bid_modifier_error: Incomplete
    context_error: Incomplete
    field_error: Incomplete
    shared_set_error: Incomplete
    shared_criterion_error: Incomplete
    campaign_shared_set_error: Incomplete
    conversion_action_error: Incomplete
    conversion_adjustment_upload_error: Incomplete
    conversion_custom_variable_error: Incomplete
    conversion_upload_error: Incomplete
    conversion_value_rule_error: Incomplete
    conversion_value_rule_set_error: Incomplete
    header_error: Incomplete
    database_error: Incomplete
    policy_finding_error: Incomplete
    enum_error: Incomplete
    keyword_plan_error: Incomplete
    keyword_plan_campaign_error: Incomplete
    keyword_plan_campaign_keyword_error: Incomplete
    keyword_plan_ad_group_error: Incomplete
    keyword_plan_ad_group_keyword_error: Incomplete
    keyword_plan_idea_error: Incomplete
    account_budget_proposal_error: Incomplete
    user_list_error: Incomplete
    change_event_error: Incomplete
    change_status_error: Incomplete
    feed_error: Incomplete
    geo_target_constant_suggestion_error: Incomplete
    campaign_draft_error: Incomplete
    feed_item_error: Incomplete
    label_error: Incomplete
    billing_setup_error: Incomplete
    customer_client_link_error: Incomplete
    customer_manager_link_error: Incomplete
    feed_mapping_error: Incomplete
    customer_feed_error: Incomplete
    ad_group_feed_error: Incomplete
    campaign_feed_error: Incomplete
    custom_interest_error: Incomplete
    campaign_experiment_error: Incomplete
    extension_feed_item_error: Incomplete
    ad_parameter_error: Incomplete
    feed_item_validation_error: Incomplete
    extension_setting_error: Incomplete
    feed_item_set_error: Incomplete
    feed_item_set_link_error: Incomplete
    feed_item_target_error: Incomplete
    policy_violation_error: Incomplete
    partial_failure_error: Incomplete
    policy_validation_parameter_error: Incomplete
    size_limit_error: Incomplete
    offline_user_data_job_error: Incomplete
    not_allowlisted_error: Incomplete
    manager_link_error: Incomplete
    currency_code_error: Incomplete
    experiment_error: Incomplete
    access_invitation_error: Incomplete
    reach_plan_error: Incomplete
    invoice_error: Incomplete
    payments_account_error: Incomplete
    time_zone_error: Incomplete
    asset_link_error: Incomplete
    user_data_error: Incomplete
    batch_job_error: Incomplete
    account_link_error: Incomplete
    third_party_app_analytics_link_error: Incomplete
    customer_user_access_error: Incomplete
    custom_audience_error: Incomplete
    audience_error: Incomplete
    experiment_arm_error: Incomplete
    audience_insights_error: Incomplete

class ErrorLocation(proto.Message):
    class FieldPathElement(proto.Message):
        field_name: Incomplete
        index: Incomplete
    field_path_elements: Incomplete

class ErrorDetails(proto.Message):
    unpublished_error_code: Incomplete
    policy_violation_details: Incomplete
    policy_finding_details: Incomplete
    quota_error_details: Incomplete
    resource_count_details: Incomplete

class PolicyViolationDetails(proto.Message):
    external_policy_description: Incomplete
    key: Incomplete
    external_policy_name: Incomplete
    is_exemptible: Incomplete

class PolicyFindingDetails(proto.Message):
    policy_topic_entries: Incomplete

class QuotaErrorDetails(proto.Message):
    class QuotaRateScope(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ACCOUNT: int
        DEVELOPER: int
    rate_scope: Incomplete
    rate_name: Incomplete
    retry_delay: Incomplete

class ResourceCountDetails(proto.Message):
    enclosing_id: Incomplete
    enclosing_resource: Incomplete
    limit: Incomplete
    limit_type: Incomplete
    existing_count: Incomplete