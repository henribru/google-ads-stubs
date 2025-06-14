from .transports.base import RemarketingActionServiceTransport
from _typeshed import Incomplete
from google.ads.googleads.v18.services.types import remarketing_action_service
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from typing import Callable, MutableSequence, Sequence, Tuple

__all__ = ['RemarketingActionServiceAsyncClient']

class RemarketingActionServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    remarketing_action_path: Incomplete
    parse_remarketing_action_path: Incomplete
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
    def transport(self) -> RemarketingActionServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(self, *, credentials: ga_credentials.Credentials | None = None, transport: str | RemarketingActionServiceTransport | Callable[..., RemarketingActionServiceTransport] | None = 'grpc_asyncio', client_options: ClientOptions | None = None, client_info: gapic_v1.client_info.ClientInfo = ...) -> None: ...
    async def mutate_remarketing_actions(self, request: remarketing_action_service.MutateRemarketingActionsRequest | dict | None = None, *, customer_id: str | None = None, operations: MutableSequence[remarketing_action_service.RemarketingActionOperation] | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[Tuple[str, str | bytes]] = ()) -> remarketing_action_service.MutateRemarketingActionsResponse: ...
    async def __aenter__(self) -> RemarketingActionServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
