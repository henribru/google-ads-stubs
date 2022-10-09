from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1, operations_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2

from google.ads.googleads.v11.services.types import campaign_experiment_service

from .base import CampaignExperimentServiceTransport

class CampaignExperimentServiceGrpcTransport(CampaignExperimentServiceTransport):
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: str = ...,
        scopes: Sequence[str] = ...,
        channel: grpc.Channel = ...,
        api_mtls_endpoint: str = ...,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = ...,
        ssl_channel_credentials: grpc.ChannelCredentials = ...,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: str = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def operations_client(self) -> operations_v1.OperationsClient: ...  # type: ignore
    @property
    def create_campaign_experiment(
        self,
    ) -> Callable[
        [campaign_experiment_service.CreateCampaignExperimentRequest],
        operations_pb2.Operation,
    ]: ...
    @property
    def mutate_campaign_experiments(
        self,
    ) -> Callable[
        [campaign_experiment_service.MutateCampaignExperimentsRequest],
        campaign_experiment_service.MutateCampaignExperimentsResponse,
    ]: ...
    @property
    def graduate_campaign_experiment(
        self,
    ) -> Callable[
        [campaign_experiment_service.GraduateCampaignExperimentRequest],
        campaign_experiment_service.GraduateCampaignExperimentResponse,
    ]: ...
    @property
    def promote_campaign_experiment(
        self,
    ) -> Callable[
        [campaign_experiment_service.PromoteCampaignExperimentRequest],
        operations_pb2.Operation,
    ]: ...
    @property
    def end_campaign_experiment(
        self,
    ) -> Callable[
        [campaign_experiment_service.EndCampaignExperimentRequest], empty_pb2.Empty
    ]: ...
    @property
    def list_campaign_experiment_async_errors(
        self,
    ) -> Callable[
        [campaign_experiment_service.ListCampaignExperimentAsyncErrorsRequest],
        campaign_experiment_service.ListCampaignExperimentAsyncErrorsResponse,
    ]: ...
    def close(self) -> None: ...
