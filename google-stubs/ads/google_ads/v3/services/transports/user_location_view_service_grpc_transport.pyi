from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    user_location_view_service_pb2_grpc as user_location_view_service_pb2_grpc,
)

class UserLocationViewServiceGrpcTransport:
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
    def get_user_location_view(self): ...
