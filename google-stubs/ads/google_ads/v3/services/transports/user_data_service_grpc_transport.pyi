from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    user_data_service_pb2_grpc as user_data_service_pb2_grpc,
)

class UserDataServiceGrpcTransport:
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
    def upload_user_data(self): ...
