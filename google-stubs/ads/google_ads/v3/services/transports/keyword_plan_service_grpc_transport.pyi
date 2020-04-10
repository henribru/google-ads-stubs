from google.ads.google_ads.v3.proto.services import (
    keyword_plan_service_pb2_grpc as keyword_plan_service_pb2_grpc,
)
from typing import Any, Optional

class KeywordPlanServiceGrpcTransport:
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
    def get_keyword_plan(self): ...
    @property
    def mutate_keyword_plans(self): ...
    @property
    def generate_forecast_metrics(self): ...
    @property
    def generate_historical_metrics(self): ...
