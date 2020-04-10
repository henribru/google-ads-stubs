from google.ads.google_ads.v3.proto.services import (
    customer_client_service_pb2 as customer_client_service_pb2,
)
from google.ads.google_ads.v3.services import (
    customer_client_service_client_config as customer_client_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    customer_client_service_grpc_transport as customer_client_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.customer_client_service_grpc_transport import (
    CustomerClientServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.customer_client_pb2 import CustomerClient

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
        CustomerClientServiceGrpcTransport,
        Callable[[Credentials, type], CustomerClientServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CustomerClientServiceGrpcTransport,
                Callable[[Credentials, type], CustomerClientServiceGrpcTransport],
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
