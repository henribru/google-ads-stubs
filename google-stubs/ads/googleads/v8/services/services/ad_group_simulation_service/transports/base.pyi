import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import ad_group_simulation
from google.ads.googleads.v8.services.types import ad_group_simulation_service

class AdGroupSimulationServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_ad_group_simulation(
        self,
    ) -> typing.Callable[
        [ad_group_simulation_service.GetAdGroupSimulationRequest],
        ad_group_simulation.AdGroupSimulation,
    ]: ...
