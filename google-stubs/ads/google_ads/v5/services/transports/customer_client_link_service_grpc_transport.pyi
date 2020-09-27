from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    customer_client_link_service_pb2_grpc as customer_client_link_service_pb2_grpc,
)

class CustomerClientLinkServiceGrpcTransport:
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
    def get_customer_client_link(self): ...
    @property
    def mutate_customer_client_link(self): ...
