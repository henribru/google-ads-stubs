from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1, operations_v1
from google.auth import credentials
from google.longrunning import operations_pb2 as operations

from google.ads.googleads.v7.resources.types import campaign_draft
from google.ads.googleads.v7.services.types import campaign_draft_service

from .base import CampaignDraftServiceTransport

class CampaignDraftServiceGrpcTransport(CampaignDraftServiceTransport):
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
    def operations_client(self) -> operations_v1.OperationsClient: ...
    @property
    def get_campaign_draft(
        self,
    ) -> Callable[
        [campaign_draft_service.GetCampaignDraftRequest], campaign_draft.CampaignDraft
    ]: ...
    @property
    def mutate_campaign_drafts(
        self,
    ) -> Callable[
        [campaign_draft_service.MutateCampaignDraftsRequest],
        campaign_draft_service.MutateCampaignDraftsResponse,
    ]: ...
    @property
    def promote_campaign_draft(
        self,
    ) -> Callable[
        [campaign_draft_service.PromoteCampaignDraftRequest], operations.Operation
    ]: ...
    @property
    def list_campaign_draft_async_errors(
        self,
    ) -> Callable[
        [campaign_draft_service.ListCampaignDraftAsyncErrorsRequest],
        campaign_draft_service.ListCampaignDraftAsyncErrorsResponse,
    ]: ...