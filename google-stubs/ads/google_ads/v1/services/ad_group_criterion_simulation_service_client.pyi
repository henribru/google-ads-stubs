import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.ad_group_criterion_simulation_service_grpc_transport import (
    AdGroupCriterionSimulationServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.ad_group_criterion_simulation_pb2 import (
    AdGroupCriterionSimulation,
)

class AdGroupCriterionSimulationServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupCriterionSimulationServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupCriterionSimulationServiceClient: ...
    @classmethod
    def ad_group_criterion_simulation_path(
        cls, customer: Any, ad_group_criterion_simulation: Any
    ) -> str: ...
    transport: Union[
        AdGroupCriterionSimulationServiceGrpcTransport,
        Callable[[Credentials, type], AdGroupCriterionSimulationServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AdGroupCriterionSimulationServiceGrpcTransport,
                Callable[
                    [Credentials, type], AdGroupCriterionSimulationServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_ad_group_criterion_simulation(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdGroupCriterionSimulation: ...
