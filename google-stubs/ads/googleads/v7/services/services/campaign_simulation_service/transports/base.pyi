import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import campaign_simulation
from google.ads.googleads.v7.services.types import campaign_simulation_service

class CampaignSimulationServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_campaign_simulation(
        self,
    ) -> typing.Callable[
        [campaign_simulation_service.GetCampaignSimulationRequest],
        campaign_simulation.CampaignSimulation,
    ]: ...