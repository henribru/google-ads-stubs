import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import bidding_strategy
from google.ads.googleads.v7.services.types import bidding_strategy_service

class BiddingStrategyServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_bidding_strategy(
        self,
    ) -> typing.Callable[
        [bidding_strategy_service.GetBiddingStrategyRequest],
        bidding_strategy.BiddingStrategy,
    ]: ...
    @property
    def mutate_bidding_strategies(
        self,
    ) -> typing.Callable[
        [bidding_strategy_service.MutateBiddingStrategiesRequest],
        bidding_strategy_service.MutateBiddingStrategiesResponse,
    ]: ...
