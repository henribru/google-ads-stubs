from typing import Any, Optional

from google.ads.google_ads.v4.proto.services import (
    click_view_service_pb2_grpc as click_view_service_pb2_grpc,
)

class ClickViewServiceGrpcTransport:
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
    def get_click_view(self): ...
