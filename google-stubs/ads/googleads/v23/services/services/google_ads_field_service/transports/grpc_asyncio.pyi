from typing import Awaitable, Callable, Sequence

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from grpc.experimental import aio

from google.ads.googleads.v23.resources.types import google_ads_field
from google.ads.googleads.v23.services.types import google_ads_field_service

from .base import GoogleAdsFieldServiceTransport

__all__ = ["GoogleAdsFieldServiceGrpcAsyncIOTransport"]

class _LoggingClientAIOInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    async def intercept_unary_unary(
        self, continuation, client_call_details, request
    ): ...

class GoogleAdsFieldServiceGrpcAsyncIOTransport(GoogleAdsFieldServiceTransport):
    @classmethod
    def create_channel(
        cls,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        **kwargs,
    ) -> aio.Channel: ...
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        channel: aio.Channel | Callable[..., aio.Channel] | None = None,
        api_mtls_endpoint: str | None = None,
        client_cert_source: Callable[[], tuple[bytes, bytes]] | None = None,
        ssl_channel_credentials: grpc.ChannelCredentials | None = None,
        client_cert_source_for_mtls: Callable[[], tuple[bytes, bytes]] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        api_audience: str | None = None,
    ) -> None: ...
    @property
    def grpc_channel(self) -> aio.Channel: ...
    @property
    def get_google_ads_field(
        self,
    ) -> Callable[
        [google_ads_field_service.GetGoogleAdsFieldRequest],
        Awaitable[google_ads_field.GoogleAdsField],
    ]: ...
    @property
    def search_google_ads_fields(
        self,
    ) -> Callable[
        [google_ads_field_service.SearchGoogleAdsFieldsRequest],
        Awaitable[google_ads_field_service.SearchGoogleAdsFieldsResponse],
    ]: ...
    def close(self): ...
    @property
    def kind(self) -> str: ...
