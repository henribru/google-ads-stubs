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
    feed_item_set_link_service_pb2 as feed_item_set_link_service_pb2,
)
from google.ads.google_ads.v6.services import (
    feed_item_set_link_service_client_config as feed_item_set_link_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    feed_item_set_link_service_grpc_transport as feed_item_set_link_service_grpc_transport,
)
from google.ads.google_ads.v6.types import FeedItemSetLink

class FeedItemSetLinkServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedItemSetLinkServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedItemSetLinkServiceClient: ...
    @classmethod
    def feed_item_set_link_path(cls, customer: Any, feed_item_set_link: Any) -> str: ...
    transport: Union[
        feed_item_set_link_service_grpc_transport.FeedItemSetLinkServiceGrpcTransport,
        Callable[
            [Credentials, type],
            feed_item_set_link_service_grpc_transport.FeedItemSetLinkServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                feed_item_set_link_service_grpc_transport.FeedItemSetLinkServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    feed_item_set_link_service_grpc_transport.FeedItemSetLinkServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_feed_item_set_link(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> FeedItemSetLink: ...
    def mutate_feed_item_set_links(
        self,
        customer_id: str,
        operations: List[
            Union[
                Dict[str, Any], feed_item_set_link_service_pb2.FeedItemSetLinkOperation
            ]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> feed_item_set_link_service_pb2.MutateFeedItemSetLinksResponse: ...
