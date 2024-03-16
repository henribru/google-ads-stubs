import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2

from google.ads.googleads.v14.services.types import campaign_draft_service

__all__ = ["CampaignDraftServiceTransport"]

class CampaignDraftServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        **kwargs,
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def operations_client(self) -> None: ...
    @property
    def mutate_campaign_drafts(
        self,
    ) -> Callable[
        [campaign_draft_service.MutateCampaignDraftsRequest],
        campaign_draft_service.MutateCampaignDraftsResponse
        | Awaitable[campaign_draft_service.MutateCampaignDraftsResponse],
    ]: ...
    @property
    def promote_campaign_draft(
        self,
    ) -> Callable[
        [campaign_draft_service.PromoteCampaignDraftRequest],
        operations_pb2.Operation | Awaitable[operations_pb2.Operation],
    ]: ...
    @property
    def list_campaign_draft_async_errors(
        self,
    ) -> Callable[
        [campaign_draft_service.ListCampaignDraftAsyncErrorsRequest],
        campaign_draft_service.ListCampaignDraftAsyncErrorsResponse
        | Awaitable[campaign_draft_service.ListCampaignDraftAsyncErrorsResponse],
    ]: ...
