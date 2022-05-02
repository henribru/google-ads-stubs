import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2

from google.ads.googleads.v10.services.types import campaign_experiment_service

class CampaignExperimentServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def operations_client(self) -> None: ...
    @property
    def create_campaign_experiment(
        self,
    ) -> Callable[
        [campaign_experiment_service.CreateCampaignExperimentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]: ...
    @property
    def mutate_campaign_experiments(
        self,
    ) -> Callable[
        [campaign_experiment_service.MutateCampaignExperimentsRequest],
        Union[
            campaign_experiment_service.MutateCampaignExperimentsResponse,
            Awaitable[campaign_experiment_service.MutateCampaignExperimentsResponse],
        ],
    ]: ...
    @property
    def graduate_campaign_experiment(
        self,
    ) -> Callable[
        [campaign_experiment_service.GraduateCampaignExperimentRequest],
        Union[
            campaign_experiment_service.GraduateCampaignExperimentResponse,
            Awaitable[campaign_experiment_service.GraduateCampaignExperimentResponse],
        ],
    ]: ...
    @property
    def promote_campaign_experiment(
        self,
    ) -> Callable[
        [campaign_experiment_service.PromoteCampaignExperimentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]: ...
    @property
    def end_campaign_experiment(
        self,
    ) -> Callable[
        [campaign_experiment_service.EndCampaignExperimentRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]: ...
    @property
    def list_campaign_experiment_async_errors(
        self,
    ) -> Callable[
        [campaign_experiment_service.ListCampaignExperimentAsyncErrorsRequest],
        Union[
            campaign_experiment_service.ListCampaignExperimentAsyncErrorsResponse,
            Awaitable[
                campaign_experiment_service.ListCampaignExperimentAsyncErrorsResponse
            ],
        ],
    ]: ...
