from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence

import google.rpc.status_pb2 as status_pb2
from _typeshed import Incomplete
from google.api_core import gapic_v1, retry as retries, retry_async as retries_async

from google.ads.googleads.v22.services.types import experiment_service

OptionalRetry: Incomplete
OptionalAsyncRetry: Incomplete

class ListExperimentAsyncErrorsPager:
    def __init__(
        self,
        method: Callable[..., experiment_service.ListExperimentAsyncErrorsResponse],
        request: experiment_service.ListExperimentAsyncErrorsRequest,
        response: experiment_service.ListExperimentAsyncErrorsResponse,
        *,
        retry: retries.Retry | gapic_v1.method._MethodDefault | None = ...,
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
        retry: retries_async.AsyncRetry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    async def pages(
        self,
    ) -> AsyncIterator[experiment_service.ListExperimentAsyncErrorsResponse]: ...
    def __aiter__(self) -> AsyncIterator[status_pb2.Status]: ...
