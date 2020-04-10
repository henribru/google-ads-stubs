from google.ads.google_ads.v3.proto.services import (
    feed_mapping_service_pb2 as feed_mapping_service_pb2,
)
from google.ads.google_ads.v3.services import (
    feed_mapping_service_client_config as feed_mapping_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    feed_mapping_service_grpc_transport as feed_mapping_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.feed_mapping_service_grpc_transport import (
    FeedMappingServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.feed_mapping_pb2 import FeedMapping
from google.ads.google_ads.v3.proto.services.feed_mapping_service_pb2 import (
    FeedMappingOperation,
    MutateFeedMappingsResponse,
)

class FeedMappingServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedMappingServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedMappingServiceClient: ...
    @classmethod
    def feed_mapping_path(cls, customer: Any, feed_mapping: Any) -> str: ...
    transport: Union[
        FeedMappingServiceGrpcTransport,
        Callable[[Credentials, type], FeedMappingServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                FeedMappingServiceGrpcTransport,
                Callable[[Credentials, type], FeedMappingServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_feed_mapping(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> FeedMapping: ...
    def mutate_feed_mappings(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], FeedMappingOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateFeedMappingsResponse: ...
