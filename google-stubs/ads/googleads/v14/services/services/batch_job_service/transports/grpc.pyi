from typing import Callable, Sequence, Tuple

import grpc
from google.api_core import gapic_v1, operations_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2

from google.ads.googleads.v14.services.types import batch_job_service

from .base import BatchJobServiceTransport

__all__ = ["BatchJobServiceGrpcTransport"]

class BatchJobServiceGrpcTransport(BatchJobServiceTransport):
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        channel: grpc.Channel | None = None,
        api_mtls_endpoint: str | None = None,
        client_cert_source: Callable[[], tuple[bytes, bytes]] | None = None,
        ssl_channel_credentials: grpc.ChannelCredentials | None = None,
        client_cert_source_for_mtls: Callable[[], tuple[bytes, bytes]] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        **kwargs,
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def operations_client(self) -> operations_v1.OperationsClient: ...  # type: ignore[override]
    @property
    def mutate_batch_job(
        self,
    ) -> Callable[
        [batch_job_service.MutateBatchJobRequest],
        batch_job_service.MutateBatchJobResponse,
    ]: ...
    @property
    def list_batch_job_results(
        self,
    ) -> Callable[
        [batch_job_service.ListBatchJobResultsRequest],
        batch_job_service.ListBatchJobResultsResponse,
    ]: ...
    @property
    def run_batch_job(
        self,
    ) -> Callable[[batch_job_service.RunBatchJobRequest], operations_pb2.Operation]: ...
    @property
    def add_batch_job_operations(
        self,
    ) -> Callable[
        [batch_job_service.AddBatchJobOperationsRequest],
        batch_job_service.AddBatchJobOperationsResponse,
    ]: ...
    def close(self) -> None: ...
