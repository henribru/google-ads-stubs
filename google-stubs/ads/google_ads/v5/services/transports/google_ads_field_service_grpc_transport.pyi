from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    google_ads_field_service_pb2_grpc as google_ads_field_service_pb2_grpc,
)

class GoogleAdsFieldServiceGrpcTransport:
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
    def get_google_ads_field(self): ...
    @property
    def search_google_ads_fields(self): ...
