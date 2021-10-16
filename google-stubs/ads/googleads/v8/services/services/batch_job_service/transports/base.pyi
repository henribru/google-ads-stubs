import abc
import typing
from typing import Any

from google.api_core import gapic_v1, operations_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2

from google.ads.googleads.v8.resources.types import batch_job
from google.ads.googleads.v8.services.types import batch_job_service

class BatchJobServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def operations_client(self) -> operations_v1.OperationsClient: ...
    @property
    def mutate_batch_job(
        self,
    ) -> typing.Callable[
        [batch_job_service.MutateBatchJobRequest],
        batch_job_service.MutateBatchJobResponse,
    ]: ...
    @property
    def get_batch_job(
        self,
    ) -> typing.Callable[
        [batch_job_service.GetBatchJobRequest], batch_job.BatchJob
    ]: ...
    @property
    def list_batch_job_results(
        self,
    ) -> typing.Callable[
        [batch_job_service.ListBatchJobResultsRequest],
        batch_job_service.ListBatchJobResultsResponse,
    ]: ...
    @property
    def run_batch_job(
        self,
    ) -> typing.Callable[
        [batch_job_service.RunBatchJobRequest], operations_pb2.Operation
    ]: ...
    @property
    def add_batch_job_operations(
        self,
    ) -> typing.Callable[
        [batch_job_service.AddBatchJobOperationsRequest],
        batch_job_service.AddBatchJobOperationsResponse,
    ]: ...
