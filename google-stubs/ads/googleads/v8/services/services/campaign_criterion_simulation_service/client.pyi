from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import campaign_criterion_simulation
from google.ads.googleads.v8.services.types import campaign_criterion_simulation_service

from .transports.base import CampaignCriterionSimulationServiceTransport

class CampaignCriterionSimulationServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[CampaignCriterionSimulationServiceTransport]: ...

class CampaignCriterionSimulationServiceClient(
    metaclass=CampaignCriterionSimulationServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> CampaignCriterionSimulationServiceTransport: ...
    @staticmethod
    def campaign_criterion_simulation_path(
        customer_id: str,
        campaign_id: str,
        criterion_id: str,
        type: str,
        modification_method: str,
        start_date: str,
        end_date: str,
    ) -> str: ...
    @staticmethod
    def parse_campaign_criterion_simulation_path(path: str) -> Dict[str, str]: ...
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
        credentials: Optional[ga_credentials.Credentials] = ...,
        transport: Union[str, CampaignCriterionSimulationServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_campaign_criterion_simulation(
        self,
        request: campaign_criterion_simulation_service.GetCampaignCriterionSimulationRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> campaign_criterion_simulation.CampaignCriterionSimulation: ...