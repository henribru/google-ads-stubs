from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    customer_extension_setting_service_pb2_grpc as customer_extension_setting_service_pb2_grpc,
)

class CustomerExtensionSettingServiceGrpcTransport:
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
    def get_customer_extension_setting(self): ...
    @property
    def mutate_customer_extension_settings(self): ...
