from typing import Any, Optional

from google.ads.google_ads.v4.proto.services import (
    asset_service_pb2_grpc as asset_service_pb2_grpc,
)

class AssetServiceGrpcTransport:
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
    def get_asset(self): ...
    @property
    def mutate_assets(self): ...
