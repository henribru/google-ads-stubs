from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry as retries, retry_async as retries_async

from google.ads.googleads.v23.services.types import batch_job_service

OptionalRetry: Incomplete
OptionalAsyncRetry: Incomplete

class ListBatchJobResultsPager:
    def __init__(
        self,
        method: Callable[..., batch_job_service.ListBatchJobResultsResponse],
        request: batch_job_service.ListBatchJobResultsRequest,
        response: batch_job_service.ListBatchJobResultsResponse,
        *,
        retry: retries.Retry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(self) -> Iterator[batch_job_service.ListBatchJobResultsResponse]: ...
    def __iter__(self) -> Iterator[batch_job_service.BatchJobResult]: ...

class ListBatchJobResultsAsyncPager:
    def __init__(
        self,
        method: Callable[..., Awaitable[batch_job_service.ListBatchJobResultsResponse]],
        request: batch_job_service.ListBatchJobResultsRequest,
        response: batch_job_service.ListBatchJobResultsResponse,
        *,
        retry: retries_async.AsyncRetry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    async def pages(
        self,
    ) -> AsyncIterator[batch_job_service.ListBatchJobResultsResponse]: ...
    def __aiter__(self) -> AsyncIterator[batch_job_service.BatchJobResult]: ...
