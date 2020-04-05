import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.campaign_feed_service_grpc_transport import (
    CampaignFeedServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.campaign_feed_pb2 import CampaignFeed
from google.ads.google_ads.v1.proto.services.campaign_feed_service_pb2 import (
    CampaignFeedOperation,
    MutateCampaignFeedsResponse,
)

class CampaignFeedServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignFeedServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignFeedServiceClient: ...
    @classmethod
    def campaign_feed_path(cls, customer: Any, campaign_feed: Any) -> str: ...
    transport: Union[
        CampaignFeedServiceGrpcTransport,
        Callable[[Credentials, type], CampaignFeedServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CampaignFeedServiceGrpcTransport,
                Callable[[Credentials, type], CampaignFeedServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_campaign_feed(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CampaignFeed: ...
    def mutate_campaign_feeds(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], CampaignFeedOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCampaignFeedsResponse: ...
