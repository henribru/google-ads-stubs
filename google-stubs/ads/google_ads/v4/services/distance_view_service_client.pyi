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

from google.ads.google_ads.v4.proto.services import (
    distance_view_service_pb2 as distance_view_service_pb2,
)
from google.ads.google_ads.v4.services import (
    distance_view_service_client_config as distance_view_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    distance_view_service_grpc_transport as distance_view_service_grpc_transport,
)
from google.ads.google_ads.v4.types import DistanceView

class DistanceViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> DistanceViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> DistanceViewServiceClient: ...
    @classmethod
    def distance_view_path(cls, customer: Any, distance_view: Any) -> str: ...
    transport: Union[
        distance_view_service_grpc_transport.DistanceViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            distance_view_service_grpc_transport.DistanceViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                distance_view_service_grpc_transport.DistanceViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    distance_view_service_grpc_transport.DistanceViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_distance_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> DistanceView: ...
