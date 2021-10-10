from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    operation,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import campaign_draft
from google.ads.googleads.v7.services.services.campaign_draft_service import pagers
from google.ads.googleads.v7.services.types import campaign_draft_service

from .transports.base import CampaignDraftServiceTransport

class CampaignDraftServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[CampaignDraftServiceTransport]: ...

class CampaignDraftServiceClient(metaclass=CampaignDraftServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> CampaignDraftServiceTransport: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_draft_path(
        customer_id: str, base_campaign_id: str, draft_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_draft_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]: ...
    def __init__(
        self,
        *,
        credentials: Optional[credentials.Credentials] = ...,
        transport: Union[str, CampaignDraftServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_campaign_draft(
        self,
        request: campaign_draft_service.GetCampaignDraftRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> campaign_draft.CampaignDraft: ...
    def mutate_campaign_drafts(
        self,
        request: campaign_draft_service.MutateCampaignDraftsRequest = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[campaign_draft_service.CampaignDraftOperation] = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> campaign_draft_service.MutateCampaignDraftsResponse: ...
    def promote_campaign_draft(
        self,
        request: campaign_draft_service.PromoteCampaignDraftRequest = ...,
        *,
        campaign_draft: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> operation.Operation: ...
    def list_campaign_draft_async_errors(
        self,
        request: campaign_draft_service.ListCampaignDraftAsyncErrorsRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> pagers.ListCampaignDraftAsyncErrorsPager: ...
