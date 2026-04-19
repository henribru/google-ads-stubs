from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry as retries, retry_async as retries_async

from google.ads.googleads.v21.services.types import google_ads_service

OptionalRetry: Incomplete
OptionalAsyncRetry: Incomplete

class SearchPager:
    def __init__(
        self,
        method: Callable[..., google_ads_service.SearchGoogleAdsResponse],
        request: google_ads_service.SearchGoogleAdsRequest,
        response: google_ads_service.SearchGoogleAdsResponse,
        *,
        retry: retries.Retry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(self) -> Iterator[google_ads_service.SearchGoogleAdsResponse]: ...
    def __iter__(self) -> Iterator[google_ads_service.GoogleAdsRow]: ...

class SearchAsyncPager:
    def __init__(
        self,
        method: Callable[..., Awaitable[google_ads_service.SearchGoogleAdsResponse]],
        request: google_ads_service.SearchGoogleAdsRequest,
        response: google_ads_service.SearchGoogleAdsResponse,
        *,
        retry: retries_async.AsyncRetry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    async def pages(
        self,
    ) -> AsyncIterator[google_ads_service.SearchGoogleAdsResponse]: ...
    def __aiter__(self) -> AsyncIterator[google_ads_service.GoogleAdsRow]: ...
