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
    feed_item_service_pb2 as feed_item_service_pb2,
)
from google.ads.google_ads.v6.services import (
    feed_item_service_client_config as feed_item_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    feed_item_service_grpc_transport as feed_item_service_grpc_transport,
)
from google.ads.google_ads.v6.types import FeedItem, ResponseContentTypeEnum

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
        feed_item_service_grpc_transport.FeedItemServiceGrpcTransport,
        Callable[
            [Credentials, type],
            feed_item_service_grpc_transport.FeedItemServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                feed_item_service_grpc_transport.FeedItemServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    feed_item_service_grpc_transport.FeedItemServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
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
        operations: List[
            Union[Dict[str, Any], feed_item_service_pb2.FeedItemOperation]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        response_content_type: Optional[
            ResponseContentTypeEnum.ResponseContentTypeValue
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> feed_item_service_pb2.MutateFeedItemsResponse: ...
