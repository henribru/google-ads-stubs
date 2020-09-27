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

from google.ads.google_ads.v5.proto.services import (
    feed_placeholder_view_service_pb2 as feed_placeholder_view_service_pb2,
)
from google.ads.google_ads.v5.services import (
    feed_placeholder_view_service_client_config as feed_placeholder_view_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    feed_placeholder_view_service_grpc_transport as feed_placeholder_view_service_grpc_transport,
)
from google.ads.google_ads.v5.types import FeedPlaceholderView

class FeedPlaceholderViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedPlaceholderViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedPlaceholderViewServiceClient: ...
    @classmethod
    def feed_placeholder_view_path(
        cls, customer: Any, feed_placeholder_view: Any
    ) -> str: ...
    transport: Union[
        feed_placeholder_view_service_grpc_transport.FeedPlaceholderViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            feed_placeholder_view_service_grpc_transport.FeedPlaceholderViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                feed_placeholder_view_service_grpc_transport.FeedPlaceholderViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    feed_placeholder_view_service_grpc_transport.FeedPlaceholderViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_feed_placeholder_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> FeedPlaceholderView: ...
