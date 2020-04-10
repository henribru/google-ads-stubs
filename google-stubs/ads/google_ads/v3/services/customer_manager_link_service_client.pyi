from google.ads.google_ads.v3.proto.services import (
    customer_manager_link_service_pb2 as customer_manager_link_service_pb2,
)
from google.ads.google_ads.v3.services import (
    customer_manager_link_service_client_config as customer_manager_link_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    customer_manager_link_service_grpc_transport as customer_manager_link_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.customer_manager_link_service_grpc_transport import (
    CustomerManagerLinkServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.customer_manager_link_pb2 import (
    CustomerManagerLink,
)
from google.ads.google_ads.v3.proto.services.customer_manager_link_service_pb2 import (
    CustomerManagerLinkOperation,
    MutateCustomerManagerLinkResponse,
    MoveManagerLinkResponse,
)

class CustomerManagerLinkServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerManagerLinkServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerManagerLinkServiceClient: ...
    @classmethod
    def customer_manager_link_path(
        cls, customer: Any, customer_manager_link: Any
    ) -> str: ...
    transport: Union[
        CustomerManagerLinkServiceGrpcTransport,
        Callable[[Credentials, type], CustomerManagerLinkServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CustomerManagerLinkServiceGrpcTransport,
                Callable[[Credentials, type], CustomerManagerLinkServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_customer_manager_link(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CustomerManagerLink: ...
    def mutate_customer_manager_link(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], CustomerManagerLinkOperation]],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCustomerManagerLinkResponse: ...
    def move_manager_link(
        self,
        customer_id: str,
        previous_customer_manager_link: str,
        new_manager: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MoveManagerLinkResponse: ...
