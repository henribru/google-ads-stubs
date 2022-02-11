import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.services.types import customer_customizer_service

class CustomerCustomizerServiceTransport(metaclass=abc.ABCMeta):
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
    def mutate_customer_customizers(
        self,
    ) -> typing.Callable[
        [customer_customizer_service.MutateCustomerCustomizersRequest],
        customer_customizer_service.MutateCustomerCustomizersResponse,
    ]: ...
