import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.resources.types import merchant_center_link
from google.ads.googleads.v14.services.types import merchant_center_link_service

__all__ = ["MerchantCenterLinkServiceTransport"]

class MerchantCenterLinkServiceTransport(abc.ABC):
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
    def list_merchant_center_links(
        self,
    ) -> Callable[
        [merchant_center_link_service.ListMerchantCenterLinksRequest],
        merchant_center_link_service.ListMerchantCenterLinksResponse
        | Awaitable[merchant_center_link_service.ListMerchantCenterLinksResponse],
    ]: ...
    @property
    def get_merchant_center_link(
        self,
    ) -> Callable[
        [merchant_center_link_service.GetMerchantCenterLinkRequest],
        merchant_center_link.MerchantCenterLink
        | Awaitable[merchant_center_link.MerchantCenterLink],
    ]: ...
    @property
    def mutate_merchant_center_link(
        self,
    ) -> Callable[
        [merchant_center_link_service.MutateMerchantCenterLinkRequest],
        merchant_center_link_service.MutateMerchantCenterLinkResponse
        | Awaitable[merchant_center_link_service.MutateMerchantCenterLinkResponse],
    ]: ...
