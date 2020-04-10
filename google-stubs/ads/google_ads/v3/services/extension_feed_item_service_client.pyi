from google.ads.google_ads.v3.proto.services import (
    extension_feed_item_service_pb2 as extension_feed_item_service_pb2,
)
from google.ads.google_ads.v3.services import (
    extension_feed_item_service_client_config as extension_feed_item_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    extension_feed_item_service_grpc_transport as extension_feed_item_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.extension_feed_item_service_grpc_transport import (
    ExtensionFeedItemServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.extension_feed_item_pb2 import (
    ExtensionFeedItem,
)
from google.ads.google_ads.v3.proto.services.extension_feed_item_service_pb2 import (
    ExtensionFeedItemOperation,
    MutateExtensionFeedItemsResponse,
)

class ExtensionFeedItemServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ExtensionFeedItemServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ExtensionFeedItemServiceClient: ...
    @classmethod
    def extension_feed_item_path(
        cls, customer: Any, extension_feed_item: Any
    ) -> str: ...
    transport: Union[
        ExtensionFeedItemServiceGrpcTransport,
        Callable[[Credentials, type], ExtensionFeedItemServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ExtensionFeedItemServiceGrpcTransport,
                Callable[[Credentials, type], ExtensionFeedItemServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_extension_feed_item(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ExtensionFeedItem: ...
    def mutate_extension_feed_items(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], ExtensionFeedItemOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateExtensionFeedItemsResponse: ...
