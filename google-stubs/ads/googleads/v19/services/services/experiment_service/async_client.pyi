from .transports.base import ExperimentServiceTransport
from _typeshed import Incomplete
from google.ads.googleads.v19.services.services.experiment_service import pagers
from google.ads.googleads.v19.services.types import experiment_service
from google.api_core import gapic_v1, operation_async, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from typing import Callable, MutableSequence, Sequence

__all__ = ['ExperimentServiceAsyncClient']

class ExperimentServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    campaign_path: Incomplete
    parse_campaign_path: Incomplete
    campaign_budget_path: Incomplete
    parse_campaign_budget_path: Incomplete
    experiment_path: Incomplete
    parse_experiment_path: Incomplete
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
    def get_mtls_endpoint_and_cert_source(cls, client_options: ClientOptions | None = None): ...
    @property
    def transport(self) -> ExperimentServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(self, *, credentials: ga_credentials.Credentials | None = None, transport: str | ExperimentServiceTransport | Callable[..., ExperimentServiceTransport] | None = 'grpc_asyncio', client_options: ClientOptions | None = None, client_info: gapic_v1.client_info.ClientInfo = ...) -> None: ...
    async def mutate_experiments(self, request: experiment_service.MutateExperimentsRequest | dict | None = None, *, customer_id: str | None = None, operations: MutableSequence[experiment_service.ExperimentOperation] | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> experiment_service.MutateExperimentsResponse: ...
    async def end_experiment(self, request: experiment_service.EndExperimentRequest | dict | None = None, *, experiment: str | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> None: ...
    async def list_experiment_async_errors(self, request: experiment_service.ListExperimentAsyncErrorsRequest | dict | None = None, *, resource_name: str | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> pagers.ListExperimentAsyncErrorsAsyncPager: ...
    async def graduate_experiment(self, request: experiment_service.GraduateExperimentRequest | dict | None = None, *, experiment: str | None = None, campaign_budget_mappings: MutableSequence[experiment_service.CampaignBudgetMapping] | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> None: ...
    async def schedule_experiment(self, request: experiment_service.ScheduleExperimentRequest | dict | None = None, *, resource_name: str | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> operation_async.AsyncOperation: ...
    async def promote_experiment(self, request: experiment_service.PromoteExperimentRequest | dict | None = None, *, resource_name: str | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> operation_async.AsyncOperation: ...
    async def __aenter__(self) -> ExperimentServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
