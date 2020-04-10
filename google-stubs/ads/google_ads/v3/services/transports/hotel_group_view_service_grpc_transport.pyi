from google.ads.google_ads.v3.proto.services import (
    hotel_group_view_service_pb2_grpc as hotel_group_view_service_pb2_grpc,
)
from typing import Any, Optional

class HotelGroupViewServiceGrpcTransport:
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
    def get_hotel_group_view(self): ...
