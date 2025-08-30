from typing import Callable, MutableSequence, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1, operation_async, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.services.services.campaign_draft_service import pagers
from google.ads.googleads.v20.services.types import campaign_draft_service

from .transports.base import CampaignDraftServiceTransport

__all__ = ["CampaignDraftServiceAsyncClient"]

class CampaignDraftServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    campaign_path: Incomplete
    parse_campaign_path: Incomplete
    campaign_draft_path: Incomplete
    parse_campaign_draft_path: Incomplete
    common_billing_account_path: Incomplete
    parse_common_billing_account_path: Incomplete
    common_folder_path: Incomplete
    parse_common_folder_path: Incomplete
    common_organization_path: Incomplete
    parse_common_organization_path: Incomplete
    common_project_path: Incomplete
    parse_common_project_path: Incomplete
    common_location_path: Incomplete
    parse_common_location_path: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: ClientOptions | None = None
    ): ...
    @property
    def transport(self) -> CampaignDraftServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str
        | CampaignDraftServiceTransport
        | Callable[..., CampaignDraftServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def mutate_campaign_drafts(
        self,
        request: campaign_draft_service.MutateCampaignDraftsRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[campaign_draft_service.CampaignDraftOperation]
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> campaign_draft_service.MutateCampaignDraftsResponse: ...
    async def promote_campaign_draft(
        self,
        request: campaign_draft_service.PromoteCampaignDraftRequest
        | dict
        | None = None,
        *,
        campaign_draft: str | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> operation_async.AsyncOperation: ...
    async def list_campaign_draft_async_errors(
        self,
        request: campaign_draft_service.ListCampaignDraftAsyncErrorsRequest
        | dict
        | None = None,
        *,
        resource_name: str | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> pagers.ListCampaignDraftAsyncErrorsAsyncPager: ...
    async def __aenter__(self) -> CampaignDraftServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
