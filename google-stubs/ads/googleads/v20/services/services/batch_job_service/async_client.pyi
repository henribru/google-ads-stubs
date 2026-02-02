from typing import Callable, MutableSequence, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1, operation_async, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.services.services.batch_job_service import pagers
from google.ads.googleads.v20.services.types import (
    batch_job_service,
    google_ads_service,
)

from .transports.base import BatchJobServiceTransport

__all__ = ["BatchJobServiceAsyncClient"]

class BatchJobServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    accessible_bidding_strategy_path: Incomplete
    parse_accessible_bidding_strategy_path: Incomplete
    ad_path: Incomplete
    parse_ad_path: Incomplete
    ad_group_path: Incomplete
    parse_ad_group_path: Incomplete
    ad_group_ad_path: Incomplete
    parse_ad_group_ad_path: Incomplete
    ad_group_ad_label_path: Incomplete
    parse_ad_group_ad_label_path: Incomplete
    ad_group_asset_path: Incomplete
    parse_ad_group_asset_path: Incomplete
    ad_group_bid_modifier_path: Incomplete
    parse_ad_group_bid_modifier_path: Incomplete
    ad_group_criterion_path: Incomplete
    parse_ad_group_criterion_path: Incomplete
    ad_group_criterion_customizer_path: Incomplete
    parse_ad_group_criterion_customizer_path: Incomplete
    ad_group_criterion_label_path: Incomplete
    parse_ad_group_criterion_label_path: Incomplete
    ad_group_customizer_path: Incomplete
    parse_ad_group_customizer_path: Incomplete
    ad_group_label_path: Incomplete
    parse_ad_group_label_path: Incomplete
    ad_parameter_path: Incomplete
    parse_ad_parameter_path: Incomplete
    asset_path: Incomplete
    parse_asset_path: Incomplete
    asset_group_path: Incomplete
    parse_asset_group_path: Incomplete
    asset_group_asset_path: Incomplete
    parse_asset_group_asset_path: Incomplete
    asset_group_listing_group_filter_path: Incomplete
    parse_asset_group_listing_group_filter_path: Incomplete
    asset_group_signal_path: Incomplete
    parse_asset_group_signal_path: Incomplete
    asset_set_path: Incomplete
    parse_asset_set_path: Incomplete
    asset_set_asset_path: Incomplete
    parse_asset_set_asset_path: Incomplete
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
    campaign_path: Incomplete
    parse_campaign_path: Incomplete
    campaign_asset_path: Incomplete
    parse_campaign_asset_path: Incomplete
    campaign_asset_set_path: Incomplete
    parse_campaign_asset_set_path: Incomplete
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
    campaign_group_path: Incomplete
    parse_campaign_group_path: Incomplete
    campaign_label_path: Incomplete
    parse_campaign_label_path: Incomplete
    campaign_shared_set_path: Incomplete
    parse_campaign_shared_set_path: Incomplete
    carrier_constant_path: Incomplete
    parse_carrier_constant_path: Incomplete
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
    custom_conversion_goal_path: Incomplete
    parse_custom_conversion_goal_path: Incomplete
    customer_path: Incomplete
    parse_customer_path: Incomplete
    customer_asset_path: Incomplete
    parse_customer_asset_path: Incomplete
    customer_conversion_goal_path: Incomplete
    parse_customer_conversion_goal_path: Incomplete
    customer_customizer_path: Incomplete
    parse_customer_customizer_path: Incomplete
    customer_label_path: Incomplete
    parse_customer_label_path: Incomplete
    customer_negative_criterion_path: Incomplete
    parse_customer_negative_criterion_path: Incomplete
    customizer_attribute_path: Incomplete
    parse_customizer_attribute_path: Incomplete
    detailed_demographic_path: Incomplete
    parse_detailed_demographic_path: Incomplete
    experiment_path: Incomplete
    parse_experiment_path: Incomplete
    experiment_arm_path: Incomplete
    parse_experiment_arm_path: Incomplete
    geo_target_constant_path: Incomplete
    parse_geo_target_constant_path: Incomplete
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
    label_path: Incomplete
    parse_label_path: Incomplete
    language_constant_path: Incomplete
    parse_language_constant_path: Incomplete
    life_event_path: Incomplete
    parse_life_event_path: Incomplete
    mobile_app_category_constant_path: Incomplete
    parse_mobile_app_category_constant_path: Incomplete
    mobile_device_constant_path: Incomplete
    parse_mobile_device_constant_path: Incomplete
    operating_system_version_constant_path: Incomplete
    parse_operating_system_version_constant_path: Incomplete
    recommendation_subscription_path: Incomplete
    parse_recommendation_subscription_path: Incomplete
    remarketing_action_path: Incomplete
    parse_remarketing_action_path: Incomplete
    shared_criterion_path: Incomplete
    parse_shared_criterion_path: Incomplete
    shared_set_path: Incomplete
    parse_shared_set_path: Incomplete
    smart_campaign_setting_path: Incomplete
    parse_smart_campaign_setting_path: Incomplete
    topic_constant_path: Incomplete
    parse_topic_constant_path: Incomplete
    user_interest_path: Incomplete
    parse_user_interest_path: Incomplete
    user_list_path: Incomplete
    parse_user_list_path: Incomplete
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
    def transport(self) -> BatchJobServiceTransport: ...
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
        | BatchJobServiceTransport
        | Callable[..., BatchJobServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def mutate_batch_job(
        self,
        request: batch_job_service.MutateBatchJobRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        operation: batch_job_service.BatchJobOperation | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> batch_job_service.MutateBatchJobResponse: ...
    async def list_batch_job_results(
        self,
        request: batch_job_service.ListBatchJobResultsRequest | dict | None = None,
        *,
        resource_name: str | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> pagers.ListBatchJobResultsAsyncPager: ...
    async def run_batch_job(
        self,
        request: batch_job_service.RunBatchJobRequest | dict | None = None,
        *,
        resource_name: str | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> operation_async.AsyncOperation: ...
    async def add_batch_job_operations(
        self,
        request: batch_job_service.AddBatchJobOperationsRequest | dict | None = None,
        *,
        resource_name: str | None = None,
        sequence_token: str | None = None,
        mutate_operations: MutableSequence[google_ads_service.MutateOperation]
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> batch_job_service.AddBatchJobOperationsResponse: ...
    async def __aenter__(self) -> BatchJobServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
