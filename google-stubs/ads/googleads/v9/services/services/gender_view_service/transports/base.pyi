import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import gender_view
from google.ads.googleads.v9.services.types import gender_view_service

class GenderViewServiceTransport(metaclass=abc.ABCMeta):
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
    def get_gender_view(
        self,
    ) -> typing.Callable[
        [gender_view_service.GetGenderViewRequest], gender_view.GenderView
    ]: ...
