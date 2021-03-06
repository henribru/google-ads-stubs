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

from google.ads.google_ads.v6.proto.services import (
    hotel_performance_view_service_pb2 as hotel_performance_view_service_pb2,
)
from google.ads.google_ads.v6.services import (
    hotel_performance_view_service_client_config as hotel_performance_view_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    hotel_performance_view_service_grpc_transport as hotel_performance_view_service_grpc_transport,
)
from google.ads.google_ads.v6.types import HotelPerformanceView

class HotelPerformanceViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> HotelPerformanceViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> HotelPerformanceViewServiceClient: ...
    @classmethod
    def hotel_performance_view_path(cls, customer_id: Any) -> str: ...
    transport: Union[
        hotel_performance_view_service_grpc_transport.HotelPerformanceViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            hotel_performance_view_service_grpc_transport.HotelPerformanceViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                hotel_performance_view_service_grpc_transport.HotelPerformanceViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    hotel_performance_view_service_grpc_transport.HotelPerformanceViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_hotel_performance_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> HotelPerformanceView: ...
