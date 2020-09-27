from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    paid_organic_search_term_view_service_pb2_grpc as paid_organic_search_term_view_service_pb2_grpc,
)

class PaidOrganicSearchTermViewServiceGrpcTransport:
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
    def get_paid_organic_search_term_view(self): ...
