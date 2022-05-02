from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v10.services.types import (
    experiment_service as experiment_service,
)

class ListExperimentAsyncErrorsPager:
    def __init__(
        self,
        method: Callable[..., experiment_service.ListExperimentAsyncErrorsResponse],
        request: experiment_service.ListExperimentAsyncErrorsRequest,
        response: experiment_service.ListExperimentAsyncErrorsResponse,
        metadata: Sequence[Tuple[str, str]] = ...,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterable[experiment_service.ListExperimentAsyncErrorsResponse]: ...
    def __iter__(self) -> Iterator[status_pb2.Status]: ...
