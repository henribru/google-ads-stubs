from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    conversion_upload_service_pb2_grpc as conversion_upload_service_pb2_grpc,
)

class ConversionUploadServiceGrpcTransport:
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
    def upload_click_conversions(self): ...
    @property
    def upload_call_conversions(self): ...
