import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import bidding_data_exclusion
from google.ads.googleads.v9.services.types import bidding_data_exclusion_service

class BiddingDataExclusionServiceTransport(metaclass=abc.ABCMeta):
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
    def get_bidding_data_exclusion(
        self,
    ) -> typing.Callable[
        [bidding_data_exclusion_service.GetBiddingDataExclusionRequest],
        bidding_data_exclusion.BiddingDataExclusion,
    ]: ...
    @property
    def mutate_bidding_data_exclusions(
        self,
    ) -> typing.Callable[
        [bidding_data_exclusion_service.MutateBiddingDataExclusionsRequest],
        bidding_data_exclusion_service.MutateBiddingDataExclusionsResponse,
    ]: ...
