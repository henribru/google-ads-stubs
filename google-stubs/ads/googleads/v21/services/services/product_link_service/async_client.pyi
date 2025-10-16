from typing import Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials

from google.ads.googleads.v21.resources.types import product_link as gagr_product_link
from google.ads.googleads.v21.services.types import product_link_service

from .transports.base import ProductLinkServiceTransport

__all__ = ["ProductLinkServiceAsyncClient"]

class ProductLinkServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    customer_path: Incomplete
    parse_customer_path: Incomplete
    product_link_path: Incomplete
    parse_product_link_path: Incomplete
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
    def transport(self) -> ProductLinkServiceTransport: ...
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
        | ProductLinkServiceTransport
        | Callable[..., ProductLinkServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def create_product_link(
        self,
        request: product_link_service.CreateProductLinkRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        product_link: gagr_product_link.ProductLink | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> product_link_service.CreateProductLinkResponse: ...
    async def remove_product_link(
        self,
        request: product_link_service.RemoveProductLinkRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        resource_name: str | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> product_link_service.RemoveProductLinkResponse: ...
    async def __aenter__(self) -> ProductLinkServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
