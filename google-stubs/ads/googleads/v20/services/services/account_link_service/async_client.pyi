from typing import Callable, Sequence, Tuple

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.resources.types import account_link as gagr_account_link
from google.ads.googleads.v20.services.types import account_link_service

from .transports.base import AccountLinkServiceTransport

__all__ = ["AccountLinkServiceAsyncClient"]

class AccountLinkServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    account_link_path: Incomplete
    parse_account_link_path: Incomplete
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
    def transport(self) -> AccountLinkServiceTransport: ...
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
        | AccountLinkServiceTransport
        | Callable[..., AccountLinkServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def create_account_link(
        self,
        request: account_link_service.CreateAccountLinkRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        account_link: gagr_account_link.AccountLink | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> account_link_service.CreateAccountLinkResponse: ...
    async def mutate_account_link(
        self,
        request: account_link_service.MutateAccountLinkRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        operation: account_link_service.AccountLinkOperation | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> account_link_service.MutateAccountLinkResponse: ...
    async def __aenter__(self) -> AccountLinkServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
