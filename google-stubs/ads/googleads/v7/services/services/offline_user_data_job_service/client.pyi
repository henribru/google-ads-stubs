from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    operation,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import offline_user_data_job
from google.ads.googleads.v7.services.types import offline_user_data_job_service

from .transports.base import OfflineUserDataJobServiceTransport

class OfflineUserDataJobServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[OfflineUserDataJobServiceTransport]: ...

class OfflineUserDataJobServiceClient(metaclass=OfflineUserDataJobServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> OfflineUserDataJobServiceTransport: ...
    @staticmethod
    def offline_user_data_job_path(
        customer_id: str, offline_user_data_update_id: str
    ) -> str: ...
    @staticmethod
    def parse_offline_user_data_job_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, OfflineUserDataJobServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def create_offline_user_data_job(
        self,
        request: offline_user_data_job_service.CreateOfflineUserDataJobRequest = ...,
        *,
        customer_id: str = ...,
        job: offline_user_data_job.OfflineUserDataJob = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> offline_user_data_job_service.CreateOfflineUserDataJobResponse: ...
    def get_offline_user_data_job(
        self,
        request: offline_user_data_job_service.GetOfflineUserDataJobRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> offline_user_data_job.OfflineUserDataJob: ...
    def add_offline_user_data_job_operations(
        self,
        request: offline_user_data_job_service.AddOfflineUserDataJobOperationsRequest = ...,
        *,
        resource_name: str = ...,
        operations: Sequence[
            offline_user_data_job_service.OfflineUserDataJobOperation
        ] = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> offline_user_data_job_service.AddOfflineUserDataJobOperationsResponse: ...
    def run_offline_user_data_job(
        self,
        request: offline_user_data_job_service.RunOfflineUserDataJobRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> operation.Operation: ...
