from google.ads.google_ads.v3.proto.services import (
    expanded_landing_page_view_service_pb2 as expanded_landing_page_view_service_pb2,
)
from google.ads.google_ads.v3.services import (
    expanded_landing_page_view_service_client_config as expanded_landing_page_view_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    expanded_landing_page_view_service_grpc_transport as expanded_landing_page_view_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.expanded_landing_page_view_service_grpc_transport import (
    ExpandedLandingPageViewServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.expanded_landing_page_view_pb2 import (
    ExpandedLandingPageView,
)

class ExpandedLandingPageViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ExpandedLandingPageViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ExpandedLandingPageViewServiceClient: ...
    @classmethod
    def expanded_landing_page_view_path(
        cls, customer: Any, expanded_landing_page_view: Any
    ) -> str: ...
    transport: Union[
        ExpandedLandingPageViewServiceGrpcTransport,
        Callable[[Credentials, type], ExpandedLandingPageViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ExpandedLandingPageViewServiceGrpcTransport,
                Callable[
                    [Credentials, type], ExpandedLandingPageViewServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_expanded_landing_page_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ExpandedLandingPageView: ...
