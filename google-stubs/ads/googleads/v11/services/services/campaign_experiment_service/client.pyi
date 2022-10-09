from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    operation,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v11.resources.types import (
    campaign_experiment as gagr_campaign_experiment,
)
from google.ads.googleads.v11.services.services.campaign_experiment_service import (
    pagers,
)
from google.ads.googleads.v11.services.types import campaign_experiment_service

from .transports.base import CampaignExperimentServiceTransport

class CampaignExperimentServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[CampaignExperimentServiceTransport]: ...

class CampaignExperimentServiceClient(metaclass=CampaignExperimentServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Incomplete
    @property
    def transport(self) -> CampaignExperimentServiceTransport: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
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
    def campaign_experiment_path(
        customer_id: str, campaign_experiment_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_experiment_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, CampaignExperimentServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def create_campaign_experiment(
        self,
        request: Union[
            campaign_experiment_service.CreateCampaignExperimentRequest, dict
        ] = ...,
        *,
        customer_id: str = ...,
        campaign_experiment: gagr_campaign_experiment.CampaignExperiment = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> operation.Operation: ...
    def mutate_campaign_experiments(
        self,
        request: Union[
            campaign_experiment_service.MutateCampaignExperimentsRequest, dict
        ] = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[
            campaign_experiment_service.CampaignExperimentOperation
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> campaign_experiment_service.MutateCampaignExperimentsResponse: ...
    def graduate_campaign_experiment(
        self,
        request: Union[
            campaign_experiment_service.GraduateCampaignExperimentRequest, dict
        ] = ...,
        *,
        campaign_experiment: str = ...,
        campaign_budget: str = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> campaign_experiment_service.GraduateCampaignExperimentResponse: ...
    def promote_campaign_experiment(
        self,
        request: Union[
            campaign_experiment_service.PromoteCampaignExperimentRequest, dict
        ] = ...,
        *,
        campaign_experiment: str = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> operation.Operation: ...
    def end_campaign_experiment(
        self,
        request: Union[
            campaign_experiment_service.EndCampaignExperimentRequest, dict
        ] = ...,
        *,
        campaign_experiment: str = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> None: ...
    def list_campaign_experiment_async_errors(
        self,
        request: Union[
            campaign_experiment_service.ListCampaignExperimentAsyncErrorsRequest, dict
        ] = ...,
        *,
        resource_name: str = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> pagers.ListCampaignExperimentAsyncErrorsPager: ...
