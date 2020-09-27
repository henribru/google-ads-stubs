from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    third_party_app_analytics_link_service_pb2_grpc as third_party_app_analytics_link_service_pb2_grpc,
)

class ThirdPartyAppAnalyticsLinkServiceGrpcTransport:
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
    def get_third_party_app_analytics_link(self): ...
    @property
    def regenerate_shareable_link_id(self): ...
