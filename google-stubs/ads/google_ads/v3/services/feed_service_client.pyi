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

from google.ads.google_ads.v3.proto.services import feed_service_pb2 as feed_service_pb2
from google.ads.google_ads.v3.services import (
    feed_service_client_config as feed_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    feed_service_grpc_transport as feed_service_grpc_transport,
)
from google.ads.google_ads.v3.types import Feed

class FeedServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedServiceClient: ...
    @classmethod
    def feed_path(cls, customer: Any, feed: Any) -> str: ...
    transport: Union[
        feed_service_grpc_transport.FeedServiceGrpcTransport,
        Callable[
            [Credentials, type], feed_service_grpc_transport.FeedServiceGrpcTransport
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                feed_service_grpc_transport.FeedServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    feed_service_grpc_transport.FeedServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_feed(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Feed: ...
    def mutate_feeds(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], feed_service_pb2.FeedOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> feed_service_pb2.MutateFeedsResponse: ...
