from google.ads.google_ads.v3.proto.services import (
    ad_group_ad_label_service_pb2_grpc as ad_group_ad_label_service_pb2_grpc,
)
from typing import Any, Optional

class AdGroupAdLabelServiceGrpcTransport:
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
    def get_ad_group_ad_label(self): ...
    @property
    def mutate_ad_group_ad_labels(self): ...
