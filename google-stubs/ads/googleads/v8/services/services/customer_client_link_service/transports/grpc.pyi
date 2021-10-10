from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import customer_client_link
from google.ads.googleads.v8.services.types import customer_client_link_service

from .base import CustomerClientLinkServiceTransport

class CustomerClientLinkServiceGrpcTransport(CustomerClientLinkServiceTransport):
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
    def get_customer_client_link(
        self,
    ) -> Callable[
        [customer_client_link_service.GetCustomerClientLinkRequest],
        customer_client_link.CustomerClientLink,
    ]: ...
    @property
    def mutate_customer_client_link(
        self,
    ) -> Callable[
        [customer_client_link_service.MutateCustomerClientLinkRequest],
        customer_client_link_service.MutateCustomerClientLinkResponse,
    ]: ...
