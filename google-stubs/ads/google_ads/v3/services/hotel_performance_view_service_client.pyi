from typing import Any, Callable, ClassVar, Dict, List, Optional, Sequence, Tuple, Union

import grpc  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v3.proto.resources.hotel_performance_view_pb2 import (
    HotelPerformanceView,
)
from google.ads.google_ads.v3.proto.services import (
    hotel_performance_view_service_pb2 as hotel_performance_view_service_pb2,
)
from google.ads.google_ads.v3.services import (
    hotel_performance_view_service_client_config as hotel_performance_view_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    hotel_performance_view_service_grpc_transport as hotel_performance_view_service_grpc_transport,
)
from google.ads.google_ads.v3.services.transports.hotel_performance_view_service_grpc_transport import (
    HotelPerformanceViewServiceGrpcTransport,
)

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
    def hotel_performance_view_path(cls, customer: Any): ...
    transport: Union[
        HotelPerformanceViewServiceGrpcTransport,
        Callable[[Credentials, type], HotelPerformanceViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                HotelPerformanceViewServiceGrpcTransport,
                Callable[[Credentials, type], HotelPerformanceViewServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_hotel_performance_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> HotelPerformanceView: ...
