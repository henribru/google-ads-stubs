import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.services.types import customizer_attribute_service

class CustomizerAttributeServiceTransport(metaclass=abc.ABCMeta):
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
    def mutate_customizer_attributes(
        self,
    ) -> typing.Callable[
        [customizer_attribute_service.MutateCustomizerAttributesRequest],
        customizer_attribute_service.MutateCustomizerAttributesResponse,
    ]: ...
