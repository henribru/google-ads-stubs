from .transports.base import OfflineUserDataJobServiceTransport
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import offline_user_data_job
from google.ads.googleads.v18.services.types import offline_user_data_job_service
from google.api_core import gapic_v1, operation_async, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from typing import Callable, MutableSequence, Sequence, Tuple

__all__ = ['OfflineUserDataJobServiceAsyncClient']

class OfflineUserDataJobServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    offline_user_data_job_path: Incomplete
    parse_offline_user_data_job_path: Incomplete
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
    def transport(self) -> OfflineUserDataJobServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(self, *, credentials: ga_credentials.Credentials | None = None, transport: str | OfflineUserDataJobServiceTransport | Callable[..., OfflineUserDataJobServiceTransport] | None = 'grpc_asyncio', client_options: ClientOptions | None = None, client_info: gapic_v1.client_info.ClientInfo = ...) -> None: ...
    async def create_offline_user_data_job(self, request: offline_user_data_job_service.CreateOfflineUserDataJobRequest | dict | None = None, *, customer_id: str | None = None, job: offline_user_data_job.OfflineUserDataJob | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[Tuple[str, str | bytes]] = ()) -> offline_user_data_job_service.CreateOfflineUserDataJobResponse: ...
    async def add_offline_user_data_job_operations(self, request: offline_user_data_job_service.AddOfflineUserDataJobOperationsRequest | dict | None = None, *, resource_name: str | None = None, operations: MutableSequence[offline_user_data_job_service.OfflineUserDataJobOperation] | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[Tuple[str, str | bytes]] = ()) -> offline_user_data_job_service.AddOfflineUserDataJobOperationsResponse: ...
    async def run_offline_user_data_job(self, request: offline_user_data_job_service.RunOfflineUserDataJobRequest | dict | None = None, *, resource_name: str | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[Tuple[str, str | bytes]] = ()) -> operation_async.AsyncOperation: ...
    async def __aenter__(self) -> OfflineUserDataJobServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
