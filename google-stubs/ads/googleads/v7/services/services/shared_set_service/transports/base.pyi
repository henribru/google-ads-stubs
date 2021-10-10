import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import shared_set
from google.ads.googleads.v7.services.types import shared_set_service

class SharedSetServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_shared_set(
        self,
    ) -> typing.Callable[
        [shared_set_service.GetSharedSetRequest], shared_set.SharedSet
    ]: ...
    @property
    def mutate_shared_sets(
        self,
    ) -> typing.Callable[
        [shared_set_service.MutateSharedSetsRequest],
        shared_set_service.MutateSharedSetsResponse,
    ]: ...
