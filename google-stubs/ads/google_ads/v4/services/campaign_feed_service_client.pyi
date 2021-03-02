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

import grpc
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v4.proto.services import (
    campaign_feed_service_pb2 as campaign_feed_service_pb2,
)
from google.ads.google_ads.v4.services import (
    campaign_feed_service_client_config as campaign_feed_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    campaign_feed_service_grpc_transport as campaign_feed_service_grpc_transport,
)
from google.ads.google_ads.v4.types import CampaignFeed

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
        campaign_feed_service_grpc_transport.CampaignFeedServiceGrpcTransport,
        Callable[
            [Credentials, type],
            campaign_feed_service_grpc_transport.CampaignFeedServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                campaign_feed_service_grpc_transport.CampaignFeedServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    campaign_feed_service_grpc_transport.CampaignFeedServiceGrpcTransport,
                ],
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
        operations: List[
            Union[Dict[str, Any], campaign_feed_service_pb2.CampaignFeedOperation]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> campaign_feed_service_pb2.MutateCampaignFeedsResponse: ...
