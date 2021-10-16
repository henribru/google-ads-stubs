from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import ad_group_asset
from google.ads.googleads.v8.services.types import ad_group_asset_service

from .base import AdGroupAssetServiceTransport

class AdGroupAssetServiceGrpcTransport(AdGroupAssetServiceTransport):
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
    def get_ad_group_asset(
        self,
    ) -> Callable[
        [ad_group_asset_service.GetAdGroupAssetRequest], ad_group_asset.AdGroupAsset
    ]: ...
    @property
    def mutate_ad_group_assets(
        self,
    ) -> Callable[
        [ad_group_asset_service.MutateAdGroupAssetsRequest],
        ad_group_asset_service.MutateAdGroupAssetsResponse,
    ]: ...