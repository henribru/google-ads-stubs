from typing import Any, Optional

from google.ads.google_ads.v4.proto.services import (
    campaign_bid_modifier_service_pb2_grpc as campaign_bid_modifier_service_pb2_grpc,
)

class CampaignBidModifierServiceGrpcTransport:
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
    def get_campaign_bid_modifier(self): ...
    @property
    def mutate_campaign_bid_modifiers(self): ...
