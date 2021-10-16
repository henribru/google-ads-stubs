from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1, operations_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2

from google.ads.googleads.v8.resources.types import batch_job
from google.ads.googleads.v8.services.types import batch_job_service

from .base import BatchJobServiceTransport

class BatchJobServiceGrpcTransport(BatchJobServiceTransport):
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
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def operations_client(self) -> operations_v1.OperationsClient: ...
    @property
    def mutate_batch_job(
        self,
    ) -> Callable[
        [batch_job_service.MutateBatchJobRequest],
        batch_job_service.MutateBatchJobResponse,
    ]: ...
    @property
    def get_batch_job(
        self,
    ) -> Callable[[batch_job_service.GetBatchJobRequest], batch_job.BatchJob]: ...
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
