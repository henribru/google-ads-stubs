from google.ads.google_ads.v3.proto.services import (
    feed_item_service_pb2 as feed_item_service_pb2,
)
from google.ads.google_ads.v3.services import (
    feed_item_service_client_config as feed_item_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    feed_item_service_grpc_transport as feed_item_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.feed_item_service_grpc_transport import (
    FeedItemServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.feed_item_pb2 import FeedItem
from google.ads.google_ads.v3.proto.services.feed_item_service_pb2 import (
    FeedItemOperation,
    MutateFeedItemsResponse,
)

class FeedItemServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedItemServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedItemServiceClient: ...
    @classmethod
    def feed_item_path(cls, customer: Any, feed_item: Any) -> str: ...
    transport: Union[
        FeedItemServiceGrpcTransport,
        Callable[[Credentials, type], FeedItemServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                FeedItemServiceGrpcTransport,
                Callable[[Credentials, type], FeedItemServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_feed_item(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> FeedItem: ...
    def mutate_feed_items(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], FeedItemOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateFeedItemsResponse: ...
