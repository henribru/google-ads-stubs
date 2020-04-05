import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.feed_item_target_service_grpc_transport import (
    FeedItemTargetServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.feed_item_target_pb2 import FeedItemTarget
from google.ads.google_ads.v2.proto.services.feed_item_target_service_pb2 import (
    FeedItemTargetOperation,
    MutateFeedItemTargetsResponse,
)

class FeedItemTargetServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedItemTargetServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedItemTargetServiceClient: ...
    @classmethod
    def feed_item_target_path(cls, customer: Any, feed_item_target: Any) -> str: ...
    transport: Union[
        FeedItemTargetServiceGrpcTransport,
        Callable[[Credentials, type], FeedItemTargetServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                FeedItemTargetServiceGrpcTransport,
                Callable[[Credentials, type], FeedItemTargetServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_feed_item_target(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> FeedItemTarget: ...
    def mutate_feed_item_targets(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], FeedItemTargetOperation]],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateFeedItemTargetsResponse: ...
