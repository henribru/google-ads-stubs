from typing import Any, Optional

from google.ads.google_ads.v4.proto.services import (
    recommendation_service_pb2_grpc as recommendation_service_pb2_grpc,
)

class RecommendationServiceGrpcTransport:
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
    def get_recommendation(self): ...
    @property
    def apply_recommendation(self): ...
    @property
    def dismiss_recommendation(self): ...
