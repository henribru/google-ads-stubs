import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import parental_status_view
from google.ads.googleads.v8.services.types import parental_status_view_service

class ParentalStatusViewServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_parental_status_view(
        self,
    ) -> typing.Callable[
        [parental_status_view_service.GetParentalStatusViewRequest],
        parental_status_view.ParentalStatusView,
    ]: ...
