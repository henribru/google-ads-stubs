import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.services.types import customer_conversion_goal_service

class CustomerConversionGoalServiceTransport(metaclass=abc.ABCMeta):
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
    def mutate_customer_conversion_goals(
        self,
    ) -> typing.Callable[
        [customer_conversion_goal_service.MutateCustomerConversionGoalsRequest],
        customer_conversion_goal_service.MutateCustomerConversionGoalsResponse,
    ]: ...
