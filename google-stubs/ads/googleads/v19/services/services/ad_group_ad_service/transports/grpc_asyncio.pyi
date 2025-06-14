from typing import Awaitable, Callable, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.protobuf import empty_pb2
from grpc.experimental import aio  # type: ignore[attr-defined]

from google.ads.googleads.v19.services.types import ad_group_ad_service

from .base import AdGroupAdServiceTransport

__all__ = ["AdGroupAdServiceGrpcAsyncIOTransport"]

class _LoggingClientAIOInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    async def intercept_unary_unary(
        self, continuation, client_call_details, request
    ): ...

class AdGroupAdServiceGrpcAsyncIOTransport(AdGroupAdServiceTransport):
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
    def mutate_ad_group_ads(
        self,
    ) -> Callable[
        [ad_group_ad_service.MutateAdGroupAdsRequest],
        Awaitable[ad_group_ad_service.MutateAdGroupAdsResponse],
    ]: ...
    @property
    def remove_automatically_created_assets(
        self,
    ) -> Callable[
        [ad_group_ad_service.RemoveAutomaticallyCreatedAssetsRequest],
        Awaitable[empty_pb2.Empty],
    ]: ...
    def close(self): ...
    @property
    def kind(self) -> str: ...
