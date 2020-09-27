from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    List,
    Optional,
    Sequence,
    Text,
    Tuple,
    Union,
)

import grpc  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore
from typing_extensions import TypedDict

from google.ads.google_ads.v3.proto.resources.customer_pb2 import Customer
from google.ads.google_ads.v3.proto.services import (
    customer_service_pb2 as customer_service_pb2,
)
from google.ads.google_ads.v3.proto.services.customer_service_pb2 import (
    CreateCustomerClientResponse,
    CustomerOperation,
    ListAccessibleCustomersResponse,
    MutateCustomerResponse,
)
from google.ads.google_ads.v3.services import (
    customer_service_client_config as customer_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    customer_service_grpc_transport as customer_service_grpc_transport,
)
from google.ads.google_ads.v3.services.transports.customer_service_grpc_transport import (
    CustomerServiceGrpcTransport,
)
from google.ads.google_ads.v3.types import AccessRoleEnum, Customer, StringValue

class StringValueDict(TypedDict):
    value: Text

class CustomerServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerServiceClient: ...
    @classmethod
    def customer_path(cls, customer: Any): ...
    transport: Union[
        CustomerServiceGrpcTransport,
        Callable[[Credentials, type], CustomerServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CustomerServiceGrpcTransport,
                Callable[[Credentials, type], CustomerServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_customer(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Customer: ...
    def mutate_customer(
        self,
        customer_id: str,
        operation_: Union[Dict[str, Any], CustomerOperation],
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCustomerResponse: ...
    def list_accessible_customers(
        self,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ListAccessibleCustomersResponse: ...
    def create_customer_client(
        self,
        customer_id: str,
        customer_client: Union[Dict[str, Any], Customer],
        email_address: Optional[Union[StringValueDict, StringValue]] = ...,
        access_role: Optional[AccessRoleEnum.AccessRoleValue] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CreateCustomerClientResponse: ...
