from typing import Any, Optional

from google.ads.google_ads.v4.proto.services import (
    detail_placement_view_service_pb2_grpc as detail_placement_view_service_pb2_grpc,
)

class DetailPlacementViewServiceGrpcTransport:
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
    def get_detail_placement_view(self): ...
