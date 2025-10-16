from typing import Awaitable, Callable, Sequence

import grpc
from google.api_core import gapic_v1, operations_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2
from grpc.experimental import aio  # type: ignore[attr-defined]

from google.ads.googleads.v20.services.types import campaign_draft_service

from .base import CampaignDraftServiceTransport

__all__ = ["CampaignDraftServiceGrpcAsyncIOTransport"]

class _LoggingClientAIOInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    async def intercept_unary_unary(
        self, continuation, client_call_details, request
    ): ...

class CampaignDraftServiceGrpcAsyncIOTransport(CampaignDraftServiceTransport):
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
    def operations_client(self) -> operations_v1.OperationsAsyncClient: ...  # type: ignore[override]
    @property
    def mutate_campaign_drafts(
        self,
    ) -> Callable[
        [campaign_draft_service.MutateCampaignDraftsRequest],
        Awaitable[campaign_draft_service.MutateCampaignDraftsResponse],
    ]: ...
    @property
    def promote_campaign_draft(
        self,
    ) -> Callable[
        [campaign_draft_service.PromoteCampaignDraftRequest],
        Awaitable[operations_pb2.Operation],
    ]: ...
    @property
    def list_campaign_draft_async_errors(
        self,
    ) -> Callable[
        [campaign_draft_service.ListCampaignDraftAsyncErrorsRequest],
        Awaitable[campaign_draft_service.ListCampaignDraftAsyncErrorsResponse],
    ]: ...
    def close(self): ...
    @property
    def kind(self) -> str: ...
