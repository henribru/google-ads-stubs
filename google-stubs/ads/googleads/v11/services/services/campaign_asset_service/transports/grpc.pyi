from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v11.services.types import campaign_asset_service

from .base import CampaignAssetServiceTransport

class CampaignAssetServiceGrpcTransport(CampaignAssetServiceTransport):
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
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: str = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def mutate_campaign_assets(
        self,
    ) -> Callable[
        [campaign_asset_service.MutateCampaignAssetsRequest],
        campaign_asset_service.MutateCampaignAssetsResponse,
    ]: ...
    def close(self) -> None: ...
