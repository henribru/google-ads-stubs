from google.ads.google_ads.v3.proto.services import (
    customer_feed_service_pb2_grpc as customer_feed_service_pb2_grpc,
)
from typing import Any, Optional

class CustomerFeedServiceGrpcTransport:
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
    def get_customer_feed(self): ...
    @property
    def mutate_customer_feeds(self): ...
