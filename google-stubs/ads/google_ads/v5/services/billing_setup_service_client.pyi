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

from google.ads.google_ads.v5.proto.services import (
    billing_setup_service_pb2 as billing_setup_service_pb2,
)
from google.ads.google_ads.v5.services import (
    billing_setup_service_client_config as billing_setup_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    billing_setup_service_grpc_transport as billing_setup_service_grpc_transport,
)
from google.ads.google_ads.v5.types import BillingSetup

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
        billing_setup_service_grpc_transport.BillingSetupServiceGrpcTransport,
        Callable[
            [Credentials, type],
            billing_setup_service_grpc_transport.BillingSetupServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                billing_setup_service_grpc_transport.BillingSetupServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    billing_setup_service_grpc_transport.BillingSetupServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
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
        operation_: Union[
            Dict[str, Any], billing_setup_service_pb2.BillingSetupOperation
        ],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> billing_setup_service_pb2.MutateBillingSetupResponse: ...
