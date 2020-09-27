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

from google.ads.google_ads.v4.proto.services import (
    customer_client_service_pb2 as customer_client_service_pb2,
)
from google.ads.google_ads.v4.services import (
    customer_client_service_client_config as customer_client_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    customer_client_service_grpc_transport as customer_client_service_grpc_transport,
)
from google.ads.google_ads.v4.types import CustomerClient

class CustomerClientServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerClientServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerClientServiceClient: ...
    @classmethod
    def customer_client_path(cls, customer: Any, customer_client: Any) -> str: ...
    transport: Union[
        customer_client_service_grpc_transport.CustomerClientServiceGrpcTransport,
        Callable[
            [Credentials, type],
            customer_client_service_grpc_transport.CustomerClientServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                customer_client_service_grpc_transport.CustomerClientServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    customer_client_service_grpc_transport.CustomerClientServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_customer_client(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CustomerClient: ...
