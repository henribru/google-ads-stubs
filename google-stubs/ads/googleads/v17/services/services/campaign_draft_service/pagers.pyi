from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence, Tuple

from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v17.services.types import campaign_draft_service

OptionalRetry: Incomplete
OptionalAsyncRetry: Incomplete

class ListCampaignDraftAsyncErrorsPager:
    def __init__(
        self,
        method: Callable[
            ..., campaign_draft_service.ListCampaignDraftAsyncErrorsResponse
        ],
        request: campaign_draft_service.ListCampaignDraftAsyncErrorsRequest,
        response: campaign_draft_service.ListCampaignDraftAsyncErrorsResponse,
        *,
        retry: OptionalRetry = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterator[campaign_draft_service.ListCampaignDraftAsyncErrorsResponse]: ...
    def __iter__(self) -> Iterator[status_pb2.Status]: ...

class ListCampaignDraftAsyncErrorsAsyncPager:
    def __init__(
        self,
        method: Callable[
            ..., Awaitable[campaign_draft_service.ListCampaignDraftAsyncErrorsResponse]
        ],
        request: campaign_draft_service.ListCampaignDraftAsyncErrorsRequest,
        response: campaign_draft_service.ListCampaignDraftAsyncErrorsResponse,
        *,
        retry: OptionalAsyncRetry = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    async def pages(
        self,
    ) -> AsyncIterator[campaign_draft_service.ListCampaignDraftAsyncErrorsResponse]: ...
    def __aiter__(self) -> AsyncIterator[status_pb2.Status]: ...
