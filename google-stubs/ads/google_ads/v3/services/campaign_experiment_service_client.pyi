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
from google.api_core.operation import Operation  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore
from google.protobuf import empty_pb2 as empty_pb2

from google.ads.google_ads.v3.proto.services import (
    campaign_experiment_service_pb2 as campaign_experiment_service_pb2,
)
from google.ads.google_ads.v3.services import (
    campaign_experiment_service_client_config as campaign_experiment_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    campaign_experiment_service_grpc_transport as campaign_experiment_service_grpc_transport,
)
from google.ads.google_ads.v3.types import (
    CampaignExperiment,
    GraduateCampaignExperimentResponse,
    Status,
)

class CampaignExperimentServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignExperimentServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignExperimentServiceClient: ...
    @classmethod
    def campaign_experiment_path(
        cls, customer: Any, campaign_experiment: Any
    ) -> str: ...
    transport: Union[
        campaign_experiment_service_grpc_transport.CampaignExperimentServiceGrpcTransport,
        Callable[
            [Credentials, type],
            campaign_experiment_service_grpc_transport.CampaignExperimentServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                campaign_experiment_service_grpc_transport.CampaignExperimentServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    campaign_experiment_service_grpc_transport.CampaignExperimentServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_campaign_experiment(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CampaignExperiment: ...
    def create_campaign_experiment(
        self,
        customer_id: str,
        campaign_experiment: Union[Dict[str, Any], CampaignExperiment],
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Operation: ...
    def mutate_campaign_experiments(
        self,
        customer_id: str,
        operations: List[
            Union[
                Dict[str, Any],
                campaign_experiment_service_pb2.CampaignExperimentOperation,
            ]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> campaign_experiment_service_pb2.MutateCampaignExperimentsResponse: ...
    def graduate_campaign_experiment(
        self,
        campaign_experiment: str,
        campaign_budget: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GraduateCampaignExperimentResponse: ...
    def promote_campaign_experiment(
        self,
        campaign_experiment: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Operation: ...
    def end_campaign_experiment(
        self,
        campaign_experiment: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> None: ...
    def list_campaign_experiment_async_errors(
        self,
        resource_name: str,
        page_size: Optional[int] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Iterable[Status]: ...
