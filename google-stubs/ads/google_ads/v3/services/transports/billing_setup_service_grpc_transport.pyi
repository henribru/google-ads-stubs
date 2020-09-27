from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    billing_setup_service_pb2_grpc as billing_setup_service_pb2_grpc,
)

class BillingSetupServiceGrpcTransport:
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
    def get_billing_setup(self): ...
    @property
    def mutate_billing_setup(self): ...
