from google.ads.google_ads.v3.proto.services import (
    topic_view_service_pb2_grpc as topic_view_service_pb2_grpc,
)
from typing import Any, Optional

class TopicViewServiceGrpcTransport:
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
    def get_topic_view(self): ...
