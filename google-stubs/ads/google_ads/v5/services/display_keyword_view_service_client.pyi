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
    display_keyword_view_service_pb2 as display_keyword_view_service_pb2,
)
from google.ads.google_ads.v5.services import (
    display_keyword_view_service_client_config as display_keyword_view_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    display_keyword_view_service_grpc_transport as display_keyword_view_service_grpc_transport,
)
from google.ads.google_ads.v5.types import DisplayKeywordView

class DisplayKeywordViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> DisplayKeywordViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> DisplayKeywordViewServiceClient: ...
    @classmethod
    def display_keyword_view_path(
        cls, customer: Any, display_keyword_view: Any
    ) -> str: ...
    transport: Union[
        display_keyword_view_service_grpc_transport.DisplayKeywordViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            display_keyword_view_service_grpc_transport.DisplayKeywordViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                display_keyword_view_service_grpc_transport.DisplayKeywordViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    display_keyword_view_service_grpc_transport.DisplayKeywordViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_display_keyword_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> DisplayKeywordView: ...
