from typing import Any, Optional

from google.ads.google_ads.v6.proto.services import (
    customer_user_access_invitation_service_pb2_grpc as customer_user_access_invitation_service_pb2_grpc,
)

class CustomerUserAccessInvitationServiceGrpcTransport:
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
    def get_customer_user_access_invitation(self): ...
    @property
    def mutate_customer_user_access_invitation(self): ...
