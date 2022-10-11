from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1, operations_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2

from google.ads.googleads.v11.services.types import offline_user_data_job_service

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
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: str = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def operations_client(self) -> operations_v1.OperationsClient: ...  # type: ignore
    @property
    def create_offline_user_data_job(
        self,
    ) -> Callable[
        [offline_user_data_job_service.CreateOfflineUserDataJobRequest],
        offline_user_data_job_service.CreateOfflineUserDataJobResponse,
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
    def close(self) -> None: ...
