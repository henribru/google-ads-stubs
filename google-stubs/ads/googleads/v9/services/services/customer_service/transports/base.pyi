import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import customer
from google.ads.googleads.v9.services.types import customer_service

class CustomerServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def get_customer(
        self,
    ) -> typing.Callable[[customer_service.GetCustomerRequest], customer.Customer]: ...
    @property
    def mutate_customer(
        self,
    ) -> typing.Callable[
        [customer_service.MutateCustomerRequest],
        customer_service.MutateCustomerResponse,
    ]: ...
    @property
    def list_accessible_customers(
        self,
    ) -> typing.Callable[
        [customer_service.ListAccessibleCustomersRequest],
        customer_service.ListAccessibleCustomersResponse,
    ]: ...
    @property
    def create_customer_client(
        self,
    ) -> typing.Callable[
        [customer_service.CreateCustomerClientRequest],
        customer_service.CreateCustomerClientResponse,
    ]: ...
