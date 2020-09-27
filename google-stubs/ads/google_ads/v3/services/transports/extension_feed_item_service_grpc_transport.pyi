from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    extension_feed_item_service_pb2_grpc as extension_feed_item_service_pb2_grpc,
)

class ExtensionFeedItemServiceGrpcTransport:
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
    def get_extension_feed_item(self): ...
    @property
    def mutate_extension_feed_items(self): ...
