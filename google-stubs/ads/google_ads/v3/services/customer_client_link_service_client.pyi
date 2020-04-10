from google.ads.google_ads.v3.proto.services import (
    customer_client_link_service_pb2 as customer_client_link_service_pb2,
)
from google.ads.google_ads.v3.services import (
    customer_client_link_service_client_config as customer_client_link_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    customer_client_link_service_grpc_transport as customer_client_link_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.customer_client_link_service_grpc_transport import (
    CustomerClientLinkServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.customer_client_link_pb2 import (
    CustomerClientLink,
)
from google.ads.google_ads.v3.proto.services.customer_client_link_service_pb2 import (
    CustomerClientLinkOperation,
    MutateCustomerClientLinkResponse,
)

class CustomerClientLinkServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerClientLinkServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerClientLinkServiceClient: ...
    @classmethod
    def customer_client_link_path(
        cls, customer: Any, customer_client_link: Any
    ) -> str: ...
    transport: Union[
        CustomerClientLinkServiceGrpcTransport,
        Callable[[Credentials, type], CustomerClientLinkServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CustomerClientLinkServiceGrpcTransport,
                Callable[[Credentials, type], CustomerClientLinkServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_customer_client_link(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CustomerClientLink: ...
    def mutate_customer_client_link(
        self,
        customer_id: str,
        operation_: Union[Dict[str, Any], CustomerClientLinkOperation],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCustomerClientLinkResponse: ...
