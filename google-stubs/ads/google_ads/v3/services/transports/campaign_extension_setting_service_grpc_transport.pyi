from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    campaign_extension_setting_service_pb2_grpc as campaign_extension_setting_service_pb2_grpc,
)

class CampaignExtensionSettingServiceGrpcTransport:
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
    def get_campaign_extension_setting(self): ...
    @property
    def mutate_campaign_extension_settings(self): ...
