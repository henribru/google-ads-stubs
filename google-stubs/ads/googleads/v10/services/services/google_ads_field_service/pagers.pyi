from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from google.ads.googleads.v10.resources.types import (
    google_ads_field as google_ads_field,
)
from google.ads.googleads.v10.services.types import (
    google_ads_field_service as google_ads_field_service,
)

class SearchGoogleAdsFieldsPager:
    def __init__(
        self,
        method: Callable[..., google_ads_field_service.SearchGoogleAdsFieldsResponse],
        request: google_ads_field_service.SearchGoogleAdsFieldsRequest,
        response: google_ads_field_service.SearchGoogleAdsFieldsResponse,
        metadata: Sequence[Tuple[str, str]] = ...,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterable[google_ads_field_service.SearchGoogleAdsFieldsResponse]: ...
    def __iter__(self) -> Iterator[google_ads_field.GoogleAdsField]: ...
