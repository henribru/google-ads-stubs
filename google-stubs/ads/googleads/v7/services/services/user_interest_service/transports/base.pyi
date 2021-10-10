import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import user_interest
from google.ads.googleads.v7.services.types import user_interest_service

class UserInterestServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_user_interest(
        self,
    ) -> typing.Callable[
        [user_interest_service.GetUserInterestRequest], user_interest.UserInterest
    ]: ...
