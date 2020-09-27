from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    customer_label_service_pb2_grpc as customer_label_service_pb2_grpc,
)

class CustomerLabelServiceGrpcTransport:
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
    def get_customer_label(self): ...
    @property
    def mutate_customer_labels(self): ...
