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
    geographic_view_service_pb2 as geographic_view_service_pb2,
)
from google.ads.google_ads.v4.services import (
    geographic_view_service_client_config as geographic_view_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    geographic_view_service_grpc_transport as geographic_view_service_grpc_transport,
)
from google.ads.google_ads.v4.types import GeographicView

class GeographicViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GeographicViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GeographicViewServiceClient: ...
    @classmethod
    def geographic_view_path(cls, customer: Any, geographic_view: Any) -> str: ...
    transport: Union[
        geographic_view_service_grpc_transport.GeographicViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            geographic_view_service_grpc_transport.GeographicViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                geographic_view_service_grpc_transport.GeographicViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    geographic_view_service_grpc_transport.GeographicViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_geographic_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GeographicView: ...
