from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import asset_group
from google.ads.googleads.v9.services.types import asset_group_service

from .base import AssetGroupServiceTransport

class AssetGroupServiceGrpcTransport(AssetGroupServiceTransport):
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
    def get_asset_group(
        self,
    ) -> Callable[
        [asset_group_service.GetAssetGroupRequest], asset_group.AssetGroup
    ]: ...
    @property
    def mutate_asset_groups(
        self,
    ) -> Callable[
        [asset_group_service.MutateAssetGroupsRequest],
        asset_group_service.MutateAssetGroupsResponse,
    ]: ...
