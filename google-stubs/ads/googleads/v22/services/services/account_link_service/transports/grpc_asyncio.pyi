from typing import Awaitable, Callable, Sequence

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from grpc.experimental import aio  # type: ignore[attr-defined]

from google.ads.googleads.v22.services.types import account_link_service

from .base import AccountLinkServiceTransport

__all__ = ["AccountLinkServiceGrpcAsyncIOTransport"]

class _LoggingClientAIOInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    async def intercept_unary_unary(
        self, continuation, client_call_details, request
    ): ...

class AccountLinkServiceGrpcAsyncIOTransport(AccountLinkServiceTransport):
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
    def create_account_link(
        self,
    ) -> Callable[
        [account_link_service.CreateAccountLinkRequest],
        Awaitable[account_link_service.CreateAccountLinkResponse],
    ]: ...
    @property
    def mutate_account_link(
        self,
    ) -> Callable[
        [account_link_service.MutateAccountLinkRequest],
        Awaitable[account_link_service.MutateAccountLinkResponse],
    ]: ...
    def close(self): ...
    @property
    def kind(self) -> str: ...
