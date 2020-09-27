from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    geo_target_constant_service_pb2_grpc as geo_target_constant_service_pb2_grpc,
)

class GeoTargetConstantServiceGrpcTransport:
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
    def get_geo_target_constant(self): ...
    @property
    def suggest_geo_target_constants(self): ...
