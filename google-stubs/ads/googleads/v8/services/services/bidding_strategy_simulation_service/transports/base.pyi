import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import bidding_strategy_simulation
from google.ads.googleads.v8.services.types import bidding_strategy_simulation_service

class BiddingStrategySimulationServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_bidding_strategy_simulation(
        self,
    ) -> typing.Callable[
        [bidding_strategy_simulation_service.GetBiddingStrategySimulationRequest],
        bidding_strategy_simulation.BiddingStrategySimulation,
    ]: ...