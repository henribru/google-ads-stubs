from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence, Tuple

from _typeshed import Incomplete

from google.ads.googleads.v17.services.types import google_ads_service

OptionalRetry: Incomplete
OptionalAsyncRetry: Incomplete

class SearchPager:
    def __init__(
        self,
        method: Callable[..., google_ads_service.SearchGoogleAdsResponse],
        request: google_ads_service.SearchGoogleAdsRequest,
        response: google_ads_service.SearchGoogleAdsResponse,
        *,
        retry: OptionalRetry = ...,
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
        retry: OptionalAsyncRetry = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    async def pages(
        self,
    ) -> AsyncIterator[google_ads_service.SearchGoogleAdsResponse]: ...
    def __aiter__(self) -> AsyncIterator[google_ads_service.GoogleAdsRow]: ...
