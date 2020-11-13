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

from google.ads.google_ads.v6.proto.services import (
    location_view_service_pb2 as location_view_service_pb2,
)
from google.ads.google_ads.v6.services import (
    location_view_service_client_config as location_view_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    location_view_service_grpc_transport as location_view_service_grpc_transport,
)
from google.ads.google_ads.v6.types import LocationView

class LocationViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> LocationViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> LocationViewServiceClient: ...
    @classmethod
    def location_view_path(cls, customer: Any, location_view: Any) -> str: ...
    transport: Union[
        location_view_service_grpc_transport.LocationViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            location_view_service_grpc_transport.LocationViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                location_view_service_grpc_transport.LocationViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    location_view_service_grpc_transport.LocationViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_location_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> LocationView: ...
