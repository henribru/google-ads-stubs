import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.keyword_plan_campaign_service_grpc_transport import (
    KeywordPlanCampaignServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.keyword_plan_campaign_pb2 import (
    KeywordPlanCampaign,
)
from google.ads.google_ads.v2.proto.services.keyword_plan_campaign_service_pb2 import (
    KeywordPlanCampaignOperation,
    MutateKeywordPlanCampaignsResponse,
)

class KeywordPlanCampaignServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> KeywordPlanCampaignServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> KeywordPlanCampaignServiceClient: ...
    @classmethod
    def keyword_plan_campaign_path(
        cls, customer: Any, keyword_plan_campaign: Any
    ) -> str: ...
    transport: Union[
        KeywordPlanCampaignServiceGrpcTransport,
        Callable[[Credentials, type], KeywordPlanCampaignServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                KeywordPlanCampaignServiceGrpcTransport,
                Callable[[Credentials, type], KeywordPlanCampaignServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_keyword_plan_campaign(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> KeywordPlanCampaign: ...
    def mutate_keyword_plan_campaigns(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], KeywordPlanCampaignOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateKeywordPlanCampaignsResponse: ...
