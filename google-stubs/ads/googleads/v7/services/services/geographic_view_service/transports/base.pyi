import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import geographic_view
from google.ads.googleads.v7.services.types import geographic_view_service

class GeographicViewServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_geographic_view(
        self,
    ) -> typing.Callable[
        [geographic_view_service.GetGeographicViewRequest],
        geographic_view.GeographicView,
    ]: ...
