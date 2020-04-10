from google.ads.google_ads.v3.proto.services import (
    campaign_budget_service_pb2 as campaign_budget_service_pb2,
)
from google.ads.google_ads.v3.services import (
    campaign_budget_service_client_config as campaign_budget_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    campaign_budget_service_grpc_transport as campaign_budget_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.campaign_budget_service_grpc_transport import (
    CampaignBudgetServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.campaign_budget_pb2 import CampaignBudget
from google.ads.google_ads.v3.proto.services.campaign_budget_service_pb2 import (
    CampaignBudgetOperation,
    MutateCampaignBudgetsResponse,
)

class CampaignBudgetServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignBudgetServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignBudgetServiceClient: ...
    @classmethod
    def campaign_budget_path(cls, customer: Any, campaign_budget: Any) -> str: ...
    transport: Union[
        CampaignBudgetServiceGrpcTransport,
        Callable[[Credentials, type], CampaignBudgetServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CampaignBudgetServiceGrpcTransport,
                Callable[[Credentials, type], CampaignBudgetServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_campaign_budget(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CampaignBudget: ...
    def mutate_campaign_budgets(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], CampaignBudgetOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCampaignBudgetsResponse: ...
