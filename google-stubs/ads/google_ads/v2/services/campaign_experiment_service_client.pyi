import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.campaign_experiment_service_grpc_transport import (
    CampaignExperimentServiceGrpcTransport,
)
from google.api_core.operation import Operation  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import (
    Optional,
    Dict,
    Any,
    List,
    Sequence,
    Tuple,
    Union,
    Callable,
    ClassVar,
    Iterator,
)
from google.ads.google_ads.v2.proto.resources.campaign_experiment_pb2 import (
    CampaignExperiment,
)
from google.ads.google_ads.v2.proto.services.campaign_experiment_service_pb2 import (
    CampaignExperimentOperation,
    MutateCampaignExperimentsResponse,
    GraduateCampaignExperimentResponse,
)

from google.rpc.status_pb2 import Status

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
        CampaignExperimentServiceGrpcTransport,
        Callable[[Credentials, type], CampaignExperimentServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CampaignExperimentServiceGrpcTransport,
                Callable[[Credentials, type], CampaignExperimentServiceGrpcTransport],
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
        operations: List[Union[Dict[str, Any], CampaignExperimentOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCampaignExperimentsResponse: ...
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
    ) -> Iterator[Status]: ...
