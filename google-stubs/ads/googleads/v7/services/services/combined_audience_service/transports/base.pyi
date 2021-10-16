import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import combined_audience
from google.ads.googleads.v7.services.types import combined_audience_service

class CombinedAudienceServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_combined_audience(
        self,
    ) -> typing.Callable[
        [combined_audience_service.GetCombinedAudienceRequest],
        combined_audience.CombinedAudience,
    ]: ...
