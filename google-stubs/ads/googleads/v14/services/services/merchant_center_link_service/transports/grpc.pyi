from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.resources.types import merchant_center_link
from google.ads.googleads.v14.services.types import merchant_center_link_service

from .base import MerchantCenterLinkServiceTransport

class MerchantCenterLinkServiceGrpcTransport(MerchantCenterLinkServiceTransport):
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: Optional[ga_credentials.Credentials] = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        channel: Optional[grpc.Channel] = ...,
        api_mtls_endpoint: Optional[str] = ...,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = ...,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = ...,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: Optional[ga_credentials.Credentials] = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
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
    def close(self) -> None: ...
