from typing import Callable, Sequence

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v22.services.types import data_link_service

from .base import DataLinkServiceTransport

__all__ = ["DataLinkServiceGrpcTransport"]

class _LoggingClientInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request): ...

class DataLinkServiceGrpcTransport(DataLinkServiceTransport):
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        channel: grpc.Channel | Callable[..., grpc.Channel] | None = None,
        api_mtls_endpoint: str | None = None,
        client_cert_source: Callable[[], tuple[bytes, bytes]] | None = None,
        ssl_channel_credentials: grpc.ChannelCredentials | None = None,
        client_cert_source_for_mtls: Callable[[], tuple[bytes, bytes]] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        api_audience: str | None = None,
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        **kwargs,
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def create_data_link(
        self,
    ) -> Callable[
        [data_link_service.CreateDataLinkRequest],
        data_link_service.CreateDataLinkResponse,
    ]: ...
    @property
    def remove_data_link(
        self,
    ) -> Callable[
        [data_link_service.RemoveDataLinkRequest],
        data_link_service.RemoveDataLinkResponse,
    ]: ...
    @property
    def update_data_link(
        self,
    ) -> Callable[
        [data_link_service.UpdateDataLinkRequest],
        data_link_service.UpdateDataLinkResponse,
    ]: ...
    def close(self) -> None: ...
    @property
    def kind(self) -> str: ...
