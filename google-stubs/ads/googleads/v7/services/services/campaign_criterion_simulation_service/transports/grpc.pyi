from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import campaign_criterion_simulation
from google.ads.googleads.v7.services.types import campaign_criterion_simulation_service

from .base import CampaignCriterionSimulationServiceTransport

class CampaignCriterionSimulationServiceGrpcTransport(
    CampaignCriterionSimulationServiceTransport
):
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        credentials_file: str = ...,
        scopes: Sequence[str] = ...,
        channel: grpc.Channel = ...,
        api_mtls_endpoint: str = ...,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = ...,
        ssl_channel_credentials: grpc.ChannelCredentials = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        scopes: Optional[Sequence[str]] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def get_campaign_criterion_simulation(
        self,
    ) -> Callable[
        [campaign_criterion_simulation_service.GetCampaignCriterionSimulationRequest],
        campaign_criterion_simulation.CampaignCriterionSimulation,
    ]: ...