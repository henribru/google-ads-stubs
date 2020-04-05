import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.landing_page_view_service_grpc_transport import (
    LandingPageViewServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.landing_page_view_pb2 import (
    LandingPageView,
)

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
        LandingPageViewServiceGrpcTransport,
        Callable[[Credentials, type], LandingPageViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                LandingPageViewServiceGrpcTransport,
                Callable[[Credentials, type], LandingPageViewServiceGrpcTransport],
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
