from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    feed_item_service_pb2_grpc as feed_item_service_pb2_grpc,
)

class FeedItemServiceGrpcTransport:
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
    def get_feed_item(self): ...
    @property
    def mutate_feed_items(self): ...
