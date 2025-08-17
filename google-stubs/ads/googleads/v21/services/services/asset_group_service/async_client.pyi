from .transports.base import AssetGroupServiceTransport
from _typeshed import Incomplete
from google.ads.googleads.v21.services.types import asset_group_service
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from typing import Callable, MutableSequence, Sequence

__all__ = ['AssetGroupServiceAsyncClient']

class AssetGroupServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    asset_group_path: Incomplete
    parse_asset_group_path: Incomplete
    campaign_path: Incomplete
    parse_campaign_path: Incomplete
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
    def transport(self) -> AssetGroupServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(self, *, credentials: ga_credentials.Credentials | None = None, transport: str | AssetGroupServiceTransport | Callable[..., AssetGroupServiceTransport] | None = 'grpc_asyncio', client_options: ClientOptions | None = None, client_info: gapic_v1.client_info.ClientInfo = ...) -> None: ...
    async def mutate_asset_groups(self, request: asset_group_service.MutateAssetGroupsRequest | dict | None = None, *, customer_id: str | None = None, operations: MutableSequence[asset_group_service.AssetGroupOperation] | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> asset_group_service.MutateAssetGroupsResponse: ...
    async def __aenter__(self) -> AssetGroupServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
