from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    shared_set_service_pb2_grpc as shared_set_service_pb2_grpc,
)

class SharedSetServiceGrpcTransport:
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
    def get_shared_set(self): ...
    @property
    def mutate_shared_sets(self): ...
