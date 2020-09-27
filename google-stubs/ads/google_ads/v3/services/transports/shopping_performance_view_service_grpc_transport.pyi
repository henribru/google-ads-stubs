from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    shopping_performance_view_service_pb2_grpc as shopping_performance_view_service_pb2_grpc,
)

class ShoppingPerformanceViewServiceGrpcTransport:
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
    def get_shopping_performance_view(self): ...
