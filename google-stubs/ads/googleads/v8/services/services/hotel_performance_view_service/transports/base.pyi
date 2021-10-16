import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import hotel_performance_view
from google.ads.googleads.v8.services.types import hotel_performance_view_service

class HotelPerformanceViewServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_hotel_performance_view(
        self,
    ) -> typing.Callable[
        [hotel_performance_view_service.GetHotelPerformanceViewRequest],
        hotel_performance_view.HotelPerformanceView,
    ]: ...
