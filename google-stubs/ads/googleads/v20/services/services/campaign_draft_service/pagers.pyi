from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence

import google.rpc.status_pb2 as status_pb2
from _typeshed import Incomplete
from google.api_core import gapic_v1, retry as retries, retry_async as retries_async

from google.ads.googleads.v20.services.types import campaign_draft_service

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
        retry: retries.Retry | gapic_v1.method._MethodDefault | None = ...,
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
        retry: retries_async.AsyncRetry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    async def pages(
        self,
    ) -> AsyncIterator[campaign_draft_service.ListCampaignDraftAsyncErrorsResponse]: ...
    def __aiter__(self) -> AsyncIterator[status_pb2.Status]: ...
