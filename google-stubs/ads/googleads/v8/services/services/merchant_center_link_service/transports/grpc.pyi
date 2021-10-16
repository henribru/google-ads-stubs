from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import merchant_center_link
from google.ads.googleads.v8.services.types import merchant_center_link_service

from .base import MerchantCenterLinkServiceTransport

class MerchantCenterLinkServiceGrpcTransport(MerchantCenterLinkServiceTransport):
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: str = ...,
        scopes: Sequence[str] = ...,
        channel: grpc.Channel = ...,
        api_mtls_endpoint: str = ...,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = ...,
        ssl_channel_credentials: grpc.ChannelCredentials = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        scopes: Optional[Sequence[str]] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def list_merchant_center_links(
        self,
    ) -> Callable[
        [merchant_center_link_service.ListMerchantCenterLinksRequest],
        merchant_center_link_service.ListMerchantCenterLinksResponse,
    ]: ...
    @property
    def get_merchant_center_link(
        self,
    ) -> Callable[
        [merchant_center_link_service.GetMerchantCenterLinkRequest],
        merchant_center_link.MerchantCenterLink,
    ]: ...
    @property
    def mutate_merchant_center_link(
        self,
    ) -> Callable[
        [merchant_center_link_service.MutateMerchantCenterLinkRequest],
        merchant_center_link_service.MutateMerchantCenterLinkResponse,
    ]: ...
