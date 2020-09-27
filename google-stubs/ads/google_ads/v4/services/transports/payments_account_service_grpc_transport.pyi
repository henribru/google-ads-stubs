from typing import Any, Optional

from google.ads.google_ads.v4.proto.services import (
    payments_account_service_pb2_grpc as payments_account_service_pb2_grpc,
)

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
