from google.ads.google_ads.v3.proto.services import (
    keyword_plan_ad_group_service_pb2_grpc as keyword_plan_ad_group_service_pb2_grpc,
)
from typing import Any, Optional

class KeywordPlanAdGroupServiceGrpcTransport:
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
    def get_keyword_plan_ad_group(self): ...
    @property
    def mutate_keyword_plan_ad_groups(self): ...
