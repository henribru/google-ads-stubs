from typing import Any, Optional

from google.ads.google_ads.v4.proto.services import (
    dynamic_search_ads_search_term_view_service_pb2_grpc as dynamic_search_ads_search_term_view_service_pb2_grpc,
)

class DynamicSearchAdsSearchTermViewServiceGrpcTransport:
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
    def get_dynamic_search_ads_search_term_view(self): ...
