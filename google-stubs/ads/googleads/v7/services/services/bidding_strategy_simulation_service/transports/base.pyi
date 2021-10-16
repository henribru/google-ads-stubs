import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import bidding_strategy_simulation
from google.ads.googleads.v7.services.types import bidding_strategy_simulation_service

class BiddingStrategySimulationServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_bidding_strategy_simulation(
        self,
    ) -> typing.Callable[
        [bidding_strategy_simulation_service.GetBiddingStrategySimulationRequest],
        bidding_strategy_simulation.BiddingStrategySimulation,
    ]: ...
