import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2

from google.ads.googleads.v10.services.types import offline_user_data_job_service

class OfflineUserDataJobServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def operations_client(self) -> None: ...
    @property
    def create_offline_user_data_job(
        self,
    ) -> Callable[
        [offline_user_data_job_service.CreateOfflineUserDataJobRequest],
        Union[
            offline_user_data_job_service.CreateOfflineUserDataJobResponse,
            Awaitable[offline_user_data_job_service.CreateOfflineUserDataJobResponse],
        ],
    ]: ...
    @property
    def add_offline_user_data_job_operations(
        self,
    ) -> Callable[
        [offline_user_data_job_service.AddOfflineUserDataJobOperationsRequest],
        Union[
            offline_user_data_job_service.AddOfflineUserDataJobOperationsResponse,
            Awaitable[
                offline_user_data_job_service.AddOfflineUserDataJobOperationsResponse
            ],
        ],
    ]: ...
    @property
    def run_offline_user_data_job(
        self,
    ) -> Callable[
        [offline_user_data_job_service.RunOfflineUserDataJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]: ...
