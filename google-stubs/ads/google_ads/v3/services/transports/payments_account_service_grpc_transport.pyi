from google.ads.google_ads.v3.proto.services import (
    payments_account_service_pb2_grpc as payments_account_service_pb2_grpc,
)
from typing import Any, Optional

class PaymentsAccountServiceGrpcTransport:
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
    def list_payments_accounts(self): ...
