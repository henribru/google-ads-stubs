import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import conversion_action
from google.ads.googleads.v9.services.types import conversion_action_service

class ConversionActionServiceTransport(metaclass=abc.ABCMeta):
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
    def get_conversion_action(
        self,
    ) -> typing.Callable[
        [conversion_action_service.GetConversionActionRequest],
        conversion_action.ConversionAction,
    ]: ...
    @property
    def mutate_conversion_actions(
        self,
    ) -> typing.Callable[
        [conversion_action_service.MutateConversionActionsRequest],
        conversion_action_service.MutateConversionActionsResponse,
    ]: ...
