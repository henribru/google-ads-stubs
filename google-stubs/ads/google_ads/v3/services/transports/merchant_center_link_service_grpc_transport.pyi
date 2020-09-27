from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    merchant_center_link_service_pb2_grpc as merchant_center_link_service_pb2_grpc,
)

class MerchantCenterLinkServiceGrpcTransport:
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
    def list_merchant_center_links(self): ...
    @property
    def get_merchant_center_link(self): ...
    @property
    def mutate_merchant_center_link(self): ...
