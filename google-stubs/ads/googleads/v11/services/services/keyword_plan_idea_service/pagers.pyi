from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from google.ads.googleads.v11.services.types import (
    keyword_plan_idea_service as keyword_plan_idea_service,
)

class GenerateKeywordIdeasPager:
    def __init__(
        self,
        method: Callable[..., keyword_plan_idea_service.GenerateKeywordIdeaResponse],
        request: keyword_plan_idea_service.GenerateKeywordIdeasRequest,
        response: keyword_plan_idea_service.GenerateKeywordIdeaResponse,
        metadata: Sequence[Tuple[str, str]] = ...,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterable[keyword_plan_idea_service.GenerateKeywordIdeaResponse]: ...
    def __iter__(
        self,
    ) -> Iterator[keyword_plan_idea_service.GenerateKeywordIdeaResult]: ...
