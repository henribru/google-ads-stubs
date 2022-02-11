import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2

from google.ads.googleads.v9.resources.types import offline_user_data_job
from google.ads.googleads.v9.services.types import offline_user_data_job_service

class OfflineUserDataJobServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def operations_client(self) -> None: ...
    @property
    def create_offline_user_data_job(
        self,
    ) -> typing.Callable[
        [offline_user_data_job_service.CreateOfflineUserDataJobRequest],
        offline_user_data_job_service.CreateOfflineUserDataJobResponse,
    ]: ...
    @property
    def get_offline_user_data_job(
        self,
    ) -> typing.Callable[
        [offline_user_data_job_service.GetOfflineUserDataJobRequest],
        offline_user_data_job.OfflineUserDataJob,
    ]: ...
    @property
    def add_offline_user_data_job_operations(
        self,
    ) -> typing.Callable[
        [offline_user_data_job_service.AddOfflineUserDataJobOperationsRequest],
        offline_user_data_job_service.AddOfflineUserDataJobOperationsResponse,
    ]: ...
    @property
    def run_offline_user_data_job(
        self,
    ) -> typing.Callable[
        [offline_user_data_job_service.RunOfflineUserDataJobRequest],
        operations_pb2.Operation,
    ]: ...
