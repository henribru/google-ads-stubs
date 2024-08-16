from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry as retries

from google.ads.googleads.v17.services.types import google_ads_service

OptionalRetry: Incomplete

class SearchPager:
    def __init__(
        self,
        method: Callable[..., google_ads_service.SearchGoogleAdsResponse],
        request: google_ads_service.SearchGoogleAdsRequest,
        response: google_ads_service.SearchGoogleAdsResponse,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(self) -> Iterable[google_ads_service.SearchGoogleAdsResponse]: ...
    def __iter__(self) -> Iterator[google_ads_service.GoogleAdsRow]: ...
