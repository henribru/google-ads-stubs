import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import customer_client_link
from google.ads.googleads.v7.services.types import customer_client_link_service

class CustomerClientLinkServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_customer_client_link(
        self,
    ) -> typing.Callable[
        [customer_client_link_service.GetCustomerClientLinkRequest],
        customer_client_link.CustomerClientLink,
    ]: ...
    @property
    def mutate_customer_client_link(
        self,
    ) -> typing.Callable[
        [customer_client_link_service.MutateCustomerClientLinkRequest],
        customer_client_link_service.MutateCustomerClientLinkResponse,
    ]: ...
