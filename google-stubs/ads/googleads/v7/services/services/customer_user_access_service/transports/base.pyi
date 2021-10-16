import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import customer_user_access
from google.ads.googleads.v7.services.types import customer_user_access_service

class CustomerUserAccessServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_customer_user_access(
        self,
    ) -> typing.Callable[
        [customer_user_access_service.GetCustomerUserAccessRequest],
        customer_user_access.CustomerUserAccess,
    ]: ...
    @property
    def mutate_customer_user_access(
        self,
    ) -> typing.Callable[
        [customer_user_access_service.MutateCustomerUserAccessRequest],
        customer_user_access_service.MutateCustomerUserAccessResponse,
    ]: ...
