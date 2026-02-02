from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence

from _typeshed import Incomplete

from google.ads.googleads.v23.services.types import keyword_plan_idea_service

OptionalRetry: Incomplete
OptionalAsyncRetry: Incomplete

class GenerateKeywordIdeasPager:
    def __init__(
        self,
        method: Callable[..., keyword_plan_idea_service.GenerateKeywordIdeaResponse],
        request: keyword_plan_idea_service.GenerateKeywordIdeasRequest,
        response: keyword_plan_idea_service.GenerateKeywordIdeaResponse,
        *,
        retry: OptionalRetry = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterator[keyword_plan_idea_service.GenerateKeywordIdeaResponse]: ...
    def __iter__(
        self,
    ) -> Iterator[keyword_plan_idea_service.GenerateKeywordIdeaResult]: ...

class GenerateKeywordIdeasAsyncPager:
    def __init__(
        self,
        method: Callable[
            ..., Awaitable[keyword_plan_idea_service.GenerateKeywordIdeaResponse]
        ],
        request: keyword_plan_idea_service.GenerateKeywordIdeasRequest,
        response: keyword_plan_idea_service.GenerateKeywordIdeaResponse,
        *,
        retry: OptionalAsyncRetry = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    async def pages(
        self,
    ) -> AsyncIterator[keyword_plan_idea_service.GenerateKeywordIdeaResponse]: ...
    def __aiter__(
        self,
    ) -> AsyncIterator[keyword_plan_idea_service.GenerateKeywordIdeaResult]: ...
