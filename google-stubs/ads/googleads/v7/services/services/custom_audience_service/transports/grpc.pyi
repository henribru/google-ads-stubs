from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import custom_audience
from google.ads.googleads.v7.services.types import custom_audience_service

from .base import CustomAudienceServiceTransport

class CustomAudienceServiceGrpcTransport(CustomAudienceServiceTransport):
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
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
        credentials: credentials.Credentials = ...,
        scopes: Optional[Sequence[str]] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def get_custom_audience(
        self,
    ) -> Callable[
        [custom_audience_service.GetCustomAudienceRequest],
        custom_audience.CustomAudience,
    ]: ...
    @property
    def mutate_custom_audiences(
        self,
    ) -> Callable[
        [custom_audience_service.MutateCustomAudiencesRequest],
        custom_audience_service.MutateCustomAudiencesResponse,
    ]: ...