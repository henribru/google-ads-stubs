from typing import Dict, MutableSequence, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    operation,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.services.experiment_service import pagers
from google.ads.googleads.v13.services.types import experiment_service

from .transports.base import ExperimentServiceTransport

class ExperimentServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = None
    ) -> Type[ExperimentServiceTransport]: ...

class ExperimentServiceClient(metaclass=ExperimentServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> ExperimentServiceTransport: ...
    def __enter__(self) -> ExperimentServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_budget_path(customer_id: str, campaign_budget_id: str) -> str: ...
    @staticmethod
    def parse_campaign_budget_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def experiment_path(customer_id: str, trial_id: str) -> str: ...
    @staticmethod
    def parse_experiment_path(path: str) -> Dict[str, str]: ...
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
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[Union[str, ExperimentServiceTransport]] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_experiments(
        self,
        request: Optional[
            Union[experiment_service.MutateExperimentsRequest, dict]
        ] = None,
        *,
        customer_id: Optional[str] = None,
        operations: Optional[
            MutableSequence[experiment_service.ExperimentOperation]
        ] = None,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ()
    ) -> experiment_service.MutateExperimentsResponse: ...
    def end_experiment(
        self,
        request: Optional[Union[experiment_service.EndExperimentRequest, dict]] = None,
        *,
        experiment: Optional[str] = None,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ()
    ) -> None: ...
    def list_experiment_async_errors(
        self,
        request: Optional[
            Union[experiment_service.ListExperimentAsyncErrorsRequest, dict]
        ] = None,
        *,
        resource_name: Optional[str] = None,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ()
    ) -> pagers.ListExperimentAsyncErrorsPager: ...
    def graduate_experiment(
        self,
        request: Optional[
            Union[experiment_service.GraduateExperimentRequest, dict]
        ] = None,
        *,
        experiment: Optional[str] = None,
        campaign_budget_mappings: Optional[
            MutableSequence[experiment_service.CampaignBudgetMapping]
        ] = None,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ()
    ) -> None: ...
    def schedule_experiment(
        self,
        request: Optional[
            Union[experiment_service.ScheduleExperimentRequest, dict]
        ] = None,
        *,
        resource_name: Optional[str] = None,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ()
    ) -> operation.Operation: ...
    def promote_experiment(
        self,
        request: Optional[
            Union[experiment_service.PromoteExperimentRequest, dict]
        ] = None,
        *,
        resource_name: Optional[str] = None,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ()
    ) -> operation.Operation: ...
