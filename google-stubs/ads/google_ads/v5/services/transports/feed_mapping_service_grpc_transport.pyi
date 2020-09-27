from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    feed_mapping_service_pb2_grpc as feed_mapping_service_pb2_grpc,
)

class FeedMappingServiceGrpcTransport:
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
    def get_feed_mapping(self): ...
    @property
    def mutate_feed_mappings(self): ...
