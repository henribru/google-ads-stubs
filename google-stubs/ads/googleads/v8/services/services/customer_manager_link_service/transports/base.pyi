import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import customer_manager_link
from google.ads.googleads.v8.services.types import customer_manager_link_service

class CustomerManagerLinkServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_customer_manager_link(
        self,
    ) -> typing.Callable[
        [customer_manager_link_service.GetCustomerManagerLinkRequest],
        customer_manager_link.CustomerManagerLink,
    ]: ...
    @property
    def mutate_customer_manager_link(
        self,
    ) -> typing.Callable[
        [customer_manager_link_service.MutateCustomerManagerLinkRequest],
        customer_manager_link_service.MutateCustomerManagerLinkResponse,
    ]: ...
    @property
    def move_manager_link(
        self,
    ) -> typing.Callable[
        [customer_manager_link_service.MoveManagerLinkRequest],
        customer_manager_link_service.MoveManagerLinkResponse,
    ]: ...
