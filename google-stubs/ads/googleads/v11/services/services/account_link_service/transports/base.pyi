import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v11.services.types import account_link_service

class AccountLinkServiceTransport(abc.ABC):
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
    def create_account_link(
        self,
    ) -> Callable[
        [account_link_service.CreateAccountLinkRequest],
        Union[
            account_link_service.CreateAccountLinkResponse,
            Awaitable[account_link_service.CreateAccountLinkResponse],
        ],
    ]: ...
    @property
    def mutate_account_link(
        self,
    ) -> Callable[
        [account_link_service.MutateAccountLinkRequest],
        Union[
            account_link_service.MutateAccountLinkResponse,
            Awaitable[account_link_service.MutateAccountLinkResponse],
        ],
    ]: ...
