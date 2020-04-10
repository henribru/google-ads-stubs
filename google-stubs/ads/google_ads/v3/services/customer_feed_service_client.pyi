from google.ads.google_ads.v3.proto.services import (
    customer_feed_service_pb2 as customer_feed_service_pb2,
)
from google.ads.google_ads.v3.services import (
    customer_feed_service_client_config as customer_feed_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    customer_feed_service_grpc_transport as customer_feed_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.customer_feed_service_grpc_transport import (
    CustomerFeedServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.customer_feed_pb2 import CustomerFeed
from google.ads.google_ads.v3.proto.services.customer_feed_service_pb2 import (
    CustomerFeedOperation,
    MutateCustomerFeedsResponse,
)

class CustomerFeedServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerFeedServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerFeedServiceClient: ...
    @classmethod
    def customer_feed_path(cls, customer: Any, customer_feed: Any) -> str: ...
    transport: Union[
        CustomerFeedServiceGrpcTransport,
        Callable[[Credentials, type], CustomerFeedServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CustomerFeedServiceGrpcTransport,
                Callable[[Credentials, type], CustomerFeedServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_customer_feed(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CustomerFeed: ...
    def mutate_customer_feeds(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], CustomerFeedOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCustomerFeedsResponse: ...
