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
    campaign_service_pb2 as campaign_service_pb2,
)
from google.ads.google_ads.v6.services import (
    campaign_service_client_config as campaign_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    campaign_service_grpc_transport as campaign_service_grpc_transport,
)
from google.ads.google_ads.v6.types import Campaign, ResponseContentTypeEnum

class CampaignServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignServiceClient: ...
    @classmethod
    def campaign_path(cls, customer: Any, campaign: Any) -> str: ...
    transport: Union[
        campaign_service_grpc_transport.CampaignServiceGrpcTransport,
        Callable[
            [Credentials, type],
            campaign_service_grpc_transport.CampaignServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                campaign_service_grpc_transport.CampaignServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    campaign_service_grpc_transport.CampaignServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_campaign(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Campaign: ...
    def mutate_campaigns(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], campaign_service_pb2.CampaignOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        response_content_type: Optional[
            ResponseContentTypeEnum.ResponseContentTypeValue
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> campaign_service_pb2.MutateCampaignsResponse: ...
