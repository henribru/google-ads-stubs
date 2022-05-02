import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2

from google.ads.googleads.v10.services.types import batch_job_service

class BatchJobServiceTransport(abc.ABC):
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
    def mutate_batch_job(
        self,
    ) -> Callable[
        [batch_job_service.MutateBatchJobRequest],
        Union[
            batch_job_service.MutateBatchJobResponse,
            Awaitable[batch_job_service.MutateBatchJobResponse],
        ],
    ]: ...
    @property
    def list_batch_job_results(
        self,
    ) -> Callable[
        [batch_job_service.ListBatchJobResultsRequest],
        Union[
            batch_job_service.ListBatchJobResultsResponse,
            Awaitable[batch_job_service.ListBatchJobResultsResponse],
        ],
    ]: ...
    @property
    def run_batch_job(
        self,
    ) -> Callable[
        [batch_job_service.RunBatchJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]: ...
    @property
    def add_batch_job_operations(
        self,
    ) -> Callable[
        [batch_job_service.AddBatchJobOperationsRequest],
        Union[
            batch_job_service.AddBatchJobOperationsResponse,
            Awaitable[batch_job_service.AddBatchJobOperationsResponse],
        ],
    ]: ...
