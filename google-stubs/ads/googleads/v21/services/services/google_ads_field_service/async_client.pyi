from .transports.base import GoogleAdsFieldServiceTransport
from _typeshed import Incomplete
from google.ads.googleads.v21.resources.types import google_ads_field
from google.ads.googleads.v21.services.services.google_ads_field_service import pagers
from google.ads.googleads.v21.services.types import google_ads_field_service
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from typing import Callable, Sequence

__all__ = ['GoogleAdsFieldServiceAsyncClient']

class GoogleAdsFieldServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    google_ads_field_path: Incomplete
    parse_google_ads_field_path: Incomplete
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
    def transport(self) -> GoogleAdsFieldServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(self, *, credentials: ga_credentials.Credentials | None = None, transport: str | GoogleAdsFieldServiceTransport | Callable[..., GoogleAdsFieldServiceTransport] | None = 'grpc_asyncio', client_options: ClientOptions | None = None, client_info: gapic_v1.client_info.ClientInfo = ...) -> None: ...
    async def get_google_ads_field(self, request: google_ads_field_service.GetGoogleAdsFieldRequest | dict | None = None, *, resource_name: str | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> google_ads_field.GoogleAdsField: ...
    async def search_google_ads_fields(self, request: google_ads_field_service.SearchGoogleAdsFieldsRequest | dict | None = None, *, query: str | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> pagers.SearchGoogleAdsFieldsAsyncPager: ...
    async def __aenter__(self) -> GoogleAdsFieldServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
