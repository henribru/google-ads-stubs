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
    ad_group_criterion_simulation_service_pb2 as ad_group_criterion_simulation_service_pb2,
)
from google.ads.google_ads.v4.services import (
    ad_group_criterion_simulation_service_client_config as ad_group_criterion_simulation_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    ad_group_criterion_simulation_service_grpc_transport as ad_group_criterion_simulation_service_grpc_transport,
)
from google.ads.google_ads.v4.types import AdGroupCriterionSimulation

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
        ad_group_criterion_simulation_service_grpc_transport.AdGroupCriterionSimulationServiceGrpcTransport,
        Callable[
            [Credentials, type],
            ad_group_criterion_simulation_service_grpc_transport.AdGroupCriterionSimulationServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ad_group_criterion_simulation_service_grpc_transport.AdGroupCriterionSimulationServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    ad_group_criterion_simulation_service_grpc_transport.AdGroupCriterionSimulationServiceGrpcTransport,
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
