from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple

from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v10.services.types import (
    campaign_experiment_service as campaign_experiment_service,
)

class ListCampaignExperimentAsyncErrorsPager:
    def __init__(
        self,
        method: Callable[
            ..., campaign_experiment_service.ListCampaignExperimentAsyncErrorsResponse
        ],
        request: campaign_experiment_service.ListCampaignExperimentAsyncErrorsRequest,
        response: campaign_experiment_service.ListCampaignExperimentAsyncErrorsResponse,
        metadata: Sequence[Tuple[str, str]] = ...,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def pages(
        self,
    ) -> Iterable[
        campaign_experiment_service.ListCampaignExperimentAsyncErrorsResponse
    ]: ...
    def __iter__(self) -> Iterator[status_pb2.Status]: ...
