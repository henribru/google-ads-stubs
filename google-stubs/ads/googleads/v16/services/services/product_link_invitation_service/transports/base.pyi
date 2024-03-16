import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v16.services.types import product_link_invitation_service

__all__ = ["ProductLinkInvitationServiceTransport"]

class ProductLinkInvitationServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        **kwargs,
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def create_product_link_invitation(
        self,
    ) -> Callable[
        [product_link_invitation_service.CreateProductLinkInvitationRequest],
        product_link_invitation_service.CreateProductLinkInvitationResponse
        | Awaitable[
            product_link_invitation_service.CreateProductLinkInvitationResponse
        ],
    ]: ...
    @property
    def update_product_link_invitation(
        self,
    ) -> Callable[
        [product_link_invitation_service.UpdateProductLinkInvitationRequest],
        product_link_invitation_service.UpdateProductLinkInvitationResponse
        | Awaitable[
            product_link_invitation_service.UpdateProductLinkInvitationResponse
        ],
    ]: ...
    @property
    def remove_product_link_invitation(
        self,
    ) -> Callable[
        [product_link_invitation_service.RemoveProductLinkInvitationRequest],
        product_link_invitation_service.RemoveProductLinkInvitationResponse
        | Awaitable[
            product_link_invitation_service.RemoveProductLinkInvitationResponse
        ],
    ]: ...
