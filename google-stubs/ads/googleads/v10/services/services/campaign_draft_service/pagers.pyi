from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v10.services.types import (
    campaign_draft_service as campaign_draft_service,
)

class ListCampaignDraftAsyncErrorsPager:
    def __init__(
        self,
        method: Callable[
            ..., campaign_draft_service.ListCampaignDraftAsyncErrorsResponse
        ],
        request: campaign_draft_service.ListCampaignDraftAsyncErrorsRequest,
        response: campaign_draft_service.ListCampaignDraftAsyncErrorsResponse,
        metadata: Sequence[Tuple[str, str]] = ...,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterable[campaign_draft_service.ListCampaignDraftAsyncErrorsResponse]: ...
    def __iter__(self) -> Iterator[status_pb2.Status]: ...
