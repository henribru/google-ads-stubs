from google.ads.google_ads.v3.proto.services import (
    customer_label_service_pb2 as customer_label_service_pb2,
)
from google.ads.google_ads.v3.services import (
    customer_label_service_client_config as customer_label_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    customer_label_service_grpc_transport as customer_label_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.customer_label_service_grpc_transport import (
    CustomerLabelServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.customer_label_pb2 import CustomerLabel
from google.ads.google_ads.v3.proto.services.customer_label_service_pb2 import (
    CustomerLabelOperation,
    MutateCustomerLabelsResponse,
)

class CustomerLabelServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerLabelServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerLabelServiceClient: ...
    @classmethod
    def customer_label_path(cls, customer: Any, customer_label: Any) -> str: ...
    transport: Union[
        CustomerLabelServiceGrpcTransport,
        Callable[[Credentials, type], CustomerLabelServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CustomerLabelServiceGrpcTransport,
                Callable[[Credentials, type], CustomerLabelServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_customer_label(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CustomerLabel: ...
    def mutate_customer_labels(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], CustomerLabelOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCustomerLabelsResponse: ...
