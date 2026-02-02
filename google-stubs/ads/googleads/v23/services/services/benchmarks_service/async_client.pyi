from typing import Callable, MutableSequence, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials

from google.ads.googleads.v23.common.types import criteria
from google.ads.googleads.v23.enums.types import benchmarks_source_type
from google.ads.googleads.v23.services.types import benchmarks_service

from .transports.base import BenchmarksServiceTransport

__all__ = ["BenchmarksServiceAsyncClient"]

class BenchmarksServiceAsyncClient:
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
    def transport(self) -> BenchmarksServiceTransport: ...
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
        | BenchmarksServiceTransport
        | Callable[..., BenchmarksServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def list_benchmarks_available_dates(
        self,
        request: benchmarks_service.ListBenchmarksAvailableDatesRequest
        | dict
        | None = None,
        *,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> benchmarks_service.ListBenchmarksAvailableDatesResponse: ...
    async def list_benchmarks_locations(
        self,
        request: benchmarks_service.ListBenchmarksLocationsRequest | dict | None = None,
        *,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> benchmarks_service.ListBenchmarksLocationsResponse: ...
    async def list_benchmarks_products(
        self,
        request: benchmarks_service.ListBenchmarksProductsRequest | dict | None = None,
        *,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> benchmarks_service.ListBenchmarksProductsResponse: ...
    async def list_benchmarks_sources(
        self,
        request: benchmarks_service.ListBenchmarksSourcesRequest | dict | None = None,
        *,
        benchmarks_sources: MutableSequence[
            benchmarks_source_type.BenchmarksSourceTypeEnum.BenchmarksSourceType
        ]
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> benchmarks_service.ListBenchmarksSourcesResponse: ...
    async def generate_benchmarks_metrics(
        self,
        request: benchmarks_service.GenerateBenchmarksMetricsRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        location: criteria.LocationInfo | None = None,
        benchmarks_source: benchmarks_service.BenchmarksSource | None = None,
        product_filter: benchmarks_service.ProductFilter | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> benchmarks_service.GenerateBenchmarksMetricsResponse: ...
    async def __aenter__(self) -> BenchmarksServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
