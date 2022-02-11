import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import bidding_seasonality_adjustment
from google.ads.googleads.v9.services.types import (
    bidding_seasonality_adjustment_service,
)

class BiddingSeasonalityAdjustmentServiceTransport(metaclass=abc.ABCMeta):
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
    def get_bidding_seasonality_adjustment(
        self,
    ) -> typing.Callable[
        [bidding_seasonality_adjustment_service.GetBiddingSeasonalityAdjustmentRequest],
        bidding_seasonality_adjustment.BiddingSeasonalityAdjustment,
    ]: ...
    @property
    def mutate_bidding_seasonality_adjustments(
        self,
    ) -> typing.Callable[
        [
            bidding_seasonality_adjustment_service.MutateBiddingSeasonalityAdjustmentsRequest
        ],
        bidding_seasonality_adjustment_service.MutateBiddingSeasonalityAdjustmentsResponse,
    ]: ...
