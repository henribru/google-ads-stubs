from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    group_placement_view_service_pb2_grpc as group_placement_view_service_pb2_grpc,
)

class GroupPlacementViewServiceGrpcTransport:
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
    def get_group_placement_view(self): ...
