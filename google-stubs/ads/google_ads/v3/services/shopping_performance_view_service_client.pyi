from google.ads.google_ads.v3.proto.services import (
    shopping_performance_view_service_pb2 as shopping_performance_view_service_pb2,
)
from google.ads.google_ads.v3.services import (
    shopping_performance_view_service_client_config as shopping_performance_view_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    shopping_performance_view_service_grpc_transport as shopping_performance_view_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.shopping_performance_view_service_grpc_transport import (
    ShoppingPerformanceViewServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.shopping_performance_view_pb2 import (
    ShoppingPerformanceView,
)

class ShoppingPerformanceViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ShoppingPerformanceViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ShoppingPerformanceViewServiceClient: ...
    @classmethod
    def shopping_performance_view_path(cls, customer: Any): ...
    transport: Union[
        ShoppingPerformanceViewServiceGrpcTransport,
        Callable[[Credentials, type], ShoppingPerformanceViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ShoppingPerformanceViewServiceGrpcTransport,
                Callable[
                    [Credentials, type], ShoppingPerformanceViewServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_shopping_performance_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ShoppingPerformanceView: ...
