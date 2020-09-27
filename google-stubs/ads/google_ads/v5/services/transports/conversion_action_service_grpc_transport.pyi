from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    conversion_action_service_pb2_grpc as conversion_action_service_pb2_grpc,
)

class ConversionActionServiceGrpcTransport:
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
    def get_conversion_action(self): ...
    @property
    def mutate_conversion_actions(self): ...
