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

from google.ads.google_ads.v6.proto.services import (
    campaign_criterion_service_pb2 as campaign_criterion_service_pb2,
)
from google.ads.google_ads.v6.services import (
    campaign_criterion_service_client_config as campaign_criterion_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    campaign_criterion_service_grpc_transport as campaign_criterion_service_grpc_transport,
)
from google.ads.google_ads.v6.types import CampaignCriterion, ResponseContentTypeEnum

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
        campaign_criterion_service_grpc_transport.CampaignCriterionServiceGrpcTransport,
        Callable[
            [Credentials, type],
            campaign_criterion_service_grpc_transport.CampaignCriterionServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                campaign_criterion_service_grpc_transport.CampaignCriterionServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    campaign_criterion_service_grpc_transport.CampaignCriterionServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
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
        operations: List[
            Union[
                Dict[str, Any],
                campaign_criterion_service_pb2.CampaignCriterionOperation,
            ]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        response_content_type: Optional[
            ResponseContentTypeEnum.ResponseContentTypeValue
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> campaign_criterion_service_pb2.MutateCampaignCriteriaResponse: ...
