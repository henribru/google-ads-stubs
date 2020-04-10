from google.ads.google_ads.v3.proto.services import (
    reach_plan_service_pb2_grpc as reach_plan_service_pb2_grpc,
)
from typing import Any, Optional

class ReachPlanServiceGrpcTransport:
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
    def list_plannable_locations(self): ...
    @property
    def list_plannable_products(self): ...
    @property
    def generate_product_mix_ideas(self): ...
    @property
    def generate_reach_forecast(self): ...
