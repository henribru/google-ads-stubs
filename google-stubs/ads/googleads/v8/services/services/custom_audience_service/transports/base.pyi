import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import custom_audience
from google.ads.googleads.v8.services.types import custom_audience_service

class CustomAudienceServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_custom_audience(
        self,
    ) -> typing.Callable[
        [custom_audience_service.GetCustomAudienceRequest],
        custom_audience.CustomAudience,
    ]: ...
    @property
    def mutate_custom_audiences(
        self,
    ) -> typing.Callable[
        [custom_audience_service.MutateCustomAudiencesRequest],
        custom_audience_service.MutateCustomAudiencesResponse,
    ]: ...
