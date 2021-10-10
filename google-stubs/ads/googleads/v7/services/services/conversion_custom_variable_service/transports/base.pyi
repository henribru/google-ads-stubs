import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import conversion_custom_variable
from google.ads.googleads.v7.services.types import conversion_custom_variable_service

class ConversionCustomVariableServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_conversion_custom_variable(
        self,
    ) -> typing.Callable[
        [conversion_custom_variable_service.GetConversionCustomVariableRequest],
        conversion_custom_variable.ConversionCustomVariable,
    ]: ...
    @property
    def mutate_conversion_custom_variables(
        self,
    ) -> typing.Callable[
        [conversion_custom_variable_service.MutateConversionCustomVariablesRequest],
        conversion_custom_variable_service.MutateConversionCustomVariablesResponse,
    ]: ...
