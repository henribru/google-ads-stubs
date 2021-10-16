import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import accessible_bidding_strategy
from google.ads.googleads.v8.services.types import accessible_bidding_strategy_service

class AccessibleBiddingStrategyServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_accessible_bidding_strategy(
        self,
    ) -> typing.Callable[
        [accessible_bidding_strategy_service.GetAccessibleBiddingStrategyRequest],
        accessible_bidding_strategy.AccessibleBiddingStrategy,
    ]: ...
