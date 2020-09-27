from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    hotel_performance_view_service_pb2_grpc as hotel_performance_view_service_pb2_grpc,
)

class HotelPerformanceViewServiceGrpcTransport:
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
    def get_hotel_performance_view(self): ...
