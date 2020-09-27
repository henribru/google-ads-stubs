from typing import Any, Callable, ClassVar, Dict, List, Optional, Sequence, Tuple, Union

import grpc  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore

from google.ads.google_ads.v2.proto.resources.feed_placeholder_view_pb2 import (
    FeedPlaceholderView,
)
from google.ads.google_ads.v2.services.transports.feed_placeholder_view_service_grpc_transport import (
    FeedPlaceholderViewServiceGrpcTransport,
)

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
        FeedPlaceholderViewServiceGrpcTransport,
        Callable[[Credentials, type], FeedPlaceholderViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                FeedPlaceholderViewServiceGrpcTransport,
                Callable[[Credentials, type], FeedPlaceholderViewServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_feed_placeholder_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> FeedPlaceholderView: ...
