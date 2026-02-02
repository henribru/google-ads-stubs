from typing import Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials

from google.ads.googleads.v23.services.types import (
    customer_sk_ad_network_conversion_value_schema_service,
)

from .transports.base import CustomerSkAdNetworkConversionValueSchemaServiceTransport

__all__ = ["CustomerSkAdNetworkConversionValueSchemaServiceAsyncClient"]

class CustomerSkAdNetworkConversionValueSchemaServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    customer_sk_ad_network_conversion_value_schema_path: Incomplete
    parse_customer_sk_ad_network_conversion_value_schema_path: Incomplete
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
    def transport(self) -> CustomerSkAdNetworkConversionValueSchemaServiceTransport: ...
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
        | CustomerSkAdNetworkConversionValueSchemaServiceTransport
        | Callable[..., CustomerSkAdNetworkConversionValueSchemaServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def mutate_customer_sk_ad_network_conversion_value_schema(
        self,
        request: customer_sk_ad_network_conversion_value_schema_service.MutateCustomerSkAdNetworkConversionValueSchemaRequest
        | dict
        | None = None,
        *,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> customer_sk_ad_network_conversion_value_schema_service.MutateCustomerSkAdNetworkConversionValueSchemaResponse: ...
    async def __aenter__(
        self,
    ) -> CustomerSkAdNetworkConversionValueSchemaServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
