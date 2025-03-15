from typing import AsyncIterable, Awaitable, Callable, MutableSequence, Sequence, Tuple

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials

from google.ads.googleads.v17.services.services.google_ads_service import pagers
from google.ads.googleads.v17.services.types import google_ads_service

from .transports.base import GoogleAdsServiceTransport

__all__ = ["GoogleAdsServiceAsyncClient"]

class GoogleAdsServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    accessible_bidding_strategy_path: Incomplete
    parse_accessible_bidding_strategy_path: Incomplete
    account_budget_path: Incomplete
    parse_account_budget_path: Incomplete
    account_budget_proposal_path: Incomplete
    parse_account_budget_proposal_path: Incomplete
    account_link_path: Incomplete
    parse_account_link_path: Incomplete
    ad_path: Incomplete
    parse_ad_path: Incomplete
    ad_group_path: Incomplete
    parse_ad_group_path: Incomplete
    ad_group_ad_path: Incomplete
    parse_ad_group_ad_path: Incomplete
    ad_group_ad_asset_combination_view_path: Incomplete
    parse_ad_group_ad_asset_combination_view_path: Incomplete
    ad_group_ad_asset_view_path: Incomplete
    parse_ad_group_ad_asset_view_path: Incomplete
    ad_group_ad_label_path: Incomplete
    parse_ad_group_ad_label_path: Incomplete
    ad_group_asset_path: Incomplete
    parse_ad_group_asset_path: Incomplete
    ad_group_asset_set_path: Incomplete
    parse_ad_group_asset_set_path: Incomplete
    ad_group_audience_view_path: Incomplete
    parse_ad_group_audience_view_path: Incomplete
    ad_group_bid_modifier_path: Incomplete
    parse_ad_group_bid_modifier_path: Incomplete
    ad_group_criterion_path: Incomplete
    parse_ad_group_criterion_path: Incomplete
    ad_group_criterion_customizer_path: Incomplete
    parse_ad_group_criterion_customizer_path: Incomplete
    ad_group_criterion_label_path: Incomplete
    parse_ad_group_criterion_label_path: Incomplete
    ad_group_criterion_simulation_path: Incomplete
    parse_ad_group_criterion_simulation_path: Incomplete
    ad_group_customizer_path: Incomplete
    parse_ad_group_customizer_path: Incomplete
    ad_group_extension_setting_path: Incomplete
    parse_ad_group_extension_setting_path: Incomplete
    ad_group_feed_path: Incomplete
    parse_ad_group_feed_path: Incomplete
    ad_group_label_path: Incomplete
    parse_ad_group_label_path: Incomplete
    ad_group_simulation_path: Incomplete
    parse_ad_group_simulation_path: Incomplete
    ad_parameter_path: Incomplete
    parse_ad_parameter_path: Incomplete
    ad_schedule_view_path: Incomplete
    parse_ad_schedule_view_path: Incomplete
    age_range_view_path: Incomplete
    parse_age_range_view_path: Incomplete
    android_privacy_shared_key_google_ad_group_path: Incomplete
    parse_android_privacy_shared_key_google_ad_group_path: Incomplete
    android_privacy_shared_key_google_campaign_path: Incomplete
    parse_android_privacy_shared_key_google_campaign_path: Incomplete
    android_privacy_shared_key_google_network_type_path: Incomplete
    parse_android_privacy_shared_key_google_network_type_path: Incomplete
    asset_path: Incomplete
    parse_asset_path: Incomplete
    asset_field_type_view_path: Incomplete
    parse_asset_field_type_view_path: Incomplete
    asset_group_path: Incomplete
    parse_asset_group_path: Incomplete
    asset_group_asset_path: Incomplete
    parse_asset_group_asset_path: Incomplete
    asset_group_listing_group_filter_path: Incomplete
    parse_asset_group_listing_group_filter_path: Incomplete
    asset_group_product_group_view_path: Incomplete
    parse_asset_group_product_group_view_path: Incomplete
    asset_group_signal_path: Incomplete
    parse_asset_group_signal_path: Incomplete
    asset_group_top_combination_view_path: Incomplete
    parse_asset_group_top_combination_view_path: Incomplete
    asset_set_path: Incomplete
    parse_asset_set_path: Incomplete
    asset_set_asset_path: Incomplete
    parse_asset_set_asset_path: Incomplete
    asset_set_type_view_path: Incomplete
    parse_asset_set_type_view_path: Incomplete
    audience_path: Incomplete
    parse_audience_path: Incomplete
    batch_job_path: Incomplete
    parse_batch_job_path: Incomplete
    bidding_data_exclusion_path: Incomplete
    parse_bidding_data_exclusion_path: Incomplete
    bidding_seasonality_adjustment_path: Incomplete
    parse_bidding_seasonality_adjustment_path: Incomplete
    bidding_strategy_path: Incomplete
    parse_bidding_strategy_path: Incomplete
    bidding_strategy_simulation_path: Incomplete
    parse_bidding_strategy_simulation_path: Incomplete
    billing_setup_path: Incomplete
    parse_billing_setup_path: Incomplete
    call_view_path: Incomplete
    parse_call_view_path: Incomplete
    campaign_path: Incomplete
    parse_campaign_path: Incomplete
    campaign_aggregate_asset_view_path: Incomplete
    parse_campaign_aggregate_asset_view_path: Incomplete
    campaign_asset_path: Incomplete
    parse_campaign_asset_path: Incomplete
    campaign_asset_set_path: Incomplete
    parse_campaign_asset_set_path: Incomplete
    campaign_audience_view_path: Incomplete
    parse_campaign_audience_view_path: Incomplete
    campaign_bid_modifier_path: Incomplete
    parse_campaign_bid_modifier_path: Incomplete
    campaign_budget_path: Incomplete
    parse_campaign_budget_path: Incomplete
    campaign_conversion_goal_path: Incomplete
    parse_campaign_conversion_goal_path: Incomplete
    campaign_criterion_path: Incomplete
    parse_campaign_criterion_path: Incomplete
    campaign_customizer_path: Incomplete
    parse_campaign_customizer_path: Incomplete
    campaign_draft_path: Incomplete
    parse_campaign_draft_path: Incomplete
    campaign_extension_setting_path: Incomplete
    parse_campaign_extension_setting_path: Incomplete
    campaign_feed_path: Incomplete
    parse_campaign_feed_path: Incomplete
    campaign_group_path: Incomplete
    parse_campaign_group_path: Incomplete
    campaign_label_path: Incomplete
    parse_campaign_label_path: Incomplete
    campaign_lifecycle_goal_path: Incomplete
    parse_campaign_lifecycle_goal_path: Incomplete
    campaign_search_term_insight_path: Incomplete
    parse_campaign_search_term_insight_path: Incomplete
    campaign_shared_set_path: Incomplete
    parse_campaign_shared_set_path: Incomplete
    campaign_simulation_path: Incomplete
    parse_campaign_simulation_path: Incomplete
    carrier_constant_path: Incomplete
    parse_carrier_constant_path: Incomplete
    change_event_path: Incomplete
    parse_change_event_path: Incomplete
    change_status_path: Incomplete
    parse_change_status_path: Incomplete
    channel_aggregate_asset_view_path: Incomplete
    parse_channel_aggregate_asset_view_path: Incomplete
    click_view_path: Incomplete
    parse_click_view_path: Incomplete
    combined_audience_path: Incomplete
    parse_combined_audience_path: Incomplete
    conversion_action_path: Incomplete
    parse_conversion_action_path: Incomplete
    conversion_custom_variable_path: Incomplete
    parse_conversion_custom_variable_path: Incomplete
    conversion_goal_campaign_config_path: Incomplete
    parse_conversion_goal_campaign_config_path: Incomplete
    conversion_value_rule_path: Incomplete
    parse_conversion_value_rule_path: Incomplete
    conversion_value_rule_set_path: Incomplete
    parse_conversion_value_rule_set_path: Incomplete
    currency_constant_path: Incomplete
    parse_currency_constant_path: Incomplete
    custom_audience_path: Incomplete
    parse_custom_audience_path: Incomplete
    custom_conversion_goal_path: Incomplete
    parse_custom_conversion_goal_path: Incomplete
    customer_path: Incomplete
    parse_customer_path: Incomplete
    customer_asset_path: Incomplete
    parse_customer_asset_path: Incomplete
    customer_asset_set_path: Incomplete
    parse_customer_asset_set_path: Incomplete
    customer_client_path: Incomplete
    parse_customer_client_path: Incomplete
    customer_client_link_path: Incomplete
    parse_customer_client_link_path: Incomplete
    customer_conversion_goal_path: Incomplete
    parse_customer_conversion_goal_path: Incomplete
    customer_customizer_path: Incomplete
    parse_customer_customizer_path: Incomplete
    customer_extension_setting_path: Incomplete
    parse_customer_extension_setting_path: Incomplete
    customer_feed_path: Incomplete
    parse_customer_feed_path: Incomplete
    customer_label_path: Incomplete
    parse_customer_label_path: Incomplete
    customer_lifecycle_goal_path: Incomplete
    parse_customer_lifecycle_goal_path: Incomplete
    customer_manager_link_path: Incomplete
    parse_customer_manager_link_path: Incomplete
    customer_negative_criterion_path: Incomplete
    parse_customer_negative_criterion_path: Incomplete
    customer_search_term_insight_path: Incomplete
    parse_customer_search_term_insight_path: Incomplete
    customer_user_access_path: Incomplete
    parse_customer_user_access_path: Incomplete
    customer_user_access_invitation_path: Incomplete
    parse_customer_user_access_invitation_path: Incomplete
    custom_interest_path: Incomplete
    parse_custom_interest_path: Incomplete
    customizer_attribute_path: Incomplete
    parse_customizer_attribute_path: Incomplete
    detailed_demographic_path: Incomplete
    parse_detailed_demographic_path: Incomplete
    detail_placement_view_path: Incomplete
    parse_detail_placement_view_path: Incomplete
    display_keyword_view_path: Incomplete
    parse_display_keyword_view_path: Incomplete
    distance_view_path: Incomplete
    parse_distance_view_path: Incomplete
    domain_category_path: Incomplete
    parse_domain_category_path: Incomplete
    dynamic_search_ads_search_term_view_path: Incomplete
    parse_dynamic_search_ads_search_term_view_path: Incomplete
    expanded_landing_page_view_path: Incomplete
    parse_expanded_landing_page_view_path: Incomplete
    experiment_path: Incomplete
    parse_experiment_path: Incomplete
    experiment_arm_path: Incomplete
    parse_experiment_arm_path: Incomplete
    extension_feed_item_path: Incomplete
    parse_extension_feed_item_path: Incomplete
    feed_path: Incomplete
    parse_feed_path: Incomplete
    feed_item_path: Incomplete
    parse_feed_item_path: Incomplete
    feed_item_set_path: Incomplete
    parse_feed_item_set_path: Incomplete
    feed_item_set_link_path: Incomplete
    parse_feed_item_set_link_path: Incomplete
    feed_item_target_path: Incomplete
    parse_feed_item_target_path: Incomplete
    feed_mapping_path: Incomplete
    parse_feed_mapping_path: Incomplete
    feed_placeholder_view_path: Incomplete
    parse_feed_placeholder_view_path: Incomplete
    gender_view_path: Incomplete
    parse_gender_view_path: Incomplete
    geographic_view_path: Incomplete
    parse_geographic_view_path: Incomplete
    geo_target_constant_path: Incomplete
    parse_geo_target_constant_path: Incomplete
    group_placement_view_path: Incomplete
    parse_group_placement_view_path: Incomplete
    hotel_group_view_path: Incomplete
    parse_hotel_group_view_path: Incomplete
    hotel_performance_view_path: Incomplete
    parse_hotel_performance_view_path: Incomplete
    hotel_reconciliation_path: Incomplete
    parse_hotel_reconciliation_path: Incomplete
    income_range_view_path: Incomplete
    parse_income_range_view_path: Incomplete
    keyword_plan_path: Incomplete
    parse_keyword_plan_path: Incomplete
    keyword_plan_ad_group_path: Incomplete
    parse_keyword_plan_ad_group_path: Incomplete
    keyword_plan_ad_group_keyword_path: Incomplete
    parse_keyword_plan_ad_group_keyword_path: Incomplete
    keyword_plan_campaign_path: Incomplete
    parse_keyword_plan_campaign_path: Incomplete
    keyword_plan_campaign_keyword_path: Incomplete
    parse_keyword_plan_campaign_keyword_path: Incomplete
    keyword_theme_constant_path: Incomplete
    parse_keyword_theme_constant_path: Incomplete
    keyword_view_path: Incomplete
    parse_keyword_view_path: Incomplete
    label_path: Incomplete
    parse_label_path: Incomplete
    landing_page_view_path: Incomplete
    parse_landing_page_view_path: Incomplete
    language_constant_path: Incomplete
    parse_language_constant_path: Incomplete
    lead_form_submission_data_path: Incomplete
    parse_lead_form_submission_data_path: Incomplete
    life_event_path: Incomplete
    parse_life_event_path: Incomplete
    local_services_employee_path: Incomplete
    parse_local_services_employee_path: Incomplete
    local_services_lead_path: Incomplete
    parse_local_services_lead_path: Incomplete
    local_services_lead_conversation_path: Incomplete
    parse_local_services_lead_conversation_path: Incomplete
    local_services_verification_artifact_path: Incomplete
    parse_local_services_verification_artifact_path: Incomplete
    location_view_path: Incomplete
    parse_location_view_path: Incomplete
    managed_placement_view_path: Incomplete
    parse_managed_placement_view_path: Incomplete
    media_file_path: Incomplete
    parse_media_file_path: Incomplete
    mobile_app_category_constant_path: Incomplete
    parse_mobile_app_category_constant_path: Incomplete
    mobile_device_constant_path: Incomplete
    parse_mobile_device_constant_path: Incomplete
    offline_conversion_upload_client_summary_path: Incomplete
    parse_offline_conversion_upload_client_summary_path: Incomplete
    offline_conversion_upload_conversion_action_summary_path: Incomplete
    parse_offline_conversion_upload_conversion_action_summary_path: Incomplete
    offline_user_data_job_path: Incomplete
    parse_offline_user_data_job_path: Incomplete
    operating_system_version_constant_path: Incomplete
    parse_operating_system_version_constant_path: Incomplete
    paid_organic_search_term_view_path: Incomplete
    parse_paid_organic_search_term_view_path: Incomplete
    parental_status_view_path: Incomplete
    parse_parental_status_view_path: Incomplete
    payments_account_path: Incomplete
    parse_payments_account_path: Incomplete
    per_store_view_path: Incomplete
    parse_per_store_view_path: Incomplete
    product_category_constant_path: Incomplete
    parse_product_category_constant_path: Incomplete
    product_group_view_path: Incomplete
    parse_product_group_view_path: Incomplete
    product_link_path: Incomplete
    parse_product_link_path: Incomplete
    product_link_invitation_path: Incomplete
    parse_product_link_invitation_path: Incomplete
    qualifying_question_path: Incomplete
    parse_qualifying_question_path: Incomplete
    recommendation_path: Incomplete
    parse_recommendation_path: Incomplete
    recommendation_subscription_path: Incomplete
    parse_recommendation_subscription_path: Incomplete
    remarketing_action_path: Incomplete
    parse_remarketing_action_path: Incomplete
    search_term_view_path: Incomplete
    parse_search_term_view_path: Incomplete
    shared_criterion_path: Incomplete
    parse_shared_criterion_path: Incomplete
    shared_set_path: Incomplete
    parse_shared_set_path: Incomplete
    shopping_performance_view_path: Incomplete
    parse_shopping_performance_view_path: Incomplete
    shopping_product_path: Incomplete
    parse_shopping_product_path: Incomplete
    smart_campaign_search_term_view_path: Incomplete
    parse_smart_campaign_search_term_view_path: Incomplete
    smart_campaign_setting_path: Incomplete
    parse_smart_campaign_setting_path: Incomplete
    third_party_app_analytics_link_path: Incomplete
    parse_third_party_app_analytics_link_path: Incomplete
    topic_constant_path: Incomplete
    parse_topic_constant_path: Incomplete
    topic_view_path: Incomplete
    parse_topic_view_path: Incomplete
    travel_activity_group_view_path: Incomplete
    parse_travel_activity_group_view_path: Incomplete
    travel_activity_performance_view_path: Incomplete
    parse_travel_activity_performance_view_path: Incomplete
    user_interest_path: Incomplete
    parse_user_interest_path: Incomplete
    user_list_path: Incomplete
    parse_user_list_path: Incomplete
    user_list_customer_type_path: Incomplete
    parse_user_list_customer_type_path: Incomplete
    user_location_view_path: Incomplete
    parse_user_location_view_path: Incomplete
    video_path: Incomplete
    parse_video_path: Incomplete
    webpage_view_path: Incomplete
    parse_webpage_view_path: Incomplete
    common_billing_account_path: Incomplete
    parse_common_billing_account_path: Incomplete
    common_folder_path: Incomplete
    parse_common_folder_path: Incomplete
    common_organization_path: Incomplete
    parse_common_organization_path: Incomplete
    common_project_path: Incomplete
    parse_common_project_path: Incomplete
    common_location_path: Incomplete
    parse_common_location_path: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: ClientOptions | None = None
    ): ...
    @property
    def transport(self) -> GoogleAdsServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str
        | GoogleAdsServiceTransport
        | Callable[..., GoogleAdsServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def search(
        self,
        request: google_ads_service.SearchGoogleAdsRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        query: str | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> pagers.SearchAsyncPager: ...
    def search_stream(
        self,
        request: google_ads_service.SearchGoogleAdsStreamRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        query: str | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> Awaitable[AsyncIterable[google_ads_service.SearchGoogleAdsStreamResponse]]: ...
    async def mutate(
        self,
        request: google_ads_service.MutateGoogleAdsRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        mutate_operations: MutableSequence[google_ads_service.MutateOperation]
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> google_ads_service.MutateGoogleAdsResponse: ...
    async def __aenter__(self) -> GoogleAdsServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
