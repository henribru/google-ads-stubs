from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence

from _typeshed import Incomplete

from google.ads.googleads.v19.services.types import batch_job_service

OptionalRetry: Incomplete
OptionalAsyncRetry: Incomplete

class ListBatchJobResultsPager:
    def __init__(
        self,
        method: Callable[..., batch_job_service.ListBatchJobResultsResponse],
        request: batch_job_service.ListBatchJobResultsRequest,
        response: batch_job_service.ListBatchJobResultsResponse,
        *,
        retry: OptionalRetry = ...,
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
        retry: OptionalAsyncRetry = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    async def pages(
        self,
    ) -> AsyncIterator[batch_job_service.ListBatchJobResultsResponse]: ...
    def __aiter__(self) -> AsyncIterator[batch_job_service.BatchJobResult]: ...
