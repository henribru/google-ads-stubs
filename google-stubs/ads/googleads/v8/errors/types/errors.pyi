from typing import Any

import proto
from google.protobuf import duration_pb2 as duration_pb2

from google.ads.googleads.v8.common.types import policy as policy, value as value
from google.ads.googleads.v8.enums.types import (
    resource_limit_type as resource_limit_type,
)

__protobuf__: Any

class GoogleAdsFailure(proto.Message):
    errors: Any
    request_id: Any

class GoogleAdsError(proto.Message):
    error_code: Any
    message: Any
    trigger: Any
    location: Any
    details: Any

class ErrorCode(proto.Message):
    request_error: Any
    bidding_strategy_error: Any
    url_field_error: Any
    list_operation_error: Any
    query_error: Any
    mutate_error: Any
    field_mask_error: Any
    authorization_error: Any
    internal_error: Any
    quota_error: Any
    ad_error: Any
    ad_group_error: Any
    campaign_budget_error: Any
    campaign_error: Any
    authentication_error: Any
    ad_group_criterion_error: Any
    ad_customizer_error: Any
    ad_group_ad_error: Any
    ad_sharing_error: Any
    adx_error: Any
    asset_error: Any
    bidding_error: Any
    campaign_criterion_error: Any
    collection_size_error: Any
    country_code_error: Any
    criterion_error: Any
    customer_error: Any
    date_error: Any
    date_range_error: Any
    distinct_error: Any
    feed_attribute_reference_error: Any
    function_error: Any
    function_parsing_error: Any
    id_error: Any
    image_error: Any
    language_code_error: Any
    media_bundle_error: Any
    media_upload_error: Any
    media_file_error: Any
    multiplier_error: Any
    new_resource_creation_error: Any
    not_empty_error: Any
    null_error: Any
    operator_error: Any
    range_error: Any
    recommendation_error: Any
    region_code_error: Any
    setting_error: Any
    string_format_error: Any
    string_length_error: Any
    operation_access_denied_error: Any
    resource_access_denied_error: Any
    resource_count_limit_exceeded_error: Any
    youtube_video_registration_error: Any
    ad_group_bid_modifier_error: Any
    context_error: Any
    field_error: Any
    shared_set_error: Any
    shared_criterion_error: Any
    campaign_shared_set_error: Any
    conversion_action_error: Any
    conversion_adjustment_upload_error: Any
    conversion_custom_variable_error: Any
    conversion_upload_error: Any
    conversion_value_rule_error: Any
    conversion_value_rule_set_error: Any
    header_error: Any
    database_error: Any
    policy_finding_error: Any
    enum_error: Any
    keyword_plan_error: Any
    keyword_plan_campaign_error: Any
    keyword_plan_campaign_keyword_error: Any
    keyword_plan_ad_group_error: Any
    keyword_plan_ad_group_keyword_error: Any
    keyword_plan_idea_error: Any
    account_budget_proposal_error: Any
    user_list_error: Any
    change_event_error: Any
    change_status_error: Any
    feed_error: Any
    geo_target_constant_suggestion_error: Any
    campaign_draft_error: Any
    feed_item_error: Any
    label_error: Any
    billing_setup_error: Any
    customer_client_link_error: Any
    customer_manager_link_error: Any
    feed_mapping_error: Any
    customer_feed_error: Any
    ad_group_feed_error: Any
    campaign_feed_error: Any
    custom_interest_error: Any
    campaign_experiment_error: Any
    extension_feed_item_error: Any
    ad_parameter_error: Any
    feed_item_validation_error: Any
    extension_setting_error: Any
    feed_item_set_error: Any
    feed_item_set_link_error: Any
    feed_item_target_error: Any
    policy_violation_error: Any
    partial_failure_error: Any
    policy_validation_parameter_error: Any
    size_limit_error: Any
    offline_user_data_job_error: Any
    not_allowlisted_error: Any
    manager_link_error: Any
    currency_code_error: Any
    access_invitation_error: Any
    reach_plan_error: Any
    invoice_error: Any
    payments_account_error: Any
    time_zone_error: Any
    asset_link_error: Any
    user_data_error: Any
    batch_job_error: Any
    account_link_error: Any
    third_party_app_analytics_link_error: Any
    customer_user_access_error: Any
    custom_audience_error: Any

class ErrorLocation(proto.Message):
    class FieldPathElement(proto.Message):
        field_name: Any
        index: Any
    field_path_elements: Any

class ErrorDetails(proto.Message):
    unpublished_error_code: Any
    policy_violation_details: Any
    policy_finding_details: Any
    quota_error_details: Any
    resource_count_details: Any

class PolicyViolationDetails(proto.Message):
    external_policy_description: Any
    key: Any
    external_policy_name: Any
    is_exemptible: Any

class PolicyFindingDetails(proto.Message):
    policy_topic_entries: Any

class QuotaErrorDetails(proto.Message):
    class QuotaRateScope(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ACCOUNT: int
        DEVELOPER: int
    rate_scope: Any
    rate_name: Any
    retry_delay: Any

class ResourceCountDetails(proto.Message):
    enclosing_id: Any
    enclosing_resource: Any
    limit: Any
    limit_type: Any
    existing_count: Any
