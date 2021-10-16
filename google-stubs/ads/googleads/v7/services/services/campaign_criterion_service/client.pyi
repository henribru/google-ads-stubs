from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import campaign_criterion
from google.ads.googleads.v7.services.types import campaign_criterion_service

from .transports.base import CampaignCriterionServiceTransport

class CampaignCriterionServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[CampaignCriterionServiceTransport]: ...

class CampaignCriterionServiceClient(metaclass=CampaignCriterionServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> CampaignCriterionServiceTransport: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_criterion_path(
        customer_id: str, campaign_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_criterion_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, CampaignCriterionServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_campaign_criterion(
        self,
        request: campaign_criterion_service.GetCampaignCriterionRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> campaign_criterion.CampaignCriterion: ...
    def mutate_campaign_criteria(
        self,
        request: campaign_criterion_service.MutateCampaignCriteriaRequest = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[
            campaign_criterion_service.CampaignCriterionOperation
        ] = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> campaign_criterion_service.MutateCampaignCriteriaResponse: ...
