import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.ad_group_simulation_service_grpc_transport import (
    AdGroupSimulationServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.ad_group_simulation_pb2 import (
    AdGroupSimulation,
)

class AdGroupSimulationServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupSimulationServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupSimulationServiceClient: ...
    @classmethod
    def ad_group_simulation_path(
        cls, customer: Any, ad_group_simulation: Any
    ) -> str: ...
    transport: Union[
        AdGroupSimulationServiceGrpcTransport,
        Callable[[Credentials, type], AdGroupSimulationServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AdGroupSimulationServiceGrpcTransport,
                Callable[[Credentials, type], AdGroupSimulationServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_ad_group_simulation(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdGroupSimulation: ...
