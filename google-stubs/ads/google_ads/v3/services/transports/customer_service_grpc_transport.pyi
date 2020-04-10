from google.ads.google_ads.v3.proto.services import (
    customer_service_pb2_grpc as customer_service_pb2_grpc,
)
from typing import Any, Optional

class CustomerServiceGrpcTransport:
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
    def get_customer(self): ...
    @property
    def mutate_customer(self): ...
    @property
    def list_accessible_customers(self): ...
    @property
    def create_customer_client(self): ...
