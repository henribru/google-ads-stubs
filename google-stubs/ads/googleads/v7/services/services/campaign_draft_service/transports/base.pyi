import abc
import typing
from typing import Any

from google.api_core import gapic_v1, operations_v1
from google.auth import credentials
from google.longrunning import operations_pb2 as operations

from google.ads.googleads.v7.resources.types import campaign_draft
from google.ads.googleads.v7.services.types import campaign_draft_service

class CampaignDraftServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def operations_client(self) -> operations_v1.OperationsClient: ...
    @property
    def get_campaign_draft(
        self,
    ) -> typing.Callable[
        [campaign_draft_service.GetCampaignDraftRequest], campaign_draft.CampaignDraft
    ]: ...
    @property
    def mutate_campaign_drafts(
        self,
    ) -> typing.Callable[
        [campaign_draft_service.MutateCampaignDraftsRequest],
        campaign_draft_service.MutateCampaignDraftsResponse,
    ]: ...
    @property
    def promote_campaign_draft(
        self,
    ) -> typing.Callable[
        [campaign_draft_service.PromoteCampaignDraftRequest], operations.Operation
    ]: ...
    @property
    def list_campaign_draft_async_errors(
        self,
    ) -> typing.Callable[
        [campaign_draft_service.ListCampaignDraftAsyncErrorsRequest],
        campaign_draft_service.ListCampaignDraftAsyncErrorsResponse,
    ]: ...
