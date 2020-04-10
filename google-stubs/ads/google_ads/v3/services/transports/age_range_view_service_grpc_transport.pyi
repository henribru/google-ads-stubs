from google.ads.google_ads.v3.proto.services import (
    age_range_view_service_pb2_grpc as age_range_view_service_pb2_grpc,
)
from typing import Any, Optional

class AgeRangeViewServiceGrpcTransport:
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
    def get_age_range_view(self): ...
