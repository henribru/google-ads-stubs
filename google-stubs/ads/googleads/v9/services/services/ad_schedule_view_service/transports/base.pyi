import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import ad_schedule_view
from google.ads.googleads.v9.services.types import ad_schedule_view_service

class AdScheduleViewServiceTransport(metaclass=abc.ABCMeta):
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
    def get_ad_schedule_view(
        self,
    ) -> typing.Callable[
        [ad_schedule_view_service.GetAdScheduleViewRequest],
        ad_schedule_view.AdScheduleView,
    ]: ...
