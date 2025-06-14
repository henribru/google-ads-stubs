from .transports.base import CustomerServiceTransport
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import customer
from google.ads.googleads.v19.services.types import customer_service
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from typing import Callable, Sequence, Tuple

__all__ = ['CustomerServiceAsyncClient']

class CustomerServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    conversion_action_path: Incomplete
    parse_conversion_action_path: Incomplete
    customer_path: Incomplete
    parse_customer_path: Incomplete
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
    def transport(self) -> CustomerServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(self, *, credentials: ga_credentials.Credentials | None = None, transport: str | CustomerServiceTransport | Callable[..., CustomerServiceTransport] | None = 'grpc_asyncio', client_options: ClientOptions | None = None, client_info: gapic_v1.client_info.ClientInfo = ...) -> None: ...
    async def mutate_customer(self, request: customer_service.MutateCustomerRequest | dict | None = None, *, customer_id: str | None = None, operation: customer_service.CustomerOperation | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[Tuple[str, str | bytes]] = ()) -> customer_service.MutateCustomerResponse: ...
    async def list_accessible_customers(self, request: customer_service.ListAccessibleCustomersRequest | dict | None = None, *, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[Tuple[str, str | bytes]] = ()) -> customer_service.ListAccessibleCustomersResponse: ...
    async def create_customer_client(self, request: customer_service.CreateCustomerClientRequest | dict | None = None, *, customer_id: str | None = None, customer_client: customer.Customer | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[Tuple[str, str | bytes]] = ()) -> customer_service.CreateCustomerClientResponse: ...
    async def __aenter__(self) -> CustomerServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
