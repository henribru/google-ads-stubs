from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    account_link_service_pb2_grpc as account_link_service_pb2_grpc,
)

class AccountLinkServiceGrpcTransport:
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
    def get_account_link(self): ...
    @property
    def create_account_link(self): ...
    @property
    def mutate_account_link(self): ...
