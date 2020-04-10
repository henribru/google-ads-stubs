from google.ads.google_ads.v3.proto.services import (
    campaign_criterion_service_pb2 as campaign_criterion_service_pb2,
)
from google.ads.google_ads.v3.services import (
    campaign_criterion_service_client_config as campaign_criterion_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    campaign_criterion_service_grpc_transport as campaign_criterion_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.campaign_criterion_service_grpc_transport import (
    CampaignCriterionServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.campaign_criterion_pb2 import (
    CampaignCriterion,
)
from google.ads.google_ads.v3.proto.services.campaign_criterion_service_pb2 import (
    CampaignCriterionOperation,
    MutateCampaignCriteriaResponse,
)

class CampaignCriterionServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignCriterionServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignCriterionServiceClient: ...
    @classmethod
    def campaign_criteria_path(cls, customer: Any, campaign_criteria: Any) -> str: ...
    transport: Union[
        CampaignCriterionServiceGrpcTransport,
        Callable[[Credentials, type], CampaignCriterionServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CampaignCriterionServiceGrpcTransport,
                Callable[[Credentials, type], CampaignCriterionServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_campaign_criterion(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CampaignCriterion: ...
    def mutate_campaign_criteria(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], CampaignCriterionOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCampaignCriteriaResponse: ...
