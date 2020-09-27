from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    google_ads_service_pb2_grpc as google_ads_service_pb2_grpc,
)

class GoogleAdsServiceGrpcTransport:
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
    def search(self): ...
    @property
    def search_stream(self): ...
    @property
    def mutate(self): ...
