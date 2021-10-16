import abc
import typing
from typing import Any

from google.api_core import gapic_v1, operations_v1
from google.auth import credentials
from google.longrunning import operations_pb2 as operations
from google.protobuf import empty_pb2 as empty

from google.ads.googleads.v7.resources.types import campaign_experiment
from google.ads.googleads.v7.services.types import campaign_experiment_service

class CampaignExperimentServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def operations_client(self) -> operations_v1.OperationsClient: ...
    @property
    def get_campaign_experiment(
        self,
    ) -> typing.Callable[
        [campaign_experiment_service.GetCampaignExperimentRequest],
        campaign_experiment.CampaignExperiment,
    ]: ...
    @property
    def create_campaign_experiment(
        self,
    ) -> typing.Callable[
        [campaign_experiment_service.CreateCampaignExperimentRequest],
        operations.Operation,
    ]: ...
    @property
    def mutate_campaign_experiments(
        self,
    ) -> typing.Callable[
        [campaign_experiment_service.MutateCampaignExperimentsRequest],
        campaign_experiment_service.MutateCampaignExperimentsResponse,
    ]: ...
    @property
    def graduate_campaign_experiment(
        self,
    ) -> typing.Callable[
        [campaign_experiment_service.GraduateCampaignExperimentRequest],
        campaign_experiment_service.GraduateCampaignExperimentResponse,
    ]: ...
    @property
    def promote_campaign_experiment(
        self,
    ) -> typing.Callable[
        [campaign_experiment_service.PromoteCampaignExperimentRequest],
        operations.Operation,
    ]: ...
    @property
    def end_campaign_experiment(
        self,
    ) -> typing.Callable[
        [campaign_experiment_service.EndCampaignExperimentRequest], empty.Empty
    ]: ...
    @property
    def list_campaign_experiment_async_errors(
        self,
    ) -> typing.Callable[
        [campaign_experiment_service.ListCampaignExperimentAsyncErrorsRequest],
        campaign_experiment_service.ListCampaignExperimentAsyncErrorsResponse,
    ]: ...
