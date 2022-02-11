from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1, operations_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2

from google.ads.googleads.v9.resources.types import offline_user_data_job
from google.ads.googleads.v9.services.types import offline_user_data_job_service

from .base import OfflineUserDataJobServiceTransport

class OfflineUserDataJobServiceGrpcTransport(OfflineUserDataJobServiceTransport):
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: str = ...,
        scopes: Sequence[str] = ...,
        channel: grpc.Channel = ...,
        api_mtls_endpoint: str = ...,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = ...,
        ssl_channel_credentials: grpc.ChannelCredentials = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        scopes: Optional[Sequence[str]] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    def close(self) -> None: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def operations_client(self) -> operations_v1.OperationsClient: ...  # type: ignore[override]
    @property
    def create_offline_user_data_job(
        self,
    ) -> Callable[
        [offline_user_data_job_service.CreateOfflineUserDataJobRequest],
        offline_user_data_job_service.CreateOfflineUserDataJobResponse,
    ]: ...
    @property
    def get_offline_user_data_job(
        self,
    ) -> Callable[
        [offline_user_data_job_service.GetOfflineUserDataJobRequest],
        offline_user_data_job.OfflineUserDataJob,
    ]: ...
    @property
    def add_offline_user_data_job_operations(
        self,
    ) -> Callable[
        [offline_user_data_job_service.AddOfflineUserDataJobOperationsRequest],
        offline_user_data_job_service.AddOfflineUserDataJobOperationsResponse,
    ]: ...
    @property
    def run_offline_user_data_job(
        self,
    ) -> Callable[
        [offline_user_data_job_service.RunOfflineUserDataJobRequest],
        operations_pb2.Operation,
    ]: ...
