# Stubs for google.ads.google_ads.v6.services.transports.merchant_center_link_service_grpc_transport (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

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
