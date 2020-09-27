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
    landing_page_view_service_pb2 as landing_page_view_service_pb2,
)
from google.ads.google_ads.v4.services import (
    landing_page_view_service_client_config as landing_page_view_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    landing_page_view_service_grpc_transport as landing_page_view_service_grpc_transport,
)
from google.ads.google_ads.v4.types import LandingPageView

class LandingPageViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> LandingPageViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> LandingPageViewServiceClient: ...
    @classmethod
    def landing_page_view_path(cls, customer: Any, landing_page_view: Any) -> str: ...
    transport: Union[
        landing_page_view_service_grpc_transport.LandingPageViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            landing_page_view_service_grpc_transport.LandingPageViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                landing_page_view_service_grpc_transport.LandingPageViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    landing_page_view_service_grpc_transport.LandingPageViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_landing_page_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> LandingPageView: ...
