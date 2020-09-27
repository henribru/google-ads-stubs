from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    feed_service_pb2_grpc as feed_service_pb2_grpc,
)

class FeedServiceGrpcTransport:
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
    def get_feed(self): ...
    @property
    def mutate_feeds(self): ...
