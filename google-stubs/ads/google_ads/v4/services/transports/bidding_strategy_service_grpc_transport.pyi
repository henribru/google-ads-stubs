from typing import Any, Optional

from google.ads.google_ads.v4.proto.services import (
    bidding_strategy_service_pb2_grpc as bidding_strategy_service_pb2_grpc,
)

class BiddingStrategyServiceGrpcTransport:
    def __init__(
        self,
        channel: Optional[Any] = ...,
        credentials: Optional[Any] = ...,
        address: str = ...,
    ) -> None: ...
    @classmethod
    def create_channel(
        cls, address: str = ..., credentials: Optional[Any] = ..., **kwargs: Any
    ): ...
    @property
    def channel(self): ...
    @property
    def get_bidding_strategy(self): ...
    @property
    def mutate_bidding_strategies(self): ...
