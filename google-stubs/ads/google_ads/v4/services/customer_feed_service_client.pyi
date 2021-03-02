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

import grpc
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v4.proto.services import (
    customer_feed_service_pb2 as customer_feed_service_pb2,
)
from google.ads.google_ads.v4.services import (
    customer_feed_service_client_config as customer_feed_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    customer_feed_service_grpc_transport as customer_feed_service_grpc_transport,
)
from google.ads.google_ads.v4.types import CustomerFeed

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
        customer_feed_service_grpc_transport.CustomerFeedServiceGrpcTransport,
        Callable[
            [Credentials, type],
            customer_feed_service_grpc_transport.CustomerFeedServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                customer_feed_service_grpc_transport.CustomerFeedServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    customer_feed_service_grpc_transport.CustomerFeedServiceGrpcTransport,
                ],
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
        operations: List[
            Union[Dict[str, Any], customer_feed_service_pb2.CustomerFeedOperation]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> customer_feed_service_pb2.MutateCustomerFeedsResponse: ...
