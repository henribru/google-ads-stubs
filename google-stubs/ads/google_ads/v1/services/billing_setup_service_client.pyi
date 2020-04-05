import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.billing_setup_service_grpc_transport import (
    BillingSetupServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.billing_setup_pb2 import BillingSetup
from google.ads.google_ads.v1.proto.services.billing_setup_service_pb2 import (
    BillingSetupOperation,
    MutateBillingSetupResponse,
)

class BillingSetupServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> BillingSetupServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> BillingSetupServiceClient: ...
    @classmethod
    def billing_setup_path(cls, customer: Any, billing_setup: Any) -> str: ...
    transport: Union[
        BillingSetupServiceGrpcTransport,
        Callable[[Credentials, type], BillingSetupServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                BillingSetupServiceGrpcTransport,
                Callable[[Credentials, type], BillingSetupServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_billing_setup(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> BillingSetup: ...
    def mutate_billing_setup(
        self,
        customer_id: str,
        operation_: Union[Dict[str, Any], BillingSetupOperation],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateBillingSetupResponse: ...
