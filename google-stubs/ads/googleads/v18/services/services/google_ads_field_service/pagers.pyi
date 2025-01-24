from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry as retries

from google.ads.googleads.v18.resources.types import (
    google_ads_field as google_ads_field,
)
from google.ads.googleads.v18.services.types import google_ads_field_service

OptionalRetry: Incomplete

class SearchGoogleAdsFieldsPager:
    def __init__(
        self,
        method: Callable[..., google_ads_field_service.SearchGoogleAdsFieldsResponse],
        request: google_ads_field_service.SearchGoogleAdsFieldsRequest,
        response: google_ads_field_service.SearchGoogleAdsFieldsResponse,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterable[google_ads_field_service.SearchGoogleAdsFieldsResponse]: ...
    def __iter__(self) -> Iterator[google_ads_field.GoogleAdsField]: ...
