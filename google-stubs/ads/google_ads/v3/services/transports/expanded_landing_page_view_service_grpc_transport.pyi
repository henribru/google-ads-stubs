from google.ads.google_ads.v3.proto.services import (
    expanded_landing_page_view_service_pb2_grpc as expanded_landing_page_view_service_pb2_grpc,
)
from typing import Any, Optional

class ExpandedLandingPageViewServiceGrpcTransport:
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
    def get_expanded_landing_page_view(self): ...
