import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2

from google.ads.googleads.v9.resources.types import campaign_experiment
from google.ads.googleads.v9.services.types import campaign_experiment_service

class CampaignExperimentServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def operations_client(self) -> None: ...
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
        operations_pb2.Operation,
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
        operations_pb2.Operation,
    ]: ...
    @property
    def end_campaign_experiment(
        self,
    ) -> typing.Callable[
        [campaign_experiment_service.EndCampaignExperimentRequest], empty_pb2.Empty
    ]: ...
    @property
    def list_campaign_experiment_async_errors(
        self,
    ) -> typing.Callable[
        [campaign_experiment_service.ListCampaignExperimentAsyncErrorsRequest],
        campaign_experiment_service.ListCampaignExperimentAsyncErrorsResponse,
    ]: ...
