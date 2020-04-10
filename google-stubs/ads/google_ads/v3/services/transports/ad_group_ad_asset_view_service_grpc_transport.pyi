from google.ads.google_ads.v3.proto.services import (
    ad_group_ad_asset_view_service_pb2_grpc as ad_group_ad_asset_view_service_pb2_grpc,
)
from typing import Any, Optional

class AdGroupAdAssetViewServiceGrpcTransport:
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
    def get_ad_group_ad_asset_view(self): ...
