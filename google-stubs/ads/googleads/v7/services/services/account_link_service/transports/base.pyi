import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import account_link
from google.ads.googleads.v7.services.types import account_link_service

class AccountLinkServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_account_link(
        self,
    ) -> typing.Callable[
        [account_link_service.GetAccountLinkRequest], account_link.AccountLink
    ]: ...
    @property
    def create_account_link(
        self,
    ) -> typing.Callable[
        [account_link_service.CreateAccountLinkRequest],
        account_link_service.CreateAccountLinkResponse,
    ]: ...
    @property
    def mutate_account_link(
        self,
    ) -> typing.Callable[
        [account_link_service.MutateAccountLinkRequest],
        account_link_service.MutateAccountLinkResponse,
    ]: ...
