from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from google.ads.googleads.v11.services.types import (
    batch_job_service as batch_job_service,
)

class ListBatchJobResultsPager:
    def __init__(
        self,
        method: Callable[..., batch_job_service.ListBatchJobResultsResponse],
        request: batch_job_service.ListBatchJobResultsRequest,
        response: batch_job_service.ListBatchJobResultsResponse,
        metadata: Sequence[Tuple[str, str]] = ...,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(self) -> Iterable[batch_job_service.ListBatchJobResultsResponse]: ...
    def __iter__(self) -> Iterator[batch_job_service.BatchJobResult]: ...
