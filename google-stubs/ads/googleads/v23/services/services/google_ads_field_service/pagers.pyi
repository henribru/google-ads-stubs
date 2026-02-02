from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence

from _typeshed import Incomplete

from google.ads.googleads.v23.resources.types import (
    google_ads_field as google_ads_field,
)
from google.ads.googleads.v23.services.types import google_ads_field_service

OptionalRetry: Incomplete
OptionalAsyncRetry: Incomplete

class SearchGoogleAdsFieldsPager:
    def __init__(
        self,
        method: Callable[..., google_ads_field_service.SearchGoogleAdsFieldsResponse],
        request: google_ads_field_service.SearchGoogleAdsFieldsRequest,
        response: google_ads_field_service.SearchGoogleAdsFieldsResponse,
        *,
        retry: OptionalRetry = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterator[google_ads_field_service.SearchGoogleAdsFieldsResponse]: ...
    def __iter__(self) -> Iterator[google_ads_field.GoogleAdsField]: ...

class SearchGoogleAdsFieldsAsyncPager:
    def __init__(
        self,
        method: Callable[
            ..., Awaitable[google_ads_field_service.SearchGoogleAdsFieldsResponse]
        ],
        request: google_ads_field_service.SearchGoogleAdsFieldsRequest,
        response: google_ads_field_service.SearchGoogleAdsFieldsResponse,
        *,
        retry: OptionalAsyncRetry = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    async def pages(
        self,
    ) -> AsyncIterator[google_ads_field_service.SearchGoogleAdsFieldsResponse]: ...
    def __aiter__(self) -> AsyncIterator[google_ads_field.GoogleAdsField]: ...
