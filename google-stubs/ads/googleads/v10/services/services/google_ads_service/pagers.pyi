from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from google.ads.googleads.v10.services.types import (
    google_ads_service as google_ads_service,
)

class SearchPager:
    def __init__(
        self,
        method: Callable[..., google_ads_service.SearchGoogleAdsResponse],
        request: google_ads_service.SearchGoogleAdsRequest,
        response: google_ads_service.SearchGoogleAdsResponse,
        metadata: Sequence[Tuple[str, str]] = ...,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(self) -> Iterable[google_ads_service.SearchGoogleAdsResponse]: ...
    def __iter__(self) -> Iterator[google_ads_service.GoogleAdsRow]: ...
