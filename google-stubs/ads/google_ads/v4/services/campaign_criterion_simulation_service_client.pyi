from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import grpc  # type: ignore
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v4.proto.services import (
    campaign_criterion_simulation_service_pb2 as campaign_criterion_simulation_service_pb2,
)
from google.ads.google_ads.v4.services import (
    campaign_criterion_simulation_service_client_config as campaign_criterion_simulation_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    campaign_criterion_simulation_service_grpc_transport as campaign_criterion_simulation_service_grpc_transport,
)
from google.ads.google_ads.v4.types import CampaignCriterionSimulation

class CampaignCriterionSimulationServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignCriterionSimulationServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignCriterionSimulationServiceClient: ...
    @classmethod
    def campaign_criterion_simulation_path(
        cls, customer: Any, campaign_criterion_simulation: Any
    ) -> str: ...
    transport: Union[
        campaign_criterion_simulation_service_grpc_transport.CampaignCriterionSimulationServiceGrpcTransport,
        Callable[
            [Credentials, type],
            campaign_criterion_simulation_service_grpc_transport.CampaignCriterionSimulationServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                campaign_criterion_simulation_service_grpc_transport.CampaignCriterionSimulationServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    campaign_criterion_simulation_service_grpc_transport.CampaignCriterionSimulationServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_campaign_criterion_simulation(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CampaignCriterionSimulation: ...
