import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import custom_interest
from google.ads.googleads.v8.services.types import custom_interest_service

class CustomInterestServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_custom_interest(
        self,
    ) -> typing.Callable[
        [custom_interest_service.GetCustomInterestRequest],
        custom_interest.CustomInterest,
    ]: ...
    @property
    def mutate_custom_interests(
        self,
    ) -> typing.Callable[
        [custom_interest_service.MutateCustomInterestsRequest],
        custom_interest_service.MutateCustomInterestsResponse,
    ]: ...
