from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence, Tuple

from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v17.services.types import experiment_service

OptionalRetry: Incomplete
OptionalAsyncRetry: Incomplete

class ListExperimentAsyncErrorsPager:
    def __init__(
        self,
        method: Callable[..., experiment_service.ListExperimentAsyncErrorsResponse],
        request: experiment_service.ListExperimentAsyncErrorsRequest,
        response: experiment_service.ListExperimentAsyncErrorsResponse,
        *,
        retry: OptionalRetry = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterator[experiment_service.ListExperimentAsyncErrorsResponse]: ...
    def __iter__(self) -> Iterator[status_pb2.Status]: ...

class ListExperimentAsyncErrorsAsyncPager:
    def __init__(
        self,
        method: Callable[
            ..., Awaitable[experiment_service.ListExperimentAsyncErrorsResponse]
        ],
        request: experiment_service.ListExperimentAsyncErrorsRequest,
        response: experiment_service.ListExperimentAsyncErrorsResponse,
        *,
        retry: OptionalAsyncRetry = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    async def pages(
        self,
    ) -> AsyncIterator[experiment_service.ListExperimentAsyncErrorsResponse]: ...
    def __aiter__(self) -> AsyncIterator[status_pb2.Status]: ...
