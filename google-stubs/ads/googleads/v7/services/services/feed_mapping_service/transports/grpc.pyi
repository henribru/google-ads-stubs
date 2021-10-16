from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import feed_mapping
from google.ads.googleads.v7.services.types import feed_mapping_service

from .base import FeedMappingServiceTransport

class FeedMappingServiceGrpcTransport(FeedMappingServiceTransport):
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
    def get_feed_mapping(
        self,
    ) -> Callable[
        [feed_mapping_service.GetFeedMappingRequest], feed_mapping.FeedMapping
    ]: ...
    @property
    def mutate_feed_mappings(
        self,
    ) -> Callable[
        [feed_mapping_service.MutateFeedMappingsRequest],
        feed_mapping_service.MutateFeedMappingsResponse,
    ]: ...
