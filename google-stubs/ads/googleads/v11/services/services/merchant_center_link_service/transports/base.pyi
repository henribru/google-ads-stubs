import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v11.resources.types import merchant_center_link
from google.ads.googleads.v11.services.types import merchant_center_link_service

class MerchantCenterLinkServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def list_merchant_center_links(
        self,
    ) -> Callable[
        [merchant_center_link_service.ListMerchantCenterLinksRequest],
        Union[
            merchant_center_link_service.ListMerchantCenterLinksResponse,
            Awaitable[merchant_center_link_service.ListMerchantCenterLinksResponse],
        ],
    ]: ...
    @property
    def get_merchant_center_link(
        self,
    ) -> Callable[
        [merchant_center_link_service.GetMerchantCenterLinkRequest],
        Union[
            merchant_center_link.MerchantCenterLink,
            Awaitable[merchant_center_link.MerchantCenterLink],
        ],
    ]: ...
    @property
    def mutate_merchant_center_link(
        self,
    ) -> Callable[
        [merchant_center_link_service.MutateMerchantCenterLinkRequest],
        Union[
            merchant_center_link_service.MutateMerchantCenterLinkResponse,
            Awaitable[merchant_center_link_service.MutateMerchantCenterLinkResponse],
        ],
    ]: ...
