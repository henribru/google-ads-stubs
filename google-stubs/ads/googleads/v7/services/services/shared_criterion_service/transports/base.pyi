import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import shared_criterion
from google.ads.googleads.v7.services.types import shared_criterion_service

class SharedCriterionServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_shared_criterion(
        self,
    ) -> typing.Callable[
        [shared_criterion_service.GetSharedCriterionRequest],
        shared_criterion.SharedCriterion,
    ]: ...
    @property
    def mutate_shared_criteria(
        self,
    ) -> typing.Callable[
        [shared_criterion_service.MutateSharedCriteriaRequest],
        shared_criterion_service.MutateSharedCriteriaResponse,
    ]: ...
