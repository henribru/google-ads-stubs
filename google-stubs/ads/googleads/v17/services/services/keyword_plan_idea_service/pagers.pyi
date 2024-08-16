from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry as retries

from google.ads.googleads.v17.services.types import keyword_plan_idea_service

OptionalRetry: Incomplete

class GenerateKeywordIdeasPager:
    def __init__(
        self,
        method: Callable[..., keyword_plan_idea_service.GenerateKeywordIdeaResponse],
        request: keyword_plan_idea_service.GenerateKeywordIdeasRequest,
        response: keyword_plan_idea_service.GenerateKeywordIdeaResponse,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterable[keyword_plan_idea_service.GenerateKeywordIdeaResponse]: ...
    def __iter__(
        self,
    ) -> Iterator[keyword_plan_idea_service.GenerateKeywordIdeaResult]: ...
