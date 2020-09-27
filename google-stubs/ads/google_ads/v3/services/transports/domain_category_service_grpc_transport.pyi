from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    domain_category_service_pb2_grpc as domain_category_service_pb2_grpc,
)

class DomainCategoryServiceGrpcTransport:
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
    def get_domain_category(self): ...
