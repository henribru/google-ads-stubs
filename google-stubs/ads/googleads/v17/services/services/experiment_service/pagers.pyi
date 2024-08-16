from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry as retries
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v17.services.types import experiment_service

OptionalRetry: Incomplete

class ListExperimentAsyncErrorsPager:
    def __init__(
        self,
        method: Callable[..., experiment_service.ListExperimentAsyncErrorsResponse],
        request: experiment_service.ListExperimentAsyncErrorsRequest,
        response: experiment_service.ListExperimentAsyncErrorsResponse,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterable[experiment_service.ListExperimentAsyncErrorsResponse]: ...
    def __iter__(self) -> Iterator[status_pb2.Status]: ...
