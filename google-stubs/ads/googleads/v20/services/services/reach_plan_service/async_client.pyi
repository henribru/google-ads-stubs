from typing import Callable, MutableSequence, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.services.types import reach_plan_service

from .transports.base import ReachPlanServiceTransport

__all__ = ["ReachPlanServiceAsyncClient"]

class ReachPlanServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
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
    def transport(self) -> ReachPlanServiceTransport: ...
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
        | ReachPlanServiceTransport
        | Callable[..., ReachPlanServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def generate_conversion_rates(
        self,
        request: reach_plan_service.GenerateConversionRatesRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> reach_plan_service.GenerateConversionRatesResponse: ...
    async def list_plannable_locations(
        self,
        request: reach_plan_service.ListPlannableLocationsRequest | dict | None = None,
        *,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> reach_plan_service.ListPlannableLocationsResponse: ...
    async def list_plannable_products(
        self,
        request: reach_plan_service.ListPlannableProductsRequest | dict | None = None,
        *,
        plannable_location_id: str | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> reach_plan_service.ListPlannableProductsResponse: ...
    async def generate_reach_forecast(
        self,
        request: reach_plan_service.GenerateReachForecastRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        campaign_duration: reach_plan_service.CampaignDuration | None = None,
        planned_products: MutableSequence[reach_plan_service.PlannedProduct]
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> reach_plan_service.GenerateReachForecastResponse: ...
    async def list_plannable_user_lists(
        self,
        request: reach_plan_service.ListPlannableUserListsRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> reach_plan_service.ListPlannableUserListsResponse: ...
    async def __aenter__(self) -> ReachPlanServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
