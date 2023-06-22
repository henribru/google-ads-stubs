import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.types import product_link_service

class ProductLinkServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: Optional[ga_credentials.Credentials] = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def create_product_link(
        self,
    ) -> Callable[
        [product_link_service.CreateProductLinkRequest],
        Union[
            product_link_service.CreateProductLinkResponse,
            Awaitable[product_link_service.CreateProductLinkResponse],
        ],
    ]: ...
    @property
    def remove_product_link(
        self,
    ) -> Callable[
        [product_link_service.RemoveProductLinkRequest],
        Union[
            product_link_service.RemoveProductLinkResponse,
            Awaitable[product_link_service.RemoveProductLinkResponse],
        ],
    ]: ...
