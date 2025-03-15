from typing import Callable, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v17.services.types import campaign_asset_set_service

from .base import CampaignAssetSetServiceTransport

__all__ = ["CampaignAssetSetServiceGrpcTransport"]

class _LoggingClientInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request): ...

class CampaignAssetSetServiceGrpcTransport(CampaignAssetSetServiceTransport):
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
    def mutate_campaign_asset_sets(
        self,
    ) -> Callable[
        [campaign_asset_set_service.MutateCampaignAssetSetsRequest],
        campaign_asset_set_service.MutateCampaignAssetSetsResponse,
    ]: ...
    def close(self) -> None: ...
    @property
    def kind(self) -> str: ...
