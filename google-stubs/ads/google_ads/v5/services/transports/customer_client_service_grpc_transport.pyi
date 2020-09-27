from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    customer_client_service_pb2_grpc as customer_client_service_pb2_grpc,
)

class CustomerClientServiceGrpcTransport:
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
    def get_customer_client(self): ...
