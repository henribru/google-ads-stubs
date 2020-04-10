from google.ads.google_ads.v3.proto.services import (
    remarketing_action_service_pb2_grpc as remarketing_action_service_pb2_grpc,
)
from typing import Any, Optional

class RemarketingActionServiceGrpcTransport:
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
    def get_remarketing_action(self): ...
    @property
    def mutate_remarketing_actions(self): ...
