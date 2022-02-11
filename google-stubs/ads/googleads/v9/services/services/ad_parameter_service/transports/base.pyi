import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import ad_parameter
from google.ads.googleads.v9.services.types import ad_parameter_service

class AdParameterServiceTransport(metaclass=abc.ABCMeta):
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
    def get_ad_parameter(
        self,
    ) -> typing.Callable[
        [ad_parameter_service.GetAdParameterRequest], ad_parameter.AdParameter
    ]: ...
    @property
    def mutate_ad_parameters(
        self,
    ) -> typing.Callable[
        [ad_parameter_service.MutateAdParametersRequest],
        ad_parameter_service.MutateAdParametersResponse,
    ]: ...
