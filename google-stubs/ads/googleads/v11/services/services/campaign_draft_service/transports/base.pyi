import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2

from google.ads.googleads.v11.services.types import campaign_draft_service

class CampaignDraftServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def operations_client(self) -> None: ...
    @property
    def mutate_campaign_drafts(
        self,
    ) -> Callable[
        [campaign_draft_service.MutateCampaignDraftsRequest],
        Union[
            campaign_draft_service.MutateCampaignDraftsResponse,
            Awaitable[campaign_draft_service.MutateCampaignDraftsResponse],
        ],
    ]: ...
    @property
    def promote_campaign_draft(
        self,
    ) -> Callable[
        [campaign_draft_service.PromoteCampaignDraftRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]: ...
    @property
    def list_campaign_draft_async_errors(
        self,
    ) -> Callable[
        [campaign_draft_service.ListCampaignDraftAsyncErrorsRequest],
        Union[
            campaign_draft_service.ListCampaignDraftAsyncErrorsResponse,
            Awaitable[campaign_draft_service.ListCampaignDraftAsyncErrorsResponse],
        ],
    ]: ...
