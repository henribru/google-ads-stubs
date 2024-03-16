import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2

from google.ads.googleads.v14.services.types import offline_user_data_job_service

__all__ = ["OfflineUserDataJobServiceTransport"]

class OfflineUserDataJobServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        **kwargs,
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def operations_client(self) -> None: ...
    @property
    def create_offline_user_data_job(
        self,
    ) -> Callable[
        [offline_user_data_job_service.CreateOfflineUserDataJobRequest],
        offline_user_data_job_service.CreateOfflineUserDataJobResponse
        | Awaitable[offline_user_data_job_service.CreateOfflineUserDataJobResponse],
    ]: ...
    @property
    def add_offline_user_data_job_operations(
        self,
    ) -> Callable[
        [offline_user_data_job_service.AddOfflineUserDataJobOperationsRequest],
        offline_user_data_job_service.AddOfflineUserDataJobOperationsResponse
        | Awaitable[
            offline_user_data_job_service.AddOfflineUserDataJobOperationsResponse
        ],
    ]: ...
    @property
    def run_offline_user_data_job(
        self,
    ) -> Callable[
        [offline_user_data_job_service.RunOfflineUserDataJobRequest],
        operations_pb2.Operation | Awaitable[operations_pb2.Operation],
    ]: ...
