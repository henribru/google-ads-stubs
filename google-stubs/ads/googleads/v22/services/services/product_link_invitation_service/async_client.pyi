from .transports.base import ProductLinkInvitationServiceTransport
from _typeshed import Incomplete
from google.ads.googleads.v22.enums.types import product_link_invitation_status as gage_product_link_invitation_status
from google.ads.googleads.v22.resources.types import product_link_invitation as gagr_product_link_invitation
from google.ads.googleads.v22.services.types import product_link_invitation_service
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from typing import Callable, Sequence

__all__ = ['ProductLinkInvitationServiceAsyncClient']

class ProductLinkInvitationServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    customer_path: Incomplete
    parse_customer_path: Incomplete
    product_link_invitation_path: Incomplete
    parse_product_link_invitation_path: Incomplete
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
    def transport(self) -> ProductLinkInvitationServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(self, *, credentials: ga_credentials.Credentials | None = None, transport: str | ProductLinkInvitationServiceTransport | Callable[..., ProductLinkInvitationServiceTransport] | None = 'grpc_asyncio', client_options: ClientOptions | None = None, client_info: gapic_v1.client_info.ClientInfo = ...) -> None: ...
    async def create_product_link_invitation(self, request: product_link_invitation_service.CreateProductLinkInvitationRequest | dict | None = None, *, customer_id: str | None = None, product_link_invitation: gagr_product_link_invitation.ProductLinkInvitation | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> product_link_invitation_service.CreateProductLinkInvitationResponse: ...
    async def update_product_link_invitation(self, request: product_link_invitation_service.UpdateProductLinkInvitationRequest | dict | None = None, *, customer_id: str | None = None, product_link_invitation_status: gage_product_link_invitation_status.ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus | None = None, resource_name: str | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> product_link_invitation_service.UpdateProductLinkInvitationResponse: ...
    async def remove_product_link_invitation(self, request: product_link_invitation_service.RemoveProductLinkInvitationRequest | dict | None = None, *, customer_id: str | None = None, resource_name: str | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> product_link_invitation_service.RemoveProductLinkInvitationResponse: ...
    async def __aenter__(self) -> ProductLinkInvitationServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
