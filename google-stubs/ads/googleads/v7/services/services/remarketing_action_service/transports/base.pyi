import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import remarketing_action
from google.ads.googleads.v7.services.types import remarketing_action_service

class RemarketingActionServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_remarketing_action(
        self,
    ) -> typing.Callable[
        [remarketing_action_service.GetRemarketingActionRequest],
        remarketing_action.RemarketingAction,
    ]: ...
    @property
    def mutate_remarketing_actions(
        self,
    ) -> typing.Callable[
        [remarketing_action_service.MutateRemarketingActionsRequest],
        remarketing_action_service.MutateRemarketingActionsResponse,
    ]: ...
