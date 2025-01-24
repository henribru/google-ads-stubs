from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry as retries
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v18.services.types import campaign_draft_service

OptionalRetry: Incomplete

class ListCampaignDraftAsyncErrorsPager:
    def __init__(
        self,
        method: Callable[
            ..., campaign_draft_service.ListCampaignDraftAsyncErrorsResponse
        ],
        request: campaign_draft_service.ListCampaignDraftAsyncErrorsRequest,
        response: campaign_draft_service.ListCampaignDraftAsyncErrorsResponse,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterable[campaign_draft_service.ListCampaignDraftAsyncErrorsResponse]: ...
    def __iter__(self) -> Iterator[status_pb2.Status]: ...
