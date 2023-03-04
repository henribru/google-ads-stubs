from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import campaign_shared_set_service

from .base import CampaignSharedSetServiceTransport

class CampaignSharedSetServiceGrpcTransport(CampaignSharedSetServiceTransport):
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
    def mutate_campaign_shared_sets(
        self,
    ) -> Callable[
        [campaign_shared_set_service.MutateCampaignSharedSetsRequest],
        campaign_shared_set_service.MutateCampaignSharedSetsResponse,
    ]: ...
    def close(self) -> None: ...