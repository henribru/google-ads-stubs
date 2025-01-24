from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry as retries

from google.ads.googleads.v18.services.types import batch_job_service

OptionalRetry: Incomplete

class ListBatchJobResultsPager:
    def __init__(
        self,
        method: Callable[..., batch_job_service.ListBatchJobResultsResponse],
        request: batch_job_service.ListBatchJobResultsRequest,
        response: batch_job_service.ListBatchJobResultsResponse,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(self) -> Iterable[batch_job_service.ListBatchJobResultsResponse]: ...
    def __iter__(self) -> Iterator[batch_job_service.BatchJobResult]: ...
