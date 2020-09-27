from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    landing_page_view_service_pb2_grpc as landing_page_view_service_pb2_grpc,
)

class LandingPageViewServiceGrpcTransport:
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
    def get_landing_page_view(self): ...
