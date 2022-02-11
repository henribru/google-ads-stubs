from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.services.types import google_ads_service

from .base import GoogleAdsServiceTransport

class GoogleAdsServiceGrpcTransport(GoogleAdsServiceTransport):
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
    def close(self) -> None: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def search(
        self,
    ) -> Callable[
        [google_ads_service.SearchGoogleAdsRequest],
        google_ads_service.SearchGoogleAdsResponse,
    ]: ...
    @property
    def search_stream(
        self,
    ) -> Callable[
        [google_ads_service.SearchGoogleAdsStreamRequest],
        google_ads_service.SearchGoogleAdsStreamResponse,
    ]: ...
    @property
    def mutate(
        self,
    ) -> Callable[
        [google_ads_service.MutateGoogleAdsRequest],
        google_ads_service.MutateGoogleAdsResponse,
    ]: ...
