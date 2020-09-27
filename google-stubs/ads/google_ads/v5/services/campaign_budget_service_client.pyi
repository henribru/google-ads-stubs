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

from google.ads.google_ads.v5.proto.services import (
    campaign_budget_service_pb2 as campaign_budget_service_pb2,
)
from google.ads.google_ads.v5.services import (
    campaign_budget_service_client_config as campaign_budget_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    campaign_budget_service_grpc_transport as campaign_budget_service_grpc_transport,
)
from google.ads.google_ads.v5.types import CampaignBudget, ResponseContentTypeEnum

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
        campaign_budget_service_grpc_transport.CampaignBudgetServiceGrpcTransport,
        Callable[
            [Credentials, type],
            campaign_budget_service_grpc_transport.CampaignBudgetServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                campaign_budget_service_grpc_transport.CampaignBudgetServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    campaign_budget_service_grpc_transport.CampaignBudgetServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
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
        operations: List[
            Union[Dict[str, Any], campaign_budget_service_pb2.CampaignBudgetOperation]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        response_content_type: Optional[
            ResponseContentTypeEnum.ResponseContentTypeValue
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> campaign_budget_service_pb2.MutateCampaignBudgetsResponse: ...
